"""Task model for the event-driven Edict backend.

This schema intentionally matches the Alembic migration and the service/API
layer that already use UUID primary keys plus trace metadata.
"""

import enum
import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Enum, Index, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID

from ..db import Base


class TaskState(str, enum.Enum):
    """Canonical task states for the Sansheng-Liubu workflow."""

    PENDING = "Pending"
    TAIZI = "Taizi"
    ZHONGSHU = "Zhongshu"
    MENXIA = "Menxia"
    ASSIGNED = "Assigned"
    NEXT = "Next"
    DOING = "Doing"
    REVIEW = "Review"
    DONE = "Done"
    BLOCKED = "Blocked"
    CANCELLED = "Cancelled"


TERMINAL_STATES = {TaskState.DONE, TaskState.CANCELLED}

STATE_TRANSITIONS = {
    TaskState.PENDING: {TaskState.TAIZI, TaskState.CANCELLED},
    TaskState.TAIZI: {TaskState.ZHONGSHU, TaskState.CANCELLED},
    TaskState.ZHONGSHU: {TaskState.MENXIA, TaskState.CANCELLED, TaskState.BLOCKED},
    TaskState.MENXIA: {TaskState.ASSIGNED, TaskState.ZHONGSHU, TaskState.CANCELLED},
    TaskState.ASSIGNED: {TaskState.DOING, TaskState.NEXT, TaskState.CANCELLED, TaskState.BLOCKED},
    TaskState.NEXT: {TaskState.DOING, TaskState.CANCELLED},
    TaskState.DOING: {TaskState.REVIEW, TaskState.DONE, TaskState.BLOCKED, TaskState.CANCELLED},
    TaskState.REVIEW: {TaskState.DONE, TaskState.DOING, TaskState.CANCELLED},
    TaskState.BLOCKED: {
        TaskState.TAIZI,
        TaskState.ZHONGSHU,
        TaskState.MENXIA,
        TaskState.ASSIGNED,
        TaskState.DOING,
    },
}

STATE_AGENT_MAP = {
    TaskState.TAIZI: "taizi",
    TaskState.ZHONGSHU: "zhongshu",
    TaskState.MENXIA: "menxia",
    TaskState.ASSIGNED: "shangshu",
    TaskState.REVIEW: "shangshu",
}

ORG_AGENT_MAP = {
    "户部": "hubu",
    "礼部": "libu",
    "兵部": "bingbu",
    "刑部": "xingbu",
    "工部": "gongbu",
    "吏部": "libu_hr",
}


class Task(Base):
    """Primary task record persisted in Postgres."""

    __tablename__ = "tasks"

    task_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    trace_id = Column(String(64), nullable=False, default=lambda: str(uuid.uuid4()))
    title = Column(String(200), nullable=False)
    description = Column(Text, default="")
    priority = Column(String(10), default="中")
    state = Column(
        Enum(TaskState, name="task_state", native_enum=False, values_callable=lambda enum_cls: [item.value for item in enum_cls]),
        nullable=False,
        default=TaskState.TAIZI,
    )
    assignee_org = Column(String(50), nullable=True)
    creator = Column(String(50), default="emperor")
    tags = Column(JSONB, default=list)
    flow_log = Column(JSONB, default=list)
    progress_log = Column(JSONB, default=list)
    todos = Column(JSONB, default=list)
    scheduler = Column(JSONB, nullable=True)
    meta = Column(JSONB, default=dict)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    __table_args__ = (
        Index("ix_tasks_state", "state"),
        Index("ix_tasks_trace_id", "trace_id"),
        Index("ix_tasks_assignee_org", "assignee_org"),
        Index("ix_tasks_created_at", "created_at"),
        Index("ix_tasks_tags", "tags", postgresql_using="gin"),
    )

    @property
    def id(self) -> str:
        return str(self.task_id)

    @property
    def org(self) -> str:
        return self.assignee_org or ""

    def to_dict(self) -> dict:
        state = self.state.value if isinstance(self.state, TaskState) else str(self.state or "")
        return {
            "task_id": str(self.task_id),
            "id": str(self.task_id),
            "trace_id": self.trace_id,
            "title": self.title,
            "description": self.description or "",
            "priority": self.priority,
            "state": state,
            "assignee_org": self.assignee_org,
            "org": self.assignee_org or "",
            "creator": self.creator,
            "tags": self.tags or [],
            "flow_log": self.flow_log or [],
            "progress_log": self.progress_log or [],
            "todos": self.todos or [],
            "scheduler": self.scheduler,
            "meta": self.meta or {},
            "created_at": self.created_at.isoformat() if self.created_at else "",
            "updated_at": self.updated_at.isoformat() if self.updated_at else "",
        }

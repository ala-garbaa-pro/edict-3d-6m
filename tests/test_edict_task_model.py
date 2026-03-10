"""Regression tests for the event-driven Edict task schema."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "edict" / "backend"))

from app.models.task import STATE_AGENT_MAP, ORG_AGENT_MAP, Task, TaskState


def test_task_model_matches_service_schema():
    task = Task(
        title="Audit the rewrite schema drift",
        description="Ensure ORM matches service and API expectations",
        assignee_org="工部",
        tags=["JJC-LEGACY-001"],
        meta={"legacy_id": "JJC-LEGACY-001"},
    )

    payload = task.to_dict()

    assert hasattr(task, "task_id")
    assert hasattr(task, "trace_id")
    assert payload["title"] == "Audit the rewrite schema drift"
    assert payload["description"] == "Ensure ORM matches service and API expectations"
    assert payload["assignee_org"] == "工部"
    assert payload["org"] == "工部"
    assert payload["tags"] == ["JJC-LEGACY-001"]
    assert payload["meta"] == {"legacy_id": "JJC-LEGACY-001"}


def test_task_state_contract_matches_workers():
    assert TaskState("Taizi") is TaskState.TAIZI
    assert TaskState("Assigned") is TaskState.ASSIGNED
    assert STATE_AGENT_MAP[TaskState.TAIZI] == "taizi"
    assert STATE_AGENT_MAP[TaskState.REVIEW] == "shangshu"
    assert ORG_AGENT_MAP["工部"] == "gongbu"

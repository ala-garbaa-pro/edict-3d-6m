<h1 align="center">⚔️ Edict · Multi-Agent Orchestration</h1>

<p align="center">
  <strong>I modeled an AI multi-agent system after China's 1,300-year-old imperial governance.<br>Turns out, ancient bureaucracy understood separation of powers better than modern AI frameworks.</strong>
</p>

<p align="center">
  <sub>12 AI agents (11 business roles + 1 compatibility role) form the Three Departments & Six Ministries: Crown Prince triages, Planning proposes, Review vetoes, Dispatch assigns, Ministries execute.<br>Built-in <b>institutional review gates</b> that CrewAI doesn't have. A <b>real-time dashboard</b> that AutoGen doesn't have.</sub>
</p>

<p align="center">
  <a href="#-demo">Demo</a> ·
  <a href="#-quick-start">Quick Start</a> ·
  <a href="#-architecture">Architecture</a> ·
  <a href="#-features">Features</a> ·
  <a href="CONTRIBUTING.md">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/OpenClaw-Required-blue?style=flat-square" alt="OpenClaw">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Agents-12_Specialized-8B5CF6?style=flat-square" alt="Agents">
  <img src="https://img.shields.io/badge/Dashboard-Real--time-F59E0B?style=flat-square" alt="Dashboard">
  <img src="https://img.shields.io/badge/License-MIT-22C55E?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Zero_Deps-stdlib_only-EC4899?style=flat-square" alt="Zero Dependencies">
</p>

---

## Demo

<p align="center">
  <video src="docs/Agent_video_Pippit_20260225121727.mp4" width="100%" autoplay muted loop playsinline controls>
    Your browser does not support video playback. See the GIF below or <a href="docs/Agent_video_Pippit_20260225121727.mp4">download the video</a>.
  </video>
  <br>
  <sub>Full demo: AI multi-agent collaboration with the Three Departments and Six Ministries workflow</sub>
</p>

<details>
<summary>GIF Preview</summary>
<p align="center">
  <img src="docs/demo.gif" alt="Edict Demo" width="100%">
  <br>
  <sub>Issue edict → Crown Prince triage → Planning → Review → Ministries execute → Report back</sub>
</p>
</details>

> No OpenClaw? Run `docker run -p 7891:7891 cft0808/edict` to try the dashboard with simulated data.

---

## The Idea

Most multi-agent frameworks let agents talk freely and produce opaque results that are hard to audit, replay, or interrupt. Edict takes a different approach by using a governance model inspired by the imperial system:

```text
You (Emperor) → Crown Prince → Planning → Review → Dispatch → 6 Ministries → Report Back
```

This is not just a theme. It is a concrete control model for AI coordination:

- Crown Prince triages incoming messages
- Planning decomposes work into explicit tasks
- Review can reject weak plans and force rework
- Dispatch assigns approved work to specialist agents
- Ministries execute in parallel
- The dashboard exposes status, health, and intervention controls

---

## Why Edict?

| | CrewAI | MetaGPT | AutoGen | Edict |
|---|:---:|:---:|:---:|:---:|
| Built-in review and veto | ❌ | ⚠️ | ⚠️ | ✅ |
| Real-time Kanban dashboard | ❌ | ❌ | ❌ | ✅ |
| Stop / cancel / resume tasks | ❌ | ❌ | ❌ | ✅ |
| Full audit trail | ⚠️ | ⚠️ | ❌ | ✅ |
| Agent health monitoring | ❌ | ❌ | ❌ | ✅ |
| Hot-swap LLM models | ❌ | ❌ | ❌ | ✅ |
| Skill management | ❌ | ❌ | ❌ | ✅ |
| Daily news aggregation | ❌ | ❌ | ❌ | ✅ |

Core differentiator: institutional review, full observability, and real-time intervention.

---

## Features

### Twelve-agent workflow

- Crown Prince message triage
- Three departments for planning, review, and dispatch
- Six specialist ministries plus a morning-briefing role
- Per-agent workspaces, skills, and model configuration
- Task title sanitization to strip file paths, metadata, and junk prefixes

### Dashboard

- Edict board
- Monitoring panel
- Memorial archive
- Template library
- Officials overview
- News panel
- Model configuration
- Skills configuration
- Session tracking
- Opening ceremony animation

---

## Quick Start

### 1. Install OpenClaw

```bash
brew install openclaw
openclaw init
```

### 2. Clone and install Edict

```bash
git clone https://github.com/cft0808/edict.git
cd edict
chmod +x install.sh && ./install.sh
```

The installer will:

- create 12 agent workspaces under `~/.openclaw`
- write each agent's `SOUL.md`
- register agents and permissions in `openclaw.json`
- configure task sanitization rules
- build the React frontend into `dashboard/dist/`
- initialize local data
- run the first sync
- restart the OpenClaw gateway

### 3. Configure a channel

Set `taizi` as the command entry agent for Feishu, Telegram, or Signal:

```bash
openclaw channels list
openclaw channels add --type feishu --agent taizi
```

### 4. Start the services

```bash
bash scripts/run_loop.sh
python3 dashboard/server.py
```

Open `http://127.0.0.1:7891`.

---

## Architecture

Business flow:

```text
Emperor → Crown Prince → Zhongshu → Menxia → Shangshu → Ministries → Report
```

Technical layers:

- OpenClaw-based multi-agent orchestration
- JSON-file-backed dashboard flow in the current stable path
- Event-driven rewrite under `edict/` with FastAPI, Postgres, Redis, and React

See:

- `docs/getting-started.md`
- `docs/task-dispatch-architecture.md`
- `edict_agent_architecture.md`

---

## Repository Layout

| Path | Purpose |
|---|---|
| `agents/` | Agent personas and role instructions |
| `dashboard/` | Dashboard frontend and local API server |
| `scripts/` | Sync, refresh, screenshot, and skill-management tooling |
| `docs/` | User guides and architecture docs |
| `edict/` | Event-driven backend/frontend rewrite |
| `tests/` | Regression and E2E tests |

---

## Development

```bash
python3 -m py_compile dashboard/server.py
python3 -m py_compile scripts/kanban_update.py
python3 tests/test_e2e_kanban.py
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

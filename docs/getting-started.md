# Quick Start

> Build and run the Edict multi-agent system in about five minutes.

---

## Step 1: Install OpenClaw

Edict runs on [OpenClaw](https://openclaw.ai), so install it first:

```bash
# macOS
brew install openclaw

# Or download an installer
# https://openclaw.ai/download
```

Initialize it after installation:

```bash
openclaw init
```

## Step 2: Clone and install Edict

```bash
git clone https://github.com/cft0808/edict.git
cd edict
chmod +x install.sh && ./install.sh
```

The installer will:
- create 12 agent workspaces under `~/.openclaw/workspace-*`
- write each department's `SOUL.md`
- register agents and permission rules in `openclaw.json`
- configure task-sanitization rules
- build the React frontend into `dashboard/dist/` when Node.js 18+ is available
- initialize the data directory
- run the first data sync
- restart the OpenClaw gateway

## Step 3: Configure a messaging channel

Configure Feishu, Telegram, or Signal in OpenClaw and set `taizi` as the task entry agent. `taizi` triages casual chat vs actual commands, extracts a usable title, and forwards real work to `zhongshu`.

```bash
# List channels
openclaw channels list

# Add a Feishu channel with taizi as the entry agent
openclaw channels add --type feishu --agent taizi
```

See also: https://docs.openclaw.ai/channels

## Step 4: Start the services

```bash
# Terminal 1: data refresh loop (every 15 seconds)
bash scripts/run_loop.sh

# Terminal 2: dashboard server
python3 dashboard/server.py

# Open the dashboard
open http://127.0.0.1:7891
```

`run_loop.sh` syncs data every 15 seconds. Run it with `&` if you want it in the background.

`server.py` serves `dashboard/dashboard.html` directly, so no extra frontend build is required for the stable dashboard path. The Docker image includes a prebuilt React frontend.

## Step 5: Send your first task

Send a command through the configured channel:

```
Please build a text classifier in Python:
1. Use scikit-learn
2. Support multi-class classification
3. Output a confusion matrix
4. Include complete documentation
```

## Step 6: Watch the workflow

Open `http://127.0.0.1:7891`.

1. `Edict Board` shows tasks moving across states.
2. `Monitor` shows workload across departments.
3. `Memorials` archives completed tasks.

Typical flow:
```
Inbox → Taizi → Zhongshu → Menxia → Assigned → Doing → Done
```

---

## Advanced Usage

### Use command templates

Dashboard → `Templates` → choose a template → fill in parameters → issue the task

Included templates cover weekly reports, code review, API design, competitor analysis, data reports, blog writing, deployment plans, email drafts, and standup summaries.

### Change an agent model

Dashboard → `Models` → choose a model → apply changes

The gateway restarts automatically and applies the change in about five seconds.

### Manage skills

Dashboard → `Skills` → inspect installed skills → add a new one

### Stop or cancel a task

Use the `Stop` or `Cancel` actions from the board or task details.

### Subscribe to the morning brief

Dashboard → `Morning Brief` → subscription settings → choose categories, add feeds, and configure Feishu delivery

---

## Troubleshooting

### Dashboard says the server is not running
```bash
# Confirm the server is running
python3 dashboard/server.py
```

### An agent does not respond
```bash
# Check gateway status
openclaw gateway status

# Restart if needed
openclaw gateway restart
```

### Data is not refreshing
```bash
# Check whether the refresh loop is running
ps aux | grep run_loop

# Run one sync manually
python3 scripts/refresh_live_data.py
```

### Heartbeat is red or warning
```bash
# Check the agent process
openclaw agent status <agent-id>

# Restart the agent
openclaw agent restart <agent-id>
```

### A model change did not take effect
Wait about five seconds for the gateway restart. If it still does not apply:
```bash
python3 scripts/apply_model_changes.py
openclaw gateway restart
```

---

## More Resources

- [Project home](https://github.com/cft0808/edict)
- [README](../README.md)
- [Contributing](../CONTRIBUTING.md)
- [OpenClaw docs](https://docs.openclaw.ai)
- [`wechat.md`](wechat.md) for historical project notes and publication links

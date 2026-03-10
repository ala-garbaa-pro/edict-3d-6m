# Screenshot Guide

Dashboard screenshots are used in the README and docs. Start the dashboard, then capture the views below in order and store them in this directory.

## Shot List

| File | Content | Panel |
|--------|------|---------|
| `01-kanban-main.png` | Main Edict Board overview | Edict Board |
| `02-monitor.png` | Department monitor | Monitor |
| `03-task-detail.png` | Task flow detail view | Edict Board detail |
| `04-model-config.png` | Model configuration panel | Models |
| `05-skills-config.png` | Skills configuration panel | Skills |
| `06-official-overview.png` | Officials overview for all agents | Officials |
| `07-sessions.png` | Session view | Sessions |
| `08-memorials.png` | Memorial archive | Memorials |
| `09-templates.png` | Template library | Templates |
| `10-morning-briefing.png` | Morning brief | Morning Brief |
| `11-ceremony.png` | Opening ceremony animation | Opening animation |

## Automated Capture

```bash
# Make sure the dashboard server is running
python3 dashboard/server.py &

# Capture all 11 screenshots
python3 scripts/take_screenshots.py

# Record the demo GIF (requires ffmpeg)
python3 scripts/record_demo.py
```

## Recommendations

- Use `1920x1080` or `2560x1440`
- Make sure the dashboard has enough data, ideally at least five tasks
- Dark theme captures usually look best
- Refresh data before taking screenshots

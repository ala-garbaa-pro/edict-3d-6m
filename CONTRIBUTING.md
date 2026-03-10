## Contributing

<p align="center">
  <strong>Contributions are welcome.</strong><br>
  <sub>Bug fixes, documentation improvements, and new agent roles are all useful.</sub>
</p>

---

## Ways To Contribute

### Report a bug

Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template and include:

- OpenClaw version: `openclaw --version`
- Python version: `python3 --version`
- operating system
- clear reproduction steps
- expected behavior vs actual behavior
- screenshots if the dashboard UI is involved

### Suggest a feature

Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template.

### Submit a pull request

```bash
# 1. Fork the repository
# 2. Clone your fork
git clone https://github.com/<your-username>/edict.git
cd edict

# 3. Create a feature branch
git checkout -b feat/my-awesome-feature

# 4. Develop and test
python3 dashboard/server.py

# 5. Commit
git add .
git commit -m "feat: add my awesome feature"

# 6. Push and open a PR
git push origin feat/my-awesome-feature
```

---

## Development Environment

### Prerequisites
- [OpenClaw](https://openclaw.ai) installed
- Python 3.9+
- macOS / Linux

### Run locally

```bash
# Install
./install.sh

# Start the data refresh loop
bash scripts/run_loop.sh &

# Start the dashboard server
python3 dashboard/server.py

# Open the dashboard
open http://127.0.0.1:7891
```

`server.py` serves the built dashboard directly. The Docker image includes a prebuilt React frontend.

### Repository layout

| Path | Description | Churn |
|----------|------|--------|
| `dashboard/dashboard.html` | Dashboard frontend | High |
| `dashboard/server.py` | Standard-library API server | High |
| `agents/*/SOUL.md` | Agent role prompts | Medium |
| `scripts/kanban_update.py` | Dashboard CLI and task sanitization | Medium |
| `scripts/*.py` | Sync and automation scripts | Medium |
| `tests/test_e2e_kanban.py` | End-to-end dashboard regression test | Medium |
| `install.sh` | Installer | Low |

---

## Commit Style

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat:     new feature
fix:      bug fix
docs:     documentation update
style:    formatting only
refactor: code restructuring
perf:     performance improvement
test:     tests
chore:    maintenance
ci:       CI/CD config
```

Examples:
```
feat: add memorial export to PDF
fix: restart the gateway after model changes
docs: refresh README screenshots
```

---

## High-Value Contribution Areas

### Dashboard UI

- dark/light theme switching
- responsive layout improvements
- better animation polish
- accessibility improvements

### Agent roles

- specialist agents for new industries or workflows
- new `SOUL.md` persona templates
- better agent coordination patterns

### Skills ecosystem

- department-specific skill packs
- MCP integrations
- data processing, code analysis, and document generation skills

### Integrations

- Notion / Jira / Linear sync
- GitHub Issues / PR automation
- Slack / Discord channels
- webhook extensions

### Internationalization

- Japanese / Korean / Spanish translations
- multilingual dashboard support

### Mobile

- responsive improvements
- PWA support
- mobile-focused task operations

---

## Testing

```bash
# Syntax checks
python3 -m py_compile dashboard/server.py
python3 -m py_compile scripts/kanban_update.py

# End-to-end dashboard test
python3 tests/test_e2e_kanban.py

# Verify data sync
python3 scripts/refresh_live_data.py
python3 scripts/sync_agent_config.py

# Start the server and verify the API
python3 dashboard/server.py &
curl -s http://localhost:7891/api/live-status | python3 -m json.tool | head -20
```

---

## Code Style

- **Python**: follow PEP 8 and prefer `pathlib` for paths
- **TypeScript/React**: use function components and hooks
- **CSS**: prefer CSS variables such as `--bg`, `--text`, and `--acc`
- **Markdown**: use `#` headings, `-` lists, and language-tagged code fences

---

## Code of Conduct

- Be respectful and constructive
- Value different perspectives and experience levels
- Accept good-faith criticism
- Focus on what helps the project and community most
- Show empathy to other contributors

Harassment is not tolerated.

---

## Contact

- GitHub Issues: [report an issue](https://github.com/cft0808/edict/issues)
- GitHub Discussions: [join the discussion](https://github.com/cft0808/edict/discussions)

---

<p align="center">
  <sub>Thanks to every contributor helping improve Edict.</sub>
</p>

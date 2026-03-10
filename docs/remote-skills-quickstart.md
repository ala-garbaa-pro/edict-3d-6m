# Remote Skills Quickstart

## 5-Minute Walkthrough

### 1. Start the server

```bash
# Make sure you are in the project root
python3 dashboard/server.py
# Expected output: dashboard server started at http://127.0.0.1:7891
```

### 2. Add an official skill from the CLI

```bash
# Add the code review skill to zhongshu
python3 scripts/skill_manager.py add-remote \
  --agent zhongshu \
  --name code_review \
  --source https://raw.githubusercontent.com/openclaw-ai/skills-hub/main/code_review/SKILL.md \
  --description "Code review capability"

# Example output:
# ⏳ Downloading from https://raw.githubusercontent.com/...
# ✅ Added skill code_review to zhongshu
#    Path: /Users/xxx/.openclaw/workspace-zhongshu/skills/code_review/SKILL.md
#    Size: 2048 bytes
```

### 3. List all remote skills

```bash
python3 scripts/skill_manager.py list-remote

# Example output:
# 📋 1 remote skill found:
# 
# Agent       | Skill name           | Description                    | Added at
# ------------|----------------------|--------------------------------|----------
# zhongshu    | code_review          | Code review capability         | 2026-03-02
```

### 4. Inspect the API response

```bash
curl http://localhost:7891/api/remote-skills-list | jq .

# Example output:
# {
#   "ok": true,
#   "remoteSkills": [
#     {
#       "skillName": "code_review",
#       "agentId": "zhongshu",
#       "sourceUrl": "https://raw.githubusercontent.com/...",
#       "description": "Code review capability",
#       "localPath": "/Users/xxx/.openclaw/workspace-zhongshu/skills/code_review/SKILL.md",
#       "addedAt": "2026-03-02T14:30:00Z",
#       "lastUpdated": "2026-03-02T14:30:00Z",
#       "status": "valid"
#     }
#   ],
#   "count": 1,
#   "listedAt": "2026-03-02T14:35:00Z"
# }
```

---

## Common Operations

### Import official skills in one shot

```bash
python3 scripts/skill_manager.py import-official-hub \
  --agents zhongshu,menxia,shangshu,bingbu,xingbu
```

This imports a curated set of skills for each agent:
- `zhongshu`: `code_review`, `api_design`, `doc_generation`
- `menxia`: `code_review`, `api_design`, `security_audit`, `data_analysis`, `doc_generation`, `test_framework`
- `shangshu`: same set as `menxia`
- `bingbu`: `code_review`, `api_design`, `test_framework`
- `xingbu`: `code_review`, `security_audit`, `test_framework`

### Update a skill to the latest version

```bash
python3 scripts/skill_manager.py update-remote \
  --agent zhongshu \
  --name code_review

# Example output:
# ⏳ Downloading from https://raw.githubusercontent.com/...
# ✅ Added skill code_review to zhongshu
# ✅ Skill updated
#    Path: /Users/xxx/.openclaw/workspace-zhongshu/skills/code_review/SKILL.md
#    Size: 2156 bytes
```

### Remove a skill

```bash
python3 scripts/skill_manager.py remove-remote \
  --agent zhongshu \
  --name code_review

# Example output:
# ✅ Removed skill code_review from zhongshu
```

---

## Dashboard UI Workflow

### Add a remote skill from the dashboard

1. 打开 http://localhost:7891
2. Go to the `Skills` panel
3. Click `Add Remote Skill`
4. Fill in:
   - `Agent`: target agent, for example `zhongshu`
   - `Skill name`: internal ID such as `code_review`
   - `Remote URL`: a GitHub raw URL or another HTTPS source
   - `Description`: optional short label
5. Click `Import`
6. Wait 1-2 seconds for the success message

### Manage imported skills

In Dashboard → `Skills` → `Remote Skills`:

- `View`: inspect the `SKILL.md`
- `Update`: download the latest version again from the source URL
- `Delete`: remove the local copy
- `Copy URL`: share the source quickly

---

## Create Your Own Skill Hub

### Directory layout

```
my-skills-hub/
├── code_review/
│   └── SKILL.md
├── api_design/
│   └── SKILL.md
├── data_analysis/
│   └── SKILL.md
└── README.md
```

### SKILL.md template

```markdown
---
name: my_custom_skill
description: Short description
version: 1.0.0
tags: [tag1, tag2]
---

# Full skill name

Detailed description...

## Input

Describe accepted parameters

## Process

Steps...

## Output

Expected output format
```

### 上传到 GitHub

```bash
git init
git add .
git commit -m "Initial commit: my-skills-hub"
git remote add origin https://github.com/yourname/my-skills-hub
git push -u origin main
```

### 导入自己的 Skill

```bash
python3 scripts/skill_manager.py add-remote \
  --agent zhongshu \
  --name my_skill \
  --source https://raw.githubusercontent.com/yourname/my-skills-hub/main/my_skill/SKILL.md \
  --description "我的定制技能"
```

---

## API 完整参考

### POST /api/add-remote-skill

添加远程 skill。

**请求：**
```bash
curl -X POST http://localhost:7891/api/add-remote-skill \
  -H "Content-Type: application/json" \
  -d '{
    "agentId": "zhongshu",
    "skillName": "code_review",
    "sourceUrl": "https://raw.githubusercontent.com/...",
    "description": "代码审查"
  }'
```

**响应 (200):**
```json
{
  "ok": true,
  "message": "技能 code_review 已从远程源添加到 zhongshu",
  "skillName": "code_review",
  "agentId": "zhongshu",
  "source": "https://raw.githubusercontent.com/...",
  "localPath": "/Users/xxx/.openclaw/workspace-zhongshu/skills/code_review/SKILL.md",
  "size": 2048,
  "addedAt": "2026-03-02T14:30:00Z"
}
```

### GET /api/remote-skills-list

列出所有远程 skills。

```bash
curl http://localhost:7891/api/remote-skills-list
```

**响应:**
```json
{
  "ok": true,
  "remoteSkills": [
    {
      "skillName": "code_review",
      "agentId": "zhongshu",
      "sourceUrl": "https://raw.githubusercontent.com/...",
      "description": "代码审查能力",
      "localPath": "/Users/xxx/.openclaw/workspace-zhongshu/skills/code_review/SKILL.md",
      "addedAt": "2026-03-02T14:30:00Z",
      "lastUpdated": "2026-03-02T14:30:00Z",
      "status": "valid"
    }
  ],
  "count": 1,
  "listedAt": "2026-03-02T14:35:00Z"
}
```

### POST /api/update-remote-skill

更新远程 skill 为最新版本。

```bash
curl -X POST http://localhost:7891/api/update-remote-skill \
  -H "Content-Type: application/json" \
  -d '{
    "agentId": "zhongshu",
    "skillName": "code_review"
  }'
```

### DELETE /api/remove-remote-skill

移除远程 skill。

```bash
curl -X POST http://localhost:7891/api/remove-remote-skill \
  -H "Content-Type: application/json" \
  -d '{
    "agentId": "zhongshu",
    "skillName": "code_review"
  }'
```

---

## 故障排查

### Q: 下载失败，提示 "Connection timeout"

**A:** 检查网络连接和 URL 有效性

```bash
curl -I https://raw.githubusercontent.com/...
# 应该返回 HTTP/1.1 200 OK
```

### Q: 文件格式无效

**A:** 确保 SKILL.md 以 YAML frontmatter 开头

```markdown
---
name: skill_name
description: 描述
---

# 正文开始...
```

### Q: 导入后看不到 Skill

**A:** 刷新看板或检查 Agent 是否配置正确

```bash
# 检查 Agent 是否存在
python3 scripts/skill_manager.py list-remote

# 检查本地文件
ls -la ~/.openclaw/workspace-zhongshu/skills/
```

---

## 更多信息

- 📚 [完整指南](remote-skills-guide.md)
- 🏛️ [架构文档](task-dispatch-architecture.md)
- 🤝 [项目贡献](../CONTRIBUTING.md)

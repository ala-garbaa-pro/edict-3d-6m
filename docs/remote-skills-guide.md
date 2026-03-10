# Remote Skills Management Guide

## Overview

Edict can install and manage skill resources from remote sources without manual file copying. Supported sources include:

- GitHub raw URLs
- any HTTPS URL that returns a valid skill file
- local file paths
- the built-in official skills hub

---

## Feature Layout

### 1. API Endpoints

#### `POST /api/add-remote-skill`

Add a skill for a specific agent from a remote URL or local path.

**Request body**
```json
{
  "agentId": "zhongshu",
  "skillName": "code_review",
  "sourceUrl": "https://raw.githubusercontent.com/org/skills-repo/main/code_review/SKILL.md",
  "description": "Code review skill"
}
```

**Parameters**
- `agentId` (string, required): target agent ID
- `skillName` (string, required): internal skill name
- `sourceUrl` (string, required): remote URL or local file path
- `description` (string, optional): short description

**Success response**
```json
{
  "ok": true,
  "message": "Added code_review to zhongshu",
  "skillName": "code_review",
  "agentId": "zhongshu",
  "source": "https://raw.githubusercontent.com/...",
  "localPath": "/Users/bingsen/.openclaw/workspace-zhongshu/skills/code_review/SKILL.md",
  "size": 2048,
  "addedAt": "2026-03-02T14:30:00Z"
}
```

**Failure response**
```json
{
  "ok": false,
  "error": "URL is invalid or unreachable",
  "details": "Connection timeout after 10s"
}
```

#### `GET /api/remote-skills-list`

List all imported remote skills and their source metadata.

**响应：**
```json
{
  "ok": true,
  "remoteSkills": [
    {
      "skillName": "code_review",
      "agentId": "zhongshu",
      "sourceUrl": "https://raw.githubusercontent.com/org/skills-repo/main/code_review/SKILL.md",
      "description": "Code review skill",
      "localPath": "/Users/bingsen/.openclaw/workspace-zhongshu/skills/code_review/SKILL.md",
      "lastUpdated": "2026-03-02T14:30:00Z",
      "status": "valid"
    }
  ],
  "count": 5
}
```

#### `POST /api/update-remote-skill`

Update an imported remote skill to the latest source version.

**请求体：**
```json
{
  "agentId": "zhongshu",
  "skillName": "code_review"
}
```

**响应：**
```json
{
  "ok": true,
  "message": "Skill updated",
  "skillName": "code_review",
  "newVersion": "2.1.0",
  "updatedAt": "2026-03-02T15:00:00Z"
}
```

#### `DELETE /api/remove-remote-skill`

Remove an imported remote skill.

**请求体：**
```json
{
  "agentId": "zhongshu",
  "skillName": "code_review"
}
```

---

## CLI Commands

### Add a remote skill

```bash
python3 scripts/skill_manager.py add-remote \
  --agent zhongshu \
  --name code_review \
  --source https://raw.githubusercontent.com/org/skills-repo/main/code_review/SKILL.md \
  --description "Code review skill"
```

### List remote skills

```bash
python3 scripts/skill_manager.py list-remote
```

### Update a remote skill

```bash
python3 scripts/skill_manager.py update-remote \
  --agent zhongshu \
  --name code_review
```

### Remove a remote skill

```bash
python3 scripts/skill_manager.py remove-remote \
  --agent zhongshu \
  --name code_review
```

---

## Official Skills Hub

### OpenClaw Skills Hub

Official hub: https://github.com/openclaw-ai/skills-hub

Available skills:

| Skill | Description | Typical agents | Source URL |
|-----------|------|----------|--------|
| `code_review` | Code review for Python/JS/Go | Bingbu / Xingbu | https://raw.githubusercontent.com/openclaw-ai/skills-hub/main/code_review/SKILL.md |
| `api_design` | API design review | Bingbu / Gongbu | https://raw.githubusercontent.com/openclaw-ai/skills-hub/main/api_design/SKILL.md |
| `security_audit` | Security auditing | Xingbu | https://raw.githubusercontent.com/openclaw-ai/skills-hub/main/security_audit/SKILL.md |
| `data_analysis` | Data analysis | Hubu | https://raw.githubusercontent.com/openclaw-ai/skills-hub/main/data_analysis/SKILL.md |
| `doc_generation` | Document generation | Libu | https://raw.githubusercontent.com/openclaw-ai/skills-hub/main/doc_generation/SKILL.md |
| `test_framework` | Test framework design | Gongbu / Xingbu | https://raw.githubusercontent.com/openclaw-ai/skills-hub/main/test_framework/SKILL.md |

**Import the official set**

```bash
python3 scripts/skill_manager.py import-official-hub \
  --agents zhongshu,menxia,shangshu,bingbu,xingbu,libu
```

---

## Dashboard UI Workflow

### Quick add flow

1. Open the dashboard and go to the `Skills` panel.
2. Click `Add Remote Skill`.
3. Fill in the target agent, skill name, source URL, and optional description.
4. Confirm the import.

### Manage imported skills

Available actions:
- view the current `SKILL.md`
- update from the source URL
- remove the local copy
- copy the source URL

---

## Skill File Format

Remote skills should follow a standard Markdown structure.

### Minimum structure

```markdown
---
name: skill_internal_name
description: Short description
version: 1.0.0
tags: [tag1, tag2]
---

# Skill name

Detailed description...

## Input

Describe accepted parameters

## Process

List the steps

## Output

Describe the expected output format
```

### Full example

```markdown
---
name: code_review
description: Review Python or JavaScript code and propose improvements
version: 2.1.0
author: openclaw-ai
tags: [code-quality, security, performance]
compatibleAgents: [bingbu, xingbu, menxia]
---

# Code Review Skill

This skill is intended for multi-dimensional review of production code...

## Input

- `code`: source code to review
- `language`: 编程语言 (python, javascript, go, rust)
- `focusAreas`: 审查重点 (security, performance, style, structure)

## 处理流程

1. 语言识别与语法验证
2. 安全漏洞扫描
3. 性能瓶颈识别
4. 代码风格检查
5. 最佳实践建议

## 输出规范

```json
{
  "issues": [
    {
      "type": "security|performance|style|structure",
      "severity": "critical|high|medium|low",
      "location": "line:column",
      "message": "问题描述",
      "suggestion": "修复建议"
    }
  ],
  "summary": {
    "totalIssues": 3,
    "criticalCount": 1,
    "highCount": 2
  }
}
```

## 适用场景

- 兵部（代码实现）的代码产出审查
- 刑部（合规审计）的安全检查
- 门下省（审议把关）的质量评估

## 依赖与限制

- 需要 Python 3.9+
- 支持文件大小: 最多 50KB
- 执行超时: 30 秒
```

---

## 数据存储

### 本地存储结构

```
~/.openclaw/
├── workspace-zhongshu/
│   └── skills/
│       ├── code_review/
│       │   ├── SKILL.md
│       │   └── .source.json    # 存储源 URL 和元数据
│       └── api_design/
│           ├── SKILL.md
│           └── .source.json
├── ...
```

### .source.json 格式

```json
{
  "skillName": "code_review",
  "sourceUrl": "https://raw.githubusercontent.com/...",
  "description": "代码审查专项技能",
  "version": "2.1.0",
  "addedAt": "2026-03-02T14:30:00Z",
  "lastUpdated": "2026-03-02T14:30:00Z",
  "lastUpdateCheck": "2026-03-02T15:00:00Z",
  "checksum": "sha256:abc123...",
  "status": "valid"
}
```

---

## 安全考虑

### URL 验证

✅ **允许的 URL 类型:**
- HTTPS URLs: `https://`
- 本地文件: `file://` 或绝对路径
- 相对路径: `./skills/`

❌ **禁止的 URL 类型:**
- HTTP (非 HTTPS): `http://` 被拒绝
- 本地模式 HTTP: `http://localhost/` (避免环回攻击)
- FTP/SSH: `ftp://`, `ssh://`

### 内容验证

1. **格式验证**: 确保是有效的 Markdown YAML frontmatter
2. **大小限制**: 最多 10 MB
3. **超时保护**: 下载超过 30 秒自动中止
4. **路径遍历防护**: 检查解析后的 skill 名称，禁用 `../` 模式
5. **checksum 验证**: 可选的 GPG 签名验证（仅官方库）

### 隔离执行

- 远程 skills 在沙箱中执行（由 OpenClaw runtime 提供）
- 无法访问 `~/.openclaw/config.json` 等敏感文件
- 只能访问分配的 workspace 目录

---

## 故障排查

### 常见问题

**Q: 下载失败，提示 "Connection timeout"**

A: 检查网络连接和 URL 有效性：
```bash
curl -I https://raw.githubusercontent.com/...
```

**Q: Skill 显示 "invalid" 状态**

A: 检查文件格式：
```bash
python3 -m json.tool ~/.openclaw/workspace-zhongshu/skills/xxx/SKILL.md
```

**Q: 能否从私有 GitHub 仓库导入？**

A: 不支持（安全考虑）。可以：
1. 将仓库设为公开
2. 在本地下载后直接添加
3. 通过 GitHub Gist 的公开链接

**Q: 如何创建自己的 skills 库？**

A: 参考 [OpenClaw Skills Hub](https://github.com/openclaw-ai/skills-hub) 的结构创建自己的仓库，然后：

```bash
git clone https://github.com/yourname/my-skills-hub.git
cd my-skills-hub
# 创建 skill 文件结构
# 提交 & 推送到 GitHub
```

然后通过 URL 或官方库导入功能添加即可。

---

## 最佳实践

### 1. 版本管理

始终在 SKILL.md 的 frontmatter 中标注版本号：
```yaml
---
version: 2.1.0
---
```

### 2. 向后兼容

更新 skill 时保持输入/输出格式兼容，避免破坏现有流程。

### 3. 文档完整

包含详细的:
- 功能描述
- 适用场景
- 依赖说明
- 输出示例

### 4. 定期更新

设置定期检查更新（周期可在看板中配置）：
```bash
python3 scripts/skill_manager.py check-updates --interval weekly
```

### 5. 贡献社区

成熟的 skills 可向 [OpenClaw Skills Hub](https://github.com/openclaw-ai/skills-hub) 贡献。

---

## API 完整参考

详见 [任务分发流转架构文档](task-dispatch-architecture.md) 的第三部分（API 与工具）。

---

<p align="center">
  <sub>用 <strong>开放</strong> 的生态，赋能 <strong>制度化</strong> 的 AI 协作</sub>
</p>

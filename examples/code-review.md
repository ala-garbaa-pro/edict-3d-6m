# Example 2: FastAPI Security Review

> **Command:** Review a FastAPI codebase for security issues and produce a prioritized finding list plus fixes.

---

## Original Command

```
Review the following FastAPI code for security issues, focusing on:
1. authentication and authorization flaws
2. SQL injection risk
3. input validation
4. sensitive data exposure

Return a finding list ordered by severity and include fixes.

[Attachments: app/main.py, app/models.py, app/auth.py — 320 LOC total]
```

**Task ID:** `JJC-20260221-007`
**Issued at:** 2026-02-21 14:30:00

---

## Zhongshu Planning

Planning completed within 30 seconds.

**Plan**

| # | Subtask | Department | Notes |
|---|--------|----------|------|
| 1 | Code security scan | Bingbu | Inspect each file and flag issues |
| 2 | Compliance and best-practice review | Xingbu | Review against OWASP Top 10 |
| 3 | Fix output | Bingbu | Produce concrete fixes per issue |

**Estimated duration:** 12 minutes  
**Estimated tokens:** ~9,000

---

## Menxia Review

Review duration: 18 seconds.

### Approved on the first round

**Review note:** *"The division of work is sound. Bingbu handles engineering-side review, Xingbu handles compliance review. Xingbu must provide a line-by-line OWASP mapping rather than a vague 'mostly compliant' summary. Approved."*

---

## Department Outputs

### Bingbu: code security scan (5 minutes)

**Six issues found**

| # | Severity | File | Issue |
|---|--------|------|------|
| 1 | Critical | auth.py:23 | JWT secret is hardcoded in source |
| 2 | Critical | main.py:45 | SQL query uses f-string interpolation |
| 3 | High | main.py:67 | User input has no length limit |
| 4 | High | auth.py:41 | Token expiration is set to 30 days |
| 5 | Medium | main.py:12 | CORS uses `allow_origins=["*"]` |
| 6 | Medium | models.py:8 | Password field is exposed in response output |

### Xingbu: OWASP compliance check (4 minutes)

**OWASP Top 10 mapping**

| OWASP ID | Category | Status | Notes |
|-----------|------|------|------|
| A01 | Broken Access Control | Partial | JWT exists but role-level authorization is missing |
| A02 | Cryptographic Failures | Failing | Secret is hardcoded |
| A03 | Injection | Failing | SQL interpolation |
| A04 | Insecure Design | Pass | Overall architecture is reasonable |
| A05 | Security Misconfiguration | Needs improvement | CORS is too broad |
| A06 | Vulnerable Components | Pass | Dependencies are relatively current |
| A07 | Identification and Authentication Failures | Partial | Token lifetime is too long |
| A08 | Software and Data Integrity Failures | Pass | No major issue found |
| A09 | Security Logging and Monitoring Failures | Needs improvement | Security event logging is missing |
| A10 | SSRF | Pass | No external request path found |

**Xingbu conclusion:** 6 of 10 areas need action, including two failing categories that should be fixed immediately.

### Bingbu: fixes (3 minutes)

```python
# Fix #1: auth.py - load JWT secret from environment
import os
JWT_SECRET = os.environ["JWT_SECRET"]

# Fix #2: main.py - use parameterized SQL
from sqlalchemy import text
result = db.execute(text("SELECT * FROM users WHERE id = :id"), {"id": user_id})

# Fix #3: main.py - add input length limits
from pydantic import Field
class UserInput(BaseModel):
    name: str = Field(..., max_length=100)
    email: str = Field(..., max_length=255)

# Fix #4: auth.py - reduce token lifetime
ACCESS_TOKEN_EXPIRE = timedelta(hours=1)

# Fix #5: main.py - tighten CORS
app.add_middleware(CORSMiddleware, allow_origins=["https://yourdomain.com"])

# Fix #6: models.py - exclude password from response model
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    # password is intentionally omitted
```

---

## Final Memorial

**Memorial ID:** `JJC-20260221-007`  
**Total duration:** 14 minutes  
**Total tokens:** 8,200

### Summary

The system reviewed 320 lines of FastAPI code and found 6 security issues: 2 critical, 2 high, and 2 medium. Two OWASP categories were non-compliant. Fixes were provided for all six findings.

Menxia approved the plan on the first round. Bingbu covered code-level review and fixes, while Xingbu handled standards and compliance review.

### Suggested priority

1. **Immediate:** hardcoded JWT secret and SQL injection risk
2. **This week:** input length limits and token expiration policy
3. **Next iteration:** CORS restrictions and response-model cleanup

---

*Based on a real run. Code content has been redacted.*

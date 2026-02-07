# Security Review Checklist

A comprehensive security checklist for code reviews, organized by OWASP Top 10 and common vulnerability categories.

## Injection Vulnerabilities

### SQL Injection
```
VULNERABLE:
query = f"SELECT * FROM users WHERE id = {user_input}"

SECURE:
cursor.execute("SELECT * FROM users WHERE id = ?", (user_input,))
```

**Check for:**
- [ ] All database queries use parameterized statements
- [ ] ORMs configured to prevent raw query injection
- [ ] Dynamic table/column names validated against allowlist
- [ ] No string concatenation in query building

### Command Injection
```
VULNERABLE:
os.system(f"ping {user_input}")

SECURE:
subprocess.run(["ping", user_input], shell=False)
```

**Check for:**
- [ ] No shell=True with user input
- [ ] Command arguments as arrays, not strings
- [ ] Input validated against expected patterns
- [ ] Dangerous characters escaped or rejected

### XSS (Cross-Site Scripting)
```
VULNERABLE:
element.innerHTML = userInput;

SECURE:
element.textContent = userInput;
// Or use framework escaping
```

**Check for:**
- [ ] All user content HTML-escaped before rendering
- [ ] `innerHTML` not used with untrusted data
- [ ] Content Security Policy (CSP) headers set
- [ ] React/Vue/Angular auto-escaping not bypassed
- [ ] URL parameters sanitized before use

### Path Traversal
```
VULNERABLE:
file_path = f"/uploads/{user_filename}"

SECURE:
safe_name = os.path.basename(user_filename)
file_path = os.path.join("/uploads", safe_name)
```

**Check for:**
- [ ] User-provided paths normalized and validated
- [ ] No `..` sequences allowed in paths
- [ ] Base directory enforced
- [ ] Symlinks handled appropriately

---

## Authentication & Authorization

### Authentication
- [ ] Passwords hashed with bcrypt/argon2 (not MD5/SHA1)
- [ ] Password requirements enforced (length, complexity)
- [ ] Rate limiting on login attempts
- [ ] Account lockout after failed attempts
- [ ] Session tokens regenerated after login
- [ ] Secure password reset flow (time-limited tokens)

### Session Management
- [ ] Session tokens cryptographically random
- [ ] Sessions expire after inactivity
- [ ] Logout invalidates session server-side
- [ ] Cookies have Secure, HttpOnly, SameSite flags
- [ ] Session fixation prevented

### Authorization
- [ ] Every endpoint checks user permissions
- [ ] Authorization at data level, not just UI
- [ ] No reliance on hidden fields for authz
- [ ] Admin functions properly restricted
- [ ] IDOR (Insecure Direct Object Reference) prevented

```
VULNERABLE:
GET /api/users/{id}/profile  // Any user can access any profile

SECURE:
GET /api/users/{id}/profile
// Server validates: current_user.id == id OR current_user.is_admin
```

---

## Sensitive Data

### Secrets Management
- [ ] No hardcoded credentials in code
- [ ] API keys loaded from environment/secrets manager
- [ ] .env files in .gitignore
- [ ] No secrets in logs or error messages
- [ ] Secrets rotated periodically

**Patterns to flag:**
```
password = "secret123"           // Hardcoded
api_key = "sk-xxxxx"            // Hardcoded API key
connectionString = "...pwd=..." // Connection string in code
```

### Data Exposure
- [ ] Sensitive fields excluded from API responses
- [ ] No PII in URLs or query parameters
- [ ] Error messages don't leak internal details
- [ ] Stack traces disabled in production
- [ ] Logs don't contain sensitive data

### Encryption
- [ ] HTTPS enforced for all connections
- [ ] TLS 1.2+ required
- [ ] Sensitive data encrypted at rest
- [ ] Encryption keys properly managed
- [ ] No custom cryptography implementations

---

## Input Validation

### General Validation
- [ ] All input validated on server side
- [ ] Validation uses allowlists, not blocklists
- [ ] Input length limits enforced
- [ ] Type checking/coercion performed
- [ ] Encoding handled correctly (UTF-8)

### File Uploads
- [ ] File type validated by content, not extension
- [ ] File size limits enforced
- [ ] Uploaded files stored outside web root
- [ ] Filenames sanitized
- [ ] Antivirus scanning for uploads

### API Validation
- [ ] Request body schema validated
- [ ] Query parameters type-checked
- [ ] JSON/XML parsers configured securely
- [ ] Array/object nesting depth limited

---

## Common Web Vulnerabilities

### CSRF (Cross-Site Request Forgery)
- [ ] CSRF tokens on state-changing requests
- [ ] SameSite cookie attribute set
- [ ] Origin/Referer headers validated
- [ ] GET requests don't modify state

### Clickjacking
- [ ] X-Frame-Options header set
- [ ] CSP frame-ancestors directive configured
- [ ] Sensitive actions require re-authentication

### SSRF (Server-Side Request Forgery)
- [ ] URL destinations validated against allowlist
- [ ] Internal network addresses blocked
- [ ] Redirects limited or disabled
- [ ] DNS rebinding prevented

### Open Redirects
```
VULNERABLE:
redirect(request.params.get('next'))

SECURE:
next_url = request.params.get('next')
if is_safe_url(next_url, allowed_hosts):
    redirect(next_url)
```

---

## Dependency Security

### Third-Party Code
- [ ] Dependencies from trusted sources
- [ ] Package integrity verified (checksums/signatures)
- [ ] No known vulnerabilities in dependencies
- [ ] Dependencies regularly updated
- [ ] Minimal dependency footprint

**Commands to check:**
```bash
# Node.js
npm audit

# Python
pip-audit
safety check

# Go
govulncheck ./...

# Rust
cargo audit
```

---

## Logging & Monitoring

### Secure Logging
- [ ] Security events logged (auth, access, changes)
- [ ] Log injection prevented
- [ ] Logs don't contain sensitive data
- [ ] Log integrity protected
- [ ] Sufficient detail for forensics

### Events to Log
- Authentication attempts (success/failure)
- Authorization failures
- Input validation failures
- Application errors
- Admin actions
- Data access/modification

---

## Security Headers

**Required headers for web applications:**

```
Content-Security-Policy: default-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-XSS-Protection: 0  (deprecated, rely on CSP)
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), microphone=()
```

---

## Quick Security Grep Patterns

Search codebase for potential issues:

```bash
# Hardcoded secrets
grep -rn "password\s*=\s*['\"]" --include="*.py" --include="*.js"
grep -rn "api_key\s*=\s*['\"]" --include="*.py" --include="*.js"
grep -rn "secret\s*=\s*['\"]" --include="*.py" --include="*.js"

# SQL injection risks
grep -rn "execute.*\+" --include="*.py"
grep -rn "query.*\`" --include="*.js" --include="*.ts"

# Command injection risks
grep -rn "shell=True" --include="*.py"
grep -rn "exec(" --include="*.js" --include="*.ts"
grep -rn "child_process" --include="*.js" --include="*.ts"

# XSS risks
grep -rn "innerHTML" --include="*.js" --include="*.ts"
grep -rn "dangerouslySetInnerHTML" --include="*.jsx" --include="*.tsx"
grep -rn "v-html" --include="*.vue"

# Eval usage
grep -rn "eval(" --include="*.py" --include="*.js"
```

---

## Severity Classification

### Critical (Block Merge)
- SQL/Command injection
- Authentication bypass
- Hardcoded production credentials
- Remote code execution

### High (Requires Fix)
- XSS vulnerabilities
- CSRF without protection
- Broken authorization
- Sensitive data exposure

### Medium (Should Fix)
- Missing security headers
- Verbose error messages
- Weak cryptography
- Session management issues

### Low (Track for Later)
- Minor information disclosure
- Missing rate limiting
- Incomplete input validation

---
name: security-review
description: OWASP-based security code review. Use when the user says "security review", "OWASP", "vulnerability check", "secure code", "security audit", or wants to check code for security issues.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - Task
---

# Security Review Skill

Perform security-focused code reviews based on OWASP Top 10 and security best practices to identify vulnerabilities before they reach production.

## Invocation

This skill activates when:
- User asks for a security review
- User mentions "OWASP", "security audit", "vulnerability check"
- User wants to check if code is secure
- User asks about security best practices for code

Arguments: `$ARGUMENTS` (file paths, components to review, or specific security concerns)

---

## OWASP Top 10 (2025) Checklist

### A01: Broken Access Control

**What to look for:**
- [ ] Authorization checks on every endpoint/function
- [ ] Server-side enforcement (not just client-side)
- [ ] Principle of least privilege
- [ ] IDOR (Insecure Direct Object References)
- [ ] Missing function-level access control
- [ ] CORS misconfiguration

**Code patterns to flag:**
```javascript
// BAD: No authorization check
app.get('/api/users/:id', (req, res) => {
  return db.users.findById(req.params.id); // Anyone can access any user!
});

// GOOD: Authorization check
app.get('/api/users/:id', requireAuth, (req, res) => {
  if (req.user.id !== req.params.id && !req.user.isAdmin) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  return db.users.findById(req.params.id);
});
```

---

### A02: Security Misconfiguration

**What to look for:**
- [ ] Debug mode disabled in production
- [ ] Default credentials changed
- [ ] Unnecessary features disabled
- [ ] Security headers configured
- [ ] Error messages don't leak information
- [ ] Directory listing disabled

**Code patterns to flag:**
```javascript
// BAD: Debug in production
app.use(errorHandler({ debug: true }));

// BAD: Default secret
const JWT_SECRET = process.env.JWT_SECRET || 'secret123';

// BAD: Detailed errors to client
catch (error) {
  res.status(500).json({ error: error.stack }); // Leaks internals!
}
```

---

### A03: Software Supply Chain Failures

**What to look for:**
- [ ] Dependencies are up to date
- [ ] No known vulnerable packages
- [ ] Package integrity verified (lock files)
- [ ] CI/CD pipeline secured
- [ ] Third-party code reviewed

**Commands to run:**
```bash
# JavaScript/Node
npm audit
npx snyk test

# Python
pip-audit
safety check

# Go
govulncheck ./...
```

---

### A04: Cryptographic Failures

**What to look for:**
- [ ] Strong encryption algorithms (AES-256, RSA-2048+)
- [ ] Secure password hashing (bcrypt, Argon2)
- [ ] Proper key management
- [ ] TLS/HTTPS enforced
- [ ] Sensitive data encrypted at rest
- [ ] No hardcoded secrets

**Code patterns to flag:**
```javascript
// BAD: Weak hashing
const hash = crypto.createHash('md5').update(password).digest('hex');

// GOOD: Strong hashing
const hash = await bcrypt.hash(password, 12);

// BAD: Hardcoded secret
const API_KEY = 'sk-abc123...';

// GOOD: Environment variable
const API_KEY = process.env.API_KEY;
```

---

### A05: Injection

**What to look for:**
- [ ] SQL injection prevention (parameterized queries)
- [ ] Command injection prevention
- [ ] LDAP injection prevention
- [ ] NoSQL injection prevention
- [ ] Template injection prevention

**Code patterns to flag:**
```javascript
// BAD: SQL Injection
db.query(`SELECT * FROM users WHERE id = ${userId}`);

// GOOD: Parameterized query
db.query('SELECT * FROM users WHERE id = ?', [userId]);

// BAD: Command injection
exec(`ping ${userInput}`);

// GOOD: Use libraries that escape properly
execFile('ping', [userInput]);

// BAD: NoSQL injection
db.users.find({ username: req.body.username });

// GOOD: Validate input type
const username = String(req.body.username);
db.users.find({ username });
```

---

### A06: Insecure Design

**What to look for:**
- [ ] Threat modeling performed
- [ ] Rate limiting implemented
- [ ] Business logic flaws
- [ ] Missing re-authentication for sensitive operations
- [ ] Insufficient anti-automation

**Code patterns to flag:**
```javascript
// BAD: No rate limiting on auth
app.post('/api/login', loginHandler);

// GOOD: Rate limited
app.post('/api/login', rateLimit({ windowMs: 15*60*1000, max: 5 }), loginHandler);

// BAD: No re-auth for sensitive operations
app.post('/api/change-password', requireAuth, changePassword);

// GOOD: Re-authentication required
app.post('/api/change-password', requireAuth, requireCurrentPassword, changePassword);
```

---

### A07: Identification and Authentication Failures

**What to look for:**
- [ ] Secure password requirements
- [ ] Account lockout after failed attempts
- [ ] Secure session management
- [ ] Multi-factor authentication support
- [ ] Secure password recovery

**Code patterns to flag:**
```javascript
// BAD: Weak password requirement
if (password.length >= 4) { /* accept */ }

// GOOD: Strong requirements
const isStrong = password.length >= 12 &&
                 /[A-Z]/.test(password) &&
                 /[0-9]/.test(password) &&
                 /[^A-Za-z0-9]/.test(password);

// BAD: No session expiration
jwt.sign(payload, secret); // No expiration!

// GOOD: Session expiration
jwt.sign(payload, secret, { expiresIn: '1h' });
```

---

### A08: Software and Data Integrity Failures

**What to look for:**
- [ ] CI/CD pipeline integrity
- [ ] Signed artifacts
- [ ] Serialization security
- [ ] Subresource integrity for CDN assets

**Code patterns to flag:**
```html
<!-- BAD: No integrity check -->
<script src="https://cdn.example.com/lib.js"></script>

<!-- GOOD: Subresource integrity -->
<script src="https://cdn.example.com/lib.js"
        integrity="sha384-abc123..."
        crossorigin="anonymous"></script>
```

```javascript
// BAD: Unsafe deserialization
const data = JSON.parse(userInput);
eval(data.code); // Never do this!

// GOOD: Validate before use
const data = JSON.parse(userInput);
if (isValidSchema(data)) {
  processData(data);
}
```

---

### A09: Security Logging and Monitoring Failures

**What to look for:**
- [ ] Authentication events logged
- [ ] Authorization failures logged
- [ ] Input validation failures logged
- [ ] Logs don't contain sensitive data
- [ ] Logs protected from tampering

**Code patterns to flag:**
```javascript
// BAD: Logging sensitive data
logger.info(`User logged in: ${username} with password: ${password}`);

// GOOD: Log without sensitive data
logger.info(`User logged in: ${username}`);

// BAD: No logging on auth failure
if (!isValidPassword) {
  return res.status(401).json({ error: 'Invalid' });
}

// GOOD: Log auth failures
if (!isValidPassword) {
  logger.warn(`Failed login attempt for user: ${username} from IP: ${req.ip}`);
  return res.status(401).json({ error: 'Invalid' });
}
```

---

### A10: Mishandling of Exceptional Conditions

**What to look for:**
- [ ] Proper error handling
- [ ] Fail securely (deny by default)
- [ ] Resource cleanup on errors
- [ ] Error messages don't leak sensitive info

**Code patterns to flag:**
```javascript
// BAD: Fail open
try {
  const isAuthorized = await checkAuth(user);
} catch (error) {
  // Auth service failed, let them through anyway
  isAuthorized = true;
}

// GOOD: Fail closed
try {
  const isAuthorized = await checkAuth(user);
} catch (error) {
  logger.error('Auth service failed', error);
  return res.status(503).json({ error: 'Service unavailable' });
}
```

---

## XSS (Cross-Site Scripting) Prevention

**What to look for:**
- [ ] Output encoding for HTML context
- [ ] Content Security Policy headers
- [ ] HttpOnly cookies
- [ ] Input sanitization

**Code patterns to flag:**
```javascript
// BAD: Direct HTML insertion
element.innerHTML = userInput;

// GOOD: Use text content or sanitize
element.textContent = userInput;
// OR
element.innerHTML = DOMPurify.sanitize(userInput);

// BAD: No CSP
// Missing Content-Security-Policy header

// GOOD: CSP configured
app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'"],
  }
}));
```

---

## Security Review Report Template

```markdown
## Security Review Report

**Files Reviewed:** [list]
**Date:** [date]
**Reviewer:** [name]

### Summary
[Overall security posture assessment]

### Critical Findings
> Must fix before deployment

| ID | Category | Location | Description | Recommendation |
|----|----------|----------|-------------|----------------|
| 1 | A05 Injection | file.ts:42 | SQL injection via... | Use parameterized queries |

### High Severity
> Should fix before deployment

| ID | Category | Location | Description | Recommendation |
|----|----------|----------|-------------|----------------|

### Medium Severity
> Should fix soon

| ID | Category | Location | Description | Recommendation |
|----|----------|----------|-------------|----------------|

### Low Severity / Informational
> Consider fixing

| ID | Category | Location | Description | Recommendation |
|----|----------|----------|-------------|----------------|

### Positive Findings
- [Good security practices observed]

### Recommendations
1. [Prioritized recommendation]
2. [Prioritized recommendation]
```

---

## Quick Security Commands

**Check for secrets in code:**
```bash
# Using git-secrets
git secrets --scan

# Using trufflehog
trufflehog filesystem --directory=.

# Simple grep patterns
grep -r "password\|secret\|api_key" --include="*.js" --include="*.ts"
```

**Check HTTP security headers:**
```bash
curl -I https://example.com | grep -i "security\|policy\|strict"
```

**Check dependencies:**
```bash
# npm
npm audit

# Python
pip-audit

# Ruby
bundle audit check
```

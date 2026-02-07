---
name: threat-model
description: Threat modeling using STRIDE framework. Use when the user says "threat model", "security design", "attack vectors", "risk assessment", "security architecture", or wants to analyze potential threats to a system.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - Task
---

# Threat Modeling Skill

Guide through systematic threat modeling using the STRIDE framework to identify security risks before they become vulnerabilities.

## Invocation

This skill activates when:
- User wants to analyze security threats
- User mentions "threat model", "STRIDE", "security architecture"
- User asks about attack vectors or security risks
- User is designing a new system and wants security input

Arguments: `$ARGUMENTS` (system description, architecture diagrams, or specific components)

---

## The STRIDE Framework

STRIDE is a mnemonic for six categories of security threats:

| Threat | Description | Security Property Violated |
|--------|-------------|---------------------------|
| **S**poofing | Pretending to be someone/something else | Authentication |
| **T**ampering | Modifying data or code | Integrity |
| **R**epudiation | Denying actions taken | Non-repudiation |
| **I**nformation Disclosure | Exposing data to unauthorized parties | Confidentiality |
| **D**enial of Service | Making system unavailable | Availability |
| **E**levation of Privilege | Gaining unauthorized access | Authorization |

---

## Threat Modeling Process

### Step 1: Define Scope and Assets

**Identify what you're protecting:**

```markdown
## System Overview

**System Name:** [Name]
**Description:** [Brief description]
**Business Criticality:** [Critical/High/Medium/Low]

## Assets

| Asset | Type | Sensitivity | Description |
|-------|------|-------------|-------------|
| User PII | Data | High | Names, emails, addresses |
| Payment info | Data | Critical | Credit card numbers |
| API keys | Credential | High | Third-party integrations |
| Auth tokens | Credential | High | User session tokens |
| Audit logs | Data | Medium | System activity records |
```

### Step 2: Create a Data Flow Diagram (DFD)

**Components to identify:**

```markdown
## System Components

### External Entities (rectangles)
- Web Browser (User)
- Mobile App (User)
- Third-party API (External)
- Payment Processor (External)

### Processes (circles)
- Web Server
- API Server
- Authentication Service
- Payment Service
- Background Worker

### Data Stores (parallel lines)
- User Database
- Session Cache
- Message Queue
- File Storage

### Trust Boundaries (dashed lines)
- Public Internet ↔ DMZ
- DMZ ↔ Internal Network
- Application ↔ Database
```

**Data Flow Diagram (ASCII):**

```
                         Trust Boundary
                              |
    [User Browser] ----HTTP-->| [Web Server] -----> [Auth Service]
                              |       |
                              |       ↓
    [Mobile App] ----API---->| [API Server] -----> [User DB]
                              |       |
                              |       ↓
    [Payment API] <----------| [Payment Service]
                              |
```

### Step 3: Apply STRIDE to Each Component

For each component and data flow, analyze threats:

---

## STRIDE Threat Analysis

### S - Spoofing Threats

**Question:** Can an attacker pretend to be a legitimate user, component, or system?

**Common attack vectors:**
- Credential theft (phishing, keyloggers)
- Session hijacking
- Token replay attacks
- Man-in-the-middle attacks
- Forged requests (CSRF)

**Checklist:**
- [ ] Authentication required for sensitive operations
- [ ] Multi-factor authentication available
- [ ] Strong password policies enforced
- [ ] Session tokens are unpredictable
- [ ] Certificate pinning for mobile apps
- [ ] HTTPS enforced everywhere

**Mitigations:**
| Threat | Mitigation |
|--------|------------|
| Credential stuffing | Rate limiting, MFA |
| Session hijacking | HttpOnly cookies, short expiry |
| CSRF | CSRF tokens, SameSite cookies |
| Man-in-the-middle | TLS everywhere, cert pinning |

---

### T - Tampering Threats

**Question:** Can an attacker modify data in transit or at rest?

**Common attack vectors:**
- SQL/NoSQL injection
- Parameter manipulation
- File upload attacks
- Code injection
- Cache poisoning

**Checklist:**
- [ ] Input validation on all user data
- [ ] Parameterized queries for databases
- [ ] Integrity checks on file uploads
- [ ] Code signing for deployments
- [ ] Database audit logging enabled

**Mitigations:**
| Threat | Mitigation |
|--------|------------|
| SQL injection | Parameterized queries, ORM |
| File tampering | Checksums, signed uploads |
| Code injection | Input sanitization, CSP |
| Config tampering | Immutable infrastructure |

---

### R - Repudiation Threats

**Question:** Can users deny their actions without being disproved?

**Common attack vectors:**
- Deleting or modifying logs
- Performing actions without audit trail
- Shared credentials preventing attribution
- Time-based attacks on logging

**Checklist:**
- [ ] Comprehensive audit logging
- [ ] Log integrity protection (append-only)
- [ ] Non-repudiable actions (digital signatures)
- [ ] Individual accountability (no shared accounts)
- [ ] Timestamp synchronization (NTP)

**Mitigations:**
| Threat | Mitigation |
|--------|------------|
| Log tampering | Immutable audit logs, SIEM |
| Denied transactions | Digital signatures |
| Anonymous actions | Individual accounts, attribution |

---

### I - Information Disclosure Threats

**Question:** Can sensitive data be exposed to unauthorized parties?

**Common attack vectors:**
- Error messages leaking info
- Verbose logging
- Insecure data storage
- Data in URL parameters
- Backup exposure
- Side-channel attacks

**Checklist:**
- [ ] Data classification defined
- [ ] Encryption at rest and in transit
- [ ] Sensitive data not in logs
- [ ] Proper access controls on data
- [ ] Secure error handling (no stack traces)
- [ ] Data masking for non-production

**Mitigations:**
| Threat | Mitigation |
|--------|------------|
| Data leaks | Encryption, access control |
| Verbose errors | Generic error messages |
| Log exposure | Scrub PII from logs |
| Backup theft | Encrypted backups |

---

### D - Denial of Service Threats

**Question:** Can an attacker make the system unavailable?

**Common attack vectors:**
- Resource exhaustion (CPU, memory, disk)
- Network flooding
- Application-layer attacks (slowloris)
- Logical DoS (expensive queries)
- Amplification attacks

**Checklist:**
- [ ] Rate limiting on all endpoints
- [ ] Resource quotas per user/tenant
- [ ] Timeouts on all operations
- [ ] DDoS protection (WAF, CDN)
- [ ] Graceful degradation plan
- [ ] Auto-scaling configured

**Mitigations:**
| Threat | Mitigation |
|--------|------------|
| Volumetric DDoS | CDN, DDoS protection |
| App-layer DoS | Rate limiting, WAF |
| Resource exhaustion | Quotas, timeouts |
| Logical DoS | Query complexity limits |

---

### E - Elevation of Privilege Threats

**Question:** Can an attacker gain higher privileges than intended?

**Common attack vectors:**
- Privilege escalation bugs
- Insecure direct object references (IDOR)
- Role confusion
- JWT manipulation
- Path traversal

**Checklist:**
- [ ] Principle of least privilege
- [ ] Authorization checks on every request
- [ ] Role-based access control (RBAC)
- [ ] Object-level permissions
- [ ] Secure token validation
- [ ] Regular privilege audits

**Mitigations:**
| Threat | Mitigation |
|--------|------------|
| IDOR | Object-level authorization |
| Role manipulation | Server-side role enforcement |
| JWT attacks | Signature validation, short expiry |
| Path traversal | Input validation, sandboxing |

---

## Threat Model Document Template

```markdown
# Threat Model: [System Name]

## Document Information
- **Version:** 1.0
- **Date:** [Date]
- **Author:** [Author]
- **Reviewers:** [Names]

## 1. System Description

### 1.1 Overview
[High-level description of the system]

### 1.2 Architecture Diagram
[Include DFD or architecture diagram]

### 1.3 Technologies Used
- Frontend: [e.g., React, Vue]
- Backend: [e.g., Node.js, Python]
- Database: [e.g., PostgreSQL, MongoDB]
- Infrastructure: [e.g., AWS, GCP]

## 2. Assets

| Asset | Sensitivity | Location | Owner |
|-------|-------------|----------|-------|
| [Asset] | [Critical/High/Medium/Low] | [Where stored] | [Team] |

## 3. Trust Boundaries

| Boundary | Components | Security Controls |
|----------|------------|-------------------|
| [Name] | [What crosses it] | [Controls in place] |

## 4. Threat Analysis

### 4.1 Spoofing
| ID | Threat | Risk | Mitigation | Status |
|----|--------|------|------------|--------|
| S1 | [Threat] | [H/M/L] | [Mitigation] | [Mitigated/Accepted/Open] |

### 4.2 Tampering
| ID | Threat | Risk | Mitigation | Status |
|----|--------|------|------------|--------|
| T1 | [Threat] | [H/M/L] | [Mitigation] | [Status] |

### 4.3 Repudiation
| ID | Threat | Risk | Mitigation | Status |
|----|--------|------|------------|--------|
| R1 | [Threat] | [H/M/L] | [Mitigation] | [Status] |

### 4.4 Information Disclosure
| ID | Threat | Risk | Mitigation | Status |
|----|--------|------|------------|--------|
| I1 | [Threat] | [H/M/L] | [Mitigation] | [Status] |

### 4.5 Denial of Service
| ID | Threat | Risk | Mitigation | Status |
|----|--------|------|------------|--------|
| D1 | [Threat] | [H/M/L] | [Mitigation] | [Status] |

### 4.6 Elevation of Privilege
| ID | Threat | Risk | Mitigation | Status |
|----|--------|------|------------|--------|
| E1 | [Threat] | [H/M/L] | [Mitigation] | [Status] |

## 5. Risk Summary

| Risk Level | Count | Examples |
|------------|-------|----------|
| Critical | [N] | [IDs] |
| High | [N] | [IDs] |
| Medium | [N] | [IDs] |
| Low | [N] | [IDs] |

## 6. Recommendations

### Priority 1 (Immediate)
1. [Recommendation]

### Priority 2 (Short-term)
1. [Recommendation]

### Priority 3 (Long-term)
1. [Recommendation]

## 7. Assumptions and Limitations

- [Assumption about the analysis]
- [Known limitation]

## 8. Review Schedule

This threat model should be reviewed:
- When significant changes are made
- Annually at minimum
- After security incidents
```

---

## Risk Assessment Matrix

| Impact | Likelihood: Low | Likelihood: Medium | Likelihood: High |
|--------|-----------------|-------------------|------------------|
| **Critical** | High | Critical | Critical |
| **High** | Medium | High | Critical |
| **Medium** | Low | Medium | High |
| **Low** | Low | Low | Medium |

---

## Quick Reference: Questions per Component

### Web Application
- How are users authenticated?
- How is session state managed?
- What input validation exists?
- How are errors handled?
- What logging is in place?

### API
- How are API calls authenticated?
- Is rate limiting in place?
- What data validation exists?
- Are all endpoints documented?
- What happens on error?

### Database
- How are connections authenticated?
- Is data encrypted at rest?
- What are the access controls?
- Is there query logging?
- How are backups protected?

### Message Queue
- How are publishers authenticated?
- How are messages protected?
- What happens if queue is full?
- How are poison messages handled?

### External Integration
- How is the connection secured?
- What data is exchanged?
- What happens if they're compromised?
- Is there a fallback?

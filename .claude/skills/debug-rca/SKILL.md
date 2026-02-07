---
name: debug-rca
description: Systematic debugging and root cause analysis. Use when the user says "debug", "root cause", "why is this happening", "investigate bug", "troubleshoot", or needs help understanding why something is broken.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - Task
---

# Debug & Root Cause Analysis Skill

A systematic approach to debugging issues and finding root causes using proven techniques like the 5 Whys and the RIACP framework.

## Invocation

This skill activates when:
- User needs help debugging an issue
- User asks "why is this happening?"
- User mentions "root cause", "investigate", "troubleshoot"
- User describes unexpected behavior or errors

Arguments: `$ARGUMENTS` (error messages, symptoms, or problem description)

---

## The RIACP Framework

A systematic debugging workflow:

| Phase | Description |
|-------|-------------|
| **R**eproduce | Consistently trigger the bug |
| **I**solate | Narrow down the cause |
| **A**nalyze | Understand *why* it happens |
| **C**orrect | Fix the root cause |
| **P**revent | Add tests and safeguards |

---

## Phase 1: Reproduce

### Goals
- Confirm the bug exists
- Find reliable reproduction steps
- Identify the minimal reproduction case

### Process

1. **Gather information**
   - What is the expected behavior?
   - What is the actual behavior?
   - When did this start happening?
   - What changed recently?

2. **Create reproduction steps**
   ```markdown
   ## Steps to Reproduce
   1. [First action]
   2. [Second action]
   3. [Third action]

   ## Expected Result
   [What should happen]

   ## Actual Result
   [What actually happens]

   ## Environment
   - OS: [e.g., Windows 11, macOS 14]
   - Runtime: [e.g., Node 20, Python 3.11]
   - Version: [app version or commit]
   ```

3. **Verify reproduction**
   - Can you trigger it 100% of the time?
   - If intermittent, what conditions affect it?

### Red Flags (Reproduction Issues)
- "It works on my machine" → Environment difference
- "It only happens sometimes" → Race condition, timing, or state-dependent
- "It only happens in production" → Data, scale, or configuration difference

---

## Phase 2: Isolate

### Goals
- Narrow down the problem area
- Identify the specific component/function/line causing the issue

### Techniques

**Binary Search Debugging**
- Comment out half the code, does the bug persist?
- Keep halving until you find the problematic section

**Input Isolation**
- What's the minimal input that triggers the bug?
- Which specific field/value causes the problem?

**Environment Isolation**
- Does it happen in a fresh environment?
- Does it happen with default configuration?

**Time/Commit Isolation (Git Bisect)**
```bash
# Start bisect
git bisect start

# Mark current state as bad
git bisect bad

# Mark a known good commit
git bisect good <commit-hash>

# Git checks out middle commit, test and mark:
git bisect good  # or
git bisect bad

# Repeat until culprit found
git bisect reset  # when done
```

**Component Isolation Questions**
- Frontend or backend?
- Client or server?
- Code or configuration?
- Your code or dependency?
- Development or production only?

---

## Phase 3: Analyze (5 Whys Technique)

### Goals
- Understand the true root cause
- Go beyond symptoms to underlying issues

### The 5 Whys Process

Start with the symptom and ask "Why?" repeatedly:

```markdown
## 5 Whys Analysis

**Problem**: Users are seeing 500 errors on the checkout page

1. **Why are users seeing 500 errors?**
   → The payment service is throwing an unhandled exception

2. **Why is the payment service throwing an exception?**
   → It's receiving null for the customer email field

3. **Why is the email field null?**
   → The frontend form allows submission with empty email

4. **Why does the form allow empty email?**
   → Validation was removed during a recent refactor

5. **Why was validation removed during the refactor?**
   → There were no tests covering the validation behavior

**Root Cause**: Missing test coverage for form validation
**Contributing Factor**: No validation on backend (defense in depth missing)
```

### Analysis Tools

**Log Analysis**
```bash
# Search logs for errors
grep -i "error\|exception\|failed" /var/log/app.log | tail -50

# Follow logs in real-time
tail -f /var/log/app.log | grep -i error

# Check for patterns around timestamp
grep "2024-01-15 14:3" /var/log/app.log
```

**Stack Trace Analysis**
- Start from the top (most recent call)
- Find the first line in YOUR code
- Look at the immediate cause and context

**Database Investigation**
```sql
-- Check for unexpected NULL values
SELECT * FROM users WHERE email IS NULL;

-- Look for recent changes
SELECT * FROM audit_log WHERE created_at > NOW() - INTERVAL '1 hour';

-- Check for constraint violations
SELECT * FROM orders WHERE customer_id NOT IN (SELECT id FROM customers);
```

---

## Phase 4: Correct

### Goals
- Fix the root cause, not just the symptom
- Avoid introducing new issues

### Fix Principles

1. **Fix the root cause, not symptoms**
   - Bad: Add try-catch to suppress the error
   - Good: Fix why the error occurs in the first place

2. **Minimal change principle**
   - Change as little as possible
   - Avoid "while I'm here" fixes in the same commit

3. **Verify the fix**
   - Does it fix all reproduction cases?
   - Does it pass existing tests?
   - Does it handle edge cases?

### Fix Template

```markdown
## Fix Summary

**Root Cause**: [What was actually wrong]

**Solution**: [What we changed and why]

**Files Changed**:
- `path/to/file.ts` - [What changed]

**Verification**:
- [ ] Reproduction case no longer occurs
- [ ] All existing tests pass
- [ ] New test added for this scenario
- [ ] Tested in environment where bug occurred
```

---

## Phase 5: Prevent

### Goals
- Ensure this bug never happens again
- Improve system resilience

### Prevention Checklist

- [ ] **Add regression test** that would have caught this bug
- [ ] **Add input validation** at boundaries
- [ ] **Add logging/monitoring** for similar issues
- [ ] **Update documentation** if behavior was unclear
- [ ] **Create runbook** if this could happen again
- [ ] **Review similar code** for same pattern

### Post-Mortem Template

```markdown
## Bug Post-Mortem: [Brief Description]

### Timeline
- [Time] - Bug reported
- [Time] - Investigation started
- [Time] - Root cause identified
- [Time] - Fix deployed

### Root Cause
[Technical explanation of what went wrong]

### Impact
- [Number] users affected
- [Duration] of impact
- [Business impact if any]

### What Went Well
- [Quick detection, effective debugging, etc.]

### What Could Be Improved
- [Missing tests, monitoring gaps, etc.]

### Action Items
- [ ] [Specific action] - Owner: @person - Due: [date]
- [ ] [Specific action] - Owner: @person - Due: [date]

### Lessons Learned
- [Key takeaway for the team]
```

---

## Common Bug Patterns

### Race Conditions
**Symptoms**: Works sometimes, fails randomly
**Investigation**: Add logging with timestamps, look for parallel execution
**Fix**: Locks, transactions, or redesign to avoid shared state

### Off-by-One Errors
**Symptoms**: Missing first/last item, array out of bounds
**Investigation**: Check loop boundaries, array indexing
**Fix**: Careful review of boundary conditions

### Null/Undefined References
**Symptoms**: "Cannot read property of undefined"
**Investigation**: Trace data flow, find where value becomes null
**Fix**: Add null checks, use optional chaining, fix data source

### State Management Issues
**Symptoms**: Stale data, inconsistent UI
**Investigation**: Log state changes, check update timing
**Fix**: Proper state synchronization, fix update logic

### Memory Leaks
**Symptoms**: Performance degradation over time
**Investigation**: Memory profiling, check for unbounded growth
**Fix**: Clean up event listeners, clear caches, fix circular references

### N+1 Queries
**Symptoms**: Slow database operations, many similar queries
**Investigation**: Enable query logging, look for loops with queries
**Fix**: Eager loading, batch queries, caching

---

## Quick Debugging Commands

**Check recent changes**
```bash
git log --oneline -20
git diff HEAD~5..HEAD
```

**Search codebase for pattern**
```bash
grep -r "functionName" --include="*.ts"
```

**Check process status**
```bash
# Node.js
node --inspect app.js

# Python
python -m pdb script.py
```

**Network debugging**
```bash
# Check if port is in use
netstat -an | grep :3000

# Test endpoint
curl -v http://localhost:3000/api/health
```

---

## When to Escalate

Consider escalating when:
- Reproduction takes more than 2 hours
- Root cause spans multiple systems/teams
- Fix requires architectural changes
- Bug has security implications
- Impact is growing while investigating

**Escalation Template**:
```markdown
## Bug Escalation

**Summary**: [One sentence]
**Severity**: [Critical/High/Medium/Low]
**Impact**: [Who/what is affected]
**Investigation so far**: [What you've tried]
**Blockers**: [Why you need help]
**Suspected area**: [Your best guess]
```

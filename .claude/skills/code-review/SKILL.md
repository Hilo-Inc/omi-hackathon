---
name: code-review
description: Performs thorough code reviews on files, commits, pull requests, or diffs. Use when reviewing code, checking code quality, auditing changes, or when the user says "review", "code review", "check my code", or "audit".
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - Task
---

# Code Review Skill

Perform comprehensive code reviews that provide actionable, constructive feedback.

## Invocation

This skill activates when:
- User asks to review code, files, or changes
- User mentions "code review", "review my code", "check this code"
- User wants to audit a commit, PR, or diff

Arguments: `$ARGUMENTS` (file paths, commit hashes, or PR numbers)

## Review Process

### 1. Gather Context

First, understand what needs to be reviewed:

```bash
# For uncommitted changes
git diff

# For staged changes
git diff --staged

# For a specific commit
git show <commit-hash>

# For a branch comparison
git diff main..HEAD
```

### 2. Analyze the Code

Review each file/change against these categories:

#### Correctness
- Does the code do what it's supposed to do?
- Are there logic errors or edge cases not handled?
- Are there off-by-one errors, null pointer risks, or race conditions?

#### Security
- Input validation and sanitization
- SQL injection, XSS, command injection risks
- Hardcoded secrets or credentials
- Proper authentication/authorization checks
- See [security-checks.md](security-checks.md) for detailed checklist

#### Code Quality
- Clear, descriptive naming (variables, functions, classes)
- Single responsibility principle
- DRY (Don't Repeat Yourself)
- Appropriate abstraction level
- Consistent code style

#### Performance
- Unnecessary loops or redundant operations
- N+1 query patterns
- Memory leaks or resource cleanup
- Inefficient algorithms for the data size

#### Maintainability
- Is the code easy to understand?
- Are complex sections documented?
- Is it testable?
- Does it follow project conventions?

#### Error Handling
- Are errors properly caught and handled?
- Are error messages helpful for debugging?
- Is there appropriate logging?

### 3. Format Your Review

Structure feedback as follows:

```markdown
## Code Review Summary

**Files Reviewed:** [list files]
**Overall Assessment:** [APPROVE / REQUEST CHANGES / NEEDS DISCUSSION]

### Critical Issues
> Issues that must be fixed before merging

- **[FILE:LINE]** [Category] Description of issue
  - Suggested fix or approach

### Suggestions
> Improvements that would enhance the code

- **[FILE:LINE]** [Category] Description
  - Recommendation

### Positive Observations
> What's done well (reinforce good practices)

- [Observation]

### Questions
> Clarifications needed from the author

- [Question about design decision or intent]
```

## Review Guidelines

### Be Constructive
- Focus on the code, not the person
- Explain *why* something is an issue
- Provide concrete suggestions, not just criticism
- Acknowledge good work

### Prioritize Feedback
1. **Critical**: Security vulnerabilities, bugs, data loss risks
2. **Important**: Performance issues, maintainability problems
3. **Minor**: Style, naming, documentation improvements
4. **Nitpick**: Preferences (mark as optional)

### Context Matters
- Consider the PR's scope and purpose
- Don't demand unrelated refactoring
- Understand project constraints and conventions

## Language-Specific Checklists

For detailed checklists by language/framework, see [checklists.md](checklists.md).

## Quick Commands

Review current staged changes:
```bash
git diff --staged
```

Review a specific file:
```bash
# Read and analyze
cat path/to/file.ts
```

Review recent commits:
```bash
git log --oneline -10
git show HEAD
```

Compare with main branch:
```bash
git diff main..HEAD --stat
git diff main..HEAD
```

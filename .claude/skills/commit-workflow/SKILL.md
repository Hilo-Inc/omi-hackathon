---
name: commit-workflow
description: Generates Conventional Commits messages, changelogs, and release notes. Use when the user says "commit", "changelog", "release notes", "version bump", "prepare release", or wants help with git commit messages.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - Task
---

# Commit Workflow Skill

Generate professional commit messages following the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification, auto-generate changelogs, and prepare release notes.

## Invocation

This skill activates when:
- User asks for help with commit messages
- User mentions "conventional commit", "changelog", "release notes"
- User wants to "prepare a release" or "version bump"

Arguments: `$ARGUMENTS` (optional: specific files, version number, or release type)

## Workflow Modes

| Mode | Trigger | Description |
|------|---------|-------------|
| **Commit** | "commit", "commit message" | Generate a conventional commit message for staged changes |
| **Changelog** | "changelog", "generate changelog" | Generate CHANGELOG.md from commit history |
| **Release** | "release", "prepare release", "version bump" | Prepare release notes and version bump |

---

## Mode 1: Commit Message Generation

### Process

1. **Analyze staged changes**
   ```bash
   git diff --staged --stat
   git diff --staged
   ```

2. **Identify the change type** based on the diff:
   - `feat`: New feature for the user
   - `fix`: Bug fix for the user
   - `docs`: Documentation only changes
   - `style`: Formatting, missing semi-colons, etc. (no code change)
   - `refactor`: Code change that neither fixes a bug nor adds a feature
   - `perf`: Performance improvement
   - `test`: Adding or correcting tests
   - `build`: Changes to build system or dependencies
   - `ci`: Changes to CI configuration
   - `chore`: Other changes that don't modify src or test files
   - `revert`: Reverts a previous commit

3. **Determine scope** (optional): The area of the codebase affected
   - Examples: `api`, `ui`, `auth`, `db`, `config`

4. **Check for breaking changes**: Look for:
   - API signature changes
   - Removed or renamed exports
   - Changed default behavior
   - Database schema changes requiring migration

5. **Generate the commit message**

### Commit Message Format

```
<type>[optional scope][!]: <description>

[optional body]

[optional footer(s)]
```

**Structure Rules:**
- **Header**: Max 72 characters, imperative mood ("add" not "added")
- **Body**: Wrap at 72 characters, explain *what* and *why* (not *how*)
- **Footer**: References to issues, breaking change notes

### Examples

**Simple feature:**
```
feat(auth): add password reset functionality
```

**Bug fix with body:**
```
fix(api): prevent race condition in user creation

Multiple concurrent requests could create duplicate users.
Added mutex lock around the user creation transaction.

Fixes #234
```

**Breaking change:**
```
feat(api)!: change authentication endpoint response format

BREAKING CHANGE: The /auth/login endpoint now returns a structured
response with `token` and `user` fields instead of just the token string.

Migration: Update all clients to extract `response.token` instead of
using the response directly.
```

**Multiple changes (use separate commits):**
```
refactor(db): extract query builder into separate module

test(db): add unit tests for query builder

feat(db): add support for complex joins in query builder
```

---

## Mode 2: Changelog Generation

### Process

1. **Analyze commit history since last tag**
   ```bash
   git log --oneline $(git describe --tags --abbrev=0 2>/dev/null || echo "")..HEAD
   ```

2. **Parse commits by type** and group them

3. **Generate CHANGELOG.md entry**

### Changelog Format

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New feature X (#123)
- New feature Y (#124)

### Changed
- Updated behavior of Z (#125)

### Deprecated
- Feature A will be removed in v2.0

### Removed
- Removed deprecated feature B

### Fixed
- Fixed bug in C (#126)
- Fixed crash when D (#127)

### Security
- Patched vulnerability in E (#128)

## [1.0.0] - 2024-01-15

### Added
- Initial release
```

### Mapping Conventional Commits to Changelog

| Commit Type | Changelog Section |
|-------------|-------------------|
| `feat` | Added |
| `fix` | Fixed |
| `perf` | Changed |
| `refactor` | Changed |
| `docs` | (usually omitted, or Changed) |
| `style` | (usually omitted) |
| `test` | (usually omitted) |
| `build` | Changed |
| `ci` | (usually omitted) |
| `chore` | (usually omitted) |
| `BREAKING CHANGE` | Changed (highlight prominently) |
| Security fixes | Security |

---

## Mode 3: Release Preparation

### Process

1. **Determine version bump** based on commits since last release:
   - `BREAKING CHANGE` or `!` → **Major** (1.0.0 → 2.0.0)
   - `feat` → **Minor** (1.0.0 → 1.1.0)
   - `fix`, `perf`, etc. → **Patch** (1.0.0 → 1.0.1)

2. **Generate release notes**

3. **Update version files** (if applicable):
   - `package.json`
   - `Cargo.toml`
   - `pyproject.toml`
   - `version.go`

4. **Update CHANGELOG.md** with release date

### Release Notes Template

```markdown
# Release v1.2.0

## Highlights

[2-3 sentence summary of the most important changes]

## What's New

### Features
- **Feature Name**: Brief description (#PR)

### Improvements
- Improvement description (#PR)

### Bug Fixes
- Fix description (#PR)

### Breaking Changes
- **Action Required**: Description of what users need to do

## Upgrade Guide

[Steps to upgrade from previous version, if needed]

## Contributors

Thanks to @contributor1, @contributor2 for their contributions!

## Full Changelog

[Link to compare view or full changelog]
```

---

## Commit Message Quality Checklist

Before finalizing a commit message, verify:

- [ ] Type accurately describes the change
- [ ] Scope is specific and consistent with project conventions
- [ ] Description is in imperative mood ("add" not "added")
- [ ] Description explains *what* changed, not *how*
- [ ] Breaking changes are marked with `!` and explained in footer
- [ ] Issue/PR references included in footer if applicable
- [ ] Header is under 72 characters
- [ ] Body lines wrapped at 72 characters

---

## Quick Commands

**View staged changes:**
```bash
git diff --staged
```

**View recent commits:**
```bash
git log --oneline -20
```

**View commits since last tag:**
```bash
git log --oneline $(git describe --tags --abbrev=0)..HEAD
```

**List all tags:**
```bash
git tag --sort=-v:refname
```

**Create annotated tag:**
```bash
git tag -a v1.0.0 -m "Release v1.0.0"
```

---

## Common Patterns

### Squash Commits

When asked to help squash commits:
```bash
# Interactive rebase for last N commits
git rebase -i HEAD~N

# In the editor, change 'pick' to 'squash' or 's' for commits to combine
```

### Amend Last Commit

```bash
# Change message only
git commit --amend -m "new message"

# Add more changes to last commit
git add .
git commit --amend --no-edit
```

### Revert a Commit

```
revert: undo feature X

This reverts commit abc1234.

Reason: Feature X caused performance regression in production.
```

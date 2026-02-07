# Task Processing Reference

Detailed guidelines for working through task lists systematically.

## Core Principles

### 1. One Sub-Task at a Time

**NEVER** proceed to the next sub-task without explicit user permission.

After completing each sub-task:
1. Update the task file (mark `[x]`)
2. Report what was done
3. Ask: "Ready to proceed to the next task?"
4. **Wait** for "yes", "y", or similar confirmation

### 2. Immediate Completion Marking

The moment a sub-task is done:
```markdown
# Before
- [ ] 2.1 Create GET /api/profile/:id endpoint

# After
- [x] 2.1 Create GET /api/profile/:id endpoint
```

Do this IMMEDIATELY, not in batches.

### 3. Parent Task Completion Protocol

When ALL sub-tasks under a parent are `[x]`:

```
Step 1: Run full test suite
        └─ npm test / pytest / flutter test / etc.

Step 2: Only if tests pass → git add .
        └─ If tests fail, fix them first

Step 3: Clean up
        └─ Remove console.logs, debug code, temp files

Step 4: Commit with descriptive message
        └─ Use conventional commits format

Step 5: Mark parent task [x]
```

## Commit Message Format

Use the `-m` flag format for clean single-line commits:

```bash
git commit -m "feat: add profile editing API" -m "- GET /api/profile/:id returns user profile" -m "- PATCH /api/profile/:id updates profile fields" -m "- Input validation with Zod schemas" -m "- Unit tests for all endpoints" -m "Task 2.0 from user-profile-editing PRD"
```

### Commit Types

| Type | Use For |
|------|---------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `refactor:` | Code restructuring (no behavior change) |
| `test:` | Adding/updating tests only |
| `docs:` | Documentation only |
| `chore:` | Build, config, dependencies |
| `style:` | Formatting (no code change) |

### Message Structure

```
<type>: <short summary in present tense>

- Bullet point details
- What was added/changed
- Important implementation notes

Task X.0 from [PRD name]
```

## Task File Maintenance

### Updating Progress

After each sub-task:
1. Open the task file
2. Change `[ ]` to `[x]` for completed item
3. Save the file

### Adding New Tasks

If you discover additional work needed:

```markdown
# Add under appropriate parent
- [x] 3.1 Create ProfileEditor component
- [x] 3.2 Add form validation
- [ ] 3.3 Connect to API  # Original task
- [ ] 3.4 Add loading states  # NEW: Discovered during implementation
- [ ] 3.5 Write tests
```

### Updating Relevant Files

Keep the file list current:

```markdown
## Relevant Files

### New Files
- `src/components/ProfileEditor.tsx` - Profile form component
- `src/components/ProfileEditor.test.tsx` - Unit tests
- `src/hooks/useProfile.ts` - Profile data hook (ADDED: discovered need)

### Modified Files
- `src/types/user.ts` - Added Profile type
- `src/api/client.ts` - Added profile endpoints (ADDED: needed base config)
```

## Workflow Example

```
USER: Let's work on the profile editing tasks

ASSISTANT: I'll check the task list to find the next incomplete sub-task.

Looking at tasks-0001-prd-user-profile-editing.md:

- [x] 1.0 Set up database schema
  - [x] 1.1 Add profile fields to schema
  - [x] 1.2 Run migration
  - [x] 1.3 Update TypeScript types
- [ ] 2.0 Implement profile API
  - [ ] 2.1 Create GET /api/profile/:id endpoint  ← NEXT
  - [ ] 2.2 Create PATCH endpoint
  ...

The next task is 2.1: Create GET /api/profile/:id endpoint.

I'll implement this now...

[Implementation happens]

Done! I've created the GET endpoint in src/api/profile.ts that:
- Fetches user profile by ID
- Returns 404 if not found
- Includes proper TypeScript types

I've updated the task file to mark 2.1 as complete.

Ready to proceed to task 2.2 (Create PATCH endpoint)?

USER: yes

ASSISTANT: Working on 2.2...
```

## Pre-Work Checklist

Before starting any sub-task:

1. **Read the task file** - Find next incomplete item
2. **Read the PRD** - Understand the requirement context
3. **Check relevant files** - Understand what exists
4. **Plan the approach** - Know what you'll create/modify
5. **Start implementation** - Execute the plan

## Post-Work Checklist

After completing a sub-task:

1. **Code complete** - Implementation matches requirement
2. **Tests pass** - All relevant tests green
3. **No debug code** - Remove console.logs, TODOs
4. **Task file updated** - Marked `[x]`
5. **Files list updated** - New/modified files noted
6. **User notified** - Report completion, ask to proceed

## Handling Issues

### Tests Failing

```
1. Do NOT proceed to next task
2. Fix the failing tests
3. If it requires significant changes, note it
4. Get tests passing before continuing
```

### Blocked by Missing Information

```
1. Note what information is needed
2. Add to "Open Questions" if significant
3. Ask user for clarification
4. Wait for response before proceeding
```

### Scope Creep Discovery

```
1. Complete current task as scoped
2. Note the additional work needed
3. Add as new task(s) to the list
4. Don't expand current task scope
```

### Task Too Large

If a sub-task turns out to be larger than expected:

```
1. Complete what's reasonable
2. Split into multiple sub-tasks
3. Update task file with new breakdown
4. Continue with refined tasks
```

## Commands Reference

### Testing
```bash
# JavaScript/TypeScript
npm test
npm test -- --watch
npm test -- path/to/file.test.ts

# Python
pytest
pytest path/to/test_file.py
pytest -v  # verbose

# Flutter
flutter test
flutter test test/specific_test.dart
```

### Git
```bash
# Stage all changes
git add .

# Stage specific files
git add src/components/ProfileEditor.tsx

# Commit
git commit -m "feat: message" -m "- detail"

# Check status
git status

# View diff
git diff
```

## Final Reminders

1. **Always wait for permission** between sub-tasks
2. **Update task file immediately** when completing items
3. **Run tests before commits** - never commit failing tests
4. **Clean up before committing** - no debug code
5. **Keep files list accurate** - helps track progress
6. **Write for junior developers** - clear commit messages

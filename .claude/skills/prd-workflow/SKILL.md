---
name: prd-workflow
description: Create PRDs, generate task lists, and process tasks step-by-step. Use when the user wants to create a PRD, generate tasks from a PRD, work through a task list, or mentions "PRD", "product requirements", "task list", or "implement tasks".
---

# PRD Workflow Skill

A complete workflow for creating Product Requirements Documents (PRDs), generating actionable task lists, and systematically implementing them.

## Workflow Modes

This skill supports three modes based on what you're trying to accomplish:

| Mode | Trigger | Description |
|------|---------|-------------|
| **Create PRD** | "create a PRD", "new feature", "write requirements" | Generate a PRD from a feature idea |
| **Generate Tasks** | "generate tasks", "create task list", "break down PRD" | Create implementation tasks from a PRD |
| **Process Tasks** | "work on tasks", "implement", "next task" | Execute tasks one-by-one with commits |

## Mode 1: Create PRD

**Triggers:** User describes a new feature or asks for a PRD

### Process

1. **Receive the initial feature description**
2. **Ask clarifying questions** (REQUIRED before writing)
   - Present options as lettered/numbered lists for easy selection
   - Cover: problem/goal, target user, core functionality, acceptance criteria, scope
3. **Generate the PRD** using the structure below
4. **Save to:** `/tasks/[NNNN]-prd-[feature-name].md`

### PRD Structure

```markdown
# [Feature Name] PRD

## 1. Introduction/Overview
Brief description of the feature and the problem it solves.

## 2. Goals
- Specific, measurable objectives

## 3. User Stories
- As a [user], I want to [action] so that [benefit]

## 4. Functional Requirements
1. The system must...
2. The system must...

## 5. Non-Goals (Out of Scope)
- What this feature will NOT include

## 6. Design Considerations
- UI/UX requirements, mockups, component references

## 7. Technical Considerations
- Dependencies, constraints, integration points

## 8. Success Metrics
- How success will be measured

## 9. Open Questions
- Remaining items needing clarification
```

**Important:** Do NOT start implementing. Ask clarifying questions first.

For detailed question examples, see [prd-creation.md](prd-creation.md).

---

## Mode 2: Generate Tasks

**Triggers:** User references a PRD and wants tasks generated

### Process

1. **Read and analyze the PRD**
2. **Assess current codebase** - identify patterns, existing components, relevant files
3. **Phase 1: Generate parent tasks** (high-level, ~5 tasks)
   - Present to user and ask: "Ready to generate sub-tasks? Reply 'Go' to proceed."
4. **Wait for user confirmation**
5. **Phase 2: Generate sub-tasks** - break down each parent into actionable items
6. **Identify relevant files** - what will be created/modified
7. **Save to:** `/tasks/tasks-[prd-filename].md`

### Task List Format

```markdown
## Relevant Files

- `path/to/file.ts` - Description of purpose
- `path/to/file.test.ts` - Unit tests for file.ts

### Notes

- Unit tests should be placed alongside code files
- Use `npm test` / `pytest` / etc. to run tests

## Tasks

- [ ] 1.0 Parent Task Title
  - [ ] 1.1 Sub-task description
  - [ ] 1.2 Sub-task description
- [ ] 2.0 Parent Task Title
  - [ ] 2.1 Sub-task description
```

For detailed guidelines, see [task-generation.md](task-generation.md).

---

## Mode 3: Process Tasks

**Triggers:** User wants to work through a task list

### Core Rules

1. **One sub-task at a time** - Do NOT proceed until user says "yes" or "y"
2. **Mark completion immediately** - Change `[ ]` to `[x]` when done
3. **Commit when parent completes** - After all sub-tasks are `[x]`

### Completion Protocol

When a sub-task is finished:
1. Mark it `[x]` in the task file
2. If ALL sub-tasks under a parent are now `[x]`:
   - Run the full test suite
   - Only if tests pass: `git add .`
   - Remove any temporary files/code
   - Commit with descriptive message:
   ```bash
   git commit -m "feat: add payment validation" -m "- Validates card type" -m "- Adds unit tests" -m "Task 1.0 from PRD"
   ```
3. Mark the parent task `[x]`
4. **Stop and wait** for user approval before next task

### Task File Maintenance

- Update task list after each significant change
- Add new tasks as they emerge
- Keep "Relevant Files" section accurate
- Check which sub-task is next before starting work

For detailed protocol, see [task-processing.md](task-processing.md).

---

## Quick Reference

### File Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| PRD | `[NNNN]-prd-[feature].md` | `0001-prd-user-authentication.md` |
| Tasks | `tasks-[prd-filename].md` | `tasks-0001-prd-user-authentication.md` |

### Commit Message Format

```
<type>: <summary>

- Detail 1
- Detail 2

Task X.0 from [PRD name]
```

Types: `feat:`, `fix:`, `refactor:`, `test:`, `docs:`, `chore:`

### Interaction Checkpoints

| Checkpoint | Wait For |
|------------|----------|
| After clarifying questions | User answers |
| After parent tasks generated | User says "Go" |
| After each sub-task completed | User says "yes" or "y" |

---

## Target Audience

All PRDs and task lists should be written for a **junior developer**:
- Be explicit and unambiguous
- Avoid unexplained jargon
- Provide enough detail to understand purpose and logic

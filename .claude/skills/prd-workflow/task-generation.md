# Task Generation Reference

Detailed guidelines for generating task lists from PRDs.

## Analysis Phase

Before generating tasks, thoroughly analyze:

### 1. PRD Analysis
- Read all functional requirements
- Understand user stories and acceptance criteria
- Note technical considerations and constraints
- Identify dependencies between requirements

### 2. Codebase Assessment
- Review existing architecture and patterns
- Identify reusable components
- Find related features that can inform approach
- Note testing patterns in use
- Check for existing utilities that apply

### 3. Gap Analysis
- What exists vs. what's needed
- Which files need modification vs. creation
- What new patterns might be introduced

## Task Structure

### Parent Tasks (Phase 1)

Parent tasks are high-level groupings. Aim for ~5 parent tasks that cover:

1. **Setup/Foundation** - Initial structure, dependencies, configuration
2. **Core Implementation** - Main functionality
3. **Data Layer** - Database, API, state management
4. **UI Components** - User interface elements
5. **Integration & Testing** - Connecting pieces, comprehensive tests

Example parent tasks:
```markdown
- [ ] 1.0 Set up database schema and migrations for user profiles
- [ ] 2.0 Implement profile API endpoints
- [ ] 3.0 Create profile editing UI components
- [ ] 4.0 Add image upload and processing
- [ ] 5.0 Integrate components and add end-to-end tests
```

**After generating parent tasks, STOP and ask:**
> "I have generated the high-level tasks based on the PRD. Ready to generate the sub-tasks? Respond with 'Go' to proceed."

### Sub-Tasks (Phase 2)

Sub-tasks should be:
- **Atomic** - Can be completed in one focused session
- **Testable** - Clear completion criteria
- **Ordered** - Dependencies flow top to bottom
- **Specific** - No ambiguity about what to do

Good sub-task:
```markdown
- [ ] 2.1 Create GET /api/profile/:id endpoint that returns user profile data
```

Bad sub-task:
```markdown
- [ ] 2.1 Do the API stuff
```

### Numbering Convention

```
X.0 - Parent task
X.1 - First sub-task
X.2 - Second sub-task
...
```

## Relevant Files Section

List ALL files that will be touched:

```markdown
## Relevant Files

### New Files
- `src/components/ProfileEditor.tsx` - Main profile editing form component
- `src/components/ProfileEditor.test.tsx` - Unit tests for ProfileEditor
- `src/api/profile.ts` - Profile API client functions
- `src/api/profile.test.ts` - API client tests

### Modified Files
- `src/types/user.ts` - Add profile-related type definitions
- `src/routes/index.tsx` - Add profile route
- `prisma/schema.prisma` - Add profile fields to User model

### Configuration
- `.env.example` - Add new environment variables if needed
```

## Notes Section

Include project-specific guidance:

```markdown
### Notes

- Unit tests should be placed alongside source files (e.g., `Component.tsx` and `Component.test.tsx`)
- Run tests with `npm test` or `npm test -- --watch` for development
- This project uses React Query for data fetching - follow existing patterns in `src/hooks/`
- Form validation uses Zod schemas - see `src/schemas/` for examples
```

## Complete Example

```markdown
# Tasks for 0001-prd-user-profile-editing

## Relevant Files

### New Files
- `src/components/profile/ProfileEditor.tsx` - Profile editing form
- `src/components/profile/ProfileEditor.test.tsx` - Tests
- `src/components/profile/AvatarUpload.tsx` - Avatar upload component
- `src/components/profile/AvatarUpload.test.tsx` - Tests
- `src/api/profile.ts` - Profile API functions
- `src/api/profile.test.ts` - API tests
- `prisma/migrations/xxx_add_profile_fields.sql` - Database migration

### Modified Files
- `src/types/user.ts` - Profile type definitions
- `src/app/routes.tsx` - Add /profile route
- `prisma/schema.prisma` - User model updates

### Notes

- Follow existing form patterns in `src/components/forms/`
- Image uploads go through `/api/upload` endpoint
- Run `npm test` to execute tests
- Run `npx prisma migrate dev` to apply migrations

## Tasks

- [ ] 1.0 Set up database schema for profile data
  - [ ] 1.1 Add profile fields to User model in schema.prisma (displayName, avatarUrl, timezone)
  - [ ] 1.2 Create and run database migration
  - [ ] 1.3 Update TypeScript types in src/types/user.ts

- [ ] 2.0 Implement profile API endpoints
  - [ ] 2.1 Create GET /api/profile/:id endpoint
  - [ ] 2.2 Create PATCH /api/profile/:id endpoint for updates
  - [ ] 2.3 Add input validation using Zod schema
  - [ ] 2.4 Write API endpoint tests

- [ ] 3.0 Create profile editing UI
  - [ ] 3.1 Create ProfileEditor component with form fields
  - [ ] 3.2 Add form validation and error display
  - [ ] 3.3 Connect form to API with React Query mutation
  - [ ] 3.4 Write component unit tests

- [ ] 4.0 Implement avatar upload
  - [ ] 4.1 Create AvatarUpload component with drag-and-drop
  - [ ] 4.2 Add client-side image validation (type, size)
  - [ ] 4.3 Implement upload progress indicator
  - [ ] 4.4 Handle upload errors gracefully
  - [ ] 4.5 Write avatar component tests

- [ ] 5.0 Integration and polish
  - [ ] 5.1 Add /profile route to app router
  - [ ] 5.2 Add profile link to user menu
  - [ ] 5.3 Add success/error toast notifications
  - [ ] 5.4 Write integration tests for full flow
  - [ ] 5.5 Update documentation
```

## Task Generation Checklist

Before finalizing, verify:

- [ ] All functional requirements from PRD have corresponding tasks
- [ ] Tasks are ordered by dependency (setup before implementation)
- [ ] Each parent task has clear, atomic sub-tasks
- [ ] Test tasks are included for each component/function
- [ ] File paths match project conventions
- [ ] Notes include relevant commands and patterns
- [ ] Tasks are clear enough for a junior developer

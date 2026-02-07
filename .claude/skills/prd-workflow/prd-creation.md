# PRD Creation Reference

Detailed guidelines for creating Product Requirements Documents.

## Clarifying Questions

Before writing any PRD, you MUST ask clarifying questions. Adapt these based on the feature:

### Problem & Goal
- "What problem does this feature solve for the user?"
- "What is the main goal we want to achieve?"
- "Why is this feature needed now?"

### Target User
- "Who is the primary user of this feature?"
- "Are there secondary users we should consider?"
- "What is the user's technical skill level?"

### Core Functionality
- "What are the key actions a user should perform?"
- "What is the minimum viable version of this feature?"
- "What's the expected user flow?"

### User Stories
- "Can you provide user stories? (As a [user], I want to [action] so that [benefit])"
- "What's the most important user story?"

### Acceptance Criteria
- "How will we know this feature is complete?"
- "What are the key success criteria?"
- "What would make this feature fail?"

### Scope & Boundaries
- "What should this feature NOT do?"
- "Are there related features we should explicitly exclude?"
- "What's the boundary between this and existing features?"

### Data Requirements
- "What data does this feature need to display?"
- "What data does it need to create/modify?"
- "Are there any data privacy considerations?"

### Design & UI
- "Are there existing mockups or designs?"
- "Should this match existing UI patterns?"
- "What's the desired look and feel?"

### Edge Cases
- "What happens if the user does X?"
- "How should errors be handled?"
- "What are the boundary conditions?"

### Technical Context
- "Are there any known technical constraints?"
- "Does this need to integrate with existing systems?"
- "Are there performance requirements?"

## Question Presentation Format

Always present options in an easy-to-answer format:

```
**Question:** What type of authentication should we support?

A) Email/password only
B) Email/password + OAuth (Google, GitHub)
C) Magic link (passwordless)
D) All of the above
E) Other (please specify)
```

## PRD Section Guidelines

### Introduction/Overview
- 2-3 sentences maximum
- State what + why
- Don't include implementation details

### Goals
- Use measurable language where possible
- Prioritize goals (P0, P1, P2) if many
- Connect goals to business value

### User Stories
- Follow format: As a [role], I want [capability] so that [benefit]
- Include happy path and key alternate paths
- Number them for easy reference

### Functional Requirements
- Start each with "The system must..." or "The system should..."
- One requirement per line
- Number them (FR-1, FR-2, etc.)
- Be specific and testable

### Non-Goals
- Explicitly state what's out of scope
- Prevent scope creep
- Can reference future phases

### Design Considerations
- Reference existing components/patterns
- Include accessibility requirements
- Note responsive/mobile considerations

### Technical Considerations
- Mention relevant APIs or services
- Note database implications
- Identify dependencies

### Success Metrics
- Quantify where possible
- Include both leading and lagging indicators
- Define measurement method

### Open Questions
- Items needing stakeholder input
- Technical unknowns
- Design decisions pending

## Example PRD Snippet

```markdown
# User Profile Editing PRD

## 1. Introduction/Overview
Allow users to update their profile information including name, avatar, and preferences. This addresses user feedback requesting the ability to personalize their accounts.

## 2. Goals
- Enable users to customize their profile appearance
- Reduce support tickets about profile updates by 50%
- Increase user engagement through personalization

## 3. User Stories
1. As a user, I want to change my display name so that my name appears correctly throughout the app.
2. As a user, I want to upload a profile picture so that other users can identify me.
3. As a user, I want to set my timezone so that timestamps display in my local time.

## 4. Functional Requirements
- FR-1: The system must allow users to edit their display name (max 50 characters)
- FR-2: The system must allow users to upload a profile picture (JPEG, PNG, max 5MB)
- FR-3: The system must validate and crop uploaded images to 256x256 pixels
- FR-4: The system must allow users to select their timezone from a dropdown

## 5. Non-Goals
- Social features (following, friending)
- Profile visibility/privacy settings (Phase 2)
- Custom profile URLs
```

## Final Reminders

1. **Always ask questions first** - Never generate a PRD without clarification
2. **Use numbered sequences** - Files should be `0001-prd-x.md`, `0002-prd-y.md`
3. **Check /tasks directory** - Find the next sequence number
4. **Write for junior developers** - Be explicit and clear
5. **Don't implement** - PRD creation is documentation only

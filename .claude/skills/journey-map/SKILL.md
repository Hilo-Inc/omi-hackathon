---
name: journey-map
description: Create user journey maps to visualize customer experiences across touchpoints. Use when the user says "journey map", "customer journey", "user flow", "experience map", "touchpoints", or wants to map out a user's experience.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
---

# User Journey Map Skill

Create comprehensive user journey maps that visualize the end-to-end customer experience across all touchpoints, revealing opportunities for improvement.

## Invocation

This skill activates when:
- User wants to create a journey map or experience map
- User mentions "customer journey", "user flow", "touchpoints"
- User wants to understand pain points in a user experience
- User needs to map out a service or product experience

Arguments: `$ARGUMENTS` (persona name, scenario, product/service, or specific journey to map)

---

## What Is a Journey Map?

A journey map is a visualization of the process a person goes through to accomplish a goal with your product or service.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Journey Map Anatomy                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PERSONA                    THE JOURNEY ACROSS STAGES                       │
│  ┌─────────────┐   ┌──────────┬──────────┬──────────┬──────────┬─────────┐ │
│  │ [Photo]     │   │ AWARENESS│CONSIDER- │ PURCHASE │ ONBOARD- │RETENTION│ │
│  │             │   │          │  ATION   │          │   ING    │         │ │
│  │ Name        │   ├──────────┼──────────┼──────────┼──────────┼─────────┤ │
│  │ Goal        │   │  GOALS   │  GOALS   │  GOALS   │  GOALS   │  GOALS  │ │
│  │ Context     │   ├──────────┼──────────┼──────────┼──────────┼─────────┤ │
│  └─────────────┘   │ ACTIONS  │ ACTIONS  │ ACTIONS  │ ACTIONS  │ ACTIONS │ │
│                    ├──────────┼──────────┼──────────┼──────────┼─────────┤ │
│                    │TOUCHPOINT│TOUCHPOINT│TOUCHPOINT│TOUCHPOINT│TOUCHPNT │ │
│                    ├──────────┴──────────┴──────────┴──────────┴─────────┤ │
│                    │                                                      │ │
│  EMOTIONAL         │    😊         😐         😟         😊        😊    │ │
│  JOURNEY           │     ╲        ╱  ╲       ╱          ╲       ╱        │ │
│                    │      ╲──────╱    ╲─────╱            ╲─────╱         │ │
│                    │                                                      │ │
│                    ├──────────┬──────────┬──────────┬──────────┬─────────┤ │
│                    │PAIN POINT│PAIN POINT│PAIN POINT│PAIN POINT│PAIN PNT │ │
│                    ├──────────┼──────────┼──────────┼──────────┼─────────┤ │
│                    │OPPORTUNTY│OPPORTUNTY│OPPORTUNTY│OPPORTUNTY│OPPORTUN │ │
│                    └──────────┴──────────┴──────────┴──────────┴─────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Types of Journey Maps

### 1. Current State Map
Maps the existing experience as it happens today.

**Use when:**
- Understanding existing pain points
- Establishing a baseline for improvement
- Aligning teams on current experience

### 2. Future State Map
Maps the ideal experience you want to create.

**Use when:**
- Designing new products or services
- Reimagining the customer experience
- Setting a north star vision

### 3. Day-in-the-Life Map
Maps a user's full daily routine, not just interactions with your product.

**Use when:**
- Understanding broader context
- Finding new opportunities
- Designing for ecosystem fit

### 4. Service Blueprint
Maps the journey plus behind-the-scenes processes.

**Use when:**
- Aligning frontend and backend operations
- Identifying process inefficiencies
- Designing service delivery

---

## Journey Map Components

### 1. Persona
The specific user whose journey you're mapping.

```markdown
### Persona: Sarah Chen

**Role:** Marketing Manager at a mid-size B2B company
**Age:** 34 | **Location:** Austin, TX

**Goal:** Find a tool to automate social media scheduling
**Context:** Team of 3, managing 5 social channels, limited budget

**Quote:** "I spend too much time on repetitive tasks instead of strategy."

**Tech Savviness:** ████████░░ 8/10
**Time Available:** ███░░░░░░░ 3/10
**Budget Authority:** █████░░░░░ 5/10
```

### 2. Scenario
The specific situation or use case being mapped.

**Template:**
> [Persona] needs to [goal] because [motivation] in the context of [situation].

**Example:**
> Sarah needs to evaluate and purchase a social media tool because her team is overwhelmed with manual posting, and she has budget approval for Q2.

### 3. Journey Stages
The high-level phases the user moves through.

**Common B2C Stages:**
```
Awareness → Consideration → Purchase → Onboarding → Usage → Renewal/Churn
```

**Common B2B Stages:**
```
Problem Recognition → Research → Evaluation → Purchase Decision → Implementation → Adoption → Expansion
```

**Common SaaS Stages:**
```
Discovery → Trial → Activation → Engagement → Conversion → Retention → Advocacy
```

### 4. User Goals
What the user is trying to accomplish at each stage.

### 5. Actions
Specific steps the user takes.

### 6. Touchpoints
Where interactions occur (website, app, email, phone, in-person).

### 7. Emotions
How the user feels throughout the journey (positive/neutral/negative).

### 8. Pain Points
Frustrations, obstacles, and problems encountered.

### 9. Opportunities
Ideas for improvement based on pain points.

---

## Workflow

### Step 1: Define Scope

**Questions to answer:**
- Which persona are we mapping?
- What scenario/goal are we mapping?
- What type of map (current, future, day-in-life)?
- What's the start and end point?

### Step 2: Identify Stages

Define 4-7 stages that cover the journey:

```markdown
| Stage | Description | Duration |
|-------|-------------|----------|
| Awareness | User becomes aware of the problem or solution | Days-Weeks |
| Research | User investigates options | 1-2 weeks |
| Evaluation | User compares and decides | 1 week |
| Purchase | User completes transaction | 1 day |
| Onboarding | User sets up and learns | 1-2 weeks |
| Ongoing Use | Regular interaction | Ongoing |
```

### Step 3: Map Each Stage

For each stage, document:

```markdown
### Stage: [Name]

**User Goals:**
- [What they want to achieve]
- [What success looks like]

**Actions:**
1. [Specific step user takes]
2. [Next step]
3. [Next step]

**Touchpoints:**
- [Channel/platform]: [Specific interaction]
- [Channel/platform]: [Specific interaction]

**Thoughts:**
> "[What the user is thinking]"

**Emotions:**
😊 Positive | 😐 Neutral | 😟 Negative | 😠 Frustrated

**Pain Points:**
- ❌ [Problem encountered]
- ❌ [Friction point]

**Opportunities:**
- 💡 [Idea for improvement]
- 💡 [Potential solution]
```

### Step 4: Add the Emotional Journey

Plot the emotional highs and lows:

```
Emotion
   ^
   │    😊           😊                    😊  😊
   │     ╲          ╱  ╲                  ╱    │
 + │      ╲        ╱    ╲                ╱     │
   │       ╲      ╱      ╲              ╱      │
───┼────────╲────╱────────╲────────────╱───────┼──► Stages
   │         ╲  ╱          ╲          ╱        │
 - │          ╲╱            ╲        ╱         │
   │          😐             ╲      ╱          │
   │                          ╲    ╱           │
   │                           ╲  ╱            │
   │                            😟             │
   │                                           │
   └───────────────────────────────────────────┘
       Aware  Consider  Purchase  Onboard  Use
```

### Step 5: Identify Moments of Truth

**Moments of Truth** are critical interactions that disproportionately impact the overall experience:

- **Make or break moments:** Where users decide to continue or abandon
- **Peak moments:** Emotional highs that create loyalty
- **Pain moments:** Emotional lows that cause churn

### Step 6: Prioritize Opportunities

Rate opportunities by:

| Opportunity | User Impact | Business Impact | Effort | Priority |
|-------------|-------------|-----------------|--------|----------|
| [Idea 1] | High | High | Low | **P1** |
| [Idea 2] | High | Medium | Medium | **P2** |
| [Idea 3] | Medium | Low | High | P3 |

---

## Journey Map Templates

### Template 1: Simple Journey Map

```markdown
# User Journey Map: [Scenario Name]

**Persona:** [Name]
**Scenario:** [One sentence description]
**Map Type:** Current State / Future State
**Date:** [Date]

---

## Journey Overview

| Stage | Awareness | Consideration | Purchase | Onboarding | Ongoing Use |
|-------|-----------|---------------|----------|------------|-------------|
| **Goal** | | | | | |
| **Actions** | | | | | |
| **Touchpoints** | | | | | |
| **Emotion** | 😊/😐/😟 | 😊/😐/😟 | 😊/😐/😟 | 😊/😐/😟 | 😊/😐/😟 |
| **Pain Points** | | | | | |
| **Opportunities** | | | | | |

---

## Key Insights

### Biggest Pain Points
1. [Pain point with highest impact]
2. [Second biggest pain point]
3. [Third pain point]

### Moments of Truth
1. [Critical moment that determines success]
2. [Make or break interaction]

### Top Opportunities
1. [Highest priority improvement]
2. [Second priority]
3. [Third priority]
```

### Template 2: Detailed Journey Map

```markdown
# User Journey Map

**Project:** [Project Name]
**Persona:** [Persona Name]
**Scenario:** [Detailed scenario description]
**Journey Type:** Current State
**Created:** [Date]
**Author:** [Name]

---

## Persona Summary

| Attribute | Details |
|-----------|---------|
| **Name** | [Persona name] |
| **Role** | [Job title/role] |
| **Goal** | [Primary goal for this journey] |
| **Context** | [Relevant background] |

---

## Stage 1: [Stage Name]

### Overview
- **Duration:** [Typical time in this stage]
- **Entry Point:** [How users enter this stage]
- **Exit Point:** [How users move to next stage]

### User Goals
- [Goal 1]
- [Goal 2]

### Actions
1. [Action 1]
2. [Action 2]
3. [Action 3]

### Touchpoints
| Channel | Interaction | Owner |
|---------|-------------|-------|
| [Website/App/Email/etc.] | [Specific interaction] | [Team] |

### User Thoughts
> "[Internal monologue]"

### Emotional State
**Rating:** 😊 Positive / 😐 Neutral / 😟 Negative

**Why:** [Explanation of emotional state]

### Pain Points
| Pain Point | Severity | Frequency |
|------------|----------|-----------|
| [Issue] | High/Med/Low | Often/Sometimes/Rare |

### Opportunities
| Opportunity | Impact | Effort |
|-------------|--------|--------|
| [Idea] | High/Med/Low | High/Med/Low |

---

## Stage 2: [Stage Name]
[Repeat format...]

---

## Emotional Journey Visualization

```
Positive  │                    ●───●
          │    ●──●           /
Neutral   │   /    \         /
          │  /      \       /
          │ /        \     /
Negative  │●          ●───●
          └─────────────────────────────
            S1   S2   S3   S4   S5
```

---

## Key Metrics to Track

| Stage | Metric | Current | Target |
|-------|--------|---------|--------|
| [Stage] | [Metric] | [Value] | [Goal] |

---

## Prioritized Opportunities

### P1 - Quick Wins (High Impact, Low Effort)
1. [Opportunity]
2. [Opportunity]

### P2 - Major Projects (High Impact, High Effort)
1. [Opportunity]

### P3 - Fill-Ins (Low Impact, Low Effort)
1. [Opportunity]

### P4 - Reconsider (Low Impact, High Effort)
1. [Opportunity]

---

## Next Steps

1. [ ] [Action item]
2. [ ] [Action item]
3. [ ] [Action item]

---

## Appendix

### Research Sources
- [User interviews, surveys, analytics used]

### Related Documents
- [Persona document]
- [Service blueprint]
- [Competitive analysis]
```

---

## Example: E-commerce Purchase Journey

```markdown
# User Journey Map: First-Time Online Purchase

**Persona:** Alex, 28, tech-savvy professional
**Scenario:** Buying running shoes online for the first time from this retailer
**Type:** Current State

---

## Stage 1: Discovery

**Goals:** Find running shoes that fit my needs
**Actions:**
1. Google "best running shoes for beginners"
2. Click on blog article
3. See product recommendation
4. Click through to retailer site

**Touchpoints:**
- Google Search
- Blog/Review site
- Retailer landing page

**Emotion:** 😊 Excited to find options

**Pain Points:**
- ❌ Too many options, overwhelming

**Opportunities:**
- 💡 Quiz to narrow down options

---

## Stage 2: Browsing

**Goals:** Compare options, find the right shoe
**Actions:**
1. Browse category page
2. Use filters (size, price, color)
3. Read reviews
4. Compare 3-4 options

**Touchpoints:**
- Product listing page
- Filter/sort tools
- Product detail pages
- Reviews section

**Emotion:** 😐 Neutral, information overload

**Pain Points:**
- ❌ Filters don't include "foot width"
- ❌ Hard to compare products side-by-side
- ❌ Reviews mention sizing issues but no guidance

**Opportunities:**
- 💡 Add foot width filter
- 💡 Add compare feature
- 💡 AI-powered size recommendation

---

## Stage 3: Decision

**Goals:** Confirm this is the right choice
**Actions:**
1. Check return policy
2. Look for discount codes
3. Check if available in my size
4. Read shipping info

**Touchpoints:**
- Product page
- Policy pages
- Coupon sites (external)

**Emotion:** 😟 Anxious about sizing

**Pain Points:**
- ❌ Return policy hard to find
- ❌ No first-time buyer discount visible
- ❌ Size chart generic, not brand-specific

**Opportunities:**
- 💡 Prominent return policy on product page
- 💡 Exit-intent popup with discount
- 💡 Brand-specific size guide

---

## Stage 4: Purchase

**Goals:** Complete purchase quickly and securely
**Actions:**
1. Add to cart
2. Create account (required)
3. Enter shipping info
4. Enter payment
5. Confirm order

**Touchpoints:**
- Cart
- Checkout flow
- Account creation
- Payment processor

**Emotion:** 😟 Frustrated at forced account creation

**Pain Points:**
- ❌ Forced account creation (no guest checkout)
- ❌ 5-step checkout feels long
- ❌ Unexpected shipping cost at end

**Opportunities:**
- 💡 Guest checkout option
- 💡 Single-page checkout
- 💡 Show shipping cost earlier

---

## Stage 5: Post-Purchase

**Goals:** Track order, prepare for delivery
**Actions:**
1. Receive confirmation email
2. Track shipment
3. Receive package
4. Try on shoes

**Touchpoints:**
- Email
- Order tracking page
- Packaging
- Product

**Emotion:** 😊 Excited when package arrives

**Pain Points:**
- ❌ Tracking updates delayed
- ❌ No unboxing experience

**Opportunities:**
- 💡 Real-time tracking notifications
- 💡 Premium packaging with tips

---

## Emotional Journey

```
😊 ─●                               ●
    │╲                             ╱│
😐 ─┼─●                           ╱ │
    │  ╲                         ╱  │
    │   ╲       ●───●           ╱   │
😟 ─┼────╲─────╱─────╲─────────╱────┼
    │     ╲   ╱       ╲       ╱     │
    └──────●─●─────────●─────●──────┘
      Discover Browse Decide Purchase Post
```

## Priority Opportunities

| # | Opportunity | Stage | Impact | Effort |
|---|-------------|-------|--------|--------|
| 1 | Guest checkout | Purchase | High | Low |
| 2 | Show shipping cost early | Decision | High | Low |
| 3 | Size recommendation tool | Browsing | High | Medium |
| 4 | Product comparison | Browsing | Medium | Medium |
| 5 | Foot width filter | Browsing | Medium | Low |
```

---

## Best Practices

### Do
- Base maps on real user research, not assumptions
- Focus on one persona and scenario per map
- Include emotional journey—it reveals the most insights
- Involve cross-functional stakeholders
- Update maps as the experience changes

### Don't
- Try to map every possible scenario in one map
- Skip the research and guess at user behaviors
- Focus only on your own touchpoints (consider full ecosystem)
- Create a map and never use it
- Ignore the "boring" stages—often where pain hides

---

## Workshop Format

For collaborative journey mapping sessions:

```markdown
### Journey Mapping Workshop Agenda (2-3 hours)

1. **Introduction** (10 min)
   - Goals for the session
   - Persona and scenario overview

2. **Individual Mapping** (20 min)
   - Each participant maps their understanding silently
   - Use sticky notes for each element

3. **Share & Consolidate** (30 min)
   - Walk through each stage together
   - Combine insights, resolve disagreements

4. **Emotional Journey** (15 min)
   - Plot the emotional highs and lows
   - Identify moments of truth

5. **Pain Point Prioritization** (20 min)
   - Vote on biggest pain points
   - Discuss root causes

6. **Opportunity Generation** (20 min)
   - Brainstorm solutions for top pain points
   - Quick feasibility check

7. **Prioritization & Next Steps** (15 min)
   - Prioritize opportunities
   - Assign owners and timelines

**Materials needed:**
- Large whiteboard or wall space
- Sticky notes (multiple colors)
- Markers
- Journey map template printed large
- Timer
```

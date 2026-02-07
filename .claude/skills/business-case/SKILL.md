---
name: business-case
description: Develop business cases with ROI analysis and cost-benefit analysis. Use when the user says "business case", "ROI analysis", "cost-benefit", "investment justification", "project proposal", or wants to justify a business investment or initiative.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
---

# Business Case Skill

Develop compelling business cases to justify investments, initiatives, and strategic decisions.

## Invocation

This skill activates when:
- User wants to build a business case
- User mentions "ROI analysis", "cost-benefit analysis"
- User needs to justify an investment or project
- User asks about project proposals or business justification

Arguments: `$ARGUMENTS` (project description, costs, expected benefits)

---

## Business Case Structure

A complete business case answers these questions:

```
┌────────────────────────────────────────────────────────────────┐
│  1. WHAT is the problem/opportunity?                           │
│  2. WHY should we address it now?                              │
│  3. HOW will we solve it?                                      │
│  4. HOW MUCH will it cost?                                     │
│  5. WHAT are the benefits?                                     │
│  6. WHAT are the risks?                                        │
│  7. WHO needs to be involved?                                  │
│  8. WHEN will we see results?                                  │
└────────────────────────────────────────────────────────────────┘
```

---

## Section 1: Executive Summary

**Purpose:** Summarize the entire case in one page

**Include:**
- Problem statement (1-2 sentences)
- Proposed solution (1-2 sentences)
- Total investment required
- Expected ROI/NPV
- Key benefits
- Recommendation

**Template:**
```markdown
## Executive Summary

**The Opportunity:** [What problem are we solving or opportunity are we capturing?]

**Proposed Solution:** [What are we recommending?]

**Investment Required:** $[X] over [Y] months/years

**Expected Return:**
- ROI: [X]%
- NPV: $[X]
- Payback Period: [X] months/years

**Key Benefits:**
• [Benefit 1 with metric]
• [Benefit 2 with metric]
• [Benefit 3 with metric]

**Recommendation:** [Approve/Proceed with Phase 1/etc.]
```

---

## Section 2: Problem Statement

**Purpose:** Establish why action is needed

**Include:**
- Current state and pain points
- Impact of the problem (quantified)
- Why now? What's the urgency?
- Cost of inaction

**Template:**
```markdown
## Problem Statement

### Current Situation
[Describe the current state and its limitations]

### Impact
| Impact Area | Metric | Annual Cost |
|-------------|--------|-------------|
| Lost productivity | X hours/week | $Y |
| Customer churn | X% increase | $Y revenue |
| Manual errors | X errors/month | $Y remediation |
| **Total Impact** | | **$Z/year** |

### Why Now?
- [Trigger event or deadline]
- [Market change]
- [Competitive pressure]

### Cost of Inaction
If we don't address this:
- Year 1: $[X] in continued losses
- Year 3: $[X] cumulative impact
- Risk: [Strategic risk if unaddressed]
```

---

## Section 3: Proposed Solution

**Purpose:** Explain what you're recommending

**Include:**
- Solution description
- Why this approach (vs. alternatives)
- Scope (what's in and out)
- Success criteria

**Template:**
```markdown
## Proposed Solution

### Overview
[2-3 paragraph description of the proposed solution]

### Key Components
1. **[Component 1]:** [Description]
2. **[Component 2]:** [Description]
3. **[Component 3]:** [Description]

### Alternatives Considered

| Option | Pros | Cons | Reason Not Selected |
|--------|------|------|---------------------|
| Do nothing | No cost | Problem persists | Unacceptable risk |
| Option B | [Pro] | [Con] | [Why not] |
| **Recommended** | [Pro] | [Con] | Best balance |

### Scope
**In Scope:**
- [Item]
- [Item]

**Out of Scope:**
- [Item]
- [Item]

### Success Criteria
| Metric | Baseline | Target | Timeline |
|--------|----------|--------|----------|
| [Metric] | [Current] | [Goal] | [When] |
```

---

## Section 4: Financial Analysis

### Cost Analysis

**Include all costs:**
- One-time costs (implementation, setup)
- Recurring costs (operations, maintenance)
- Hidden costs (training, change management)

**Template:**
```markdown
## Financial Analysis

### Cost Breakdown

#### One-Time Costs
| Category | Year 1 | Notes |
|----------|--------|-------|
| Software/Hardware | $X | [Details] |
| Implementation | $X | [Details] |
| Training | $X | [Details] |
| Change Management | $X | [Details] |
| **Total One-Time** | **$X** | |

#### Recurring Costs (Annual)
| Category | Year 1 | Year 2 | Year 3 |
|----------|--------|--------|--------|
| Licensing | $X | $X | $X |
| Support | $X | $X | $X |
| Operations | $X | $X | $X |
| **Total Recurring** | **$X** | **$X** | **$X** |

#### Total Cost of Ownership (3-Year)
| | Year 1 | Year 2 | Year 3 | Total |
|---|--------|--------|--------|-------|
| One-Time | $X | $0 | $0 | $X |
| Recurring | $X | $X | $X | $X |
| **Total** | **$X** | **$X** | **$X** | **$X** |
```

### Benefit Analysis

**Quantify all benefits:**

```markdown
### Benefit Breakdown

#### Quantifiable Benefits (Annual)
| Benefit | Calculation | Year 1 | Year 2 | Year 3 |
|---------|-------------|--------|--------|--------|
| Labor savings | X hrs × $Y/hr | $Z | $Z | $Z |
| Error reduction | X errors × $Y/error | $Z | $Z | $Z |
| Revenue increase | X% × current revenue | $Z | $Z | $Z |
| Cost avoidance | [Calculation] | $Z | $Z | $Z |
| **Total Benefits** | | **$X** | **$X** | **$X** |

#### Non-Quantifiable Benefits
- Improved employee satisfaction
- Better customer experience
- Competitive positioning
- Regulatory compliance
```

### ROI Calculations

```markdown
### Return on Investment

#### Simple ROI
ROI = (Total Benefits - Total Costs) / Total Costs × 100
ROI = ($X - $Y) / $Y × 100 = Z%

#### Payback Period
Payback = Initial Investment / Annual Net Benefit
Payback = $X / $Y = Z months/years

#### Net Present Value (NPV)
Using discount rate of X%:

| Year | Net Cash Flow | Discount Factor | Present Value |
|------|---------------|-----------------|---------------|
| 0 | ($X) | 1.000 | ($X) |
| 1 | $X | 0.XXX | $X |
| 2 | $X | 0.XXX | $X |
| 3 | $X | 0.XXX | $X |
| **NPV** | | | **$X** |

#### Internal Rate of Return (IRR)
IRR = X% (calculated using cash flows above)

### Investment Summary
| Metric | Value | Interpretation |
|--------|-------|----------------|
| Total Investment | $X | 3-year TCO |
| Total Benefits | $X | 3-year benefits |
| Net Benefit | $X | Total benefits - costs |
| ROI | X% | Return per dollar invested |
| Payback | X months | Time to recover investment |
| NPV | $X | Value in today's dollars |
| IRR | X% | Effective return rate |
```

---

## Section 5: Risk Analysis

**Purpose:** Show you've thought through what could go wrong

**Template:**
```markdown
## Risk Analysis

### Key Risks

| Risk | Probability | Impact | Risk Score | Mitigation |
|------|-------------|--------|------------|------------|
| Implementation delays | Medium | High | 6 | Phased approach, buffer time |
| User adoption | High | Medium | 6 | Change management plan |
| Technical issues | Low | High | 4 | Vendor SLA, support plan |
| Budget overrun | Medium | Medium | 4 | Contingency reserve |
| Scope creep | Medium | Medium | 4 | Governance process |

**Risk Scoring:** Probability (L=1, M=2, H=3) × Impact (L=1, M=2, H=3)

### Sensitivity Analysis
| Variable | Base Case | Pessimistic | Optimistic |
|----------|-----------|-------------|------------|
| Benefits realized | 100% | 70% | 120% |
| Implementation cost | $X | +20% | -10% |
| Timeline | X months | +3 months | -1 month |
| **NPV** | $X | $Y | $Z |

### Contingency Plan
If [risk] occurs, we will [response].
```

---

## Section 6: Implementation Plan

**Purpose:** Show how this will get done

**Template:**
```markdown
## Implementation Plan

### Timeline

| Phase | Activities | Duration | Owner |
|-------|------------|----------|-------|
| Phase 1: Planning | Requirements, vendor selection | 4 weeks | PM |
| Phase 2: Setup | Installation, configuration | 6 weeks | IT |
| Phase 3: Pilot | Test with limited group | 4 weeks | Operations |
| Phase 4: Rollout | Full deployment | 8 weeks | All |
| Phase 5: Optimization | Monitor and improve | Ongoing | Operations |

### Key Milestones
| Milestone | Target Date | Success Criteria |
|-----------|-------------|------------------|
| Vendor selected | [Date] | Contract signed |
| System live | [Date] | All users active |
| ROI achieved | [Date] | Metrics met |

### Resource Requirements
| Role | Effort | Source |
|------|--------|--------|
| Project Manager | 50% | Internal |
| Technical Lead | 100% | Internal |
| Business Analyst | 50% | Internal |
| Vendor Support | As needed | External |

### Dependencies
- [Dependency 1]
- [Dependency 2]
```

---

## Section 7: Stakeholders

**Purpose:** Identify who's involved and impacted

**Template:**
```markdown
## Stakeholders

### RACI Matrix

| Activity | Sponsor | PM | IT | Operations | Finance |
|----------|---------|----|----|------------|---------|
| Approve budget | A | I | I | I | C |
| Select vendor | I | R | C | C | I |
| Implement | I | A | R | C | I |
| Train users | I | A | C | R | I |

R = Responsible, A = Accountable, C = Consulted, I = Informed

### Impact Analysis
| Stakeholder Group | Impact | Change Required | Support Needed |
|-------------------|--------|-----------------|----------------|
| End users | High | New process | Training |
| IT team | Medium | New system | Documentation |
| Management | Low | New reports | Briefing |
```

---

## Section 8: Recommendation

**Purpose:** Make a clear ask

**Template:**
```markdown
## Recommendation

### Recommended Action
Based on the analysis presented, we recommend proceeding with [solution]
at an investment of $[X] over [Y] years.

### Expected Outcomes
- [Outcome 1 with metric]
- [Outcome 2 with metric]
- [Outcome 3 with metric]

### Decision Required
☐ Approve full implementation ($X)
☐ Approve Phase 1 only ($Y)
☐ Request additional analysis
☐ Do not proceed

### Next Steps (Upon Approval)
1. [Action] - [Owner] - [Date]
2. [Action] - [Owner] - [Date]
3. [Action] - [Owner] - [Date]
```

---

## Output Template

```markdown
# Business Case: [Project Name]

**Prepared by:** [Name]
**Date:** [Date]
**Version:** [X.X]
**Status:** [Draft/Final]

---

## Executive Summary
[One page summary]

---

## 1. Problem Statement
[Current situation and impact]

## 2. Proposed Solution
[What we're recommending]

## 3. Financial Analysis
### Costs
[Cost breakdown]

### Benefits
[Benefit breakdown]

### ROI
[ROI calculations]

## 4. Risk Analysis
[Risks and mitigations]

## 5. Implementation Plan
[Timeline and resources]

## 6. Stakeholders
[Who's involved]

## 7. Recommendation
[Clear ask]

---

## Appendix
A. Detailed calculations
B. Vendor comparison
C. Reference materials
```

---

## Quick Reference: Financial Formulas

| Metric | Formula |
|--------|---------|
| **ROI** | (Benefits - Costs) / Costs × 100 |
| **Payback** | Initial Investment / Annual Benefit |
| **NPV** | Σ (Cash Flow / (1+r)^t) |
| **IRR** | Rate where NPV = 0 |
| **TCO** | All costs over time period |
| **BCR** | Total Benefits / Total Costs |

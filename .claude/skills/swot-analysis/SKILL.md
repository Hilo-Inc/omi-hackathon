---
name: swot-analysis
description: Strategic SWOT analysis for business planning. Use when the user says "SWOT", "strategic analysis", "competitive analysis", "business strategy", "strengths weaknesses", or wants to assess business position.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
---

# SWOT Analysis Skill

Conduct comprehensive SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis for strategic business planning.

## Invocation

This skill activates when:
- User asks for a SWOT analysis
- User mentions "strategic analysis", "strengths and weaknesses"
- User wants to assess competitive position
- User is planning business strategy

Arguments: `$ARGUMENTS` (business name, industry, or specific context)

---

## The SWOT Framework

```
┌────────────────────────────────────┬────────────────────────────────────┐
│           HELPFUL                  │           HARMFUL                  │
│        (to achieving goal)         │        (to achieving goal)         │
├────────────────────────────────────┼────────────────────────────────────┤
│                                    │                                    │
│  I       STRENGTHS                 │       WEAKNESSES              I    │
│  N                                 │                               N    │
│  T   Internal attributes that      │   Internal factors that       T    │
│  E   give an advantage             │   put you at a disadvantage   E    │
│  R                                 │                               R    │
│  N   • What do you do well?        │   • What could you improve?   N    │
│  A   • What unique resources?      │   • What are you lacking?     A    │
│  L   • What do others see as       │   • What do others see as     L    │
│        your strengths?             │     your weaknesses?                │
│                                    │                                    │
├────────────────────────────────────┼────────────────────────────────────┤
│                                    │                                    │
│  E       OPPORTUNITIES             │         THREATS               E    │
│  X                                 │                               X    │
│  T   External factors you could    │   External factors that       T    │
│  E   exploit to your advantage     │   could cause trouble         E    │
│  R                                 │                               R    │
│  N   • What trends could you       │   • What obstacles do you     N    │
│  A     take advantage of?          │     face?                     A    │
│  L   • How can you turn            │   • What are competitors      L    │
│        strengths into              │     doing?                          │
│        opportunities?              │   • Are requirements          │
│                                    │     changing?                       │
│                                    │                                    │
└────────────────────────────────────┴────────────────────────────────────┘
```

---

## Analysis Process

### Step 1: Gather Information

Before starting the analysis:
- What is the goal or decision this analysis supports?
- What is the competitive context?
- What timeframe are we considering?

### Step 2: Analyze Each Quadrant

---

## Strengths (Internal, Positive)

Internal attributes that give the business an advantage.

### Categories to Explore

**Team & Capabilities**
- Unique skills or expertise
- Strong leadership
- Employee engagement
- Deep domain knowledge

**Product & Technology**
- Proprietary technology or IP
- Superior product quality
- Strong tech infrastructure
- Innovative capabilities

**Market Position**
- Brand recognition
- Customer loyalty
- Market share
- First-mover advantage

**Financial**
- Strong cash position
- Profitable operations
- Efficient cost structure
- Access to capital

**Operational**
- Efficient processes
- Strategic partnerships
- Strong supply chain
- Scalable infrastructure

### Questions to Ask

- What do you do better than competitors?
- What unique resources do you have access to?
- What do customers cite as your advantages?
- What advantages do insiders see that outsiders don't?
- What's working well in the business?

### Example Strengths

```markdown
### Strengths

1. **Technical founder with deep domain expertise**
   - Evidence: 10 years at category leader before founding
   - Impact: High
   - Category: Team

2. **Profitable from day one with strong unit economics**
   - Evidence: 85% gross margins, LTV:CAC of 5:1
   - Impact: High
   - Category: Financial

3. **Strong SEO presence driving organic acquisition**
   - Evidence: #1-3 rankings for 15 target keywords, 70% of traffic organic
   - Impact: High
   - Category: Market Position
```

---

## Weaknesses (Internal, Negative)

Internal factors that place the business at a disadvantage.

### Categories to Explore

**Team & Capabilities**
- Skill gaps
- Key person dependencies
- Limited bandwidth
- Inexperience in critical areas

**Product & Technology**
- Technical debt
- Feature gaps
- Scalability issues
- Quality problems

**Market Position**
- Low brand awareness
- Weak market position
- Limited customer base
- Geographic limitations

**Financial**
- Limited funding
- Poor unit economics
- High burn rate
- Customer concentration

**Operational**
- Inefficient processes
- Limited partnerships
- Weak supply chain
- Manual operations

### Questions to Ask

- What could you improve?
- What should you avoid?
- What do competitors do better?
- What do customers complain about?
- What internal challenges are you facing?

### Example Weaknesses

```markdown
### Weaknesses

1. **Single founder handling all functions**
   - Evidence: Currently a team of 1, no co-founder
   - Impact: Medium
   - Mitigation: Planning first hire in Q2
   - Category: Team

2. **Limited geographic reach**
   - Evidence: Only available in US market
   - Impact: Medium
   - Mitigation: International expansion planned for next year
   - Category: Market Position

3. **Dependency on single marketing channel**
   - Evidence: 80% of revenue from SEO
   - Impact: High
   - Mitigation: Testing paid acquisition and partnerships
   - Category: Operational
```

---

## Opportunities (External, Positive)

External factors the business could exploit to its advantage.

### Categories to Explore

**Market Trends**
- Growing market segments
- Emerging customer needs
- Technology shifts
- Regulatory changes favoring you

**Competitive Landscape**
- Competitor weaknesses
- Market gaps
- Consolidation opportunities
- Partnership possibilities

**Customer Opportunities**
- Underserved segments
- Adjacent markets
- Expansion possibilities
- New use cases

**Economic/Industry**
- Favorable economic trends
- Industry tailwinds
- Investment climate
- Talent availability

### Questions to Ask

- What trends could benefit the business?
- What are competitors missing?
- What underserved needs exist in the market?
- What changes in regulations could help?
- What technologies could enable new capabilities?

### Example Opportunities

```markdown
### Opportunities

1. **Market shift to remote work creating new demand**
   - Evidence: 40% increase in target segment since 2020
   - Potential: High
   - Timeframe: Short-term
   - Requirements: Marketing repositioning

2. **Major competitor acquired, customers looking for alternatives**
   - Evidence: Competitor X acquired by BigCorp, customer complaints rising
   - Potential: High
   - Timeframe: Short-term
   - Requirements: Competitive migration campaign

3. **API platform expansion**
   - Evidence: Developer requests for API access increasing
   - Potential: Medium
   - Timeframe: Medium-term
   - Requirements: Engineering investment, developer relations
```

---

## Threats (External, Negative)

External factors that could harm the business.

### Categories to Explore

**Competitive Threats**
- New entrants
- Substitute products
- Competitive moves
- Price pressure

**Market Threats**
- Changing customer preferences
- Market saturation
- Economic downturn
- Industry disruption

**Technology Threats**
- Platform risk
- Technology obsolescence
- Security/privacy concerns
- AI disruption

**Regulatory/Legal**
- Compliance requirements
- Legal risks
- Policy changes
- International regulations

### Questions to Ask

- What obstacles do you face?
- What are competitors doing?
- Are market requirements changing?
- Could technology shifts make you obsolete?
- Is your industry being disrupted?

### Example Threats

```markdown
### Threats

1. **Platform dependency on Shopify**
   - Evidence: 60% of customers use Shopify integration
   - Severity: High
   - Likelihood: Medium
   - Mitigation: Diversifying integrations, direct acquisition channel

2. **Large incumbents adding similar features**
   - Evidence: Competitor Y announced similar feature in roadmap
   - Severity: Medium
   - Likelihood: High
   - Mitigation: Focus on niche, move faster, deepen specialization

3. **Economic downturn affecting SMB spending**
   - Evidence: Market indicators, customer payment delays
   - Severity: Medium
   - Likelihood: Medium
   - Mitigation: Lower pricing tier, annual discount incentives
```

---

## TOWS Strategy Matrix

Use SWOT to generate strategies:

| | Strengths | Weaknesses |
|---|-----------|------------|
| **Opportunities** | **SO Strategies** (Maxi-Maxi): Use strengths to exploit opportunities | **WO Strategies** (Mini-Maxi): Overcome weaknesses by pursuing opportunities |
| **Threats** | **ST Strategies** (Maxi-Mini): Use strengths to avoid threats | **WT Strategies** (Mini-Mini): Minimize weaknesses and avoid threats |

### Example TOWS Strategies

```markdown
## Strategic Implications

### SO Strategies (Strengths × Opportunities)
- **Leverage SEO expertise + remote work trend**: Create content targeting
  remote-first companies, double down on what's working

### WO Strategies (Weaknesses × Opportunities)
- **Address single-founder limitation through competitor disruption**:
  Use competitor acquisition as recruiting pitch to hire their displaced talent

### ST Strategies (Strengths × Threats)
- **Use profitability + platform risk**: Build direct acquisition channel
  funded by positive cash flow, reduce dependency

### WT Strategies (Weaknesses × Threats)
- **Address channel dependency + incumbent competition**:
  Diversify before competition intensifies, explore partnerships
```

---

## Output Template

```markdown
# SWOT Analysis: [Business Name]

**Date:** [Date]
**Prepared by:** [Name]
**Purpose:** [What decision or planning this supports]

## Executive Summary

[2-3 sentence overview of key findings]

## Analysis

### Strengths
| # | Strength | Evidence | Impact |
|---|----------|----------|--------|
| S1 | [Strength] | [Evidence] | High/Med/Low |
| S2 | [Strength] | [Evidence] | High/Med/Low |

### Weaknesses
| # | Weakness | Evidence | Impact | Mitigation |
|---|----------|----------|--------|------------|
| W1 | [Weakness] | [Evidence] | High/Med/Low | [Plan] |
| W2 | [Weakness] | [Evidence] | High/Med/Low | [Plan] |

### Opportunities
| # | Opportunity | Evidence | Potential | Timeframe |
|---|-------------|----------|-----------|-----------|
| O1 | [Opportunity] | [Evidence] | High/Med/Low | Short/Med/Long |
| O2 | [Opportunity] | [Evidence] | High/Med/Low | Short/Med/Long |

### Threats
| # | Threat | Evidence | Severity | Likelihood |
|---|--------|----------|----------|------------|
| T1 | [Threat] | [Evidence] | High/Med/Low | High/Med/Low |
| T2 | [Threat] | [Evidence] | High/Med/Low | High/Med/Low |

## Strategic Implications

### SO Strategies (Leverage)
- [Strategy using strengths to capture opportunities]

### WO Strategies (Improve)
- [Strategy to overcome weaknesses by pursuing opportunities]

### ST Strategies (Defend)
- [Strategy using strengths to minimize threats]

### WT Strategies (Avoid)
- [Strategy to minimize weaknesses and avoid threats]

## Recommendations

### Priority Actions
1. [High priority action based on analysis]
2. [Second priority action]
3. [Third priority action]

## Review Schedule
- Next review: [Date]
- Trigger for update: [Conditions that warrant re-analysis]
```

---

## Best Practices

### Be Specific
- Bad: "Good marketing"
- Good: "Strong SEO presence driving 70% of traffic organically"

### Cite Evidence
- Every point should reference data or observable facts
- Distinguish between confirmed facts and assumptions

### Prioritize by Impact
- Order items by importance to the business
- Focus on the most significant factors (3-5 per quadrant)

### Consider Stage
- What's a weakness for a startup may not matter for a mature business
- Context matters for interpretation

### Stay Balanced
- Don't inflate strengths or downplay weaknesses
- Honest assessment is more valuable than optimism

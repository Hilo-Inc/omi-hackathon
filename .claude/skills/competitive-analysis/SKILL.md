---
name: competitive-analysis
description: Porter's Five Forces and competitive landscape analysis. Use when the user says "competitive analysis", "Porter's Five Forces", "market analysis", "competitor research", "industry analysis", or wants to understand competitive dynamics.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
---

# Competitive Analysis Skill

Analyze competitive dynamics using Porter's Five Forces and comprehensive competitive landscape analysis.

## Invocation

This skill activates when:
- User asks for competitive analysis
- User mentions "Porter's Five Forces", "industry analysis"
- User wants to understand competitive positioning
- User asks about competitors or market dynamics

Arguments: `$ARGUMENTS` (industry, business, or specific competitors to analyze)

---

## Porter's Five Forces Framework

Porter's Five Forces examines the competitive intensity and attractiveness of an industry:

```
                    ┌─────────────────────────┐
                    │   THREAT OF NEW         │
                    │      ENTRANTS           │
                    │                         │
                    │  How easy is it for     │
                    │  new competitors to     │
                    │  enter?                 │
                    └───────────┬─────────────┘
                                │
                                ▼
┌───────────────────┐     ┌─────────────────┐     ┌───────────────────┐
│    BARGAINING     │     │                 │     │    BARGAINING     │
│    POWER OF       │────▶│   COMPETITIVE   │◀────│    POWER OF       │
│    SUPPLIERS      │     │    RIVALRY      │     │     BUYERS        │
│                   │     │                 │     │                   │
│  How much power   │     │  How intense    │     │  How much power   │
│  do suppliers     │     │  is competition │     │  do customers     │
│  have?            │     │  among existing │     │  have?            │
│                   │     │  players?       │     │                   │
└───────────────────┘     └───────┬─────────┘     └───────────────────┘
                                │
                                ▼
                    ┌─────────────────────────┐
                    │   THREAT OF             │
                    │   SUBSTITUTES           │
                    │                         │
                    │  How easily can         │
                    │  customers switch to    │
                    │  alternatives?          │
                    └─────────────────────────┘
```

---

## Force 1: Threat of New Entrants

**Question:** How easy is it for new competitors to enter this market?

### Barriers to Entry (HIGH barrier = LOW threat)

| Barrier | Description | Questions to Ask |
|---------|-------------|------------------|
| **Capital requirements** | Investment needed to compete | How much funding is needed to start? |
| **Economies of scale** | Cost advantages from size | Do incumbents have significant cost advantages? |
| **Brand loyalty** | Customer attachment to existing brands | How strong is brand preference? |
| **Switching costs** | Cost for customers to change | What prevents customers from switching? |
| **Network effects** | Value increases with users | Does the product become more valuable with more users? |
| **Regulatory barriers** | Licenses, certifications | What approvals are needed to operate? |
| **Access to distribution** | Channels to reach customers | How hard is it to reach customers? |
| **Proprietary technology** | Patents, trade secrets | Is there protected IP? |

### Assessment Scale

| Level | Characteristics |
|-------|-----------------|
| **Low threat** (1-2) | High barriers, significant investment needed, strong brands |
| **Medium threat** (3) | Some barriers exist but can be overcome |
| **High threat** (4-5) | Low startup costs, easy customer acquisition, no protection |

---

## Force 2: Bargaining Power of Suppliers

**Question:** How much power do your suppliers have over you?

### High Supplier Power When:
- Few suppliers dominate the market
- Switching suppliers is costly
- Supplier's product is unique or differentiated
- You're not a significant customer to the supplier
- Suppliers can integrate forward (become competitors)

### Low Supplier Power When:
- Many suppliers available
- Standardized products/services
- Easy to switch suppliers
- You represent significant revenue to supplier
- You could integrate backward (make it yourself)

### Software/SaaS Specific Suppliers:
- Cloud infrastructure (AWS, GCP, Azure)
- Payment processors (Stripe, Braintree)
- Communication APIs (Twilio, SendGrid)
- Data providers
- Development tools

---

## Force 3: Bargaining Power of Buyers

**Question:** How much power do your customers have?

### High Buyer Power When:
- Few large customers dominate purchases
- Products are undifferentiated
- Switching costs are low
- Price sensitivity is high
- Buyers have full information
- Buyers can integrate backward (build it themselves)

### Low Buyer Power When:
- Many fragmented customers
- Product is differentiated or unique
- High switching costs
- Product is critical to buyer's business
- Limited alternatives available

### Assessment Questions:
- What percentage of revenue comes from top customers?
- How price-sensitive are customers?
- How differentiated is your offering?
- What are the switching costs?

---

## Force 4: Threat of Substitutes

**Question:** How easily can customers find alternative solutions?

### High Substitute Threat When:
- Many alternative ways to solve the problem
- Substitutes offer better price-performance
- Low switching costs to substitutes
- Buyers are willing to change

### Low Substitute Threat When:
- Few viable alternatives exist
- Substitutes are inferior or more expensive
- High switching costs
- Strong brand loyalty

### Types of Substitutes:
- **Direct:** Different product, same function (email vs. Slack)
- **Indirect:** Different approach to the problem (video calls vs. in-person meetings)
- **DIY:** Building internally (spreadsheets, custom development)
- **Do nothing:** Accepting the status quo

---

## Force 5: Competitive Rivalry

**Question:** How intense is competition among existing players?

### High Rivalry When:
- Many competitors of similar size
- Slow industry growth
- High fixed costs pressure pricing
- Low differentiation between products
- High exit barriers
- Diverse competitors with different strategies

### Low Rivalry When:
- Clear market leader exists
- Fast industry growth
- Products are differentiated
- High switching costs
- Competitors are similar in strategy

### Rivalry Indicators:
- Price wars occurring?
- Heavy marketing spending?
- Frequent feature releases?
- Aggressive sales tactics?
- Consolidation happening?

---

## Competitive Landscape Analysis

Beyond Porter's Five Forces, analyze specific competitors:

### Competitor Profile Template

```markdown
## Competitor: [Name]

### Overview
- **Founded:** [Year]
- **Funding:** [Total raised]
- **Size:** [Employees, revenue estimate]
- **HQ:** [Location]

### Product
- **Core offering:** [Description]
- **Target market:** [Who they serve]
- **Pricing:** [Model and price points]
- **Key features:** [Top 3-5 differentiators]

### Positioning
- **Value proposition:** [Their pitch]
- **Brand perception:** [How market sees them]
- **Strengths:** [What they do well]
- **Weaknesses:** [Where they fall short]

### Go-to-Market
- **Sales motion:** [PLG/Sales-led/Hybrid]
- **Primary channels:** [How they acquire customers]
- **Key partnerships:** [Important relationships]

### Competitive Assessment
- **Threat level:** [High/Medium/Low]
- **Direct overlap:** [Where you compete]
- **Their advantage:** [Why customers might choose them]
- **Your advantage:** [Why customers might choose you]
```

---

## Competitive Positioning Map

Visualize where you stand relative to competitors:

```
                    HIGH PRICE
                        │
                        │
          Enterprise    │    Premium
           Solutions    │    Specialists
                        │
    LOW ────────────────┼──────────────── HIGH
    FEATURE             │             FEATURE
    BREADTH             │             BREADTH
                        │
           Budget       │    Feature-Rich
           Options      │    Value Players
                        │
                        │
                    LOW PRICE

Position your business: [  ]
Competitors: A[  ], B[  ], C[  ]
```

---

## Industry Attractiveness Score

Combine the five forces into an overall assessment:

| Force | Score (1-5) | Weight | Weighted |
|-------|-------------|--------|----------|
| Threat of New Entrants | ___ | 20% | ___ |
| Supplier Power | ___ | 15% | ___ |
| Buyer Power | ___ | 25% | ___ |
| Threat of Substitutes | ___ | 20% | ___ |
| Competitive Rivalry | ___ | 20% | ___ |
| **Total** | | 100% | **___** |

**Scoring Guide:**
- 1 = Very favorable to business (low threat/power)
- 5 = Very unfavorable (high threat/power)

**Industry Attractiveness:**
- 1.0-1.8: Attractive industry
- 1.9-2.6: Above average
- 2.7-3.3: Average
- 3.4-4.1: Below average
- 4.2-5.0: Unattractive industry

---

## Output Template

```markdown
# Competitive Analysis: [Industry/Business]

**Date:** [Date]
**Analyst:** [Name]

## Executive Summary

[2-3 sentences on competitive dynamics and strategic implications]

## Porter's Five Forces Analysis

### 1. Threat of New Entrants: [LOW/MEDIUM/HIGH]

**Key Barriers:**
- [Barrier 1]: [Assessment]
- [Barrier 2]: [Assessment]

**Assessment:** [2-3 sentence analysis]

### 2. Supplier Power: [LOW/MEDIUM/HIGH]

**Key Suppliers:**
- [Supplier type]: [Power level and why]

**Assessment:** [2-3 sentence analysis]

### 3. Buyer Power: [LOW/MEDIUM/HIGH]

**Customer Profile:**
- Concentration: [Fragmented/Moderate/Concentrated]
- Price sensitivity: [High/Medium/Low]
- Switching costs: [High/Medium/Low]

**Assessment:** [2-3 sentence analysis]

### 4. Threat of Substitutes: [LOW/MEDIUM/HIGH]

**Key Substitutes:**
| Substitute | Threat Level | Price-Performance |
|------------|--------------|-------------------|
| [Name] | [H/M/L] | [Better/Same/Worse] |

**Assessment:** [2-3 sentence analysis]

### 5. Competitive Rivalry: [LOW/MEDIUM/HIGH]

**Market Structure:**
- Number of competitors: [Few/Moderate/Many]
- Market growth: [Declining/Stable/Growing/Rapid]
- Differentiation: [Low/Medium/High]

**Assessment:** [2-3 sentence analysis]

## Key Competitors

### [Competitor 1]
- **Position:** [Their market position]
- **Strengths:** [What they do well]
- **Weaknesses:** [Where they fall short]
- **Threat level:** [High/Medium/Low]

### [Competitor 2]
[Same format]

## Competitive Positioning

[Include positioning map or description]

## Overall Assessment

**Industry Attractiveness Score:** [X.X/5.0]
**Interpretation:** [Attractive/Average/Unattractive]

**Dominant Forces:** [Which 1-2 forces most impact this industry]

## Strategic Recommendations

1. **[Recommendation 1]** - [Brief rationale]
2. **[Recommendation 2]** - [Brief rationale]
3. **[Recommendation 3]** - [Brief rationale]

## Competitive Risks to Monitor

- [Risk 1]
- [Risk 2]
```

---

## Questions for Different Scenarios

### For Entering a New Market
- What's the minimum viable differentiation?
- Which incumbent is most vulnerable?
- What's the fastest path to sustainable position?

### For Defending Position
- Where are we most vulnerable to new entrants?
- How can we increase switching costs?
- What competitor moves should we anticipate?

### For Growth Strategy
- Which adjacent markets have favorable dynamics?
- Can we change the competitive rules?
- Where can we build barriers others can't cross?

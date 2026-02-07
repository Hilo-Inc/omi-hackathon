---
name: market-sizing
description: TAM/SAM/SOM market size analysis for business planning. Use when the user says "market size", "TAM SAM SOM", "market opportunity", "addressable market", "market research", or wants to understand the size of a market opportunity.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
---

# Market Sizing Skill

Calculate and analyze market size using TAM/SAM/SOM framework for business planning and investor presentations.

## Invocation

This skill activates when:
- User wants to size a market opportunity
- User mentions "TAM", "SAM", "SOM"
- User asks about addressable market
- User is preparing investor materials

Arguments: `$ARGUMENTS` (business description, target market, or specific market to size)

---

## TAM/SAM/SOM Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │                         TAM                              │  │
│   │         Total Addressable Market                        │  │
│   │    "If we had 100% market share globally"               │  │
│   │                                                         │  │
│   │   ┌─────────────────────────────────────────────────┐  │  │
│   │   │                     SAM                          │  │  │
│   │   │       Serviceable Addressable Market            │  │  │
│   │   │    "The portion we can actually serve"          │  │  │
│   │   │                                                 │  │  │
│   │   │   ┌─────────────────────────────────────────┐  │  │  │
│   │   │   │               SOM                        │  │  │  │
│   │   │   │    Serviceable Obtainable Market        │  │  │  │
│   │   │   │    "What we can realistically capture"  │  │  │  │
│   │   │   │                                         │  │  │  │
│   │   │   └─────────────────────────────────────────┘  │  │  │
│   │   └─────────────────────────────────────────────────┘  │  │
│   └─────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## TAM - Total Addressable Market

**Definition:** The total market demand for a product/service if you had 100% market share.

### Calculation Methods

#### 1. Top-Down Approach

Start with industry data and narrow down:

```
Industry Size × Relevant Segment % = TAM

Example:
Global CRM Market:         $65 billion
Enterprise Segment:        × 40%
─────────────────────────────────────
Enterprise CRM TAM:        $26 billion
```

**Data Sources:**
- Industry reports (Gartner, Forrester, IBISWorld)
- Government statistics
- Trade associations
- Public company filings

#### 2. Bottom-Up Approach

Build up from unit economics:

```
# of Potential Customers × Average Revenue per Customer = TAM

Example:
Small businesses in US:        30 million
% that could use CRM:          × 40%
Potential customers:           12 million
Average annual spend:          × $1,200
─────────────────────────────────────
SMB CRM TAM:                   $14.4 billion
```

#### 3. Value Theory Approach

Calculate based on value created:

```
Value Created × Ability to Capture = TAM

Example:
Hours saved per user:          10 hrs/month
Hourly cost of labor:          × $50
Annual savings per user:       $6,000
% captured in price:           × 20%
Annual value per user:         $1,200
Potential users:               × 10 million
─────────────────────────────────────
TAM:                           $12 billion
```

---

## SAM - Serviceable Addressable Market

**Definition:** The portion of TAM that you can realistically target given current limitations.

### Limiting Factors

| Factor | Question | Example Reduction |
|--------|----------|-------------------|
| **Geography** | Where can you operate? | US only = -60% of global |
| **Product fit** | Who can your product serve? | Enterprise only = -70% |
| **Language** | What markets can you reach? | English only = -50% |
| **Regulatory** | Where are you licensed? | HIPAA = healthcare only |
| **Go-to-market** | Who can you sell to? | PLG = tech-savvy SMB |

### Calculation

```
TAM - Excluded Segments = SAM

Example:
Global CRM TAM:                $65 billion
Exclude: Non-English markets   × 50%
Exclude: Enterprise (>1000)    × 30%
Exclude: Non-tech industries   × 60%
─────────────────────────────────────
SAM:                           $5.85 billion
```

### SAM Calculation Template

```markdown
## SAM Calculation

| Starting Point | | |
|----------------|---|---|
| TAM | $65B | Global CRM market |

| Reduction | % Remaining | Market Size |
|-----------|-------------|-------------|
| English-speaking only | 50% | $32.5B |
| SMB segment only | 30% | $9.75B |
| Tech industries only | 60% | $5.85B |

**SAM = $5.85B** (9% of TAM)
```

---

## SOM - Serviceable Obtainable Market

**Definition:** The realistic market share you can capture in a defined timeframe (usually 3-5 years).

### Factors Affecting SOM

| Factor | Impact |
|--------|--------|
| Competitive intensity | More competitors = smaller SOM |
| Market growth | Growing market = larger SOM |
| Product differentiation | Unique = larger SOM |
| Sales capacity | More reps = larger SOM |
| Brand awareness | Known brand = larger SOM |
| Switching costs | High = harder to capture |

### Realistic Market Share Expectations

| Market Structure | Achievable Share (5 years) |
|------------------|---------------------------|
| Fragmented, many players | 1-5% |
| Moderate concentration | 3-10% |
| Emerging market | 10-20% |
| Niche market | 15-30% |

### Calculation

```
SAM × Realistic Market Share = SOM

Example:
SAM:                           $5.85 billion
Target market share (5 yr):    × 3%
─────────────────────────────────────
SOM (5 year):                  $175 million
```

### SOM Validation

Cross-check with capacity-based calculation:

```
Sales Capacity × Win Rate × Average Deal Size = Revenue Capacity

Example:
Sales reps (Year 5):           50
Deals per rep per year:        × 24
Total deals:                   1,200
Win rate:                      × 25%
Won deals:                     300
Average deal size:             × $50,000
─────────────────────────────────────
Revenue capacity:              $15 million/year
ARR at Year 5 (cumulative):    ~$50 million
```

---

## Showing Your Math

Always include calculations for credibility:

```markdown
## Market Size Calculation

### TAM: $14.4 Billion

**Methodology:** Bottom-up from customer count

| Input | Value | Source |
|-------|-------|--------|
| Small businesses in US | 30M | US Census Bureau |
| % that need accounting software | 40% | [Industry report] |
| Addressable businesses | 12M | Calculated |
| Average annual spend | $1,200 | Competitor pricing |
| **TAM** | **$14.4B** | |

### SAM: $2.9 Billion

**Methodology:** TAM minus excluded segments

| Exclusion | Remaining | Rationale |
|-----------|-----------|-----------|
| Non-tech-savvy (60% excluded) | 40% | Our PLG model requires tech comfort |
| <$100K revenue (30% excluded) | 70% | Don't have budget |
| **SAM** | $14.4B × 0.4 × 0.7 = **$2.9B** | |

### SOM: $145 Million (5-year)

**Methodology:** SAM × achievable market share

| Factor | Assumption | Rationale |
|--------|------------|-----------|
| Market share target | 5% | Fragmented market, strong differentiation |
| Timeline | 5 years | Based on growth trajectory |
| **SOM** | $2.9B × 0.05 = **$145M** | |

**Validation:** This implies ~2,900 customers at $50K ACV, requiring
~50 sales reps at $1M quota each. Achievable with planned hiring.
```

---

## Common Mistakes to Avoid

### Red Flags

| Mistake | Problem | Better Approach |
|---------|---------|-----------------|
| **TAM without methodology** | Not credible | Show your math |
| **SOM > 10% in crowded market** | Unrealistic | Be conservative |
| **Using only top-down** | Can miss nuance | Cross-check with bottom-up |
| **Ignoring competition** | Looks naive | Acknowledge market share realities |
| **Vague customer counts** | Hard to verify | Use specific, sourced numbers |

### Green Flags

| Practice | Why It Works |
|----------|--------------|
| Multiple methodologies agree | Cross-validation builds confidence |
| Clear customer × ARPU math | Easy to understand and verify |
| Conservative assumptions | Shows discipline and credibility |
| Sources cited | Demonstrates research rigor |
| Path from current to SOM | Shows realistic planning |

---

## Market Dynamics

Beyond size, analyze market characteristics:

```markdown
## Market Dynamics

### Growth Characteristics
| Metric | Value | Source |
|--------|-------|--------|
| Market CAGR | 15% | [Report] |
| Segment growth | 22% | [Report] |
| Growth drivers | [List] | |
| Growth headwinds | [List] | |

### Market Stage
☐ Emerging (high growth, few players)
☐ Growing (strong growth, competition entering)
☐ Mature (stable, consolidated)
☐ Declining (negative growth)

### Competitive Intensity
| Factor | Assessment |
|--------|------------|
| Number of competitors | Many (>20) |
| Market concentration | Fragmented (top 5 have 30%) |
| Barriers to entry | Medium |
| Switching costs | Low |
```

---

## Output Template

```markdown
# Market Size Analysis: [Market Name]

**Date:** [Date]
**Analyst:** [Name]

## Executive Summary

| Metric | Value | Timeframe |
|--------|-------|-----------|
| TAM | $[X]B | Current |
| SAM | $[X]B | Current |
| SOM | $[X]M | 5-year |
| Market CAGR | [X]% | Projected |

## TAM Analysis

### Methodology
[Top-down / Bottom-up / Value theory]

### Calculation
[Show the math with sources]

### TAM = $[X] Billion

## SAM Analysis

### Limiting Factors
[What reduces TAM to SAM]

### Calculation
[Show the reductions]

### SAM = $[X] Billion ([X]% of TAM)

## SOM Analysis

### Market Share Assumptions
[Why this share is achievable]

### Calculation
[Show the math]

### SOM = $[X] Million ([X]% of SAM)

### Validation
[Capacity-based cross-check]

## Market Dynamics

### Growth
[CAGR and drivers]

### Competitive Landscape
[Key players and concentration]

### Trends
[What's changing in the market]

## Confidence Assessment

| Component | Confidence | Notes |
|-----------|------------|-------|
| TAM | High/Medium/Low | [Why] |
| SAM | High/Medium/Low | [Why] |
| SOM | High/Medium/Low | [Why] |

## Sources

1. [Source 1]
2. [Source 2]
3. [Source 3]
```

---

## Quick Reference

### For Investor Presentations

Focus on:
- SAM more than TAM (shows focus)
- Bottom-up validation
- Clear path to SOM
- Market growth rate

### For Internal Planning

Focus on:
- SOM accuracy (drives hiring, investment)
- Segment breakdown
- Geographic analysis
- Competitive share assumptions

### For New Market Entry

Focus on:
- TAM to understand total opportunity
- SAM to define initial target
- Market dynamics and growth
- Competitive positioning

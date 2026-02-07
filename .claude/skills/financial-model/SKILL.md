---
name: financial-model
description: SaaS financial modeling and unit economics analysis. Use when the user says "financial model", "startup financials", "SaaS metrics", "unit economics", "revenue projections", "burn rate", or wants help with business financial planning.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
---

# Financial Model Skill

Build financial models for SaaS and subscription businesses, analyze unit economics, and project growth.

## Invocation

This skill activates when:
- User wants to build a financial model
- User asks about SaaS metrics or unit economics
- User wants to project revenue, costs, or funding needs
- User mentions "burn rate", "LTV:CAC", "runway"

Arguments: `$ARGUMENTS` (current metrics, business stage, or specific analysis needed)

---

## Core SaaS Metrics

### Revenue Metrics

| Metric | Formula | Healthy Benchmark |
|--------|---------|-------------------|
| **MRR** | Monthly Recurring Revenue | Depends on stage |
| **ARR** | MRR × 12 | Depends on stage |
| **ARPU** | MRR ÷ Customers | Varies by market |
| **Revenue Growth Rate** | (New MRR - Old MRR) ÷ Old MRR | 15-20% MoM early stage |
| **Net New MRR** | New MRR + Expansion - Contraction - Churn | Positive |

### MRR Components

```
┌─────────────────────────────────────────────────────────────┐
│                        MRR Bridge                           │
├─────────────────────────────────────────────────────────────┤
│  Starting MRR                              $100,000         │
│  + New MRR (new customers)                 + $15,000        │
│  + Expansion MRR (upsells)                 +  $5,000        │
│  - Contraction MRR (downgrades)            -  $2,000        │
│  - Churned MRR (lost customers)            -  $8,000        │
│  ─────────────────────────────────────────────────────      │
│  = Ending MRR                              $110,000         │
│                                                             │
│  Net New MRR: $10,000 (10% growth)                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Unit Economics

### Customer Acquisition Cost (CAC)

**Formula:** Total Sales & Marketing Spend ÷ New Customers Acquired

**Components:**
- Paid advertising spend
- Sales team salaries + commissions
- Marketing team costs
- Marketing tools and software
- Content creation costs
- Events and sponsorships

**Benchmarks by model:**
| Business Type | Typical CAC |
|--------------|-------------|
| Self-serve SaaS | $50-500 |
| SMB SaaS | $500-2,000 |
| Mid-market SaaS | $2,000-10,000 |
| Enterprise SaaS | $10,000-100,000+ |

### Lifetime Value (LTV)

**Basic Formula:** ARPU × Gross Margin × Customer Lifetime

**Alternative:** ARPU × Gross Margin ÷ Monthly Churn Rate

**Example:**
```
ARPU:           $100/month
Gross Margin:   80%
Churn Rate:     5%/month

LTV = $100 × 0.80 ÷ 0.05 = $1,600
```

### LTV:CAC Ratio

**Formula:** LTV ÷ CAC

| Ratio | Interpretation |
|-------|----------------|
| < 1:1 | Losing money on each customer - unsustainable |
| 1:1 - 2:1 | Thin margins, problematic |
| 3:1 | Healthy target |
| 4:1 - 5:1 | Excellent, room to invest |
| > 5:1 | May be under-investing in growth |

### CAC Payback Period

**Formula:** CAC ÷ (ARPU × Gross Margin)

| Payback | Assessment |
|---------|------------|
| < 6 months | Excellent |
| 6-12 months | Good |
| 12-18 months | Acceptable for enterprise |
| > 18 months | Concerning (unless enterprise) |

---

## Retention Metrics

### Churn Rates

**Logo Churn:** % of customers who cancel
**Revenue Churn:** % of MRR lost to cancellations
**Net Revenue Churn:** % MRR lost after expansion

**Benchmarks:**
| Metric | Good | Great | Elite |
|--------|------|-------|-------|
| Monthly Logo Churn | < 5% | < 3% | < 2% |
| Annual Logo Churn | < 10% | < 7% | < 5% |
| Net Revenue Retention | > 100% | > 110% | > 120% |

### Net Revenue Retention (NRR)

**Formula:** (Starting MRR + Expansion - Contraction - Churn) ÷ Starting MRR × 100

```
Starting MRR:    $100,000
Expansion:       + $15,000
Contraction:     - $5,000
Churn:           - $8,000
                 ─────────
Ending MRR:      $102,000

NRR = 102%
```

**What NRR tells you:**
- > 100%: Growing revenue from existing customers
- = 100%: Flat (expansion equals churn)
- < 100%: Shrinking (leaky bucket)

---

## Profitability Metrics

### Gross Margin

**Formula:** (Revenue - COGS) ÷ Revenue × 100

**SaaS COGS typically includes:**
- Hosting/infrastructure costs
- Customer support salaries
- Payment processing fees
- Third-party software costs

**Benchmarks:**
| Business Type | Target Gross Margin |
|--------------|---------------------|
| SaaS | 70-85% |
| Marketplace | 50-70% |
| E-commerce | 30-50% |
| Services | 50-70% |

### Operating Efficiency Metrics

**Magic Number**
```
Formula: Net New ARR ÷ Prior Quarter S&M Spend

> 0.75 = Invest aggressively
0.5-0.75 = Solid efficiency
< 0.5 = Improve before scaling
```

**Burn Multiple**
```
Formula: Net Burn ÷ Net New ARR

< 1 = Excellent efficiency
1-2 = Good
2-3 = Mediocre
> 3 = Poor (burning too much)
```

**Rule of 40**
```
Formula: Revenue Growth Rate + Profit Margin ≥ 40%

Example: 30% growth + 15% margin = 45% ✓
Example: 50% growth + (-15%) margin = 35% ✗
```

---

## Financial Model Template

### Revenue Projections

```markdown
## Revenue Model

### Assumptions
- Starting MRR: $50,000
- New customer growth: 10% MoM
- Churn rate: 3% monthly
- ARPU: $100
- Expansion rate: 2% MoM

### 12-Month Projection

| Month | Starting MRR | New MRR | Expansion | Churn | Ending MRR |
|-------|-------------|---------|-----------|-------|------------|
| 1 | $50,000 | $5,000 | $1,000 | $1,500 | $54,500 |
| 2 | $54,500 | $5,450 | $1,090 | $1,635 | $59,405 |
| ... | ... | ... | ... | ... | ... |
| 12 | $X | $X | $X | $X | $X |

### Year 1 Summary
- Ending ARR: $X
- Total Revenue: $X
- YoY Growth: X%
```

### Cost Structure

```markdown
## Cost Structure

### Fixed Costs (Monthly)
| Category | Amount | Notes |
|----------|--------|-------|
| Engineering (salaries) | $40,000 | 4 engineers |
| Product/Design | $15,000 | 1 PM, 1 designer |
| G&A | $10,000 | Office, legal, accounting |
| Infrastructure | $5,000 | AWS, tools |
| **Total Fixed** | **$70,000** | |

### Variable Costs (Per Customer)
| Category | Cost/Customer | Notes |
|----------|---------------|-------|
| Support | $5/mo | Scales with base |
| Infrastructure | $2/mo | Per-customer usage |
| Payment processing | 2.9% + $0.30 | Stripe |
| **Total Variable** | ~**$10/customer** | |

### Sales & Marketing
| Category | Amount | Notes |
|----------|--------|-------|
| Marketing team | $15,000 | 1 marketer |
| Paid acquisition | $10,000 | Google, FB |
| Content/SEO | $5,000 | Writers, tools |
| **Total S&M** | **$30,000** | |
```

### Cash Flow Projection

```markdown
## Cash Flow Model

### Monthly Cash Flow

| Line Item | Month 1 | Month 6 | Month 12 |
|-----------|---------|---------|----------|
| Revenue | $50,000 | $80,000 | $150,000 |
| COGS | ($10,000) | ($16,000) | ($30,000) |
| **Gross Profit** | $40,000 | $64,000 | $120,000 |
| S&M | ($30,000) | ($40,000) | ($50,000) |
| R&D | ($55,000) | ($70,000) | ($90,000) |
| G&A | ($10,000) | ($12,000) | ($15,000) |
| **Net Income** | ($55,000) | ($58,000) | ($35,000) |

### Runway Analysis
- Current cash: $500,000
- Monthly burn: $55,000
- Runway: ~9 months
- Break-even at: $X MRR
```

---

## Key Financial Ratios

### For Investors

| Ratio | Formula | What It Shows |
|-------|---------|---------------|
| **LTV:CAC** | LTV ÷ CAC | Capital efficiency |
| **Payback Period** | CAC ÷ Monthly Margin | Speed of capital recovery |
| **Magic Number** | Net New ARR ÷ S&M | Sales efficiency |
| **Burn Multiple** | Net Burn ÷ Net New ARR | Capital efficiency |
| **Rule of 40** | Growth + Margin | Balance of growth and profit |

### For Operations

| Metric | Formula | What It Shows |
|--------|---------|---------------|
| **Gross Margin** | (Rev - COGS) ÷ Rev | Product profitability |
| **NRR** | Ending MRR ÷ Starting MRR | Customer expansion health |
| **Quick Ratio** | (New + Expansion) ÷ (Churn + Contraction) | Growth efficiency |
| **CAC by Channel** | Channel Spend ÷ Channel Customers | Channel efficiency |

---

## Scenario Analysis

### Best / Base / Worst Case

```markdown
## Scenario Analysis: 12-Month Outlook

|  | Pessimistic | Base | Optimistic |
|--|-------------|------|------------|
| **Growth Rate** | 5% MoM | 10% MoM | 15% MoM |
| **Churn Rate** | 5% | 3% | 2% |
| **Ending MRR** | $75K | $120K | $180K |
| **Cash Used** | $800K | $600K | $400K |
| **Runway** | 6 mo | 10 mo | 15 mo |

### Key Sensitivities
1. Churn: Each 1% reduction in churn = $X additional MRR
2. CAC: Each $100 reduction in CAC = X more customers
3. ARPU: Each $10 increase = $X additional MRR
```

---

## Funding Requirements

### Calculating Runway Needs

```
Target: 18-24 months runway post-raise

Monthly burn (current): $55,000
Monthly burn (post-raise): $100,000 (hiring)

Capital needed:
- Operating capital: $100K × 18 months = $1.8M
- Buffer (20%): $360K
- Total raise: ~$2.2M

With 25% dilution: $8.8M post-money valuation
```

### Use of Funds Template

```markdown
## Use of Funds ($2M Raise)

| Category | Amount | % | Purpose |
|----------|--------|---|---------|
| Engineering | $800K | 40% | 3 new hires, infrastructure |
| Sales & Marketing | $600K | 30% | Paid acquisition, 2 hires |
| Operations | $400K | 20% | Support, success, G&A |
| Buffer | $200K | 10% | Contingency |
| **Total** | **$2M** | 100% | |

### Milestone Targets
- Month 6: $150K MRR
- Month 12: $300K MRR
- Month 18: $500K MRR (Series A ready)
```

---

## Output Template

```markdown
# Financial Model: [Company Name]

**Version:** 1.0
**Date:** [Date]
**Stage:** [Pre-seed / Seed / Series A / etc.]

## Current State

### Key Metrics
| Metric | Value |
|--------|-------|
| MRR | $X |
| Customers | X |
| ARPU | $X |
| Churn | X% |
| CAC | $X |
| LTV | $X |
| LTV:CAC | X:1 |
| Gross Margin | X% |

### Assessment
[Overall health of unit economics]

## Projections

### 12-Month Forecast
[Revenue projection table]

### Key Assumptions
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Unit Economics Deep Dive

### LTV Calculation
[Show the math]

### CAC Breakdown
[By channel]

### Payback Analysis
[Time to recover CAC]

## Cash Flow & Runway

### Current Runway
[Months remaining]

### Funding Needs
[If applicable]

## Recommendations

1. [Financial recommendation]
2. [Operational recommendation]
3. [Growth recommendation]
```

---

## Quick Reference: SaaS Benchmarks

| Stage | ARR | Growth | Churn | LTV:CAC |
|-------|-----|--------|-------|---------|
| Pre-seed | $0-100K | - | < 7% | > 2:1 |
| Seed | $100K-1M | 15-20% MoM | < 5% | > 3:1 |
| Series A | $1-5M | 10-15% MoM | < 3% | > 3:1 |
| Series B | $5-15M | 100%+ YoY | < 2% | > 4:1 |
| Growth | $15M+ | 50%+ YoY | < 2% | > 5:1 |

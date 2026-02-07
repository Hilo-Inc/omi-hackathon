---
name: lean-canvas
description: Create Lean Canvas business models for startups and new ventures. Use when the user says "lean canvas", "business model", "startup idea", "value proposition", "problem-solution fit", or wants to validate a business concept.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
---

# Lean Canvas Skill

Create a one-page business model adapted from the Business Model Canvas, optimized for startups and new ventures.

## Invocation

This skill activates when:
- User wants to create a Lean Canvas
- User mentions "business model", "startup idea", "value proposition"
- User wants to validate or document a business concept
- User asks about problem-solution fit

Arguments: `$ARGUMENTS` (business idea description or existing business to analyze)

---

## The Lean Canvas Framework

The Lean Canvas has 9 blocks that capture the essential elements of a business model:

```
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│    PROBLEM      │    SOLUTION     │  UNIQUE VALUE   │   UNFAIR        │   CUSTOMER      │
│                 │                 │   PROPOSITION   │   ADVANTAGE     │   SEGMENTS      │
│  • Problem 1    │  • Feature 1    │                 │                 │                 │
│  • Problem 2    │  • Feature 2    │  "Headline"     │  • Advantage    │  • Target       │
│  • Problem 3    │  • Feature 3    │                 │                 │  • Early Adopter│
│                 │                 │                 │                 │                 │
│  Alternatives:  │                 │                 │                 │                 │
│  • Alt 1        │                 │                 │                 │                 │
├─────────────────┼─────────────────┼─────────────────┴─────────────────┼─────────────────┤
│  KEY METRICS    │    CHANNELS     │                                   │                 │
│                 │                 │                                   │                 │
│  • Metric 1     │  • Channel 1    │                                   │                 │
│  • Metric 2     │  • Channel 2    │                                   │                 │
│                 │                 │                                   │                 │
├─────────────────┴─────────────────┼───────────────────────────────────┴─────────────────┤
│        COST STRUCTURE             │              REVENUE STREAMS                        │
│                                   │                                                     │
│  • Fixed: $X                      │  • Model: Subscription                              │
│  • Variable: $Y per unit          │  • Price: $Z/mo                                     │
│  • CAC: $W                        │  • LTV: $V                                          │
└───────────────────────────────────┴─────────────────────────────────────────────────────┘
```

---

## Workflow

### Step 1: Gather Information

Before creating the canvas, ask clarifying questions:

1. **Problem Space**
   - What specific problem are you solving?
   - Who experiences this problem most acutely?
   - How are people solving this today?

2. **Solution Space**
   - What's your core solution?
   - What's the minimum viable product (MVP)?
   - What makes your approach different?

3. **Business Model**
   - Who will pay for this?
   - How will you reach customers?
   - What's your pricing strategy?

### Step 2: Fill Each Block

---

## Block 1: Problem (Top 3 Problems)

**What to capture:**
- Top 1-3 specific problems your target customers face
- Existing alternatives customers use today
- Limitations of current solutions

**Questions to ask:**
- What keeps your target customer up at night?
- What are they currently doing to solve this?
- Why is the current solution inadequate?

**Red flags:**
- Problems that are too vague ("save time")
- Problems you have, not your customers
- Problems that don't cause enough pain to pay for

**Example:**
```markdown
### Problem
1. Small businesses spend 10+ hours/month on bookkeeping
2. Accounting software is too complex for non-accountants
3. Can't get real-time visibility into cash flow

**Existing Alternatives:**
- Spreadsheets (manual, error-prone)
- QuickBooks (complex, expensive)
- Hire a bookkeeper ($500+/month)
```

---

## Block 2: Customer Segments

**What to capture:**
- Primary target customer (be specific)
- Early adopters (who will buy first?)
- Characteristics that define them

**Questions to ask:**
- Who has this problem most acutely?
- Who can afford to pay for a solution?
- Who is easiest to reach?

**Specificity levels:**
- Too broad: "Small businesses"
- Better: "Solo entrepreneurs with 0-2 employees"
- Best: "Solo ecommerce store owners doing $10K-100K/month in revenue"

**Example:**
```markdown
### Customer Segments

**Primary:** Solo e-commerce entrepreneurs, $10K-100K monthly revenue

**Early Adopters:**
- Shopify store owners
- Already using multiple SaaS tools
- Active in entrepreneur communities

**Characteristics:**
- Non-technical background
- Time-poor but growth-focused
- Price-sensitive to subscription fatigue
```

---

## Block 3: Unique Value Proposition

**What to capture:**
- Single, clear, compelling message
- Why you're different AND worth paying for
- The transformation you provide

**Formula:** "We help [target customer] [achieve outcome] by [unique approach]"

**Questions to ask:**
- What's the single most compelling reason to buy?
- What transformation do you provide?
- Can you say this in 8 words or less?

**Example:**
```markdown
### Unique Value Proposition

**Headline:** "Books that balance themselves"

**Subheadline:** AI-powered bookkeeping that automatically categorizes
expenses and generates financial reports - no accounting knowledge required.

**Key differentiator:** Automated categorization with 95% accuracy vs
manual entry in traditional tools
```

---

## Block 4: Solution (Top 3 Features)

**What to capture:**
- Top 1-3 features that address the problems
- Keep it minimal - MVP thinking
- Link each feature to a specific problem

**Rules:**
- Each solution should map to a problem
- Focus on outcomes, not features
- What's the simplest thing that could work?

**Example:**
```markdown
### Solution

| Problem | Solution |
|---------|----------|
| 10+ hrs on bookkeeping | Auto-import and categorize transactions |
| Too complex | Plain-English financial dashboard |
| No cash flow visibility | Real-time cash flow forecasting |

**MVP Features:**
1. Bank connection + auto-categorization
2. Simple profit/loss dashboard
3. One-click tax reports
```

---

## Block 5: Channels

**What to capture:**
- How you'll reach customers
- Free vs paid channels
- Early vs scale channels

**Channel types:**
- **Inbound:** SEO, content marketing, social media
- **Outbound:** Sales, ads, cold outreach
- **Product-led:** Viral features, referrals, integrations

**Example:**
```markdown
### Channels

**Primary (Working):**
- Content marketing (SEO blog posts)
- Shopify app marketplace

**Secondary (Testing):**
- YouTube tutorials
- Podcast sponsorships

**Future:**
- Partner integrations
- Referral program
```

---

## Block 6: Revenue Streams

**What to capture:**
- How you'll make money
- Pricing model and price points
- Unit economics basics

**Model options:**
- Subscription (monthly/annual)
- Transaction fees
- Freemium
- Usage-based
- One-time purchase

**Example:**
```markdown
### Revenue Streams

**Model:** Freemium subscription

**Pricing:**
- Free: Up to 50 transactions/month
- Starter: $19/month (500 transactions)
- Growth: $49/month (unlimited)

**Unit Economics:**
- ARPU: $35/month
- Estimated LTV: $840 (24-month avg lifetime)
```

---

## Block 7: Cost Structure

**What to capture:**
- Fixed costs (salaries, rent, subscriptions)
- Variable costs (per-customer, per-transaction)
- Customer acquisition cost

**Categories:**
- Development/Engineering
- Operations/Infrastructure
- Sales/Marketing
- Support/Success
- General/Admin

**Example:**
```markdown
### Cost Structure

**Fixed Monthly:**
- Engineering (2 devs): $20,000
- Infrastructure: $2,000
- Tools/SaaS: $500

**Variable:**
- Bank API: $0.10/connection
- Support: $2/customer/month
- Payment processing: 2.9%

**CAC:** ~$50 (content-driven acquisition)
```

---

## Block 8: Key Metrics

**What to capture:**
- The metrics that tell you if the business is working
- North Star metric (one number that matters most)
- Pirate metrics (AARRR)

**Pirate Metrics Framework:**
- **A**cquisition: How do users find you?
- **A**ctivation: Do they have a good first experience?
- **R**etention: Do they come back?
- **R**evenue: Do they pay?
- **R**eferral: Do they tell others?

**Example:**
```markdown
### Key Metrics

**North Star:** Weekly Active Users who run at least one report

**AARRR Metrics:**
- Acquisition: Monthly signups
- Activation: % connecting bank within 24hrs
- Retention: Monthly active users
- Revenue: MRR, ARPU
- Referral: Viral coefficient
```

---

## Block 9: Unfair Advantage

**What to capture:**
- What can't be easily copied or bought
- Be honest - many startups don't have one initially
- What will become defensible over time?

**Types of moats:**
- Network effects
- Proprietary data
- Switching costs
- Brand/trust
- Team/expertise
- Regulatory/legal
- Community

**Example:**
```markdown
### Unfair Advantage

**Current:**
- None yet (honest assessment)

**Building toward:**
- Transaction data that improves categorization AI
- Integrations that increase switching costs
- Community of small business owners

**Team advantage:**
- Former QuickBooks product manager
- Deep understanding of SMB pain points
```

---

## Output Template

```markdown
# Lean Canvas: [Business Name]

**Date:** [Date]
**Version:** 1.0
**Stage:** [Idea / Validation / Growth / Scale]

## The Canvas

### Problem
1. [Problem 1]
2. [Problem 2]
3. [Problem 3]

**Existing Alternatives:**
- [Alternative 1]
- [Alternative 2]

### Customer Segments
**Target:** [Specific description]
**Early Adopters:** [Who will buy first]

### Unique Value Proposition
> "[Headline - 8 words or less]"

[1-2 sentence explanation]

### Solution
1. [Feature → Problem it solves]
2. [Feature → Problem it solves]
3. [Feature → Problem it solves]

### Channels
- [Channel 1] (primary)
- [Channel 2] (testing)

### Revenue Streams
- **Model:** [Subscription/Transaction/etc.]
- **Price:** [Price points]
- **Target ARPU:** [$X/month]

### Cost Structure
- **Fixed:** [$X/month]
- **Variable:** [$Y per customer]
- **Target CAC:** [$Z]

### Key Metrics
- **North Star:** [Metric]
- **Activation:** [Metric]
- **Retention:** [Metric]

### Unfair Advantage
[Honest assessment of defensibility]

---

## Riskiest Assumptions

1. [Assumption that must be true for this to work]
2. [Next riskiest assumption]
3. [Third assumption to validate]

## Next Steps to Validate

1. [Experiment to test assumption 1]
2. [Experiment to test assumption 2]
```

---

## Validation Tips

### Testing Problem-Solution Fit
- Talk to 20+ potential customers
- Ask about their current solution
- Would they pay for yours? How much?

### Common Mistakes
- Too many features in solution
- Customer segment too broad
- UVP is a feature, not a benefit
- Ignoring existing alternatives
- Confusing "nice to have" with "must have"

### Signs of Good Canvas
- Problems are specific and painful
- Customer segment is precise
- UVP is clear and differentiated
- Revenue model is validated
- Assumptions are identified

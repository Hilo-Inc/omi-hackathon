---
name: pitch-deck
description: Create investor pitch decks for startups and fundraising. Use when the user says "pitch deck", "investor presentation", "fundraising", "startup pitch", "VC presentation", or wants help presenting their business to investors.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
---

# Pitch Deck Skill

Create compelling investor pitch decks for startup fundraising following proven structures.

## Invocation

This skill activates when:
- User wants to create a pitch deck
- User mentions "investor presentation", "fundraising"
- User wants help with startup pitch materials
- User asks about presenting to VCs or angels

Arguments: `$ARGUMENTS` (business description, stage, or specific slides needed)

---

## Pitch Deck Structure

The classic 10-12 slide structure that investors expect:

```
┌──────────────────────────────────────────────────────────────┐
│  1. Title/Hook      │  2. Problem        │  3. Solution      │
├──────────────────────────────────────────────────────────────┤
│  4. Market Size     │  5. Business Model │  6. Traction      │
├──────────────────────────────────────────────────────────────┤
│  7. Competition     │  8. Team           │  9. Financials    │
├──────────────────────────────────────────────────────────────┤
│  10. The Ask        │  11. Roadmap       │  12. Closing      │
└──────────────────────────────────────────────────────────────┘
```

---

## Slide 1: Title/Hook

**Purpose:** Make a memorable first impression

**Include:**
- Company name and logo
- One-sentence tagline
- Contact information

**Example:**
```
[LOGO]

ACME ROBOTICS
"Self-driving forklifts for the warehouse of tomorrow"

Jane Smith, CEO
jane@acmerobotics.com
```

**Tips:**
- Tagline should be memorable and clear
- Avoid jargon
- Make them want to learn more

---

## Slide 2: Problem

**Purpose:** Establish the pain point you're solving

**Structure:**
- State the problem in concrete terms
- Quantify the impact (time, money, frustration)
- Show who experiences it

**Example:**
```
## The Problem

Warehouse managers lose $2M+ annually to forklift inefficiency:

📊 30% of shifts spent on idle forklifts
⏱️ 4 hours/day on manual route planning
💸 $50K/year per forklift in labor costs

"Finding drivers is impossible. Last year we turned down
$5M in orders because we couldn't staff the warehouse."
- Operations Director, Fortune 500 Retailer
```

**Tips:**
- Use real quotes from customers
- Lead with the most compelling stat
- Make the pain visceral

---

## Slide 3: Solution

**Purpose:** Show how you solve the problem

**Structure:**
- Clear explanation of your product
- How it addresses each pain point
- Show the product (screenshot/demo)

**Example:**
```
## Our Solution

ACME transforms any forklift into an autonomous vehicle.

Before ACME                After ACME
────────────────         ────────────────
Manual drivers           Self-driving 24/7
Idle time                Optimized routes
Staffing headaches       Set and forget

[PRODUCT SCREENSHOT/VIDEO]

"We deployed ACME in one warehouse. Now we're rolling
out to all 12." - Customer Name, Title
```

**Tips:**
- Show, don't just tell
- Connect solution to problem points
- Include social proof

---

## Slide 4: Market Size

**Purpose:** Prove the opportunity is big enough

**Structure:**
- TAM (Total Addressable Market)
- SAM (Serviceable Addressable Market)
- SOM (Serviceable Obtainable Market)

**Example:**
```
## Market Opportunity

$47B                    $12B                    $500M
Total Addressable       Serviceable             Our Target
Market                  Addressable             (5 years)
                        Market

Global warehouse        North American          Enterprise
automation             warehouses >100K sf      customers

[SHOW CALCULATION]
Bottom-up: 15,000 target warehouses × $33K/year = $500M

Growing 18% CAGR driven by:
• E-commerce growth
• Labor shortages
• Safety regulations
```

**Tips:**
- Show your math
- Use bottom-up when possible
- Cite sources

---

## Slide 5: Business Model

**Purpose:** Explain how you make money

**Structure:**
- Pricing model
- Unit economics (if available)
- Revenue streams

**Example:**
```
## Business Model

Hardware + Software Subscription

$15,000              $1,500/mo           $33,000
One-time setup       Per forklift        Annual Contract
per forklift         subscription        Value (typical)

Unit Economics
───────────────────────────────────
CAC:            $8,000
LTV:            $45,000 (3-year avg)
LTV:CAC:        5.6x
Payback:        6 months
Gross Margin:   72%
```

**Tips:**
- Show you understand unit economics
- Be honest about what you know vs. assume
- Keep it simple

---

## Slide 6: Traction

**Purpose:** Prove market validation

**Structure:**
- Key metrics (revenue, users, growth)
- Milestones achieved
- Customer logos/testimonials

**Example:**
```
## Traction

Revenue Growth                 Key Milestones
─────────────                 ─────────────────
$2.5M ARR                     ✓ 50 robots deployed
450% YoY growth               ✓ 12 enterprise customers
$35K average contract         ✓ 0 safety incidents
95% annual retention          ✓ SOC 2 certified

[GRAPH: Monthly revenue showing hockey stick]

Customers include:
[LOGO] [LOGO] [LOGO] [LOGO] [LOGO]
```

**Tips:**
- Lead with strongest metrics
- Show trajectory, not just snapshot
- Be honest about what's real vs. pipeline

---

## Slide 7: Competition

**Purpose:** Show you understand the landscape

**Structure:**
- Competitive matrix or positioning map
- Your differentiation
- Why you win

**Example:**
```
## Competitive Landscape

                    Full Autonomy
                         │
         New Players     │    ACME ★
                         │
    LOW ─────────────────┼──────────────────── HIGH
    COST                 │                    COST
                         │
       Legacy Automation │    AGV Vendors
                         │
                    Partial Autonomy

Why We Win:
✓ 10x faster deployment (2 days vs. 6 months)
✓ Works with existing forklifts (vs. buying new)
✓ No infrastructure changes needed
```

**Tips:**
- Position yourself favorably (but honestly)
- Acknowledge real competitors
- Focus on differentiation, not bashing

---

## Slide 8: Team

**Purpose:** Prove you're the team to execute

**Structure:**
- Founders with relevant experience
- Key hires
- Advisors (if notable)

**Example:**
```
## Team

Jane Smith               John Doe                Sarah Lee
CEO                      CTO                     VP Sales

15 yrs robotics          Ex-Waymo               Ex-Amazon
Former VP at Boston      Led autonomy team       Built warehouse
Dynamics                 MIT PhD                 division to $50M

Advisory Board
─────────────────────────────────────
[NAME] - Former CEO, [Relevant Company]
[NAME] - Partner, [VC Firm]

Team of 25 across engineering, sales, and operations
```

**Tips:**
- Highlight relevant experience
- Show founder-market fit
- Include notable advisors/investors

---

## Slide 9: Financials

**Purpose:** Show financial trajectory and understanding

**Structure:**
- Historical revenue (if any)
- Projections (3-5 years)
- Key assumptions

**Example:**
```
## Financial Projections

Revenue ($M)
─────────────────────────────────────
         2024    2025    2026    2027
ARR      $2.5    $8.0    $20     $50
Growth    -      220%    150%    150%

Path to $50M ARR:
• 500 robots deployed (10x current)
• 50 enterprise customers
• 85% gross margin at scale
• Expansion into Europe

Key Assumptions:
• 12-month sales cycle
• 95% annual retention
• $2M CAC per customer (enterprise)
```

**Tips:**
- Be realistic, not hockey-stick fantasy
- Show you understand drivers
- Acknowledge assumptions

---

## Slide 10: The Ask

**Purpose:** Tell them what you need

**Structure:**
- Amount raising
- Use of funds
- Milestones this enables

**Example:**
```
## The Ask

Raising $10M Series A

Use of Funds                 18-Month Milestones
─────────────────           ─────────────────────
Engineering     45%         • 200 robots deployed
Sales & Mktg    35%         • $15M ARR
Operations      15%         • 40 customers
G&A              5%         • Series B ready

Current investors: [LOGOS]
This round: Lead + 2-3 strategic partners
```

**Tips:**
- Be specific about use of funds
- Connect raise to milestones
- Know your valuation expectations

---

## Slide 11: Roadmap (Optional)

**Purpose:** Show your vision and execution plan

**Structure:**
- Near-term milestones (6-12 months)
- Medium-term goals (12-24 months)
- Long-term vision

**Example:**
```
## Roadmap

Q1-Q2 2024               Q3-Q4 2024              2025
─────────────           ─────────────          ─────────────
Product                 Product                 Product
• Multi-robot           • Outdoor capability   • Full warehouse
  coordination          • Integration suite      orchestration

Go-to-Market            Go-to-Market            Go-to-Market
• Enterprise sales      • Channel partners     • International
  team (5 reps)         • Self-serve for SMB     expansion
```

---

## Slide 12: Closing

**Purpose:** End with impact

**Options:**
- Return to the vision/big picture
- Memorable closing statement
- Call to action

**Example:**
```
## The Opportunity

Warehouses move 25 billion tons of goods annually.
Labor shortages will only get worse.
Automation is inevitable.

ACME is making it accessible.

[LOGO]

Let's build the warehouse of tomorrow.

Jane Smith
jane@acmerobotics.com
(555) 123-4567
```

---

## Appendix Slides

Prepare these for Q&A:

- **Detailed financials** - Full P&L, assumptions
- **Customer case study** - Deep dive on one customer
- **Technical architecture** - For technical investors
- **Go-to-market detail** - Sales process, channels
- **Competitive deep dive** - More detailed analysis
- **Cap table** - Current ownership, ESOP
- **Product roadmap** - Detailed feature plans

---

## Pitch Deck Best Practices

### Design
- One idea per slide
- Large, readable fonts (24pt minimum)
- Consistent color scheme
- Professional, not flashy
- Dark mode optional but trendy

### Content
- 10-12 slides for main deck
- 3-5 minute verbal pitch per slide
- Tell a story (problem → solution → why now → why us)
- Data > claims
- Visuals > text

### Delivery
- Know your deck cold
- Anticipate questions
- Have appendix slides ready
- Practice with timer
- Get feedback from other founders

### Common Mistakes
- Too many slides
- Walls of text
- Unrealistic projections
- Dismissing competition
- Weak "why us" story
- Not knowing your numbers

---

## Output Template

When creating a pitch deck, output each slide as:

```markdown
# Pitch Deck: [Company Name]

## Slide 1: Title
[Content]

## Slide 2: Problem
[Content]

[Continue for all slides...]

---

## Speaker Notes

### Slide 1
[What to say when presenting this slide]

### Slide 2
[Speaker notes...]

---

## Appendix

### A1: [Topic]
[Detailed content for Q&A]
```

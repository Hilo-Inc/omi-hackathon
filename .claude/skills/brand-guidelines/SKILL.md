---
name: brand-guidelines
description: Create comprehensive brand style guides and identity documentation. Use when the user says "brand guidelines", "brand identity", "style guide", "brand manual", "brand standards", or wants to document their brand system.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
---

# Brand Guidelines Skill

Create comprehensive brand style guides that ensure consistent visual and verbal identity across all touchpoints.

## Invocation

This skill activates when:
- User wants to create brand guidelines or a style guide
- User mentions "brand identity", "brand manual", "brand standards"
- User needs to document logo usage, colors, typography rules
- User wants to establish voice and tone guidelines

Arguments: `$ARGUMENTS` (brand name, industry, existing assets, or specific sections needed)

---

## Brand Guidelines Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Brand Guidelines Contents                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. BRAND FOUNDATION        2. VISUAL IDENTITY       3. VERBAL IDENTITY    │
│  ┌─────────────────────┐    ┌─────────────────────┐  ┌─────────────────────┐│
│  │ • Mission           │    │ • Logo              │  │ • Voice & Tone     ││
│  │ • Vision            │    │ • Color Palette     │  │ • Messaging        ││
│  │ • Values            │    │ • Typography        │  │ • Taglines         ││
│  │ • Brand Story       │    │ • Photography       │  │ • Writing Style    ││
│  │ • Positioning       │    │ • Iconography       │  │ • Terminology      ││
│  │ • Target Audience   │    │ • Illustrations     │  │ • Grammar Rules    ││
│  └─────────────────────┘    │ • Data Visualization│  └─────────────────────┘│
│                             │ • Motion/Animation  │                         │
│  4. APPLICATION             └─────────────────────┘  5. DIGITAL GUIDELINES │
│  ┌─────────────────────┐                            ┌─────────────────────┐│
│  │ • Business Cards    │                            │ • UI Components     ││
│  │ • Letterhead        │                            │ • Web Standards     ││
│  │ • Presentations     │                            │ • App Guidelines    ││
│  │ • Social Media      │                            │ • Email Templates   ││
│  │ • Signage           │                            │ • Accessibility     ││
│  │ • Merchandise       │                            │ • Responsive Rules  ││
│  └─────────────────────┘                            └─────────────────────┘│
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Section 1: Brand Foundation

### Mission Statement
**What to include:**
- What the company does
- Who it serves
- How it creates value

**Template:**
> We [action verb] [target audience] to [benefit/outcome] by [unique approach].

**Example:**
> We empower small business owners to grow their revenue by providing intuitive financial tools that eliminate accounting complexity.

### Vision Statement
**What to include:**
- Future aspirational state
- Long-term impact goal
- Inspiring direction

**Template:**
> A world where [ideal future state].

**Example:**
> A world where every entrepreneur has the financial clarity to make confident business decisions.

### Brand Values
**Format each value as:**
```markdown
### [Value Name]
**Definition:** What this value means to us
**Behaviors:** How we demonstrate this value
**Example:** Specific instance of this value in action
```

**Example:**
```markdown
### Transparency
**Definition:** We believe in open, honest communication—even when it's uncomfortable.
**Behaviors:**
- Share pricing clearly without hidden fees
- Admit mistakes promptly and explain our fixes
- Provide clear documentation for all processes
**Example:** Our public changelog shows all product updates, including bug fixes.
```

### Brand Personality

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Brand Personality Spectrum                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Professional ○────────●────────○ Playful                                  │
│                     [Balanced]                                              │
│                                                                             │
│  Traditional ○────────────────●○ Innovative                                │
│                        [Modern]                                             │
│                                                                             │
│  Reserved    ○──────●──────────○ Expressive                                │
│                [Confident]                                                  │
│                                                                             │
│  Serious     ○────────●────────○ Humorous                                  │
│                   [Friendly]                                                │
│                                                                             │
│  Complex     ○──────────────●──○ Simple                                    │
│                         [Clear]                                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Target Audience

**Template:**
```markdown
### Primary Audience: [Name/Segment]
- **Demographics:** Age, location, income, education
- **Psychographics:** Values, interests, lifestyle
- **Pain Points:** Problems they face
- **Goals:** What they want to achieve
- **How We Help:** Our solution for them

### Secondary Audience: [Name/Segment]
[Same format...]
```

---

## Section 2: Visual Identity

### Logo

#### Primary Logo
```markdown
### Primary Logo
The primary logo should be used whenever possible.

[Image placeholder: Primary logo]

**Minimum Size:**
- Print: 1 inch / 25mm wide
- Digital: 100px wide

**Clear Space:**
Maintain clear space equal to the height of the logomark "X" on all sides.

┌──────────────────────────────────┐
│                                  │
│    ┌──────────────────────┐      │
│    │    X                 │      │
│ X  │    ████  BRAND NAME  │  X   │
│    │    X                 │      │
│    └──────────────────────┘      │
│                                  │
└──────────────────────────────────┘
      ↑ Clear space = X height
```

#### Logo Variations
```markdown
### Logo Variations

| Version | Use Case | File |
|---------|----------|------|
| Full color | Default, light backgrounds | logo-full-color.svg |
| Reversed | Dark backgrounds | logo-reversed.svg |
| Monochrome | Single-color applications | logo-mono.svg |
| Icon only | Favicons, small spaces | logo-icon.svg |
| Horizontal | Wide spaces, headers | logo-horizontal.svg |
| Stacked | Square spaces, social avatars | logo-stacked.svg |
```

#### Logo Misuse
```markdown
### Logo Misuse - Do Not:

✗ Stretch or distort the logo
✗ Rotate the logo
✗ Change the logo colors
✗ Add effects (shadows, gradients, outlines)
✗ Place on busy backgrounds without sufficient contrast
✗ Rearrange logo elements
✗ Use outdated versions
✗ Recreate or redraw the logo
✗ Add other elements inside clear space
✗ Use the logo smaller than minimum size
```

### Color Palette

```markdown
### Primary Colors

#### Brand Blue
The primary brand color used for key brand elements.

| Format | Value |
|--------|-------|
| HEX | #2563EB |
| RGB | 37, 99, 235 |
| CMYK | 84, 58, 0, 8 |
| Pantone | 2728 C |

**Usage:** Primary buttons, links, headings, logo

---

### Secondary Colors

#### Slate Gray
Supporting color for text and UI elements.

| Format | Value |
|--------|-------|
| HEX | #475569 |
| RGB | 71, 85, 105 |
| CMYK | 32, 19, 0, 59 |

**Usage:** Body text, secondary UI elements

---

### Accent Colors

[Additional colors with same format]

---

### Color Usage Rules

| Color | Primary Use | Max Coverage |
|-------|-------------|--------------|
| Brand Blue | CTAs, links, key elements | 10-20% |
| Slate Gray | Text, borders | 20-30% |
| White | Backgrounds | 50-60% |
| Accent | Highlights only | 5-10% |
```

### Typography

```markdown
### Primary Typeface: Inter

Inter is our primary typeface for all digital and print communications.

**Font Weights:**
- Regular (400) - Body text
- Medium (500) - Emphasis, subheadings
- Semibold (600) - Headings, buttons
- Bold (700) - Display, impact

**Fallback Stack:**
`'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`

---

### Type Scale

| Style | Size | Weight | Line Height | Letter Spacing | Use |
|-------|------|--------|-------------|----------------|-----|
| Display | 48px | Bold | 1.1 | -0.02em | Hero headlines |
| H1 | 36px | Bold | 1.2 | -0.01em | Page titles |
| H2 | 28px | Semibold | 1.25 | -0.01em | Section headers |
| H3 | 22px | Semibold | 1.3 | 0 | Subsections |
| H4 | 18px | Medium | 1.4 | 0 | Card titles |
| Body Large | 18px | Regular | 1.6 | 0 | Introductions |
| Body | 16px | Regular | 1.5 | 0 | Default text |
| Body Small | 14px | Regular | 1.5 | 0 | Captions, meta |
| Caption | 12px | Regular | 1.4 | 0.01em | Labels, footnotes |

---

### Typography Rules

**Do:**
- Maintain consistent hierarchy
- Use adequate line spacing for readability
- Left-align body text (for LTR languages)
- Use sentence case for body text

**Don't:**
- Use more than 2 typefaces
- Stretch or compress type
- Use all caps for long text
- Center-align paragraphs
- Use light weights below 16px
```

### Photography Style

```markdown
### Photography Guidelines

**Style Characteristics:**
- Natural lighting with warm tones
- Authentic, candid moments over posed shots
- Diverse representation of people
- Clean, uncluttered compositions
- Shallow depth of field for product focus

**Color Treatment:**
- Slight warmth (+5 to +10 on temperature)
- Natural contrast (avoid heavy filters)
- Consistent white balance

**Subject Guidelines:**

| Subject | Approach |
|---------|----------|
| People | Genuine expressions, diverse, in context |
| Products | Clean backgrounds, natural shadows |
| Environments | Bright, modern, aspirational spaces |
| Abstract | Brand colors subtly present |

**Don't Use:**
- Overly staged stock photography
- Heavy filters or dated treatments
- Low-resolution images
- Images with visible competitor branding
- Culturally insensitive imagery
```

### Iconography

```markdown
### Icon Style

**Characteristics:**
- 2px stroke weight
- Rounded corners (2px radius)
- 24x24px base grid
- Consistent optical sizing

**Icon Grid:**
┌────────────────────────┐
│  ┌──────────────────┐  │
│  │                  │  │ 2px padding
│  │   Icon content   │  │
│  │                  │  │
│  └──────────────────┘  │
└────────────────────────┘
       24 x 24px

**Colors:**
- Primary: Current text color (inherit)
- Interactive: Brand Blue on hover
- Disabled: Gray-400

**Usage Rules:**
- Maintain consistent stroke weight
- Don't mix icon styles (outline vs. filled)
- Ensure touch targets are 44x44px minimum
- Include accessible labels for functional icons
```

---

## Section 3: Verbal Identity

### Voice & Tone

```markdown
### Brand Voice

Our voice is **confident**, **clear**, and **helpful**.

| Voice Attribute | What It Means | Example |
|-----------------|---------------|---------|
| **Confident** | We know our stuff and share expertise without arrogance | "Here's exactly how to solve this" not "Maybe you could try..." |
| **Clear** | We explain complex things simply | "Your payment failed" not "Transaction processing exception occurred" |
| **Helpful** | We anticipate needs and provide solutions | "Try this instead" not just "That won't work" |

---

### Tone Variations

Our tone adapts to context while maintaining our voice:

| Context | Tone | Example |
|---------|------|---------|
| Marketing | Inspiring, ambitious | "Build the future you've imagined" |
| Product UI | Clear, efficient | "Save changes" |
| Help docs | Patient, thorough | "Follow these steps to..." |
| Error states | Calm, solution-focused | "We couldn't save. Check your connection and try again." |
| Celebrations | Warm, genuine | "You did it! Your first project is live." |
| Crisis | Direct, empathetic | "We're experiencing issues. Here's what we know..." |
```

### Writing Guidelines

```markdown
### Writing Style

**General Rules:**
- Use active voice
- Keep sentences short (aim for 15-20 words)
- One idea per paragraph
- Use second person ("you") over third person
- Avoid jargon and buzzwords

**Capitalization:**
- Sentence case for headlines
- Title case for proper nouns only
- Never ALL CAPS for emphasis

**Numbers:**
- Spell out one through nine
- Use numerals for 10 and above
- Always use numerals with units (5px, 3MB)
- Use commas in thousands (1,000)

**Punctuation:**
- Use the Oxford comma
- One space after periods
- Avoid exclamation points (one per page max)
- Em dashes with no spaces—like this

**Contractions:**
- Use contractions to sound natural (we're, you'll, it's)
- Avoid in legal or formal contexts
```

### Messaging Framework

```markdown
### Brand Messaging Hierarchy

**Tagline:**
> [Short memorable phrase - 3-7 words]

**Value Proposition:**
> [One sentence explaining what you do, for whom, and why it matters]

**Elevator Pitch (30 seconds):**
> [3-4 sentences covering problem, solution, differentiation, and proof]

**Boilerplate (About Us):**
> [Standard paragraph for press releases, bios, and formal contexts]

---

### Key Messages by Audience

| Audience | Core Message | Proof Points |
|----------|--------------|--------------|
| [Audience 1] | [What they care about most] | [Evidence/benefits] |
| [Audience 2] | [What they care about most] | [Evidence/benefits] |
```

---

## Section 4: Application Examples

### Business Cards

```
┌─────────────────────────────────┐
│                                 │
│  [LOGO]                         │
│                                 │
│  Jane Smith                     │
│  Product Designer               │
│                                 │
│  jane@company.com               │
│  +1 (555) 123-4567              │
│  company.com                    │
│                                 │
└─────────────────────────────────┘
3.5" x 2" | 300 DPI | CMYK
Paper: 16pt uncoated
```

### Email Signature

```markdown
### Email Signature Template

**Jane Smith**
Product Designer | Company Name

📧 jane@company.com
📱 +1 (555) 123-4567
🌐 company.com

[Logo - 100px wide max]

---

**Rules:**
- Use company font or system fallback
- No more than 4 lines of contact info
- Logo optional, max 100px wide
- No quotes, banners, or promotional content
```

### Social Media

```markdown
### Social Media Specifications

| Platform | Profile Image | Cover Image | Post Image |
|----------|---------------|-------------|------------|
| LinkedIn | 400x400px | 1128x191px | 1200x627px |
| Twitter/X | 400x400px | 1500x500px | 1200x675px |
| Instagram | 320x320px | N/A | 1080x1080px |
| Facebook | 180x180px | 820x312px | 1200x630px |

**Profile Image:**
Use logo icon or logomark on brand background color.

**Voice by Platform:**
- LinkedIn: Professional, thought leadership
- Twitter/X: Conversational, timely
- Instagram: Visual, inspirational
- Facebook: Community, engaging
```

---

## Output Template

```markdown
# [Brand Name] Brand Guidelines

**Version:** 1.0
**Last Updated:** [Date]
**Owner:** [Team/Person]

---

## Table of Contents

1. Brand Foundation
   - Mission & Vision
   - Values
   - Brand Personality
   - Target Audience

2. Visual Identity
   - Logo
   - Color Palette
   - Typography
   - Photography
   - Iconography

3. Verbal Identity
   - Voice & Tone
   - Writing Guidelines
   - Key Messages

4. Applications
   - Print Collateral
   - Digital Templates
   - Social Media

5. Resources
   - Asset Downloads
   - Contact Information

---

## 1. Brand Foundation

### Our Mission
[Mission statement]

### Our Vision
[Vision statement]

### Our Values
[3-5 core values with descriptions]

### Brand Personality
[Personality attributes and spectrum]

### Who We Serve
[Target audience profiles]

---

## 2. Visual Identity

### Logo
[Logo versions, usage rules, clear space, minimum sizes, misuse examples]

### Color Palette
[Primary, secondary, accent, semantic colors with all format values]

### Typography
[Typefaces, type scale, usage rules]

### Photography
[Style guide, treatment, do's and don'ts]

### Iconography
[Icon style, grid, colors, usage]

---

## 3. Verbal Identity

### Voice & Tone
[Voice attributes, tone variations by context]

### Writing Guidelines
[Style rules, grammar, punctuation, terminology]

### Key Messages
[Tagline, value prop, elevator pitch, boilerplate]

---

## 4. Applications

### Business Cards
[Specifications and template]

### Email Signatures
[Template and rules]

### Presentations
[Template specifications]

### Social Media
[Platform specs, voice guidelines]

---

## 5. Resources

### Asset Downloads
- Logo package (SVG, PNG, EPS)
- Color swatches (ASE, CLR)
- Font files or license info
- Icon library
- Templates

### Questions?
Contact: [brand@company.com]

---

*These guidelines are a living document. Updates are published quarterly.*
```

---

## Best Practices

### Do
- Make guidelines searchable and accessible (web-based)
- Include real examples, not just rules
- Provide downloadable assets
- Update regularly as the brand evolves
- Get stakeholder buy-in before publishing

### Don't
- Make guidelines so rigid they stifle creativity
- Include unnecessary sections
- Hide guidelines behind logins
- Forget to version and date updates
- Assume everyone reads the full document

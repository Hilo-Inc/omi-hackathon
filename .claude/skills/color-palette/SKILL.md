---
name: color-palette
description: Generate accessible color palettes for UI design. Use when the user says "color palette", "color scheme", "brand colors", "color system", "UI colors", or wants to create or evaluate colors for their design.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
---

# Color Palette Skill

Generate accessible, harmonious color palettes for web and mobile interfaces using color theory principles and WCAG contrast requirements.

## Invocation

This skill activates when:
- User wants to create a color palette or scheme
- User mentions "brand colors", "UI colors", "color system"
- User wants to check color accessibility or contrast
- User needs light/dark mode color schemes

Arguments: `$ARGUMENTS` (brand color, industry, mood, or existing colors to build from)

---

## Color Theory Fundamentals

### The Color Wheel

```
                          Yellow (60°)
                              ●
                           /     \
                         /         \
            Yellow-    /             \    Yellow-
            Green    ●                 ●   Orange
            (90°)   /                   \  (30°)
                   /                     \
        Green ●───────────────────────────● Orange
        (120°)                             (0°/360°)
                   \                     /
                    \                   /
            Cyan     ●                 ●   Red-Orange
            (180°)    \               /    (330°)
                       \             /
                        \           /
                          ●───────●
                       Blue    Magenta
                      (240°)   (300°)
```

### Color Harmony Types

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Color Harmony Schemes                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  MONOCHROMATIC        ANALOGOUS           COMPLEMENTARY                     │
│  ┌───┐                ┌───┬───┬───┐       ┌───┐     ┌───┐                  │
│  │ ● │ One hue,       │ ● │ ● │ ● │       │ ● │ ←→  │ ● │                  │
│  │ ● │ varying        └───┴───┴───┘       └───┘     └───┘                  │
│  │ ● │ lightness      Adjacent on         Opposite on                       │
│  └───┘                the wheel           the wheel                         │
│                                                                             │
│  SPLIT-COMPLEMENTARY  TRIADIC             TETRADIC                         │
│      ┌───┐            ┌───┐               ┌───┐ ┌───┐                      │
│      │ ● │              ●                 │ ● │ │ ● │                      │
│     /     \           /   \               └───┘ └───┘                      │
│  ┌───┐   ┌───┐     ●───────●             ┌───┐ ┌───┐                      │
│  │ ● │   │ ● │     Three equal           │ ● │ │ ● │                      │
│  └───┘   └───┘     spacing               └───┘ └───┘                      │
│  Base + 2 adjacent                       Two complementary                  │
│  to complement                           pairs                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## The 60-30-10 Rule

A balanced color distribution for any interface:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           60-30-10 Distribution                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ████████████████████████████████████████████████████████████  60%         │
│  DOMINANT COLOR                                                             │
│  Background, large areas, overall feel                                      │
│  Usually: Neutral (white, light gray, dark gray)                           │
│                                                                             │
│  ████████████████████████████████  30%                                     │
│  SECONDARY COLOR                                                            │
│  Supporting elements, cards, sections                                       │
│  Usually: Brand primary or secondary                                        │
│                                                                             │
│  ███████████  10%                                                          │
│  ACCENT COLOR                                                               │
│  CTAs, highlights, important elements                                       │
│  Usually: Contrasting, attention-grabbing                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## WCAG Contrast Requirements

### Minimum Contrast Ratios

| Content Type | AA Standard | AAA Standard |
|--------------|-------------|--------------|
| Normal text (< 18px) | **4.5:1** | 7:1 |
| Large text (≥ 18px bold or ≥ 24px) | **3:1** | 4.5:1 |
| UI components & graphics | **3:1** | 3:1 |
| Non-essential decorative | No requirement | No requirement |

### Contrast Ratio Examples

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Contrast Ratio Examples                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  #000000 on #FFFFFF  →  21:1    ✓ AAA (Excellent)                          │
│  #595959 on #FFFFFF  →  7:1     ✓ AAA                                      │
│  #767676 on #FFFFFF  →  4.54:1  ✓ AA                                       │
│  #949494 on #FFFFFF  →  2.79:1  ✗ Fail                                     │
│                                                                             │
│  #FFFFFF on #2563EB  →  4.56:1  ✓ AA (Blue button)                         │
│  #FFFFFF on #3B82F6  →  3.13:1  ✓ AA Large only                            │
│  #FFFFFF on #60A5FA  →  2.22:1  ✗ Fail                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Color Palette Structure

### Complete UI Palette Components

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Complete Color System                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PRIMARY              SECONDARY           ACCENT                            │
│  Brand main color     Supporting brand    Highlight/CTA                     │
│  ┌─────────────────┐  ┌─────────────────┐ ┌─────────────────┐              │
│  │ 50  ░░░░░░░░░░░ │  │ 50  ░░░░░░░░░░░ │ │ 50  ░░░░░░░░░░░ │              │
│  │ 100 ░░░░░░░░░░░ │  │ 100 ░░░░░░░░░░░ │ │ 100 ░░░░░░░░░░░ │              │
│  │ 200 ░░░░░░░░░░░ │  │ 200 ░░░░░░░░░░░ │ │ 200 ░░░░░░░░░░░ │              │
│  │ 300 ░░░░░░░░░░░ │  │ 300 ░░░░░░░░░░░ │ │ 300 ░░░░░░░░░░░ │              │
│  │ 400 ░░░░░░░░░░░ │  │ 400 ░░░░░░░░░░░ │ │ 400 ░░░░░░░░░░░ │              │
│  │ 500 ████████████ │  │ 500 ████████████ │ │ 500 ████████████ │              │
│  │ 600 ████████████ │  │ 600 ████████████ │ │ 600 ████████████ │              │
│  │ 700 ████████████ │  │ 700 ████████████ │ │ 700 ████████████ │              │
│  │ 800 ████████████ │  │ 800 ████████████ │ │ 800 ████████████ │              │
│  │ 900 ████████████ │  │ 900 ████████████ │ │ 900 ████████████ │              │
│  └─────────────────┘  └─────────────────┘ └─────────────────┘              │
│                                                                             │
│  NEUTRALS/GRAYS       SEMANTIC COLORS                                       │
│  Text, borders, BGs   Feedback states                                       │
│  ┌─────────────────┐  ┌────────┬────────┬────────┬────────┐               │
│  │ 50  ░░░░░░░░░░░ │  │SUCCESS │WARNING │ ERROR  │  INFO  │               │
│  │ 100 ░░░░░░░░░░░ │  │ Green  │ Yellow │  Red   │  Blue  │               │
│  │ 200 ░░░░░░░░░░░ │  │        │ Orange │        │        │               │
│  │ 300 ░░░░░░░░░░░ │  ├────────┼────────┼────────┼────────┤               │
│  │ 400 ░░░░░░░░░░░ │  │  BG    │   BG   │   BG   │   BG   │               │
│  │ 500 ░░░░░░░░░░░ │  │ Border │ Border │ Border │ Border │               │
│  │ 600 ████████████ │  │  Text  │  Text  │  Text  │  Text  │               │
│  │ 700 ████████████ │  │  Icon  │  Icon  │  Icon  │  Icon  │               │
│  │ 800 ████████████ │  └────────┴────────┴────────┴────────┘               │
│  │ 900 ████████████ │                                                       │
│  │ 950 ████████████ │                                                       │
│  └─────────────────┘                                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Color Psychology Reference

| Color | Associations | Best For |
|-------|--------------|----------|
| **Blue** | Trust, security, calm, professional | Finance, healthcare, tech, corporate |
| **Green** | Growth, nature, health, money | Environment, health, finance, organic |
| **Red** | Energy, urgency, passion, danger | Food, entertainment, sales, alerts |
| **Orange** | Friendly, confident, creative | Youth brands, food, creative |
| **Yellow** | Optimism, clarity, warmth | Children, food, attention |
| **Purple** | Luxury, creativity, wisdom | Beauty, luxury, spirituality |
| **Pink** | Feminine, playful, romantic | Beauty, fashion, children |
| **Black** | Sophistication, luxury, power | Luxury, fashion, tech |
| **White** | Clean, simple, pure | Healthcare, minimalist, tech |

---

## Workflow

### Step 1: Gather Requirements

Ask about:
1. **Brand identity** - Existing colors? Logo colors?
2. **Industry/audience** - What sector? Target users?
3. **Mood/personality** - Professional? Playful? Bold?
4. **Competitors** - Colors to avoid?
5. **Application** - Web? Mobile? Print?

### Step 2: Choose Base Colors

Start with:
- **Primary**: Main brand color (usually from logo)
- **Secondary**: Supporting color (complement or analogous)
- **Accent**: High-contrast for CTAs

### Step 3: Generate Color Scales

For each base color, generate a 10-step scale:
- 50: Lightest (backgrounds)
- 100-400: Light variations
- 500: Base color
- 600-900: Dark variations
- 950: Darkest

### Step 4: Add Neutrals

Create a gray scale that complements the brand:
- Warm grays for warm palettes
- Cool grays for cool palettes
- True grays for neutral palettes

### Step 5: Add Semantic Colors

Define feedback colors:
- Success (green)
- Warning (yellow/orange)
- Error (red)
- Info (blue)

### Step 6: Verify Accessibility

Check all combinations:
- Text on backgrounds
- Button text on button colors
- Icons on backgrounds
- Focus states

### Step 7: Create Dark Mode Variant

Invert and adjust:
- Swap light/dark backgrounds
- Reduce saturation slightly
- Verify contrast ratios again

---

## Output Template

```markdown
# Color Palette Specification

**Project:** [Project Name]
**Version:** 1.0
**Created:** [Date]

## Brand Colors

### Primary Color
Base color that represents the brand identity.

| Step | Hex | RGB | Usage |
|------|-----|-----|-------|
| 50 | #EFF6FF | rgb(239, 246, 255) | Lightest backgrounds |
| 100 | #DBEAFE | rgb(219, 234, 254) | Hover backgrounds |
| 200 | #BFDBFE | rgb(191, 219, 254) | Active backgrounds |
| 300 | #93C5FD | rgb(147, 197, 253) | Borders |
| 400 | #60A5FA | rgb(96, 165, 250) | Icons (secondary) |
| 500 | #3B82F6 | rgb(59, 130, 246) | Base / Icons |
| 600 | #2563EB | rgb(37, 99, 235) | **Primary buttons** |
| 700 | #1D4ED8 | rgb(29, 78, 216) | Button hover |
| 800 | #1E40AF | rgb(30, 64, 175) | Button active |
| 900 | #1E3A8A | rgb(30, 58, 138) | Dark text |
| 950 | #172554 | rgb(23, 37, 84) | Darkest |

### Secondary Color
[Same format...]

### Accent Color
[Same format...]

## Neutral Colors

| Step | Hex | RGB | Usage |
|------|-----|-----|-------|
| 50 | #F9FAFB | rgb(249, 250, 251) | Page background |
| 100 | #F3F4F6 | rgb(243, 244, 246) | Card background |
| 200 | #E5E7EB | rgb(229, 231, 235) | Dividers |
| 300 | #D1D5DB | rgb(209, 213, 219) | Borders |
| 400 | #9CA3AF | rgb(156, 163, 175) | Placeholder text |
| 500 | #6B7280 | rgb(107, 114, 128) | Secondary text |
| 600 | #4B5563 | rgb(75, 85, 99) | Body text |
| 700 | #374151 | rgb(55, 65, 81) | Headings |
| 800 | #1F2937 | rgb(31, 41, 55) | Dark headings |
| 900 | #111827 | rgb(17, 24, 39) | High contrast text |
| 950 | #030712 | rgb(3, 7, 18) | Darkest |

## Semantic Colors

### Success
| Variant | Hex | Usage |
|---------|-----|-------|
| Light | #DCFCE7 | Background |
| Default | #16A34A | Icons, text |
| Dark | #14532D | Dark mode text |

### Warning
| Variant | Hex | Usage |
|---------|-----|-------|
| Light | #FEF9C3 | Background |
| Default | #CA8A04 | Icons, text |
| Dark | #713F12 | Dark mode text |

### Error
| Variant | Hex | Usage |
|---------|-----|-------|
| Light | #FEE2E2 | Background |
| Default | #DC2626 | Icons, text |
| Dark | #7F1D1D | Dark mode text |

### Info
| Variant | Hex | Usage |
|---------|-----|-------|
| Light | #DBEAFE | Background |
| Default | #2563EB | Icons, text |
| Dark | #1E3A8A | Dark mode text |

## Accessibility Matrix

### Light Mode Contrast Ratios

| Foreground | Background | Ratio | AA | AAA |
|------------|------------|-------|----|----|
| Gray-900 | White | 15.8:1 | ✓ | ✓ |
| Gray-600 | White | 5.74:1 | ✓ | - |
| Primary-600 | White | 4.56:1 | ✓ | - |
| White | Primary-600 | 4.56:1 | ✓ | - |
| Error | White | 4.63:1 | ✓ | - |

### Dark Mode Contrast Ratios

| Foreground | Background | Ratio | AA | AAA |
|------------|------------|-------|----|----|
| Gray-100 | Gray-900 | 12.6:1 | ✓ | ✓ |
| Gray-400 | Gray-900 | 5.41:1 | ✓ | - |
| Primary-400 | Gray-900 | 4.89:1 | ✓ | - |

## Theme Definitions

### Light Theme
```css
:root {
  --color-bg-primary: #FFFFFF;
  --color-bg-secondary: #F9FAFB;
  --color-text-primary: #111827;
  --color-text-secondary: #4B5563;
  --color-border: #E5E7EB;
  --color-action-primary: #2563EB;
}
```

### Dark Theme
```css
[data-theme="dark"] {
  --color-bg-primary: #111827;
  --color-bg-secondary: #1F2937;
  --color-text-primary: #F9FAFB;
  --color-text-secondary: #9CA3AF;
  --color-border: #374151;
  --color-action-primary: #3B82F6;
}
```

## Usage Guidelines

### Do
- Use Primary-600 for main CTAs
- Use Neutrals for text and backgrounds
- Use semantic colors only for their intended purpose
- Verify contrast for all text/background combinations

### Don't
- Use pure black (#000000) for text
- Use colors outside this palette
- Use semantic colors for decorative purposes
- Rely on color alone to convey meaning

## Color Blindness Considerations

All critical interactions should work for users with:
- Protanopia (red-blind)
- Deuteranopia (green-blind)
- Tritanopia (blue-blind)

Ensure:
- Error states use icons + text, not just red
- Success/error are distinguishable without color
- Charts use patterns or labels, not just colors
```

---

## Common Mistakes to Avoid

1. **Too many colors** - Stick to 2-3 main colors + neutrals + semantic
2. **Ignoring contrast** - Always verify WCAG compliance
3. **Saturated backgrounds** - Use tints (50-200) for backgrounds
4. **No system** - Use consistent scales, not random shades
5. **Color-only meaning** - Always pair color with text/icons
6. **Forgetting dark mode** - Plan both themes from the start

---

## Tools & Resources

- **Contrast Checker:** [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- **Palette Generator:** [Coolors](https://coolors.co/)
- **Color Scales:** [Tailwind CSS Colors](https://tailwindcss.com/docs/customizing-colors)
- **Color Blindness Simulator:** [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/)
- **Adobe Color:** [color.adobe.com](https://color.adobe.com/)

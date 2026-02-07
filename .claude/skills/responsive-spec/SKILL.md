---
name: responsive-spec
description: Create responsive design specifications with mobile-first approach. Use when the user says "responsive design", "mobile first", "breakpoints", "adaptive layout", "media queries", or wants to plan how a design adapts across screen sizes.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
---

# Responsive Design Specification Skill

Create comprehensive responsive design specifications that define how interfaces adapt across devices using mobile-first methodology.

## Invocation

This skill activates when:
- User wants to plan responsive layouts
- User mentions "breakpoints", "mobile-first", "adaptive design"
- User needs to document how components behave at different screen sizes
- User wants to specify media queries or responsive behavior

Arguments: `$ARGUMENTS` (component name, page layout, or specific responsive challenge)

---

## Mobile-First Philosophy

Mobile-first means designing for the smallest screen first, then progressively enhancing for larger screens.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Mobile-First Approach                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   START HERE                         ENHANCE                                │
│        ↓                                ↓                                   │
│   ┌─────────┐      ┌───────────────┐      ┌─────────────────────────────┐  │
│   │ ░░░░░░░ │      │ ░░░░░░░░░░░░░ │      │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │  │
│   │ ░░░░░░░ │  →   │ ░░░░░░░░░░░░░ │  →   │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │  │
│   │ ░░░░░░░ │      │ ░░░░░  ░░░░░░ │      │ ░░░░░  ░░░░░░░░░░  ░░░░░░░░ │  │
│   │ ░░░░░░░ │      │ ░░░░░  ░░░░░░ │      │ ░░░░░  ░░░░░░░░░░  ░░░░░░░░ │  │
│   │ ░░░░░░░ │      │ ░░░░░░░░░░░░░ │      │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │  │
│   └─────────┘      └───────────────┘      └─────────────────────────────┘  │
│      Mobile            Tablet                    Desktop                    │
│    (< 640px)        (640-1024px)              (> 1024px)                   │
│                                                                             │
│   Base styles       Add columns,             Add more columns,              │
│   Single column     larger spacing           sidebars, enhanced             │
│   Touch-optimized   Adjust navigation        features                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Why Mobile-First?

| Benefit | Explanation |
|---------|-------------|
| **Performance** | Mobile styles load first; larger screens load additional CSS |
| **Prioritization** | Forces you to focus on essential content |
| **Future-proof** | Mobile traffic continues to grow |
| **Simpler CSS** | `min-width` queries add features, not remove them |

---

## Standard Breakpoint System

### Recommended Breakpoints

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Standard Breakpoints                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Name        Width           Common Devices                                 │
│  ─────────────────────────────────────────────────                         │
│  xs          < 480px         Small phones (iPhone SE)                       │
│  sm          ≥ 480px         Large phones (iPhone 14)                       │
│  md          ≥ 768px         Tablets (iPad Mini)                            │
│  lg          ≥ 1024px        Laptops, tablets landscape                     │
│  xl          ≥ 1280px        Desktops                                       │
│  2xl         ≥ 1536px        Large desktops, monitors                       │
│                                                                             │
│  ──────────────────────────────────────────────────────────────────────    │
│                                                                             │
│  │    xs    │    sm    │      md      │      lg      │   xl   │   2xl  │   │
│  │  <480px  │  480px+  │    768px+    │   1024px+    │ 1280px+│ 1536px+│   │
│  ├──────────┼──────────┼──────────────┼──────────────┼────────┼────────┤   │
│  │   📱     │    📱    │      📱      │      💻      │   🖥️   │   🖥️   │   │
│  │  small   │  large   │    tablet    │    laptop    │desktop │ large  │   │
│  │  phone   │  phone   │              │              │        │ screen │   │
│  └──────────┴──────────┴──────────────┴──────────────┴────────┴────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### CSS Custom Properties for Breakpoints

```css
:root {
  /* Breakpoint values (for reference in JS) */
  --breakpoint-sm: 480px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
  --breakpoint-2xl: 1536px;
}
```

### Media Query Syntax (Mobile-First)

```css
/* Base styles - Mobile (all sizes) */
.component {
  padding: 1rem;
  display: flex;
  flex-direction: column;
}

/* Small phones and up */
@media (min-width: 480px) {
  .component {
    padding: 1.5rem;
  }
}

/* Tablets and up */
@media (min-width: 768px) {
  .component {
    flex-direction: row;
    gap: 2rem;
  }
}

/* Laptops and up */
@media (min-width: 1024px) {
  .component {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }
}

/* Large desktops */
@media (min-width: 1280px) {
  .component {
    gap: 3rem;
  }
}
```

---

## Responsive Layout Patterns

### Pattern 1: Stack to Horizontal

```
Mobile (< 768px)              Tablet+ (≥ 768px)
┌─────────────────┐           ┌──────────┬──────────┐
│      Item 1     │           │  Item 1  │  Item 2  │
├─────────────────┤     →     ├──────────┼──────────┤
│      Item 2     │           │  Item 3  │  Item 4  │
├─────────────────┤           └──────────┴──────────┘
│      Item 3     │
├─────────────────┤
│      Item 4     │
└─────────────────┘
```

```css
.grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr; /* Mobile: single column */
}

@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, 1fr); /* Tablet+: 2 columns */
  }
}
```

### Pattern 2: Sidebar Collapse

```
Mobile                        Desktop
┌─────────────────┐           ┌────────┬──────────────┐
│ ☰  Header       │           │        │              │
├─────────────────┤           │  Side  │    Main      │
│                 │     →     │  bar   │   Content    │
│  Main Content   │           │        │              │
│                 │           │        │              │
└─────────────────┘           └────────┴──────────────┘
  (Sidebar hidden/            (Sidebar visible)
   hamburger menu)
```

```css
.layout {
  display: grid;
  grid-template-columns: 1fr;
}

.sidebar {
  display: none; /* Hidden on mobile */
}

@media (min-width: 1024px) {
  .layout {
    grid-template-columns: 250px 1fr;
  }

  .sidebar {
    display: block;
  }
}
```

### Pattern 3: Reflow Navigation

```
Mobile                        Desktop
┌─────────────────┐           ┌──────────────────────────────────┐
│ Logo    ☰       │           │ Logo   Nav1  Nav2  Nav3  [Login] │
├─────────────────┤     →     └──────────────────────────────────┘
│ (Menu hidden)   │
└─────────────────┘
```

### Pattern 4: Cards Grid

```
Mobile (1 col)    Tablet (2 col)    Desktop (3-4 col)
┌───────────┐     ┌─────┬─────┐     ┌────┬────┬────┬────┐
│   Card    │     │Card │Card │     │Card│Card│Card│Card│
├───────────┤  →  ├─────┼─────┤  →  ├────┼────┼────┼────┤
│   Card    │     │Card │Card │     │Card│Card│Card│Card│
├───────────┤     └─────┴─────┘     └────┴────┴────┴────┘
│   Card    │
└───────────┘
```

```css
.card-grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
}

@media (min-width: 640px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (min-width: 1280px) {
  .card-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

---

## Component Responsive Behavior

### Navigation

| Breakpoint | Behavior |
|------------|----------|
| Mobile (< 768px) | Hamburger menu, off-canvas drawer |
| Tablet (768-1023px) | Horizontal nav, may collapse less-important items |
| Desktop (≥ 1024px) | Full horizontal navigation |

```css
/* Mobile: Hamburger */
.nav-menu {
  position: fixed;
  top: 0;
  left: -100%;
  width: 80%;
  height: 100vh;
  transition: left 0.3s ease;
}

.nav-menu.open {
  left: 0;
}

.hamburger {
  display: block;
}

/* Desktop: Horizontal */
@media (min-width: 1024px) {
  .nav-menu {
    position: static;
    width: auto;
    height: auto;
    display: flex;
    gap: 2rem;
  }

  .hamburger {
    display: none;
  }
}
```

### Typography Scale

| Element | Mobile | Tablet | Desktop |
|---------|--------|--------|---------|
| H1 | 28px (1.75rem) | 36px (2.25rem) | 48px (3rem) |
| H2 | 24px (1.5rem) | 28px (1.75rem) | 36px (2.25rem) |
| H3 | 20px (1.25rem) | 22px (1.375rem) | 24px (1.5rem) |
| Body | 16px (1rem) | 16px (1rem) | 16px (1rem) |
| Small | 14px (0.875rem) | 14px (0.875rem) | 14px (0.875rem) |

```css
h1 {
  font-size: 1.75rem;
}

@media (min-width: 768px) {
  h1 {
    font-size: 2.25rem;
  }
}

@media (min-width: 1024px) {
  h1 {
    font-size: 3rem;
  }
}
```

### Spacing Scale

| Size | Mobile | Tablet | Desktop |
|------|--------|--------|---------|
| Section padding | 24px | 48px | 80px |
| Card padding | 16px | 20px | 24px |
| Grid gap | 16px | 24px | 32px |
| Container max-width | 100% | 100% | 1280px |
| Container padding | 16px | 24px | 32px |

---

## Touch Target Guidelines

### Minimum Sizes

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Touch Target Requirements                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  WCAG 2.2 Requirement: 24x24px minimum                                      │
│  Recommended: 44x44px for comfortable tapping                               │
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────────────┐                        │
│  │                 │    │                         │                        │
│  │   24 x 24px     │    │       44 x 44px         │                        │
│  │   (minimum)     │    │     (recommended)       │                        │
│  │                 │    │                         │                        │
│  └─────────────────┘    └─────────────────────────┘                        │
│                                                                             │
│  Spacing between targets: At least 8px                                      │
│                                                                             │
│  ┌──────┐ 8px ┌──────┐ 8px ┌──────┐                                        │
│  │ Btn  │ gap │ Btn  │ gap │ Btn  │                                        │
│  └──────┘     └──────┘     └──────┘                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Button Sizes by Device

```css
.button {
  /* Mobile: Larger touch targets */
  min-height: 44px;
  padding: 12px 24px;
  font-size: 16px; /* Prevents iOS zoom on focus */
}

@media (min-width: 1024px) {
  .button {
    /* Desktop: Can be smaller with mouse precision */
    min-height: 36px;
    padding: 8px 16px;
    font-size: 14px;
  }
}
```

---

## Responsive Images

### Srcset and Sizes

```html
<img
  src="image-800.jpg"
  srcset="
    image-400.jpg 400w,
    image-800.jpg 800w,
    image-1200.jpg 1200w,
    image-1600.jpg 1600w
  "
  sizes="
    (max-width: 640px) 100vw,
    (max-width: 1024px) 50vw,
    33vw
  "
  alt="Description"
/>
```

### Art Direction (Picture Element)

```html
<picture>
  <!-- Mobile: Square crop -->
  <source
    media="(max-width: 767px)"
    srcset="hero-mobile.jpg"
  />
  <!-- Tablet: 4:3 crop -->
  <source
    media="(max-width: 1023px)"
    srcset="hero-tablet.jpg"
  />
  <!-- Desktop: Wide cinematic -->
  <img
    src="hero-desktop.jpg"
    alt="Hero image"
  />
</picture>
```

### Aspect Ratio Maintenance

```css
.image-container {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9; /* Maintains ratio */
}

.image-container img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

---

## Responsive Tables

### Pattern 1: Horizontal Scroll

```css
.table-container {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

table {
  min-width: 600px;
}
```

### Pattern 2: Stack on Mobile

```
Desktop                          Mobile
┌────────┬────────┬────────┐     ┌──────────────────┐
│ Name   │ Email  │ Status │     │ Name: John       │
├────────┼────────┼────────┤     │ Email: j@ex.com  │
│ John   │ j@...  │ Active │  →  │ Status: Active   │
├────────┼────────┼────────┤     ├──────────────────┤
│ Jane   │ ja@... │ Pending│     │ Name: Jane       │
└────────┴────────┴────────┘     │ Email: ja@ex.com │
                                 │ Status: Pending  │
                                 └──────────────────┘
```

```css
@media (max-width: 767px) {
  table, thead, tbody, th, td, tr {
    display: block;
  }

  thead {
    display: none;
  }

  td {
    position: relative;
    padding-left: 50%;
  }

  td::before {
    content: attr(data-label);
    position: absolute;
    left: 0;
    font-weight: bold;
  }
}
```

---

## Container Queries (Modern CSS)

For component-based responsive design:

```css
.card-container {
  container-type: inline-size;
  container-name: card;
}

.card {
  display: flex;
  flex-direction: column;
}

@container card (min-width: 400px) {
  .card {
    flex-direction: row;
  }
}
```

---

## Output Template

```markdown
# Responsive Design Specification

**Project:** [Project Name]
**Version:** 1.0
**Date:** [Date]

---

## Breakpoint System

| Name | Min Width | Target Devices |
|------|-----------|----------------|
| xs | 0 | Small phones |
| sm | 480px | Large phones |
| md | 768px | Tablets |
| lg | 1024px | Laptops |
| xl | 1280px | Desktops |
| 2xl | 1536px | Large monitors |

---

## Global Layout

### Container

| Breakpoint | Max Width | Padding |
|------------|-----------|---------|
| xs-sm | 100% | 16px |
| md | 100% | 24px |
| lg | 1024px | 32px |
| xl | 1200px | 32px |
| 2xl | 1400px | 32px |

### Grid System

| Breakpoint | Columns | Gutter |
|------------|---------|--------|
| xs-sm | 4 | 16px |
| md | 8 | 24px |
| lg+ | 12 | 24px |

---

## Typography Scale

| Element | xs-sm | md | lg+ |
|---------|-------|----|----|
| H1 | 1.75rem / 1.2 | 2.25rem / 1.2 | 3rem / 1.1 |
| H2 | 1.5rem / 1.25 | 1.75rem / 1.25 | 2.25rem / 1.2 |
| H3 | 1.25rem / 1.3 | 1.375rem / 1.3 | 1.5rem / 1.3 |
| Body | 1rem / 1.5 | 1rem / 1.5 | 1rem / 1.5 |

---

## Component Specifications

### [Component Name]

**Description:** [What the component does]

#### Responsive Behavior

| Breakpoint | Layout | Changes |
|------------|--------|---------|
| xs-sm | [Description] | [List changes] |
| md | [Description] | [List changes] |
| lg+ | [Description] | [List changes] |

#### Visual Diagram

```
Mobile              Tablet              Desktop
┌─────────┐         ┌───────────┐       ┌─────────────────┐
│ [Layout]│    →    │  [Layout] │   →   │    [Layout]     │
└─────────┘         └───────────┘       └─────────────────┘
```

#### CSS Implementation

```css
/* Mobile-first base */
.component {
  /* styles */
}

@media (min-width: 768px) {
  .component {
    /* tablet adjustments */
  }
}

@media (min-width: 1024px) {
  .component {
    /* desktop adjustments */
  }
}
```

---

## Navigation

| Breakpoint | Pattern | Details |
|------------|---------|---------|
| < 768px | Off-canvas drawer | Hamburger trigger, slide from left |
| 768-1023px | Horizontal, condensed | Priority+ pattern if needed |
| ≥ 1024px | Full horizontal | All items visible |

---

## Images

### Hero Images

| Breakpoint | Aspect Ratio | Treatment |
|------------|--------------|-----------|
| xs-sm | 1:1 or 4:3 | Center crop, essential content |
| md | 16:9 | Medium crop |
| lg+ | 21:9 | Full cinematic |

### Thumbnail Images

| Breakpoint | Size | Columns |
|------------|------|---------|
| xs-sm | 150px | 2 |
| md | 200px | 3 |
| lg+ | 250px | 4 |

---

## Touch Targets

| Element | Min Size | Min Spacing |
|---------|----------|-------------|
| Buttons | 44x44px | 8px |
| Links (inline) | 44px height | 8px vertical |
| Form inputs | 44px height | 12px |
| Icon buttons | 44x44px | 8px |

---

## Testing Checklist

### Breakpoint Testing
- [ ] Test at each defined breakpoint
- [ ] Test at breakpoint boundaries (±1px)
- [ ] Test in-between breakpoints

### Device Testing
- [ ] iPhone SE (375px)
- [ ] iPhone 14 Pro (393px)
- [ ] iPad Mini (768px)
- [ ] iPad Pro (1024px)
- [ ] Laptop (1280px)
- [ ] Desktop (1920px)

### Interaction Testing
- [ ] Touch targets are 44px minimum
- [ ] No horizontal scrolling (except tables)
- [ ] Forms are usable on mobile
- [ ] Navigation is accessible

### Performance Testing
- [ ] Images load appropriate sizes
- [ ] Critical CSS is inline
- [ ] Layout shift is minimal (CLS < 0.1)
```

---

## Best Practices

### Do
- Design mobile-first, enhance for larger screens
- Use relative units (rem, %, vw) over fixed pixels
- Test on real devices, not just browser resizing
- Consider thumb zones for mobile interactions
- Use CSS Grid and Flexbox for layouts

### Don't
- Hide important content on mobile
- Use fixed widths that break on small screens
- Rely on hover states for essential functionality
- Forget about landscape orientation
- Ignore device pixel ratios for images

---

## Testing Tools

- **Chrome DevTools:** Device toolbar for responsive testing
- **Firefox:** Responsive Design Mode
- **BrowserStack:** Real device testing
- **Responsively App:** View multiple sizes simultaneously
- **Polypane:** Design-focused multi-view browser

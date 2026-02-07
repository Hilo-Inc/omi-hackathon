---
name: design-tokens
description: Create design token specifications for design systems. Use when the user says "design tokens", "design system", "style variables", "CSS variables", "theme tokens", or wants to document design primitives.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
---

# Design Tokens Skill

Create comprehensive design token specifications following the W3C Design Tokens standard for scalable, cross-platform design systems.

## Invocation

This skill activates when:
- User wants to create or document design tokens
- User mentions "design system", "style variables", "CSS variables"
- User wants to standardize colors, typography, spacing
- User needs theme support (light/dark mode)

Arguments: `$ARGUMENTS` (brand colors, existing styles, or specific token categories needed)

---

## What Are Design Tokens?

Design tokens are the atomic values of a design system—the single source of truth for colors, typography, spacing, and other visual properties.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Design Token Architecture                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   PRIMITIVE TOKENS          SEMANTIC TOKENS         COMPONENT TOKENS        │
│   (Raw Values)              (Purpose/Intent)        (Specific Usage)        │
│                                                                             │
│   ┌─────────────┐           ┌─────────────┐         ┌─────────────┐        │
│   │ blue-500    │ ───────►  │ color-      │ ──────► │ button-     │        │
│   │ #3b82f6     │           │ action-     │         │ primary-    │        │
│   └─────────────┘           │ primary     │         │ background  │        │
│                             └─────────────┘         └─────────────┘        │
│                                                                             │
│   ┌─────────────┐           ┌─────────────┐         ┌─────────────┐        │
│   │ gray-900    │ ───────►  │ color-      │ ──────► │ text-       │        │
│   │ #111827     │           │ text-       │         │ heading     │        │
│   └─────────────┘           │ primary     │         │             │        │
│                             └─────────────┘         └─────────────┘        │
│                                                                             │
│   Foundation ─────────────► Meaning ─────────────► Application             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Token Naming Convention

### Structure

```
[category]-[concept]-[property]-[variant]-[state]-[scale]
```

**Examples:**
- `color-background-primary`
- `color-text-primary-hover`
- `spacing-padding-md`
- `typography-heading-1-font-size`
- `border-radius-lg`

### Naming Rules

1. **Use kebab-case:** `color-primary` not `colorPrimary`
2. **Be semantic:** `color-error` not `color-red`
3. **Be consistent:** Pick a pattern and stick to it
4. **Avoid ambiguity:** `spacing-4` is clearer than `spacing-small`

---

## Token Categories

### 1. Color Tokens

#### Primitive Colors
```json
{
  "color": {
    "primitive": {
      "blue": {
        "50": { "$value": "#eff6ff" },
        "100": { "$value": "#dbeafe" },
        "200": { "$value": "#bfdbfe" },
        "300": { "$value": "#93c5fd" },
        "400": { "$value": "#60a5fa" },
        "500": { "$value": "#3b82f6" },
        "600": { "$value": "#2563eb" },
        "700": { "$value": "#1d4ed8" },
        "800": { "$value": "#1e40af" },
        "900": { "$value": "#1e3a8a" },
        "950": { "$value": "#172554" }
      },
      "gray": {
        "50": { "$value": "#f9fafb" },
        "100": { "$value": "#f3f4f6" },
        "200": { "$value": "#e5e7eb" },
        "300": { "$value": "#d1d5db" },
        "400": { "$value": "#9ca3af" },
        "500": { "$value": "#6b7280" },
        "600": { "$value": "#4b5563" },
        "700": { "$value": "#374151" },
        "800": { "$value": "#1f2937" },
        "900": { "$value": "#111827" },
        "950": { "$value": "#030712" }
      }
    }
  }
}
```

#### Semantic Colors
```json
{
  "color": {
    "background": {
      "primary": { "$value": "{color.primitive.white}" },
      "secondary": { "$value": "{color.primitive.gray.50}" },
      "tertiary": { "$value": "{color.primitive.gray.100}" },
      "inverse": { "$value": "{color.primitive.gray.900}" }
    },
    "text": {
      "primary": { "$value": "{color.primitive.gray.900}" },
      "secondary": { "$value": "{color.primitive.gray.600}" },
      "tertiary": { "$value": "{color.primitive.gray.400}" },
      "inverse": { "$value": "{color.primitive.white}" },
      "link": { "$value": "{color.primitive.blue.600}" }
    },
    "border": {
      "default": { "$value": "{color.primitive.gray.200}" },
      "strong": { "$value": "{color.primitive.gray.300}" },
      "focus": { "$value": "{color.primitive.blue.500}" }
    },
    "action": {
      "primary": { "$value": "{color.primitive.blue.600}" },
      "primary-hover": { "$value": "{color.primitive.blue.700}" },
      "primary-active": { "$value": "{color.primitive.blue.800}" }
    },
    "feedback": {
      "success": { "$value": "#16a34a" },
      "warning": { "$value": "#ca8a04" },
      "error": { "$value": "#dc2626" },
      "info": { "$value": "#2563eb" }
    }
  }
}
```

---

### 2. Typography Tokens

```json
{
  "typography": {
    "font-family": {
      "sans": { "$value": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" },
      "serif": { "$value": "'Merriweather', Georgia, serif" },
      "mono": { "$value": "'JetBrains Mono', 'Fira Code', monospace" }
    },
    "font-size": {
      "xs": { "$value": "0.75rem" },
      "sm": { "$value": "0.875rem" },
      "base": { "$value": "1rem" },
      "lg": { "$value": "1.125rem" },
      "xl": { "$value": "1.25rem" },
      "2xl": { "$value": "1.5rem" },
      "3xl": { "$value": "1.875rem" },
      "4xl": { "$value": "2.25rem" },
      "5xl": { "$value": "3rem" }
    },
    "font-weight": {
      "normal": { "$value": "400" },
      "medium": { "$value": "500" },
      "semibold": { "$value": "600" },
      "bold": { "$value": "700" }
    },
    "line-height": {
      "none": { "$value": "1" },
      "tight": { "$value": "1.25" },
      "snug": { "$value": "1.375" },
      "normal": { "$value": "1.5" },
      "relaxed": { "$value": "1.625" },
      "loose": { "$value": "2" }
    },
    "letter-spacing": {
      "tighter": { "$value": "-0.05em" },
      "tight": { "$value": "-0.025em" },
      "normal": { "$value": "0" },
      "wide": { "$value": "0.025em" },
      "wider": { "$value": "0.05em" }
    }
  }
}
```

#### Composite Typography Tokens
```json
{
  "typography": {
    "heading": {
      "1": {
        "$value": {
          "fontFamily": "{typography.font-family.sans}",
          "fontSize": "{typography.font-size.4xl}",
          "fontWeight": "{typography.font-weight.bold}",
          "lineHeight": "{typography.line-height.tight}",
          "letterSpacing": "{typography.letter-spacing.tight}"
        }
      },
      "2": {
        "$value": {
          "fontFamily": "{typography.font-family.sans}",
          "fontSize": "{typography.font-size.3xl}",
          "fontWeight": "{typography.font-weight.semibold}",
          "lineHeight": "{typography.line-height.tight}"
        }
      },
      "3": {
        "$value": {
          "fontFamily": "{typography.font-family.sans}",
          "fontSize": "{typography.font-size.2xl}",
          "fontWeight": "{typography.font-weight.semibold}",
          "lineHeight": "{typography.line-height.snug}"
        }
      }
    },
    "body": {
      "default": {
        "$value": {
          "fontFamily": "{typography.font-family.sans}",
          "fontSize": "{typography.font-size.base}",
          "fontWeight": "{typography.font-weight.normal}",
          "lineHeight": "{typography.line-height.normal}"
        }
      },
      "small": {
        "$value": {
          "fontFamily": "{typography.font-family.sans}",
          "fontSize": "{typography.font-size.sm}",
          "fontWeight": "{typography.font-weight.normal}",
          "lineHeight": "{typography.line-height.normal}"
        }
      }
    }
  }
}
```

---

### 3. Spacing Tokens

```json
{
  "spacing": {
    "0": { "$value": "0" },
    "px": { "$value": "1px" },
    "0.5": { "$value": "0.125rem" },
    "1": { "$value": "0.25rem" },
    "1.5": { "$value": "0.375rem" },
    "2": { "$value": "0.5rem" },
    "2.5": { "$value": "0.625rem" },
    "3": { "$value": "0.75rem" },
    "3.5": { "$value": "0.875rem" },
    "4": { "$value": "1rem" },
    "5": { "$value": "1.25rem" },
    "6": { "$value": "1.5rem" },
    "7": { "$value": "1.75rem" },
    "8": { "$value": "2rem" },
    "9": { "$value": "2.25rem" },
    "10": { "$value": "2.5rem" },
    "11": { "$value": "2.75rem" },
    "12": { "$value": "3rem" },
    "14": { "$value": "3.5rem" },
    "16": { "$value": "4rem" },
    "20": { "$value": "5rem" },
    "24": { "$value": "6rem" },
    "28": { "$value": "7rem" },
    "32": { "$value": "8rem" }
  }
}
```

#### Semantic Spacing
```json
{
  "spacing": {
    "component": {
      "padding-xs": { "$value": "{spacing.1}" },
      "padding-sm": { "$value": "{spacing.2}" },
      "padding-md": { "$value": "{spacing.3}" },
      "padding-lg": { "$value": "{spacing.4}" },
      "padding-xl": { "$value": "{spacing.6}" },
      "gap-xs": { "$value": "{spacing.1}" },
      "gap-sm": { "$value": "{spacing.2}" },
      "gap-md": { "$value": "{spacing.4}" },
      "gap-lg": { "$value": "{spacing.6}" },
      "gap-xl": { "$value": "{spacing.8}" }
    },
    "layout": {
      "page-margin": { "$value": "{spacing.4}" },
      "page-margin-md": { "$value": "{spacing.6}" },
      "page-margin-lg": { "$value": "{spacing.8}" },
      "section-gap": { "$value": "{spacing.16}" },
      "content-max-width": { "$value": "72rem" }
    }
  }
}
```

---

### 4. Border Tokens

```json
{
  "border": {
    "width": {
      "none": { "$value": "0" },
      "thin": { "$value": "1px" },
      "default": { "$value": "1px" },
      "medium": { "$value": "2px" },
      "thick": { "$value": "4px" }
    },
    "radius": {
      "none": { "$value": "0" },
      "sm": { "$value": "0.125rem" },
      "default": { "$value": "0.25rem" },
      "md": { "$value": "0.375rem" },
      "lg": { "$value": "0.5rem" },
      "xl": { "$value": "0.75rem" },
      "2xl": { "$value": "1rem" },
      "3xl": { "$value": "1.5rem" },
      "full": { "$value": "9999px" }
    },
    "style": {
      "solid": { "$value": "solid" },
      "dashed": { "$value": "dashed" },
      "dotted": { "$value": "dotted" }
    }
  }
}
```

---

### 5. Shadow Tokens

```json
{
  "shadow": {
    "none": { "$value": "none" },
    "xs": { "$value": "0 1px 2px 0 rgb(0 0 0 / 0.05)" },
    "sm": { "$value": "0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)" },
    "md": { "$value": "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)" },
    "lg": { "$value": "0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)" },
    "xl": { "$value": "0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)" },
    "2xl": { "$value": "0 25px 50px -12px rgb(0 0 0 / 0.25)" },
    "inner": { "$value": "inset 0 2px 4px 0 rgb(0 0 0 / 0.05)" }
  }
}
```

---

### 6. Motion/Animation Tokens

```json
{
  "motion": {
    "duration": {
      "instant": { "$value": "0ms" },
      "fast": { "$value": "100ms" },
      "normal": { "$value": "200ms" },
      "slow": { "$value": "300ms" },
      "slower": { "$value": "500ms" }
    },
    "easing": {
      "linear": { "$value": "linear" },
      "ease-in": { "$value": "cubic-bezier(0.4, 0, 1, 1)" },
      "ease-out": { "$value": "cubic-bezier(0, 0, 0.2, 1)" },
      "ease-in-out": { "$value": "cubic-bezier(0.4, 0, 0.2, 1)" },
      "bounce": { "$value": "cubic-bezier(0.68, -0.55, 0.265, 1.55)" }
    }
  }
}
```

---

### 7. Z-Index Tokens

```json
{
  "z-index": {
    "hide": { "$value": "-1" },
    "base": { "$value": "0" },
    "dropdown": { "$value": "100" },
    "sticky": { "$value": "200" },
    "fixed": { "$value": "300" },
    "modal-backdrop": { "$value": "400" },
    "modal": { "$value": "500" },
    "popover": { "$value": "600" },
    "tooltip": { "$value": "700" },
    "toast": { "$value": "800" }
  }
}
```

---

## Theme Support (Dark Mode)

```json
{
  "color": {
    "$themes": {
      "light": {
        "background": {
          "primary": { "$value": "#ffffff" },
          "secondary": { "$value": "#f9fafb" }
        },
        "text": {
          "primary": { "$value": "#111827" },
          "secondary": { "$value": "#4b5563" }
        }
      },
      "dark": {
        "background": {
          "primary": { "$value": "#111827" },
          "secondary": { "$value": "#1f2937" }
        },
        "text": {
          "primary": { "$value": "#f9fafb" },
          "secondary": { "$value": "#9ca3af" }
        }
      }
    }
  }
}
```

---

## Output Formats

### CSS Custom Properties

```css
:root {
  /* Colors - Primitive */
  --color-primitive-blue-500: #3b82f6;
  --color-primitive-blue-600: #2563eb;
  --color-primitive-gray-900: #111827;

  /* Colors - Semantic */
  --color-background-primary: var(--color-primitive-white);
  --color-text-primary: var(--color-primitive-gray-900);
  --color-action-primary: var(--color-primitive-blue-600);

  /* Typography */
  --font-family-sans: 'Inter', -apple-system, sans-serif;
  --font-size-base: 1rem;
  --font-weight-bold: 700;

  /* Spacing */
  --spacing-4: 1rem;
  --spacing-8: 2rem;

  /* Border */
  --border-radius-md: 0.375rem;

  /* Shadow */
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
}

[data-theme="dark"] {
  --color-background-primary: var(--color-primitive-gray-900);
  --color-text-primary: var(--color-primitive-gray-50);
}
```

### JavaScript/TypeScript

```typescript
export const tokens = {
  color: {
    primitive: {
      blue: {
        500: '#3b82f6',
        600: '#2563eb',
      },
    },
    background: {
      primary: 'var(--color-background-primary)',
    },
    text: {
      primary: 'var(--color-text-primary)',
    },
  },
  spacing: {
    4: '1rem',
    8: '2rem',
  },
  borderRadius: {
    md: '0.375rem',
  },
} as const;

export type ColorToken = keyof typeof tokens.color;
export type SpacingToken = keyof typeof tokens.spacing;
```

### SCSS Variables

```scss
// Colors - Primitive
$color-primitive-blue-500: #3b82f6;
$color-primitive-blue-600: #2563eb;

// Colors - Semantic
$color-background-primary: $color-primitive-white;
$color-text-primary: $color-primitive-gray-900;

// Typography
$font-family-sans: 'Inter', -apple-system, sans-serif;
$font-size-base: 1rem;

// Spacing
$spacing-4: 1rem;
$spacing-8: 2rem;

// Maps for programmatic access
$colors: (
  'background-primary': $color-background-primary,
  'text-primary': $color-text-primary,
);

$spacing: (
  '4': $spacing-4,
  '8': $spacing-8,
);
```

---

## Output Template

```markdown
# Design Tokens Specification

**Project:** [Project Name]
**Version:** 1.0.0
**Last Updated:** [Date]

## Token Architecture

This design system uses a three-tier token architecture:

1. **Primitive Tokens** - Raw values (colors, sizes)
2. **Semantic Tokens** - Purpose-based aliases
3. **Component Tokens** - Component-specific values

## Color Tokens

### Primitive Colors
[Color scales with hex values]

### Semantic Colors
[Background, text, border, action, feedback colors]

### Theme Support
[Light/dark mode token mappings]

## Typography Tokens

### Font Families
[Primary, secondary, monospace]

### Type Scale
[Font sizes with rem values]

### Font Weights
[Available weights]

### Composite Styles
[Heading and body text styles]

## Spacing Tokens

### Base Scale
[Spacing values]

### Semantic Spacing
[Component padding, layout margins]

## Border Tokens

### Border Widths
[Available widths]

### Border Radii
[Radius scale]

## Shadow Tokens
[Elevation scale]

## Motion Tokens

### Durations
[Timing values]

### Easings
[Easing functions]

## Z-Index Tokens
[Layer scale]

## Implementation

### CSS Custom Properties
[Generated CSS]

### JavaScript/TypeScript
[Generated JS/TS exports]

### Usage Examples
[Code examples showing token usage]

---

## Governance

- **Adding Tokens:** Requires design system team approval
- **Modifying Tokens:** Document breaking changes
- **Deprecating Tokens:** 2-sprint warning period
```

---

## Best Practices

### Do
- Use semantic naming over literal values
- Reference tokens via aliases, not raw values
- Document the intent of each token
- Provide clear theme support
- Include all format outputs needed

### Don't
- Create one-off tokens for single uses
- Use color names like "red" in semantic tokens
- Hard-code values that should be tokens
- Create circular token references
- Forget accessibility (contrast ratios)

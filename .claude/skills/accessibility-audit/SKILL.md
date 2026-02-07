---
name: accessibility-audit
description: Perform WCAG 2.2 AA accessibility audits on web/mobile interfaces. Use when the user says "accessibility audit", "WCAG", "a11y review", "ADA compliance", "accessibility check", or wants to evaluate accessibility compliance.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
  - WebFetch
---

# Accessibility Audit Skill

Perform comprehensive WCAG 2.2 Level AA accessibility audits with actionable remediation guidance.

## Invocation

This skill activates when:
- User wants to audit accessibility compliance
- User mentions "WCAG", "accessibility", "a11y", "ADA compliance"
- User wants to check contrast ratios, keyboard navigation, screen reader support
- User asks about accessibility requirements or standards

Arguments: `$ARGUMENTS` (URL, file path, component name, or specific area to audit)

---

## The WCAG 2.2 Framework

WCAG is organized around four principles (POUR):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        WCAG 2.2 POUR Principles                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ PERCEIVABLE │  │  OPERABLE   │  │UNDERSTANDABLE│ │   ROBUST    │        │
│  ├─────────────┤  ├─────────────┤  ├─────────────┤  ├─────────────┤        │
│  │ • Text alt  │  │ • Keyboard  │  │ • Readable  │  │ • Parsing   │        │
│  │ • Captions  │  │ • Time      │  │ • Predictable│ │ • Name/Role │        │
│  │ • Adaptable │  │ • Seizures  │  │ • Input help│  │ • Value     │        │
│  │ • Contrast  │  │ • Navigation│  │             │  │             │        │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Audit Methodology

### The 30/70 Rule

- **30%** of issues can be found with automated tools
- **70%** require manual expert testing

Always combine automated scanning with manual review.

### Step 1: Scope Definition

Determine what to audit:
- Full website/application
- Specific user flows (checkout, registration, etc.)
- Individual components
- Recent changes only

### Step 2: Automated Testing

Run automated checks for:
- Missing alt text
- Color contrast violations
- Missing form labels
- Invalid ARIA attributes
- Heading hierarchy issues
- Link text problems

### Step 3: Manual Testing

Test manually for:
- Keyboard navigation (Tab, Enter, Escape, Arrow keys)
- Screen reader compatibility
- Focus management
- Dynamic content updates
- Error handling
- Cognitive load

### Step 4: Assistive Technology Testing

Test with:
- Screen readers (NVDA, VoiceOver, JAWS)
- Keyboard only
- Screen magnification
- Voice control

---

## WCAG 2.2 AA Checklist

### 1. Perceivable

#### 1.1 Text Alternatives
| Criterion | Description | How to Test |
|-----------|-------------|-------------|
| 1.1.1 Non-text Content | All images, icons, buttons have text alternatives | Check all `<img>` for alt, icons for aria-label |

**Check:**
```markdown
- [ ] All images have appropriate alt text
- [ ] Decorative images have alt="" or role="presentation"
- [ ] Complex images have long descriptions
- [ ] Icons have accessible names
- [ ] CAPTCHAs have alternatives
```

#### 1.2 Time-based Media
| Criterion | Description | How to Test |
|-----------|-------------|-------------|
| 1.2.1 Audio-only/Video-only | Provide alternatives | Check for transcripts |
| 1.2.2 Captions | Synchronized captions for video | Review caption accuracy |
| 1.2.3 Audio Description | Describe visual content | Check for audio track |
| 1.2.5 Audio Description (Prerecorded) | All prerecorded video | Verify descriptions |

**Check:**
```markdown
- [ ] Videos have accurate captions
- [ ] Audio content has transcripts
- [ ] Video has audio descriptions where needed
- [ ] Media players are keyboard accessible
```

#### 1.3 Adaptable
| Criterion | Description | How to Test |
|-----------|-------------|-------------|
| 1.3.1 Info and Relationships | Structure is programmatic | Check HTML semantics |
| 1.3.2 Meaningful Sequence | Reading order is logical | Linearize content |
| 1.3.3 Sensory Characteristics | Don't rely on shape/color alone | Review instructions |
| 1.3.4 Orientation | Support portrait and landscape | Rotate device |
| 1.3.5 Identify Input Purpose | Autocomplete on form fields | Check autocomplete attr |

**Check:**
```markdown
- [ ] Headings use proper hierarchy (h1 → h2 → h3)
- [ ] Lists use <ul>, <ol>, <dl> appropriately
- [ ] Tables have headers (<th>) and scope
- [ ] Forms have associated labels
- [ ] Regions use landmarks (main, nav, aside)
- [ ] Content works in both orientations
- [ ] Form fields have autocomplete attributes
```

#### 1.4 Distinguishable
| Criterion | Description | Requirement |
|-----------|-------------|-------------|
| 1.4.1 Use of Color | Color not sole indicator | Add text/icons |
| 1.4.2 Audio Control | Auto-playing audio can be stopped | Pause within 3 sec |
| 1.4.3 Contrast (Minimum) | Text contrast ratio | 4.5:1 normal, 3:1 large |
| 1.4.4 Resize Text | Text resizable to 200% | No loss of function |
| 1.4.5 Images of Text | Use real text | Except logos |
| 1.4.10 Reflow | Content reflows at 320px | No horizontal scroll |
| 1.4.11 Non-text Contrast | UI components & graphics | 3:1 ratio |
| 1.4.12 Text Spacing | User can adjust spacing | No loss of content |
| 1.4.13 Content on Hover/Focus | Dismissible, hoverable, persistent | Check tooltips |

**Check:**
```markdown
- [ ] Text contrast is at least 4.5:1 (3:1 for large text)
- [ ] UI components have 3:1 contrast against background
- [ ] Links are distinguishable from surrounding text
- [ ] Focus indicators are visible (3:1 contrast)
- [ ] Content works at 200% zoom
- [ ] Content reflows at 320px width without horizontal scrolling
- [ ] Text spacing can be adjusted without breaking layout
- [ ] Hover/focus content is dismissible and persistent
```

---

### 2. Operable

#### 2.1 Keyboard Accessible
| Criterion | Description | How to Test |
|-----------|-------------|-------------|
| 2.1.1 Keyboard | All functionality via keyboard | Tab through entire page |
| 2.1.2 No Keyboard Trap | Focus can always be moved | Check modals, widgets |
| 2.1.4 Character Key Shortcuts | Can be remapped or disabled | Check for single-key shortcuts |

**Check:**
```markdown
- [ ] All interactive elements are keyboard focusable
- [ ] Tab order is logical and intuitive
- [ ] No keyboard traps (can always Tab away)
- [ ] Focus is visible at all times
- [ ] Custom widgets have appropriate key bindings
- [ ] Skip links provided for main content
- [ ] Single-character shortcuts can be disabled
```

#### 2.2 Enough Time
| Criterion | Description | Requirement |
|-----------|-------------|-------------|
| 2.2.1 Timing Adjustable | Users can extend time limits | 10x extension or disable |
| 2.2.2 Pause, Stop, Hide | Moving content controllable | User control required |

**Check:**
```markdown
- [ ] Session timeouts can be extended or disabled
- [ ] Auto-updating content can be paused
- [ ] Carousels have pause controls
- [ ] No time limits on essential functions
```

#### 2.3 Seizures and Physical Reactions
| Criterion | Description | Requirement |
|-----------|-------------|-------------|
| 2.3.1 Three Flashes | No content flashes > 3x/sec | Or below threshold |

**Check:**
```markdown
- [ ] No content flashes more than 3 times per second
- [ ] Animations respect prefers-reduced-motion
```

#### 2.4 Navigable
| Criterion | Description | How to Test |
|-----------|-------------|-------------|
| 2.4.1 Bypass Blocks | Skip repetitive content | Check skip links |
| 2.4.2 Page Titled | Descriptive page titles | Review <title> |
| 2.4.3 Focus Order | Logical focus sequence | Tab through page |
| 2.4.4 Link Purpose (In Context) | Links make sense | Review link text |
| 2.4.5 Multiple Ways | Multiple ways to find pages | Search, sitemap, nav |
| 2.4.6 Headings and Labels | Descriptive headings | Review hierarchy |
| 2.4.7 Focus Visible | Focus indicator visible | Tab through UI |
| 2.4.11 Focus Not Obscured (Minimum) | Focus not hidden | Check sticky elements |

**Check:**
```markdown
- [ ] Skip link provided to bypass navigation
- [ ] Page titles are descriptive and unique
- [ ] Focus order matches visual order
- [ ] Link text is descriptive (no "click here")
- [ ] Multiple navigation methods available
- [ ] Headings describe content structure
- [ ] Focus indicator always visible
- [ ] Focus not obscured by sticky headers/footers
```

#### 2.5 Input Modalities
| Criterion | Description | Requirement |
|-----------|-------------|-------------|
| 2.5.1 Pointer Gestures | Alternatives for complex gestures | Single pointer available |
| 2.5.2 Pointer Cancellation | Down-event not sole trigger | Up-event or abort |
| 2.5.3 Label in Name | Visible label in accessible name | For voice control |
| 2.5.4 Motion Actuation | Alternatives for motion input | For shake, tilt, etc. |
| 2.5.7 Dragging Movements | Alternative to drag | (WCAG 2.2 new) |
| 2.5.8 Target Size (Minimum) | 24x24px minimum | (WCAG 2.2 new) |

**Check:**
```markdown
- [ ] Multi-finger gestures have single-pointer alternatives
- [ ] Actions can be cancelled (up-event or undo)
- [ ] Visible labels included in accessible names
- [ ] Motion-triggered actions have alternatives
- [ ] Drag actions have single-pointer alternatives
- [ ] Touch targets are at least 24x24px
```

---

### 3. Understandable

#### 3.1 Readable
| Criterion | Description | How to Test |
|-----------|-------------|-------------|
| 3.1.1 Language of Page | Page language declared | Check <html lang> |
| 3.1.2 Language of Parts | Language changes marked | Check lang attributes |

**Check:**
```markdown
- [ ] HTML lang attribute set correctly
- [ ] Language changes marked with lang attribute
```

#### 3.2 Predictable
| Criterion | Description | Requirement |
|-----------|-------------|-------------|
| 3.2.1 On Focus | No unexpected changes on focus | Check all focusable elements |
| 3.2.2 On Input | No unexpected changes on input | Check form fields |
| 3.2.3 Consistent Navigation | Navigation consistent across pages | Compare pages |
| 3.2.4 Consistent Identification | Same function = same label | Compare similar elements |

**Check:**
```markdown
- [ ] Focus doesn't trigger unexpected changes
- [ ] Form input doesn't auto-submit unexpectedly
- [ ] Navigation is consistent across pages
- [ ] Icons and buttons are consistently labeled
```

#### 3.3 Input Assistance
| Criterion | Description | Requirement |
|-----------|-------------|-------------|
| 3.3.1 Error Identification | Errors clearly identified | Text description required |
| 3.3.2 Labels or Instructions | Form fields have instructions | Labels or hints |
| 3.3.3 Error Suggestion | Suggest corrections | When known and safe |
| 3.3.4 Error Prevention | Confirm important actions | Review, confirm, reversible |
| 3.3.7 Redundant Entry | Don't require re-entry | (WCAG 2.2 new) |
| 3.3.8 Accessible Authentication | No cognitive tests for login | (WCAG 2.2 new) |

**Check:**
```markdown
- [ ] Error messages identify the field and error
- [ ] Error messages suggest how to fix
- [ ] Form fields have visible labels
- [ ] Required fields are indicated
- [ ] Important actions can be confirmed or undone
- [ ] Previously entered data is auto-populated
- [ ] Login doesn't require cognitive tests (CAPTCHA alternatives)
```

---

### 4. Robust

#### 4.1 Compatible
| Criterion | Description | How to Test |
|-----------|-------------|-------------|
| 4.1.2 Name, Role, Value | All UI components have accessible names | Check ARIA, forms |
| 4.1.3 Status Messages | Status updates announced | Check aria-live regions |

**Check:**
```markdown
- [ ] HTML validates without errors
- [ ] Custom controls have appropriate ARIA roles
- [ ] All form controls have accessible names
- [ ] Status messages use aria-live regions
- [ ] Dynamic content changes are announced
```

---

## Severity Rating Scale

Rate each issue by impact:

| Level | Severity | Description | Priority |
|-------|----------|-------------|----------|
| 1 | **Critical** | Blocks access completely | Fix immediately |
| 2 | **Serious** | Significantly difficult to use | Fix in current sprint |
| 3 | **Moderate** | Causes frustration | Fix in next release |
| 4 | **Minor** | Small inconvenience | Fix when possible |

---

## Output Template

```markdown
# Accessibility Audit Report

**Audit Date:** [Date]
**Auditor:** Claude AI
**Standard:** WCAG 2.2 Level AA
**Scope:** [Pages/components audited]

## Executive Summary

- **Total Issues Found:** [X]
- **Critical:** [X] | **Serious:** [X] | **Moderate:** [X] | **Minor:** [X]
- **Estimated Conformance:** [Partial/Substantial/Full]

## Issues by Principle

### Perceivable Issues

#### [Issue Title]
- **Criterion:** [e.g., 1.4.3 Contrast]
- **Severity:** [Critical/Serious/Moderate/Minor]
- **Location:** [Page/component/element]
- **Description:** [What's wrong]
- **Impact:** [Who is affected and how]
- **Remediation:** [How to fix]
- **Code Example:**
  ```html
  <!-- Before -->
  <img src="logo.png">

  <!-- After -->
  <img src="logo.png" alt="Company Name logo">
  ```

### Operable Issues
[Same format...]

### Understandable Issues
[Same format...]

### Robust Issues
[Same format...]

## Recommendations

### Immediate Actions (Critical/Serious)
1. [Action item with specific fix]
2. [Action item with specific fix]

### Short-term Improvements (Moderate)
1. [Action item]
2. [Action item]

### Long-term Enhancements (Minor)
1. [Action item]
2. [Action item]

## Testing Tools Used

- [ ] Automated: [axe, WAVE, Lighthouse]
- [ ] Manual keyboard testing
- [ ] Screen reader: [NVDA/VoiceOver/JAWS]
- [ ] Color contrast checker
- [ ] HTML validator

## Compliance Statement

Based on this audit, the [product/site] is [fully conformant / partially conformant / not conformant] with WCAG 2.2 Level AA. [X] of [Y] success criteria are met.

---

*This audit provides a snapshot at the time of evaluation. Accessibility should be continuously monitored.*
```

---

## Common Issues & Quick Fixes

### Images Missing Alt Text
```html
<!-- Bad -->
<img src="chart.png">

<!-- Good: Informative -->
<img src="chart.png" alt="Sales increased 25% from Q1 to Q2 2024">

<!-- Good: Decorative -->
<img src="decorative-line.png" alt="" role="presentation">
```

### Insufficient Color Contrast
```css
/* Bad: 2.5:1 ratio */
.text { color: #767676; background: #ffffff; }

/* Good: 4.5:1 ratio */
.text { color: #595959; background: #ffffff; }
```

### Missing Form Labels
```html
<!-- Bad -->
<input type="email" placeholder="Email">

<!-- Good -->
<label for="email">Email address</label>
<input type="email" id="email" autocomplete="email">
```

### Keyboard Trap
```javascript
// Bad: Traps focus in modal
modal.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') e.preventDefault();
});

// Good: Cycles focus within modal
const focusableEls = modal.querySelectorAll('button, input, a');
const firstEl = focusableEls[0];
const lastEl = focusableEls[focusableEls.length - 1];

modal.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    if (e.shiftKey && document.activeElement === firstEl) {
      e.preventDefault();
      lastEl.focus();
    } else if (!e.shiftKey && document.activeElement === lastEl) {
      e.preventDefault();
      firstEl.focus();
    }
  }
  if (e.key === 'Escape') closeModal();
});
```

### Missing Focus Indicator
```css
/* Bad: Removes focus outline */
:focus { outline: none; }

/* Good: Custom visible focus */
:focus {
  outline: 2px solid #005fcc;
  outline-offset: 2px;
}

:focus:not(:focus-visible) {
  outline: none;
}

:focus-visible {
  outline: 2px solid #005fcc;
  outline-offset: 2px;
}
```

---

## Resources

- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WAVE Evaluation Tool](https://wave.webaim.org/)

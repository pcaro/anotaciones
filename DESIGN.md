---
name: Anotaciones
description: A personal technical notebook publicly shared — Pablo Caro's blog of Python, Linux, and AI notes.
colors:
  lab-orange: "#D9411E"
  signal-orange: "#FF5A09"
  notebook-page: "#faf7f2"
  bench-charcoal: "#333333"
  archive-ink: "#242121"
  notebook-graphite: "#999999"
  bench-dust: "#e8e4df"
  inline-ruby: "#b8332e"
  code-surface: "#f5f3f0"
  code-border: "#e0dcd6"
typography:
  display:
    fontFamily: "'Source Sans Pro', 'Roboto', 'Open Sans', sans-serif"
    fontSize: "2.4em"
    fontWeight: 300
    lineHeight: 1.1
  headline:
    fontFamily: "'Source Sans Pro', 'Roboto', 'Open Sans', sans-serif"
    fontSize: "1.6em"
    fontWeight: 300
    lineHeight: 1.1
  body:
    fontFamily: "'Source Sans Pro', 'Roboto', 'Open Sans', sans-serif"
    fontSize: "1.02em"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "'Source Sans Pro', 'Roboto', 'Open Sans', sans-serif"
    fontSize: "12px"
    fontWeight: 600
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  mono:
    fontFamily: "'Source Code Pro', 'Consolas', 'Liberation Mono', monospace"
    fontSize: "0.9em"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  sm: "3px"
  md: "4px"
  lg: "8px"
  full: "9999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "14px"
  lg: "20px"
  xl: "36px"
  section: "40px"
components:
  button-primary:
    backgroundColor: "{colors.lab-orange}"
    textColor: "#ffffff"
    rounded: "{rounded.sm}"
    padding: "0.6em 1em"
  button-primary-hover:
    backgroundColor: "{colors.signal-orange}"
  tag:
    backgroundColor: "{colors.lab-orange}"
    textColor: "#ffffff"
    rounded: "{rounded.sm}"
    padding: "0.2em 0.6em"
  tag-hover:
    backgroundColor: "{colors.signal-orange}"
  card-category:
    backgroundColor: "rgba(0,0,0,0.03)"
    rounded: "{rounded.lg}"
    padding: "1rem"
  admonition:
    rounded: "{rounded.md}"
    padding: "0.5em 1.25em 1.25em"
  sidebar:
    backgroundColor: "{colors.bench-charcoal}"
    textColor: "#ffffff"
  nav-link:
    typography: "{typography.label}"
---

# Design System: Anotaciones

## 1. Overview

**Creative North Star: "The Lab Notebook"**

A scientist's bench journal, kept in pen with orange underlining — functional, personal, slightly informal. The design serves the note-taker first: Pablo writes for his future self, and that intention shapes every visual choice. Nothing here is dressed up for an audience; everything is organized enough to find, loose enough to feel lived-in.

The system is restrained by nature, not by anxiety. A single burnt-orange accent does all the work: links, buttons, tags, the pulse of the page. Neutrals are warm — the notebook page is off-white, not sterile; the sidebar is deep charcoal, not pure black. Typography is a single humanist sans at light weights for headings, regular for body, with a technical mono for code. The layout is a classic two-column: a fixed dark sidebar anchors the left, and the content scrolls calmly in the right, capped at a comfortable reading measure.

This system rejects terminal-nostalgia, hacker-culture visual tropes, and any form of decoration that competes with the words. If it looks like a themed developer blog from 2018, it has failed. If it feels like opening a well-worn Moleskine, it has succeeded.

**Key Characteristics:**
- Content-first, code-capable: body text and code blocks share equal visual care
- Warm restraint: off-white pages, a single burnt-orange accent, no second accent
- Lived-in, not sterile: rounded corners are gentle (3-4px), shadows are rare and light
- Two-column permanence: the dark sidebar never hides; it's the spine of the notebook
- Bilingual by default: language switching lives in the header, consistently available

## 2. Colors

A restrained palette anchored by one burnt orange accent and warm paper neutrals. The orange is rare and intentional — it marks what matters.

### Primary
- **Lab Orange** (`#D9411E`): Links, buttons, tag backgrounds, and any interactive element that needs to announce "I am clickable." Used on no more than 5-8% of any given screen. On hover, lightens to Signal Orange.
- **Signal Orange** (`#FF5A09`): Hover state for all Lab Orange elements. Never used at rest.

### Neutral
- **Notebook Page** (`#faf7f2`): The main content background. Warm off-white with a faint cream tint — never pure `#fff`. Applied to the body in light mode.
- **Bench Charcoal** (`#333333`): The fixed sidebar background. Deep warm grey — never pure `#000`. Also used as the body background in dark mode.
- **Archive Ink** (`#242121`): Body text in light mode. Near-black with a warm undertone. Also used for generic admonition text.
- **Notebook Graphite** (`#999999`): Secondary text — article metadata, footer text, figure captions. Quiet but readable.
- **Bench Dust** (`#e8e4df`): Borders, horizontal rules, and the subtle tint behind blockquotes. Warmer and more deliberate than generic `#eee`.
- **Inline Ruby** (`#b8332e`): Color for inline `<code>` within body text. A muted, less saturated red that reads as a subtle highlight rather than an error.
- **Code Surface** (`#f5f3f0`): Background for inline code snippets and pre blocks. Slightly darker than the page, barely perceptible.
- **Code Border** (`#e0dcd6`): The 1px stroke around inline code elements. Subtle enough to exist, firm enough to define.

### Named Rules
**The One Accent Rule.** Lab Orange is the only accent color in the system. No secondary accent, no tertiary. Its power comes from its rarity: if Lab Orange appears, it matters.

**The Paper Rule.** No pure black (`#000`) and no pure white (`#fff`) anywhere. Every neutral carries a warm undertone toward the orange family.

## 3. Typography

**Body Font:** Source Sans Pro (with Roboto, Open Sans, Liberation Sans, and system sans-serif fallbacks)
**Mono Font:** Source Code Pro (with Consolas, Liberation Mono, and system monospace fallbacks)

**Character:** A single humanist sans across all weights — light for headings, regular for body. No display/secondary font pairing. The mono is technical but warm: Source Code Pro has a humanist skeleton that keeps code blocks from feeling cold. Together they say: "this is a person who writes code, not a machine that writes prose."

### Hierarchy
- **Display** (300, 2.4em, 1.1): Article titles. Only one per page. The light weight gives them air; the tight line-height keeps them anchored.
- **Headline** (300, 1.6em, 1.1): H3 — section headers within articles. Still light, still tight.
- **Body** (400, 1.02em, 1.6): All prose. Line-height of 1.6 opened from the current 1.2 — the current tight setting compresses technical reading. Max line length of 65ch.
- **Label** (600, 12px, 0.05em letter-spacing, uppercase): Navigation links, button text, metadata labels. Small, tracked out, all-caps. The only place 600 weight appears.
- **Mono** (400, 0.9em, 1.5): Code blocks and pre elements. Slightly smaller than body to fit longer lines without wrapping.

### Named Rules
**The Single-Voice Rule.** One font family carries all prose. No serif/sans contrast, no display/body pairing. The hierarchy is built on weight and scale alone — 300 for headings, 400 for body, 600 only for labels. This is a notebook, not a magazine.

## 4. Elevation

This is a flat system with occasional, purposeful lift. The notebook metaphor doesn't need depth — paper is flat. Shadows are used sparingly and always as light as possible.

### Shadow Vocabulary
- **Card Lift** (`box-shadow: 0 4px 12px rgba(0,0,0,0.12)`, paired with `transform: translateY(-2px)`): Applied to category cards on hover only. The lift is the interaction, not the default state.
- **Keyboard Key** (`box-shadow: 0 1px 0 rgba(63,63,63,0.25)`, paired with a 1px border): `<kbd>` elements get a subtle bottom shadow to suggest a physical key. The only element that's "lifted" at rest.

### Named Rules
**The Flat-By-Default Rule.** Surfaces are flat at rest. Shadows appear only as a response to interaction (hover, focus). If a card has a shadow without being hovered, ask why.

## 5. Components

### Buttons & Tags
- **Shape:** Gently curved (3px radius). Not pill-shaped, not sharp.
- **Primary:** Lab Orange background, white text, `0.6em` vertical padding. No border.
- **Hover/Focus:** Background shifts to Signal Orange. Smooth 150ms transition.
- **Tags:** Same orange fill, smaller (`0.2em` vertical, `0.74em` font-size). Used in article footers for category/tag links.

### Cards (Category Grid)
- **Appearance:** Subtle tinted background (`rgba(0,0,0,0.03)`), 8px radius — the largest radius in the system, reserved for containers.
- **Behavior:** Flat at rest. On hover, lift 2px with a light shadow. 150ms ease transition.
- **Layout:** Centered content, icon/image above label, count below. No internal borders, no nested cards.

### Admonitions
- **Shape:** 4px radius, internal padding `0.5em 1.25em 1.25em`.
- **Variants:** Five semantic types — attention/caution/warning (amber), danger/error (red), hint/tip (blue), important/note (green), generic (grey). Each has a distinct background tint and text color. Icon prefixed via Font Awesome pseudo-element.
- **Rule:** Never nest. Never stack more than two consecutively. They are signals, not decorations.

### Navigation
- **Desktop:** Fixed left sidebar (25vw) with Bench Charcoal background, white text. Nav links are lowercase, 1.28em, displayed as a vertical block list. Social icons are 36px circles at the bottom.
- **Top bar:** Horizontal nav in the main content area — uppercase 12px links separated by 1px right borders. Active language is bold (600 weight).
- **Mobile:** Sidebar becomes a stacked top section. Category grid adapts from 180px min columns to single column.

### Sidebar
- **Background:** Bench Charcoal (`#333333`). Fixed position, full viewport height.
- **Content:** Circular profile image (140px max, 50% radius), name in white, brief bio in 0.92em, vertical nav, social icon grid.
- **Typography:** White text on dark. Links are white, hover to light grey.

### Inline Code & Pre Blocks
- **Inline code:** 0.8em, Inline Ruby color (`#b8332e`), Code Surface background (`#f5f3f0`), 1px Code Border, 3px radius. Whitespace nowrap.
- **Pre blocks:** 0.9em, left accent border (8px wide, semi-transparent overlay), subtle background tint. Horizontal scroll on overflow. Top-right and bottom-right 5px radius.

### Blockquotes
- **Style:** Left 10px border accent, 5px right-side radius, subtle background tint. Weight 300, slightly larger than body (1.1em). No quotation marks — the border is the signal.

## 6. Do's and Don'ts

### Do:
- **Do** use Lab Orange (`#D9411E`) as the sole accent. Its power is its scarcity.
- **Do** tint every neutral toward warmth. Notebook Page (`#faf7f2`) not `#fff`. Archive Ink (`#242121`) not `#000`.
- **Do** keep body line length at 65ch max. Open body line-height to 1.6 for technical reading comfort.
- **Do** treat code blocks with the same typographic care as body text. Mono is content, not decoration.
- **Do** let the sidebar stay fixed and visible. It's the notebook's spine.
- **Do** keep shadows light and infrequent. Lift cards only on hover, and only by 2px.
- **Do** show language switching prominently in the article header. Bilingual is a feature, not an afterthought.

### Don't:
- **Don't** introduce a secondary accent color. One orange is enough. Let the warm neutrals do the rest.
- **Don't** use `border-left` greater than 1px as a colored accent stripe on cards or list items.
- **Don't** apply gradient text anywhere. Emphasis comes from weight and scale, not decorative effects.
- **Don't** let the design slip into friky/nerdy territory — no terminal emulator aesthetic, no monospace-as-body, no hacker-culture tropes. This is a human writing for humans who happen to code.
- **Don't** wrap everything in identical cards. The category grid is the only card pattern. Body content is free-flowing.
- **Don't** use glassmorphism or decorative blurs. The surface is paper, not glass.
- **Don't** add animations that aren't direct responses to user action. No scroll-driven choreography, no entrance animations.
- **Don't** use pure black or pure white anywhere. The Paper Rule is unconditional.

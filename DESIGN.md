---
name: Taysir.ai
description: A tactile Arabic RTL identity worksheet with paper surfaces and physical Neo-Brutalist controls.
colors:
  paper: "#f8f1df"
  ink: "#17151b"
  muted: "#54495b"
  field-bg: "#fffaf0"
  yellow: "#f6db75"
  pink: "#f4b8c8"
  mint: "#aee0c1"
  blue: "#b8d7ee"
  purple: "#c6b0f7"
  red: "#f2aaaa"
  yellow-text: "#8a6100"
  pink-text: "#7a1f43"
  mint-text: "#145c38"
  blue-text: "#21527a"
  purple-text: "#5b34a3"
  focus: "#7651bc"
  paper-dark: "#24212c"
  ink-dark: "#fff8e8"
  muted-dark: "#e2d5e8"
  field-bg-dark: "#35303f"
  yellow-text-dark: "#ffe37a"
  pink-text-dark: "#ffbdd1"
  mint-text-dark: "#b8f0cf"
  blue-text-dark: "#bfe0ff"
  purple-text-dark: "#d9c6ff"
typography:
  display:
    fontFamily: "Tajawal, sans-serif"
    fontSize: "clamp(2.25rem, 8vw, 5.3rem)"
    fontWeight: 900
    lineHeight: 1.12
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Tajawal, sans-serif"
    fontSize: "clamp(1.7rem, 4vw, 2.5rem)"
    fontWeight: 900
    lineHeight: 1.25
  title:
    fontFamily: "Tajawal, sans-serif"
    fontSize: "1.35rem"
    fontWeight: 900
    lineHeight: 1.5
  body:
    fontFamily: "Tajawal, sans-serif"
    fontSize: "1rem"
    fontWeight: 500
  label:
    fontFamily: "Tajawal, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 800
rounded:
  sharp: "0px"
  pill: "999px"
  circle: "50%"
spacing:
  page-inline: "1rem"
  group-gap: "0.75rem"
  card-padding: "1.5rem"
  section-gap: "2rem"
components:
  button-primary:
    backgroundColor: "{colors.purple}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sharp}"
    padding: "0.95rem 1.25rem"
  button-theme:
    backgroundColor: "{colors.mint}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sharp}"
    padding: "0.55rem 0.75rem"
  button-key:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sharp}"
    padding: "0.55rem 0.75rem"
  dialog-key:
    backgroundColor: "#fffaf0"
    textColor: "{colors.ink}"
    rounded: "{rounded.sharp}"
    padding: "1.5rem"
  input-key:
    backgroundColor: "#fffaf0"
    textColor: "{colors.ink}"
    rounded: "{rounded.sharp}"
    padding: "0.85rem"
  chip-suggestion:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0.45rem 0.85rem"
  input-project:
    backgroundColor: "{colors.field-bg}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sharp}"
    padding: "1.1rem"
  card-slogan:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sharp}"
    padding: "1.5rem"
  card-palette:
    backgroundColor: "{colors.pink}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sharp}"
    padding: "1.5rem"
  card-logo:
    backgroundColor: "{colors.mint}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sharp}"
    padding: "1.5rem"
  card-ideas:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sharp}"
    padding: "1.5rem"
---

# Design System: Taysir.ai

## Overview

**Creative North Star: "The Arabic Identity Worksheet"**

The interface feels like a generous sheet of colored working paper: direct Arabic typography, visible black construction lines, and controls that behave like physical stamps. It is playful without becoming decorative, and keeps the generation task ahead of visual ornament.

**Key Characteristics:**
- Native Arabic RTL composition with Tajawal typography.
- Cream paper ground and distinct pastel working surfaces.
- Sharp black borders and solid offset shadows with no blur.
- Buttons physically move down and right when pressed.
- Result cards stay light and readable in dark mode.

## Colors

The palette separates the shell from the work product: the shell changes between light and dark, while identity cards retain their light pastel paper colors.

### Primary
- **Soft Provincial Purple**: the single generation action, used to make the primary step unmistakable.

### Secondary
- **Honey Paper Yellow**: logo accent, loading state, loading surface, and verbal-slogan card.
- **Powder Pink**: palette card, its associated visual grouping, and the Pinterest reference action in the logo card.
- **Fresh Mint**: theme control, logo-concept card, and one suggestion variation.
- **Powder Blue**: ideas/suggestions card and the compact Coolors action in the palette card.

### Neutral
- **Warm Paper**: global light-mode ground.
- **Near-Black Ink**: borders, shadows, and primary text on pastel surfaces.
- **Cream Field**: input and inset writing surfaces.
- **Ink Night**: dark-mode shell ground; it does not recolor result cards.
- **Muted Plum**: secondary shell text.
- **Soft Signal Red**: empty-input and generation error containers.

### Named Rules
**The Light Cards Rule.** Keep all four identity cards on their yellow, pink, mint, and blue surfaces in both themes; only the shell and writing field darken.

**The One Action Rule.** Reserve purple for the main generation button so the page has one obvious primary action.

## Typography

**Display Font:** Tajawal with a sans-serif fallback.
**Body Font:** Tajawal with a sans-serif fallback.
**Label/Mono Font:** Tajawal for controls; browser monospace for LTR HEX codes.

**Character:** Heavy, spacious Arabic display lettering carries the identity; medium-weight body copy keeps instructions and generated text readable.

### Hierarchy
- **Display** (900, `clamp(2.25rem, 8vw, 5.3rem)`, 1.12): hero promise only.
- **Headline** (900, `clamp(1.7rem, 4vw, 2.5rem)`, 1.25): result-section title.
- **Title** (900, `1.35rem`): card headings.
- **Body** (500, `1rem`): controls, explanations, and generated descriptions.
- **Label** (800, `0.9rem`): theme and compact action labels.
- **Idea title** (900, `1.05rem`): each titled item in the ideas card.
- **Idea body** (700, `0.95rem`): each suggestion under an idea title.
- **Compact** (800, `0.85rem`): Coolors link, copy feedback, and API error detail.

### Named Rules
**The ID Selector Rule.** Hero, result-heading, and card-heading typography uses component-specific selectors so runtime-injected Tailwind preflight cannot reset their size or weight.

## Layout

The page is mobile-first and RTL. Wide content is capped at `72rem`; the hero is capped at `64rem` and the generator at `48rem`. Mobile page gutters are `1rem`, increasing to `1.5rem` at the small breakpoint. Suggestions wrap rather than compress. Results move from one column to a balanced two-by-two grid at `768px` and stay two columns on wide screens. Print output uses one column with protected card breaks.

## Elevation & Depth

Depth is structural, not atmospheric. Every raised surface has a sharp solid black offset and no blur. Interaction reduces the offset while translating the control toward its shadow.

### Shadow Vocabulary
- **Control lift** (`6px 6px 0 #17151b`): primary and theme buttons.
- **Worksheet lift** (`7px 7px 0 #17151b`): subtitle and project input.
- **Card lift** (`8px 8px 0 #17151b`): result cards.
- **Chip lift** (`4px 4px 0 #17151b`): suggestions and inset logo field.
- **Pressed lift** (`3px 3px 0 #17151b` or smaller): hover/active physical feedback.

### Named Rules
**The Hard Depth Rule.** Never add blur to component shadows; use opaque black offsets only.

**The Physical Press Rule.** Hover-capable controls translate by `3px` on both axes while their shadow contracts; active state moves slightly farther.

**The Stateful Motion Rule.** The loading sweep loops only while a Gemini request is in flight and disappears with the loading state; it communicates an indeterminate pending state rather than decorating static content. Reduced-motion users get an instant, static bar.

**The Press Response Rule.** The generate button answers a press with one fluid 500ms ink recoil and five hard-edged pastel chips. The recoil uses a sine ease over a decaying oscillation; the chips travel outward continuously for 620ms with a confident deceleration and fade, are `aria-hidden`, sit behind the label, remove themselves on animation end, and never blur or alter layout.

**The Promise Wave Rule.** The hero title's words share one slow 3.6s sine-like cycle with staggered negative delays. The sine is sampled at 17 linear keyframes so velocity never stalls at zero crossings; Arabic words stay whole so shaping and the exact copy never break. Reduced-motion users see the static heading.

**The Pointer Response Rule.** Inside each word, an inner `.word-shift` span answers pointer movement over the heading with a small weighted parallax driven by `requestAnimationFrame` lerping. Nearby words move more than distant ones, motion eases back to rest on leave, and the wave stays on the outer span so the two transforms compose. Pointer motion is skipped when the device has no hover or the user prefers reduced motion.

**The Touch Color Rule.** The nearest hero word takes a text-safe pastel color on hover or touch while the other four stay ink. Deeper light-mode inks and brighter dark-mode inks keep the large Arabic words legible against their paper grounds; the color eases over `160ms`, touch feedback persists briefly after release, and pointer leave clears it. The global reduced-motion override makes the color state immediate without removing it.

**The Gemini Shortcut Rule.** The API-key dialog's action row leads with a compact 42px square tile: a paper surface inside the same sharp ink frame and hard shadow, holding the four-point Gemini sparkle in its blue→violet→coral gradient. It is a real link to Google AI Studio's key page that opens in a new tab with `noopener noreferrer`, carries an Arabic accessible name, and stays a light tile inside the always-light dialog in both themes. It only helps obtain a key; it never reads, writes, or transmits one.

**The Credits Rule.** The header's «الشكر والتقدير» button reuses the same paper dialog family and hard shadow, with a star tile for its compact state. The dialog holds the two names in a pink strip and the charitable-work statement in a mint strip, both with 2px ink frames. At 420px and below the visible label is clipped for assistive tech only, leaving the star and its Arabic accessible name so the three-button header never overflows.

## Shapes

Work surfaces, fields, cards, and primary controls have square corners with `3px` black borders. Suggestions alone use fully rounded pill silhouettes. Palette samples are circles with `3px` borders. Focus uses a visible `3px` outline with a `4px` offset rather than changing component geometry.

## Components

### Buttons
- **Shape:** sharp corners and opaque hard shadows.
- **Primary:** soft purple, wide, heavy Tajawal label, with pressed translation, shadow contraction, a 500ms fluid shake, and a five-chip pastel splash on click.
- **Theme:** compact mint control; its circular indicator and accessible pressed state reflect the current theme.
- **API key:** compact yellow header control that switches to mint when a key is ready; its accessible label states whether a key is needed or ready.
- **Copy:** small cream labels inside cards; feedback appears adjacent as `تم النسخ!`.
- **Coolors:** compact blue link inside the palette card that opens the generated palette at `coolors.co/<hex>-<hex>-<hex>` in a new tab with `noopener noreferrer`.
- **Pinterest:** compact pink link inside the logo-concept card that opens a short, encoded Pinterest pin search such as `bakery logo minimal` in a new tab with `noopener noreferrer`. A local category map keeps the query general instead of pasting the full description.

### Chips
- **Style:** bordered suggestion pills with solid shadows.
- **State:** yellow, pink, and mint variants; hover and active states use the same physical press grammar as buttons.

### Dialogs
- **API key dialog:** square cream sheet with an opaque dark backdrop, 8px hard offset, masked LTR monospace key field, and save/clear/close actions that use existing yellow, red, and cream button roles.
- **State:** empty submission uses the soft-red status box; save and clear use the mint status box. The field is always empty on open and close, so the key is never displayed back to the user.

### Cards / Containers
- **Corner Style:** square.
- **Background:** yellow for slogan, pink for palette, mint for logo concept, blue for ideas and suggestions.
- **Shadow Strategy:** `8px` solid offset at screen size and `5px` in print.
- **Border:** `3px` near-black.
- **Internal Padding:** `1.5rem`.

### Inputs / Fields
- **Style:** `3px` black border, square corners, cream writing surface, and hard shadow.
- **Focus:** purple outline with an offset; dark mode uses yellow on shell controls.
- **Error / Disabled:** errors use a separate soft-red bordered box; the submit button reduces opacity while loading.
- **API key field:** masked, LTR-monospace input on cream paper; it never stores or echoes the pasted key and accepts four visible actions around it in the dialog.

### Color Swatches
Circular dynamic swatches carry a black border and sit with Arabic color names and LTR monospace HEX codes. Color values are validated before entering inline styles.

## Do's and Don'ts

### Do:
- **Do** preserve native RTL reading order and test both narrow and wide layouts.
- **Do** keep generated Arabic text in `textContent` or form-field values.
- **Do** keep printable result surfaces colored with exact print-color adjustment.
- **Do** provide reduced-motion behavior and visible keyboard focus.

### Don't:
- **Don't** use blurred shadows or rounded cards.
- **Don't** darken the four generated result cards with the shell theme.
- **Don't** let Tailwind preflight flatten component heading typography.
- **Don't** introduce additional accents where the established pastel role already exists.

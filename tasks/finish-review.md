disposition: ship

Missing inputs: none required for the code-led pinned review. There is no approved image comp, comp-diff, seeded-world quality card, or reported user viewport to evaluate; fidelity uses `the_prompt.txt`, the surface contract, source, and the captured application states. The review was performed inline after the unavailable subagent review failed.

## persistence
Pass. `PRODUCT.md` exists and matches the implemented product. This is a code-led build, so no comp-led state or approval record is required. Required web captures exist at `.impeccable/review/desktop.png` and `mobile.png`; supporting captures cover dark mode, empty-input error, and desktop/mobile results. `DESIGN.md` and `.impeccable/design.json` were written after implementation.

## fidelity
| Element | Verdict | Evidence |
|---|---|---|
| TYPE | match | Tajawal is used throughout; the rendered hero is 84.8px/900 on desktop and 36px/900 on narrow mobile. Component-specific selectors prevent Tailwind preflight from flattening headings. |
| MATERIAL | match | Captures show cream paper, opaque pastel cards, sharp black frames, and solid no-blur offset shadows; no physical raster material was requested. |
| GROUND | match | Light mode is warm cream; dark mode changes only the shell to deep ink while generated surfaces remain light. |
| Header and hero | match | RTL logo is on the right, theme button on the left, and the exact Arabic title/subtitle dominate the initial captures. |
| Generator | match | Three thick-bordered suggestion pills, large RTL textarea, purple full-width CTA, and visible pressed/focus states follow the brief. |
| Empty/error states | match | `empty-error.png` shows the specified soft-red bordered error without losing page structure; runtime checks verify API-error loading cleanup. |
| Results | match | Synthetic fixtures render the exact three output types in yellow, pink, and mint cards, with four circular swatches, copy actions, and the print action. Desktop uses three columns and mobile stacks the cards. |
| Responsive behavior | match | Desktop and 390×844 mobile captures are valid; runtime checks found no horizontal overflow at the tested narrow viewport or desktop/result states. |
| Added without approval | none | No extra product sections, commercial claims, frameworks, backend, or generated-image promises were added. |

## ceiling
Reached for the pinned brief. The native devices are Tajawal weight/scale, pastel sheet composition, physical press feedback, one clear loading state, dark mode, and print-oriented result cards. All were exercised in source or captures. Unused image-generation, elaborate illustration, and ornamental motion are not requirements of this Operate surface.

## material_fixes
None. The pre-review Tailwind heading-cascade defect was fixed and recaptured before this verdict.

## keep
Preserve the exact Arabic copy, native RTL flow, light pastel result cards, thick black frames, hard no-blur shadows, and physical press behavior.

## Addendum: pasteable API key
Verdict: ship. The requested header key control was reviewed against the pinned surface after implementation. It adds one yellow compact control to the existing header cluster and opens a square cream dialog with the same black frame, hard offset, Tajawal weight, masked LTR field, wrapped actions, and physical press grammar as the established system. No new accent color, hero content, product claim, or extra page section was introduced; mint signals the ready state and red signals validation, both already part of the system. RTL focus order, dark mode, narrow-header layout, and memory-only behavior were exercised in `.impeccable/review/api-key-runtime-results.json`; the original placeholder remains the fallback. No material fix is required.

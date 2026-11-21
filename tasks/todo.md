# Tasks: Taysir.ai V1

- [x] Task 1: Build the static RTL page and pinned visual system.
  - Acceptance: Required Arabic content, semantic controls/result regions, GPL notices, responsive layout, and print rules exist.
  - Verify: `python3 -m unittest discover -s tests -v`
  - Files: `index.html`, `style.css`, `tests/test_static.py`

- [x] Task 2: Add theme and suggestion interactions.
  - Acceptance: All three suggestions autofill relevant Arabic text; the toggle changes theme and accessible state.
  - Verify: Static tests and runtime interaction review.
  - Files: `script.js`, `index.html`, `tests/test_static.py`

- [x] Task 3: Integrate Gemini generation and defensive parsing.
  - Acceptance: Requests use Gemini structured output; invalid keys/responses and API failures produce the required error and always clear loading.
  - Verify: Static tests plus controlled runtime fixtures; live API requires a user key.
  - Files: `script.js`, `tests/test_static.py`

- [x] Task 4: Complete result rendering, copying, and PDF export.
  - Acceptance: Valid data fills three cards; copy feedback and `window.print()` work; output cannot inject HTML.
  - Verify: Full static tests and rendered-state captures.
  - Files: `script.js`, `index.html`, `style.css`, `tests/test_static.py`

- [x] Task 5: Run the design/quality finish and document actual commands.
  - Acceptance: Required captures and detector run; material issues fixed or reported; design record and AGENTS.md match the app.
  - Verify: Test suite, local HTTP response, Impeccable finish verdict, documentation review.
  - Files: application files as needed, `AGENTS.md`, `DESIGN.md`, `.impeccable/design.json`, `tasks/todo.md`
  - Evidence: `tasks/verification.md`, `tasks/finish-review.md`, and `.impeccable/review/runtime-results.json`
  - Remaining external check: live Gemini generation requires a user-supplied API key.

- [x] Task 6: Add a pasteable Gemini API key control.
  - Acceptance: Header button opens a native RTL dialog; masked key entry is memory-only; save/clear feedback and ready state work; placeholder fallback and all previous behavior remain intact.
  - Verify: 26 static tests, focused Zen Browser/Marionette runtime checks, and new dialog captures.
  - Files: `index.html`, `style.css`, `script.js`, `tests/test_static.py`, `spec/SPEC-taysir-ai.md`, `PRODUCT.md`, `DESIGN.md`, `.impeccable/design.json`, `.impeccable/surfaces/index-html.md`, `AGENTS.md`
  - Evidence: `.impeccable/review/api-key-runtime-results.json` and dialog captures in `.impeccable/review/`.
  - Remaining external check: live Gemini generation requires a real user-supplied API key; controlled browser checks used a fake key only.

- [x] Task 7: Stop the endless loading state on slow or stalled Gemini calls.
  - Acceptance: Requests abort after 45s, use low thinking with an 8192-token budget, log the underlying error without the key, and always clear loading/busy state with the exact Arabic error.
  - Verify: 29 static tests and controlled Zen Browser/Marionette success, 400-error, and never-settling-fetch checks.
  - Files: `script.js`, `index.html`, `tests/test_static.py`, `spec/SPEC-taysir-ai.md`, `tasks/verification.md`
  - Evidence: `.impeccable/review/reliability-runtime-results.json`.
  - Remaining external check: re-test with the user's real free key in the fresh `?v=3` tab; if it still fails, read the browser console error (key excluded).

- [x] Task 8: Fix the repeated hang and add a matching loading bar.
  - Acceptance: Fast `gemini-3.5-flash-lite` first with `gemini-3.8-flash` fallback on abort/429/5xx, 15s per attempt, key-free Google error detail under the exact Arabic error, and an accessible animated Neo-Brutalist progress bar that clears with the loading state.
  - Verify: 33 static tests and controlled Zen Browser/Marionette success, visible-bar, fallback, all-stall, 400-error, and 360px-width checks.
  - Files: `script.js`, `index.html`, `style.css`, `tests/test_static.py`, `spec/SPEC-taysir-ai.md`, `tasks/verification.md`, `AGENTS.md`
  - Evidence: `.impeccable/review/v4-runtime-results.json`.
  - Remaining external check: re-test with the user's real free key in the fresh `?v=4` tab; if it still fails, send the error detail shown under the Arabic message (the key is never displayed).

- [x] Task 9: Add a Coolors palette link and a titled project-ideas card.
  - Acceptance: Palette card shows a small `noopener noreferrer` link built from validated HEX values; Gemini returns 3–4 validated `{title, body}` suggestions rendered safely in a fourth pastel-blue card with copy feedback and print support; 2×2 desktop results grid with no overflow.
  - Verify: 41 static tests and controlled Zen Browser/Marionette render, copy, malformed-suggestion, injection, and responsive-layout checks.
  - Files: `index.html`, `style.css`, `script.js`, `tests/test_static.py`, `spec/SPEC-taysir-ai.md`, `PRODUCT.md`, `DESIGN.md`, `.impeccable/surfaces/index-html.md`, `tasks/verification.md`, `AGENTS.md`
  - Evidence: `.impeccable/review/suggestions-coolors-runtime-results.json`, `results-four-cards-desktop.png`, `results-four-cards-mobile.png`.
  - Remaining external check: confirm a real Gemini key returns the added `suggestions` field; malformed responses now show the exact Arabic error with detail.

- [x] Task 10: Add prompt-based Pinterest logo references to the logo card.
  - Acceptance: Logo card shows a small pink `noopener noreferrer` link with results; its Pinterest pin-search query is a short, general three-word term derived from the submitted description (or `arabic logo minimal`), URL-encoded, with no full prompt or API key; compact styling and RTL/mobile layout remain intact.
  - Verify: 45 static tests and controlled Zen Browser/Marionette category-mapping, fallback, URL-encoding, visibility, styling, and 1100px/360px layout checks.
  - Files: `index.html`, `style.css`, `script.js`, `tests/test_static.py`, `spec/SPEC-taysir-ai.md`, `PRODUCT.md`, `DESIGN.md`, `.impeccable/surfaces/index-html.md`, `tasks/verification.md`, `AGENTS.md`
  - Evidence: `.impeccable/review/pinterest-runtime-results.json`, `.impeccable/review/pinterest-short-query-results.json`, `pinterest-button-desktop.png`, `pinterest-button-mobile.png`.
  - Remaining external check: user to confirm the Pinterest search results are useful for real project prompts.

- [x] Task 11: Add tactile press feedback and a subtle hero wave.
  - Acceptance: Generate button shakes briefly and throws five inaccessible pastel chips on press; chips clean themselves up; hero title waves by whole Arabic word with exact copy preserved; both skip reduced motion and keep dark-mode/token consistency.
  - Verify: 49 static tests and controlled Zen Browser/Marionette checks for animation names, staggered delays, particle colors/cleanup, reduced-motion skip, dark mode, 360px no-overflow, plus sampled-transform smoothness checks.
  - Files: `style.css`, `script.js`, `tests/test_static.py`, `spec/SPEC-taysir-ai.md`, `PRODUCT.md`, `DESIGN.md`, `.impeccable/surfaces/index-html.md`, `tasks/verification.md`, `AGENTS.md`
  - Evidence: `.impeccable/review/motion-runtime-results.json`, `.impeccable/review/motion-smooth-runtime-results.json`, `motion-button-splash.png`, `motion-smooth-splash.png`.
  - Remaining external check: user to confirm the motion feels right in the live browser.

- [x] Task 12: Make the hero title follow the mouse smoothly.
  - Acceptance: Each of the five Arabic words carries an inner shift span; pointer movement eases nearby words with weighted parallax and eases back on leave; exact copy and the existing wave are preserved; no-hover and reduced-motion devices get no shift.
  - Verify: 50 static tests and Zen Browser/Marionette frame sampling for eased values, weighted response, return to rest, reduced-motion/no-hover skips, and 360px no-overflow.
  - Files: `style.css`, `script.js`, `tests/test_static.py`, `spec/SPEC-taysir-ai.md`, `DESIGN.md`, `tasks/verification.md`, `AGENTS.md`
  - Evidence: `.impeccable/review/hover-pointer-results.json`, `hover-pointer-shift.png`.
  - Remaining external check: user to confirm the hover feel in a real mouse browser.

- [x] Task 13: Color the touched hero word.
  - Acceptance: The nearest of the five Arabic words takes a text-safe pastel color on hover or touch while the others stay ink; touch feedback lingers briefly after release; pointer leave clears hover; dark mode, reduced motion, exact copy, wave, and 360px layout stay intact.
  - Verify: 51 static tests and Zen Browser/Marionette checks for hover/touch color state, leave/timer cleanup, dark tokens, reduced-motion color without spatial shift, and 360px no-overflow.
  - Files: `style.css`, `script.js`, `index.html`, `tests/test_static.py`, `spec/SPEC-taysir-ai.md`, `PRODUCT.md`, `DESIGN.md`, `tasks/verification.md`, `AGENTS.md`
  - Evidence: `.impeccable/review/touch-color-results.json`, `hero-touch-color.png`.
  - Remaining external check: user to confirm the hover/touch color feel in a live browser.

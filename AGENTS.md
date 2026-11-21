# Taysir.ai

## Current state
- Taysir.ai V1 is implemented as a static single-page app. The workspace is not an initialized Git repository.
- `the_prompt.txt` is the original product specification; `spec/SPEC-taysir-ai.md` is the approved V1 contract. `PRODUCT.md` records product context and `DESIGN.md` records the implemented visual system.
- No build system, package manifest, lockfile, CI, formatter, or JavaScript lint toolchain is configured. Do not introduce one without need and approval.
- Browser checks use the installed Zen Browser Flatpak. Gemini live generation remains unverified until the user supplies an API key locally. A header dialog now accepts a pasteable key held only in current-page memory. Requests try `gemini-3.5-flash-lite` first and fall back to `gemini-3.8-flash` on abort/429/5xx, abort after 15s per attempt, use low thinking with an 8192-token budget, and show/log underlying errors without the key. The loading state includes an accessible animated progress bar. Results are four pastel cards; the palette card links to coolors.co, the logo card links to prompt-based Pinterest logo references, and Gemini returns validated `suggestions` for a titled ideas card. The generate button makes a fluid decaying-shake and throws five hard-edged pastel chips that travel and fade on press, and the hero title uses a smooth 17-keyframe whole-word sine wave plus a subtle eased mouse-follow shift and a text-safe color on the hovered or touched word; all respect reduced motion.

## Commands
- Serve: `python3 -m http.server 8000 --bind 127.0.0.1`
- Open: `http://127.0.0.1:8000/index.html`
- Test: `python3 -m unittest discover -s tests -v`
- Build/lint/typecheck: not configured and not required for the static app.

## Implementation contract
- The deliverables are `index.html`, `style.css`, and `script.js`, using HTML5, vanilla JavaScript, and Tailwind CSS via CDN; no build step is required.
- Treat `the_prompt.txt` as the source of truth for the requested UI, Arabic copy, Gemini behavior, and GPLv3 notices. Do not expand beyond that scope.
- The UI is native Arabic RTL (`<html dir="rtl" lang="ar">`), mobile-first, with light/dark modes and a print stylesheet for clean PDF export.
- Preserve the Neo-Brutalist style: cream/paper background, pastel surfaces, thick sharp black borders, and solid hard shadows without blur. Check RTL alignment and responsiveness when changing frontend code.
- Gemini must return strict JSON with no surrounding Markdown: `slogan` (string), `colors` (array of `{ "hex", "name" }`), and `logoConcept` (string). Handle empty input, API failures, malformed JSON, and loading-state cleanup as specified.
- The browser integration keeps the user-supplied `GEMINI_API_KEY` placeholder described in the specification and allows a runtime-only override pasted through the header dialog; do not substitute a different provider or response shape, and never persist the pasted key.

## Working rules
- Before coding, draft a short step-by-step plan. Implement in small, testable increments rather than large rewrites.
- Ask before major structural changes. Briefly suggest worthwhile UI/UX, performance, or flow improvements instead of implementing them unapproved.
- Never commit or push automatically. Present the work first; push only after the user explicitly replies `Approved` or `Push`.
- Keep communication short and direct. Surface bugs and tradeoffs, provide the relevant work, and ask for feedback without filler.

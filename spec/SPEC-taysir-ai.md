# Spec: Taysir.ai — V1

Status: approved

## Objective
Build the static, single-page Arabic RTL application defined in `the_prompt.txt`. It helps students' startups and productive families turn an Arabic project description into visual-branding outputs using Google Gemini: a slogan, a 3–4 color palette, a logo concept, and 3–4 titled project ideas with one concrete suggestion each.

Success means a user can enter or select an idea, generate a valid identity, copy each result, open the generated palette in Coolors, open Pinterest logo references based on the submitted prompt, toggle light/dark mode, and print the result cards to PDF. Empty input, API failures, malformed responses, and loading cleanup must be handled visibly and safely.

## Approved Addition: Pasteable API Key
The header includes a «مفتاح Gemini» button that opens a native Arabic dialog with a masked password field, save, clear, and close actions. A pasted key overrides `GEMINI_API_KEY` for the current page only; it is never written to `localStorage`, `sessionStorage`, or source files, and the password field is cleared whenever the dialog opens or closes. The original `YOUR_API_KEY_HERE` placeholder remains in `script.js` as the fallback. This addition was explicitly requested and approved by the user.

## Approved Addition: Coolors Link and Ideas Card
The palette card carries a compact blue «Coolors» link that opens `https://coolors.co/<hex>-<hex>-<hex>` in a new tab with `noopener noreferrer`; the URL is rebuilt from the validated HEX values on every generation. Gemini's strict JSON response also includes `suggestions`: an array of 3–4 objects with non-empty Arabic `title` and `body` strings, rendered in a fourth pastel-blue card with its own copy action and print support. This addition was explicitly requested and approved by the user; all original copy and states remain unchanged.

## Approved Addition: Pinterest Reference Link
The logo-concept card carries a compact pink «Pinterest» link that appears with the results and opens `https://www.pinterest.com/search/pins/?q=<encoded-term>` in a new tab with `noopener noreferrer`. The query is short and general: a local keyword map turns the submitted description into a broad category (`bakery`, `perfume`, `delivery`, …) or `arabic`, then appends `logo minimal` for a three-word visual-reference search. The full description and API key are never included in this URL. This addition was explicitly requested and approved by the user; all original copy and states remain unchanged.

## Approved Addition: Press Feedback and Hero Wave
The generate button answers a press with a 500ms fluid ink recoil and five hard-edged pastel chips that travel outward with deceleration, fade, remove themselves, and never change layout. The hero title is wrapped by whole Arabic word, not by character, so a slow sine-like wave sampled at 17 linear keyframes can stagger across five words without velocity stalls or breaking Arabic shaping and the exact copy. Both effects use existing tokens, remain hidden from assistive technology where decorative, and are skipped for reduced-motion users. This addition was explicitly requested and approved by the user.

## Approved Addition: Pointer-Driven Hero Motion
The hero title's words each carry an inner shift span that follows mouse movement across the heading. A local `requestAnimationFrame` loop eases each word toward a weighted parallax target and back to rest on pointer leave, without altering the exact Arabic copy or interfering with the per-word sine wave. The effect is skipped on devices without hover and for reduced-motion users. The nearest word also takes a text-safe pastel color on hover or touch; touch feedback lingers briefly after release, and the color state remains for reduced-motion users. This addition was explicitly requested and approved by the user.

## Tech Stack
- HTML5, vanilla JavaScript, and custom CSS.
- Tailwind CSS via CDN; no package manager or build step.
- Google Fonts Tajawal or Cairo with bold Arabic weights.
- Google Gemini `generateContent` API with strict JSON output, using stable `gemini-3.8-flash` (officially documented with text output and structured-output support).
- GPLv3 notices as required by the prompt.

## Commands
- Development server: `python3 -m http.server 8000`
- Open locally: `http://localhost:8000`
- Static verification, after tests are created: `python3 -m unittest discover -s tests -v`
- Build: not required; the three application files are served directly.
- Lint/typecheck: not configured. Adding a JS toolchain requires approval.

## Project Structure
- `the_prompt.txt` — original product requirements and Arabic copy.
- `spec/SPEC-taysir-ai.md` — approved V1 contract.
- `index.html` — semantic RTL page, input, loading/error states, result cards, and footer.
- `style.css` — Neo-Brutalist utilities, animations, responsive details, and print rules.
- `script.js` — Gemini key placeholder and runtime override, suggestions, theme, generation, parsing, rendering, copying, and printing.
- `tests/test_static.py` — Python-standard-library checks for required static structure and resources.
- `.opencode/skills/` — installed agent workflows; not application code.

## Code Style
Use small single-purpose functions, `const`/`let`, async/await, semantic HTML, and `textContent` for generated text. Keep the API key placeholder only in `script.js`; never replace it with a committed real key.

```js
function showError(message, detail = "") {
  errorMessage.textContent = message;
  errorMessage.hidden = false;
  errorDetail.textContent = detail;
  errorDetail.hidden = !detail;
}
```

Keep Arabic user-facing strings faithful to `the_prompt.txt`. Use mobile-first Tailwind classes, CSS variables for shared colors where useful, and hard black shadows without blur. Generated colors must be validated as HEX values before being used as inline color values.

## Testing Strategy
- Add focused Python standard-library static tests for the RTL/language attributes, required controls and Arabic labels, external resources, Gemini key placeholder, strict response fields, and print rules.
- Verify each implementation slice with `python3 -m unittest discover -s tests -v` before expanding it.
- Cover the API key dialog's markup, memory-only behavior, placeholder fallback, and Arabic feedback in static tests; verify in-browser that a pasted key is sent as `x-goog-api-key`, that clearing restores the missing-key error, and that no key reaches browser storage.
- Verify that every Gemini request has a short abort timeout, tries a fast free-tier model before a stronger one on timeout/429/5xx, uses low thinking with a sufficient output budget, and that success, API-error, and stalled-request paths all clear loading and restore the button.
- Cover the loading progress bar's markup, accessible `progressbar` role, and matching Neo-Brutalist animation; verify that a visible error detail is shown without echoing the API key.
- Cover the Coolors deep link and the `suggestions` contract: schema fields, 3–4 item validation, safe `textContent` rendering, copy-as-lines output, rejection of malformed suggestions, and unchanged loading/error cleanup.
- Cover the Pinterest link's placement in the logo card, `noopener noreferrer` attributes, category mapping, three-word fallback, and URL-encoded short query.
- Cover the generate button's click-only shake/splash, particle cleanup, reduced-motion skip, and the hero title's whole-word wave with exact Arabic copy preserved.
- Serve through `python3 -m http.server 8000` and manually test suggestion autofill, theme toggle, keyboard operation, empty input, loading, copy feedback, and print preview at mobile and desktop widths.
- Test Gemini success and HTTP/network failures with a user-supplied key. Test malformed JSON and schema mismatches using controlled local test doubles, without sending a real key anywhere else.
- No coverage target or browser automation framework is introduced in V1. Visual and live-API checks require an available browser and API key; report any checks that cannot be run.

## Boundaries
- Always: follow `the_prompt.txt`; keep the app natively Arabic RTL and responsive; validate input and Gemini output; clean up loading state on every path; verify each slice; preserve the exact JSON response contract.
- Always: use `textContent` for generated text and `window.print()` for PDF export; keep real API keys out of repository files and test fixtures.
- Ask first: add dependencies, a build system, a backend/proxy, persistent storage, CI, additional features, or major structural/design changes; perform any Git mutation.
- Never: commit or push automatically, insert real credentials, use another AI provider, allow generated HTML injection, or hide/ignore failed checks.

## Success Criteria
1. `index.html` declares `<html dir="rtl" lang="ar">`, loads Tailwind CDN and a bold Arabic font, and includes GPLv3 source/footer notices.
2. Header has `تيسير.ai` on the right and a working Neo-Brutalist dark/light toggle on the left.
3. Hero, exact prompt-supplied Arabic title/subtitle/placeholder/CTA text, three working suggestion pills, input area, and loading spinner/text match the specification.
4. The interface uses a paper-like cream background, pastel surfaces, thick sharp black borders, hard no-blur shadows, responsive layouts, and the specified pressed-button interaction.
5. A non-empty request calls Gemini and rubric-consistent Arabic results appear in a fade-in results section with the three requested pastel cards.
6. Gemini returns and the app validates exactly `slogan` (string), `colors` (3–4 objects containing Arabic `name` and valid `hex`), and `logoConcept` (string), with no Markdown wrapper.
7. Suggestions autofill relevant Arabic descriptions; each copy button copies its card's content and briefly displays `تم النسخ!`.
8. Empty input shows `الرجاء كتابة وصف للمشروع أولاً`; request/parsing failures hide loading and show `حدث خطأ أثناء التوليد، يرجى المحاولة مرة أخرى`.
9. `تحميل الهوية (PDF)` invokes `window.print()`; print CSS hides the header, input area, and buttons while preserving readable result cards.
10. Static tests pass, the page loads through the documented local server, and completed versus unverified browser/live-API checks are reported explicitly.
11. The header key button opens a native RTL dialog; save and clear update a visible ready state, the pasted key is used for the request, no key is persisted or echoed, and clearing restores the placeholder fallback.
12. A slow, failed, or stalled Gemini call never leaves the loading state active: each attempt is aborted after a short fixed timeout, a stalled/rate-limited call falls back to a faster model, Google errors are logged to the console and shown as key-free detail, and the exact Arabic error is shown.
13. While generating, an accessible animated progress bar matches the spinner's Neo-Brutalist style and is removed with the loading state on success or failure.
14. The palette card exposes a small `noopener noreferrer` link to `coolors.co` containing the generated HEX values without `#`, rebuilt for every result.
15. Gemini returns validated `suggestions` (3–4 titled items), rendered safely in a fourth pastel-blue card with working copy feedback and included in print output.
16. The logo-concept card exposes a small `noopener noreferrer` Pinterest link whose query is a three-word, URL-encoded general category plus `logo minimal`, rebuilt for every result and never containing the full description or API key.
17. Pressing the generate button briefly shakes it and throws five inaccessible pastel chips that clean themselves up; the hero title waves by whole Arabic word with staggered timing, and both effects respect reduced-motion preferences.

## Out of Scope (Deferred)
- Backend proxy, authentication, saved identities, and database storage: not requested in V1.
- Actual generated logo image files or exports other than print/PDF: not requested.
- Additional languages, AI providers, frameworks, package tooling, or deployment configuration: outside the requested Gemini/static scope.
- Persistent theme/history and additional design sections: avoid unrequested feature growth.

## Open Questions
- A Gemini API key is required for live-API verification. `script.js` retains `YOUR_API_KEY_HERE`; the user can paste a key locally through the header dialog or edit the placeholder directly.
- The client-side key requirement means anyone who can open a deployed page can read the key. A secure production proxy is deliberately deferred, so V1 should be treated as a local/demo deployment unless the user approves that additional architecture.

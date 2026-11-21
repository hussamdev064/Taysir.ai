# Implementation Plan: Taysir.ai V1

## Contract and architecture
- Source of truth: `spec/SPEC-taysir-ai.md` and `the_prompt.txt`.
- Static Operate surface: one RTL HTML document, one custom stylesheet, and one deferred JavaScript file. No build step or application dependencies.
- Use Tailwind CDN for responsive layout and `style.css` for the pinned Neo-Brutalist tokens, interaction states, animation, dark theme, and print rules.
- Use the stable `gemini-3.8-flash` model at `/v1beta/models/gemini-3.8-flash:generateContent`; official model documentation confirms text output and structured-output support.
- Send a system instruction, the user's Arabic description, `responseMimeType: application/json`, and a response schema. Parse `candidates[0].content.parts`, validate the identity object, and only then render it.

## Ordered increments
1. **Page shell and visual system**
   - Add static structural tests, then semantic RTL markup and custom tokens/styles.
   - Checkpoint: tests pass and the static page is serviceable without JavaScript.
2. **Immediate interactions**
   - Add suggestion autofill, error clearing, and light/dark toggle behavior.
   - Checkpoint: tests pass; every immediate control has a real target and handler.
3. **Gemini path**
   - Add request construction, key-placeholder validation, loading cleanup, protected JSON parsing, and schema/HEX validation.
   - Checkpoint: static checks pass; success and malformed-response fixtures will be exercised in the final runtime pass.
4. **Results and export**
   - Render all three cards with `textContent`/DOM nodes, add copy feedback and print behavior, and cover errors consistently.
   - Checkpoint: static checks pass; no generated HTML injection path exists.
5. **Finish and document**
   - Run the full test suite, local HTTP verification, Impeccable desktop/mobile captures and interaction states, detector, finish review, and design documentation.
   - Update `AGENTS.md` from bootstrap status to the actual app/commands.
   - Live Gemini remains explicitly unverified until a user-supplied key is available.

## Dependencies and risks
- Sequential edits to `index.html` and `script.js`; no parallel implementation in the same files.
- CDN/network dependency: Tailwind and Google Fonts require network access. Core custom CSS keeps the layout legible if utility styles load late.
- Browser key exposure: accepted only for the documented local/demo V1. Never place a real key in source or tests.
- API/schema drift: use one model constant, validate every response, and report live-API status honestly.
- No Git repository exists and automatic commits are forbidden; per-slice commits are deliberately skipped while tests remain mandatory.

## Final verification
- Command: `python3 -m unittest discover -s tests -v`
- Serve: `python3 -m http.server 8000`
- Inspect mobile, desktop, dark mode, empty/error states, and print styles.
- Run `.opencode/skills/impeccable/scripts/impeccable detect --json index.html style.css script.js` once after UI implementation.
- Complete an independent Impeccable finish review and produce the required design record.

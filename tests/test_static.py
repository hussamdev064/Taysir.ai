from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def source(name):
    path = ROOT / name
    return path.read_text(encoding="utf-8") if path.exists() else ""


class PageShellTests(unittest.TestCase):
    def setUp(self):
        self.html = source("index.html")

    def test_application_files_exist(self):
        for name in ("index.html", "style.css", "script.js"):
            self.assertTrue((ROOT / name).is_file(), f"Missing {name}")

    def test_native_arabic_document_and_open_source_notice(self):
        self.assertRegex(self.html, r'<html\s+dir="rtl"\s+lang="ar">')
        self.assertTrue(self.html.lstrip().startswith("<!--"))
        self.assertIn("GPLv3", self.html.split("-->", 1)[0])
        footer = re.search(r"<footer[\s\S]*?</footer>", self.html)
        self.assertIsNotNone(footer)
        self.assertIn("GPLv3", footer.group(0))
        self.assertIn("مفتوح المصدر", footer.group(0))

    def test_required_resources(self):
        self.assertIn("https://cdn.tailwindcss.com", self.html)
        self.assertIn("fonts.googleapis.com", self.html)
        self.assertIn("Tajawal", self.html)
        self.assertRegex(self.html, r'href="style\.css(?:\?v=\d+)?"')
        self.assertRegex(self.html, r'src="script\.js(?:\?v=\d+)?"')
        self.assertIn("defer", self.html)

    def test_exact_hero_copy(self):
        self.assertIn("تيسير", self.html)
        self.assertIn("أطلق هوية مشروعك في ثوانٍ", self.html)
        self.assertIn(
            "منصة تعمل بالذكاء الاصطناعي لمساعدة الطلاب والأسر المنتجة على بناء هويتهم البصرية مجاناً",
            self.html,
        )


class RequiredMarkupTests(unittest.TestCase):
    def setUp(self):
        self.html = source("index.html")

    def test_suggestions_and_generation_controls(self):
        for label in ("مخبز منزلي", "متجر عطور", "تطبيق توصيل"):
            self.assertIn(label, self.html)
        self.assertEqual(self.html.count("data-description="), 3)
        self.assertIn("اكتب هنا فكرة مشروعك، ما الذي تبيعه؟ ومن هم عملاؤك؟", self.html)
        self.assertIn("توليد الهوية البصرية", self.html)
        self.assertIn("تيسير يبتكر هويتك الآن...", self.html)
        self.assertIn('id="loading-state"', self.html)

    def test_results_cards_and_export(self):
        self.assertRegex(self.html, r'<section[^>]*id="results-section"[^>]*hidden')
        self.assertIn("تحميل الهوية (PDF)", self.html)
        for title in ("الشعار اللفظي", "ألوان الهوية", "فكرة الشعار البصري", "أفكار ومقترحات"):
            self.assertIn(title, self.html)
        for element_id in ("slogan-output", "color-palette", "logo-concept", "suggestions-output", "print-button"):
            self.assertIn(f'id="{element_id}"', self.html)
        self.assertEqual(self.html.count("data-copy="), 4)
        self.assertRegex(self.html, r'<textarea[^>]*id="logo-concept"[^>]*readonly')


class VisualSystemTests(unittest.TestCase):
    def setUp(self):
        self.css = source("style.css")

    def test_neobrutalist_tokens_and_animation(self):
        for token in ("--paper:", "--ink:", "--yellow:", "--pink:", "--mint:", "--purple:"):
            self.assertIn(token, self.css)
        self.assertRegex(self.css, r"box-shadow:\s*[^;]*\b0\s+#")
        self.assertIn("@keyframes fade-in", self.css)
        self.assertIn("html.dark", self.css)
        self.assertIn(":focus-visible", self.css)
        self.assertIn("prefers-reduced-motion", self.css)

    def test_heading_selectors_survive_tailwind_preflight(self):
        for selector in ("#hero-title {", "#results-title {", ".result-card h3 {"):
            self.assertIn(selector, self.css)


class MotionPolishTests(unittest.TestCase):
    def setUp(self):
        self.css = source("style.css")
        self.js = source("script.js")
        self.html = source("index.html")

    def test_generate_button_shake_and_splash_styles(self):
        self.assertIn(".generate-button.is-shaking", self.css)
        self.assertIn("@keyframes generate-shake", self.css)
        self.assertIn(".splash-particle {", self.css)
        self.assertIn("@keyframes splash-pop", self.css)
        self.assertIn("box-shadow: 2px 2px 0 #17151b", self.css)

    def test_generate_button_click_builds_and_cleans_particles(self):
        self.assertIn("function splashGenerateButton(button)", self.js)
        self.assertIn('generateButton.addEventListener("click"', self.js)
        self.assertIn('prefers-reduced-motion: reduce', self.js)
        self.assertIn('className = "splash-particle"', self.js)
        self.assertIn('setProperty("--x"', self.js)
        self.assertIn('animationend', self.js)
        self.assertIn("particle.remove()", self.js)

    def test_hero_title_uses_word_level_sine_wave(self):
        self.assertIn("#hero-title .wave-word", self.css)
        self.assertIn("@keyframes hero-wave", self.css)
        self.assertIn("animation-delay: calc(var(--wave-index)", self.css)
        self.assertIn("function wrapHeroTitleWords()", self.js)
        self.assertIn('className = "wave-word"', self.js)
        self.assertIn('setProperty("--wave-index"', self.js)
        self.assertIn('<h1 id="hero-title">أطلق هوية مشروعك في ثوانٍ</h1>', self.html)

    def test_motion_is_smoother_and_clearer(self):
        def frames(name):
            return self.css.split(f"@keyframes {name} {{", 1)[1].split("\n}", 1)[0]

        hero = frames("hero-wave")
        self.assertGreaterEqual(hero.count("%"), 16)
        self.assertIn("hero-wave 3.6s linear infinite", self.css)
        self.assertIn("will-change: transform", self.css)

        shake = frames("generate-shake")
        self.assertGreaterEqual(shake.count("%"), 8)
        self.assertIn("generate-shake 500ms cubic-bezier(0.37, 0, 0.63, 1)", self.css)

        splash = frames("splash-pop")
        self.assertIn("translate(var(--x), var(--y))", splash.split("100%", 1)[1])
        self.assertIn("splash-pop 620ms cubic-bezier(0.16, 1, 0.3, 1) forwards", self.css)
        self.assertIn("520", self.js)

    def test_hero_title_follows_pointer_with_eased_per_word_shift(self):
        self.assertIn("#hero-title .word-shift", self.css)
        self.assertIn("var(--shift-x", self.css)
        self.assertIn("var(--shift-y", self.css)
        self.assertIn('wordShift.className = "word-shift"', self.js)
        self.assertIn('addEventListener("pointermove"', self.js)
        self.assertIn('addEventListener("pointerenter"', self.js)
        self.assertIn('addEventListener("pointerleave"', self.js)
        self.assertIn("requestAnimationFrame(stepHeroPointer)", self.js)
        self.assertIn("(hover: hover)", self.js)
        self.assertIn("prefers-reduced-motion: reduce", self.js)

    def test_hero_words_get_colored_on_hover_or_touch(self):
        for token in ("--yellow-text", "--pink-text", "--mint-text", "--blue-text", "--purple-text"):
            self.assertIn(f"{token}:", self.css)
        self.assertIn(".wave-word.is-touched .word-shift", self.css)
        self.assertIn("transition: color 160ms ease", self.css)
        self.assertIn("HERO_TOUCH_COLORS", self.js)
        self.assertIn('setProperty("--word-color"', self.js)
        self.assertIn('addEventListener("pointerdown"', self.js)
        self.assertIn('pointerType === "touch"', self.js)
        self.assertIn('classList.toggle("is-touched"', self.js)


class PrintAndResultsStyleTests(unittest.TestCase):
    def setUp(self):
        self.css = source("style.css")

    def test_distinct_result_cards_and_copy_feedback(self):
        for selector in (".slogan-card", ".palette-card", ".logo-card", ".ideas-card", ".suggestions-output", ".suggestion-item", ".color-swatch", ".copy-feedback"):
            self.assertIn(selector, self.css)
        self.assertIn("break-inside: avoid", self.css)

    def test_print_rules_hide_chrome_and_keep_cards(self):
        self.assertIn("@media print", self.css)
        print_css = self.css.split("@media print", 1)[1]
        for hidden_target in ("#site-header", "#identity-form", ".no-print", "button"):
            self.assertIn(hidden_target, print_css)
        self.assertIn(".result-card", print_css)
        self.assertIn("print-color-adjust: exact", print_css)


class ImmediateInteractionTests(unittest.TestCase):
    def setUp(self):
        self.js = source("script.js")

    def test_suggestion_click_autofills_and_clears_errors(self):
        self.assertIn('querySelectorAll("[data-description]")', self.js)
        self.assertIn("button.dataset.description", self.js)
        self.assertIn("descriptionInput.value", self.js)
        self.assertIn("clearError", self.js)

    def test_theme_toggle_updates_visual_and_accessible_state(self):
        self.assertIn("themeToggle.addEventListener", self.js)
        self.assertIn('classList.toggle("dark"', self.js)
        self.assertIn("aria-pressed", self.js)
        self.assertIn("themeLabel.textContent", self.js)


class ApiKeyDialogTests(unittest.TestCase):
    def setUp(self):
        self.html = source("index.html")
        self.js = source("script.js")
        self.css = source("style.css")

    def test_header_button_and_dialog_markup(self):
        for fragment in (
            'id="api-key-button"',
            'aria-haspopup="dialog"',
            'aria-controls="api-key-dialog"',
            '<dialog id="api-key-dialog"',
            'id="api-key-input"',
            'type="password"',
            'autocomplete="off"',
            'id="api-key-form"',
            'id="api-key-save"',
            'id="api-key-clear"',
            'id="api-key-close"',
        ):
            self.assertIn(fragment, self.html, fragment)
        self.assertIn("مفتاح Gemini", self.html)
        self.assertIn("الصق مفتاح Gemini هنا", self.html)
        self.assertIn("يُستخدم المفتاح لهذه الصفحة فقط", self.html)
        self.assertRegex(self.html, r'<dialog[^>]*class="[^"]*\bno-print\b')
        self.assertRegex(self.html, r'<button[^>]*id="api-key-button"[^>]*class="[^"]*\bbrutal-button\b')

    def test_dialog_has_gemini_key_link(self):
        self.assertIn('id="gemini-key-link"', self.html)
        self.assertIn('href="https://aistudio.google.com/u/2/api-keys"', self.html)
        self.assertIn('target="_blank"', self.html)
        self.assertIn('rel="noopener noreferrer"', self.html)
        self.assertIn('aria-label="فتح صفحة مفاتيح Gemini"', self.html)
        self.assertIn('class="gemini-mark"', self.html)
        self.assertIn("<linearGradient", self.html)
        self.assertIn(".gemini-key-link", self.css)
        self.assertIn(".gemini-mark", self.css)

    def test_dialog_reuses_the_pinned_visual_system(self):
        for selector in (".header-actions", ".api-key-button", ".api-key-dialog", ".api-key-input", ".api-key-status", ".api-key-actions"):
            self.assertIn(selector, self.css, selector)
        self.assertIn("box-shadow: 6px 6px 0 #17151b", self.css)

    def test_key_is_held_in_memory_only(self):
        self.assertIn('let runtimeGeminiApiKey = "";', self.js)
        self.assertNotIn("localStorage", self.js)
        self.assertNotIn("sessionStorage", self.js)
        self.assertIn("apiKeyInput.value = \"\"", self.js)
        self.assertIn('apiKeyInput.type = "password"', self.js)

    def test_placeholder_remains_the_fallback(self):
        self.assertIn("const GEMINI_API_KEY = 'YOUR_API_KEY_HERE';", self.js)
        self.assertIn("runtimeGeminiApiKey || GEMINI_API_KEY", self.js)
        self.assertIn("const apiKey = getGeminiApiKey();", self.js)
        self.assertIn('"x-goog-api-key": apiKey', self.js)

    def test_dialog_feedback_and_lifecycle(self):
        for copy in (
            "الرجاء لصق مفتاح Gemini أولاً",
            "تم حفظ المفتاح لهذه الصفحة فقط",
            "تم مسح المفتاح",
        ):
            self.assertIn(copy, self.js, copy)
        self.assertIn("apiKeyDialog.showModal()", self.js)
        self.assertIn("apiKeyDialog.close()", self.js)
        self.assertIn('apiKeyDialog.addEventListener("close"', self.js)
        self.assertIn("apiKeyInput.focus()", self.js)


class GeminiContractTests(unittest.TestCase):
    def setUp(self):
        self.js = source("script.js")

    def test_key_placeholder_and_current_stable_endpoint(self):
        self.assertIn("const GEMINI_API_KEY = 'YOUR_API_KEY_HERE';", self.js)
        self.assertIn("gemini-3.8-flash:generateContent", self.js)
        self.assertIn("x-goog-api-key", self.js)
        self.assertIn('method: "POST"', self.js)

    def test_strict_structured_output_contract(self):
        self.assertIn('responseMimeType: "application/json"', self.js)
        self.assertIn("responseSchema", self.js)
        for field in ("slogan", "colors", "logoConcept", "suggestions"):
            self.assertIn(field, self.js)
        self.assertIn("systemInstruction", self.js)
        self.assertIn("STRICT JSON", self.js)

    def test_response_and_color_validation(self):
        self.assertIn("if (!response.ok)", self.js)
        self.assertIn("JSON.parse", self.js)
        self.assertIn("payload.candidates?.[0]?.content?.parts", self.js)
        self.assertRegex(self.js, r"colors\.length < 3 \|\| colors\.length > 4")
        self.assertIn("/^#[0-9a-fA-F]{6}$/", self.js)
        self.assertIn("apiKey === \"YOUR_API_KEY_HERE\"", self.js)


class GeminiReliabilityTests(unittest.TestCase):
    def setUp(self):
        self.js = source("script.js")

    def test_request_always_times_out_and_cleans_up(self):
        self.assertIn("const GEMINI_TIMEOUT_MS = 15000;", self.js)
        self.assertIn("const controller = new AbortController();", self.js)
        self.assertIn("signal: controller.signal", self.js)
        self.assertIn("clearTimeout(timeoutId)", self.js)
        self.assertIn("finally {", self.js)

    def test_generation_budget_matches_thinking_model(self):
        self.assertIn('thinkingLevel: "low"', self.js)
        self.assertIn("maxOutputTokens: 8192", self.js)

    def test_generation_errors_are_logged_for_debugging(self):
        self.assertIn('console.error("Taysir.ai generation error:", error);', self.js)

    def test_stalled_primary_model_falls_back_to_fast_model(self):
        self.assertIn("gemini-3.8-flash:generateContent", self.js)
        self.assertIn("gemini-3.5-flash-lite:generateContent", self.js)
        self.assertIn("for (const endpoint of GEMINI_ENDPOINTS)", self.js)
        self.assertIn('error.name === "AbortError"', self.js)
        self.assertIn("error.status === 429 || error.status >= 500", self.js)

    def test_error_detail_is_visible_and_key_free(self):
        self.assertIn("function showError(message, detail = \"\")", self.js)
        self.assertIn("formErrorDetail.textContent = detail", self.js)
        self.assertIn("error.message || String(error)", self.js)


class SuggestionsTests(unittest.TestCase):
    def setUp(self):
        self.html = source("index.html")
        self.css = source("style.css")
        self.js = source("script.js")

    def test_suggestions_card_markup(self):
        self.assertIn('class="result-card ideas-card"', self.html)
        self.assertIn('id="suggestions-output"', self.html)
        self.assertIn('data-copy="suggestions"', self.html)
        self.assertIn("<ul", self.html)
        self.assertIn("md:grid-cols-2", self.html)
        self.assertNotIn("lg:grid-cols-3", self.html)

    def test_gemini_contract_includes_titled_suggestions(self):
        self.assertIn('"suggestions":[{"title"', self.js)
        self.assertIn("suggestions: {", self.js)
        self.assertIn('required: ["title", "body"]', self.js)
        self.assertIn('required: ["slogan", "colors", "logoConcept", "suggestions"]', self.js)

    def test_suggestions_are_validated_before_rendering(self):
        self.assertIn("suggestions.length < 3 || suggestions.length > 4", self.js)
        self.assertIn("!suggestion.title.trim()", self.js)
        self.assertIn("!suggestion.body.trim()", self.js)
        self.assertIn("suggestions: validSuggestions", self.js)

    def test_suggestions_render_as_safe_text_and_copy_as_lines(self):
        self.assertIn('const suggestionsOutput = byId("suggestions-output");', self.js)
        self.assertIn("suggestionsOutput.replaceChildren()", self.js)
        self.assertIn('document.createElement("li")', self.js)
        self.assertIn("suggestionTitle.textContent = suggestion.title", self.js)
        self.assertIn("suggestionBody.textContent = suggestion.body", self.js)
        self.assertIn('if (kind === "suggestions")', self.js)

    def test_ideas_card_uses_pastel_blue_and_printable_list(self):
        self.assertIn(".ideas-card {", self.css)
        self.assertIn("background: var(--blue)", self.css)
        self.assertIn(".suggestions-output {", self.css)
        self.assertIn(".suggestion-title {", self.css)
        self.assertIn(".suggestion-body {", self.css)
        self.assertIn("list-style: none", self.css)


class PinterestTests(unittest.TestCase):
    def setUp(self):
        self.html = source("index.html")
        self.css = source("style.css")
        self.js = source("script.js")

    def test_pinterest_link_markup_inside_logo_card(self):
        logo_card = re.search(r'<article class="result-card logo-card">[\s\S]*?</article>', self.html)
        self.assertIsNotNone(logo_card)
        self.assertIn('id="pinterest-link"', logo_card.group(0))
        self.assertIn('class="pinterest-button"', logo_card.group(0))
        self.assertIn('target="_blank"', logo_card.group(0))
        self.assertIn('rel="noopener noreferrer"', logo_card.group(0))
        self.assertIn("Pinterest", logo_card.group(0))

    def test_pinterest_link_uses_a_short_general_query(self):
        self.assertIn('const pinterestLink = byId("pinterest-link");', self.js)
        self.assertIn("function buildPinterestQuery(description)", self.js)
        self.assertIn('pinterestLink.href = `https://www.pinterest.com/search/pins/?q=${encodeURIComponent(buildPinterestQuery(description))}`;', self.js)
        self.assertIn('return `${category || "arabic"} logo minimal`;', self.js)
        self.assertNotIn('`${description} logo design`', self.js)
        self.assertIn("renderIdentity(identity, description)", self.js)

    def test_pinterest_categories_cover_the_prompt_examples(self):
        for keyword in ("مخبز", "معجنات", "عطور", "توصيل"):
            self.assertIn(keyword, self.js)
        for term in ("bakery", "perfume", "delivery", "arabic"):
            self.assertIn(term, self.js)

    def test_pinterest_button_uses_the_pinned_compact_action_style(self):
        self.assertIn(".pinterest-button {", self.css)
        self.assertIn("background: var(--pink)", self.css)
        self.assertIn("box-shadow: 3px 3px 0 #17151b", self.css)
        self.assertIn(".pinterest-button:hover", self.css)
        self.assertIn(".pinterest-button:active", self.css)


class CoolorsTests(unittest.TestCase):
    def setUp(self):
        self.html = source("index.html")
        self.css = source("style.css")
        self.js = source("script.js")

    def test_coolors_link_markup(self):
        self.assertIn('id="coolors-link"', self.html)
        self.assertIn('class="coolors-button"', self.html)
        self.assertIn('target="_blank"', self.html)
        self.assertIn('rel="noopener noreferrer"', self.html)
        self.assertIn("Coolors", self.html)

    def test_coolors_link_is_built_from_generated_hex_values(self):
        self.assertIn('const coolorsLink = byId("coolors-link");', self.js)
        self.assertIn("coolorsLink.href = ", self.js)
        self.assertIn("https://coolors.co/${", self.js)
        self.assertIn('.replace("#", "").toLowerCase()', self.js)
        self.assertIn('.join("-")', self.js)

    def test_coolors_button_uses_existing_palette_tokens(self):
        self.assertIn(".card-action-group {", self.css)
        self.assertIn(".coolors-button {", self.css)
        self.assertIn("background: var(--blue)", self.css)
        self.assertIn("box-shadow: 3px 3px 0 #17151b", self.css)


class LoadingBarTests(unittest.TestCase):
    def setUp(self):
        self.html = source("index.html")
        self.css = source("style.css")

    def test_progress_bar_markup(self):
        self.assertIn('class="loading-bar"', self.html)
        self.assertIn('class="loading-bar-fill"', self.html)
        self.assertIn('role="progressbar"', self.html)
        self.assertIn("aria-label=\"جارٍ التوليد\"", self.html)
        self.assertIn('id="form-error-detail"', self.html)

    def test_progress_bar_matches_loading_animation(self):
        self.assertIn(".loading-bar {", self.css)
        self.assertIn(".loading-bar-fill {", self.css)
        self.assertIn("@keyframes loading-sweep", self.css)
        self.assertIn("box-shadow: 4px 4px 0 #17151b", self.css)
        self.assertIn("prefers-reduced-motion: reduce", self.css)


class ResultRenderingTests(unittest.TestCase):
    def setUp(self):
        self.js = source("script.js")

    def test_safe_text_and_dom_rendering(self):
        self.assertIn("sloganOutput.textContent = identity.slogan", self.js)
        self.assertIn("logoOutput.value = identity.logoConcept", self.js)
        self.assertIn('document.createElement("div")', self.js)
        self.assertIn("swatch.style.backgroundColor = color.hex", self.js)
        self.assertIn("colorName.textContent = color.name", self.js)
        self.assertIn("hexCode.textContent = color.hex", self.js)
        self.assertNotIn("innerHTML", self.js)

    def test_loading_state_and_results_animation(self):
        self.assertIn("loadingState.hidden = !isLoading", self.js)
        self.assertIn("generateButton.disabled = isLoading", self.js)
        self.assertIn("resultsSection.hidden = false", self.js)
        self.assertIn('classList.add("animate-fade-in")', self.js)


class SubmissionLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.js = source("script.js")

    def test_empty_input_and_generation_errors_use_exact_arabic_copy(self):
        self.assertIn("الرجاء كتابة وصف للمشروع أولاً", self.js)
        self.assertIn("حدث خطأ أثناء التوليد، يرجى المحاولة مرة أخرى", self.js)

    def test_submit_flow_is_guarded_and_always_cleans_loading(self):
        self.assertIn('identityForm.addEventListener("submit"', self.js)
        self.assertIn("event.preventDefault()", self.js)
        self.assertIn("descriptionInput.value.trim()", self.js)
        self.assertIn("await requestIdentity(description)", self.js)
        self.assertIn("renderIdentity(identity, description)", self.js)
        self.assertRegex(self.js, r"finally\s*\{\s*setLoading\(false\)")


class CopyAndExportTests(unittest.TestCase):
    def setUp(self):
        self.js = source("script.js")

    def test_copy_buttons_copy_each_card_with_feedback(self):
        self.assertIn('querySelectorAll("[data-copy]")', self.js)
        self.assertIn("navigator.clipboard.writeText", self.js)
        self.assertIn("getCopyText", self.js)
        self.assertIn('feedback.textContent = "تم النسخ!"', self.js)
        self.assertIn("setTimeout", self.js)

    def test_print_action_uses_browser_pdf_flow_and_expands_logo(self):
        self.assertIn('byId("print-button").addEventListener("click"', self.js)
        self.assertIn("window.print()", self.js)
        self.assertIn('"beforeprint"', self.js)
        self.assertIn("resizeLogoConcept", self.js)


class CreditsDialogTests(unittest.TestCase):
    def setUp(self):
        self.html = source("index.html")
        self.css = source("style.css")
        self.js = source("script.js")

    def test_credits_button_and_dialog_markup(self):
        for fragment in (
            'id="credits-button"',
            'aria-haspopup="dialog"',
            'aria-controls="credits-dialog"',
            'aria-label="المطورين"',
            '<dialog id="credits-dialog"',
            'id="credits-title"',
            'id="credits-close"',
        ):
            self.assertIn(fragment, self.html, fragment)
        self.assertRegex(self.html, r'<dialog[^>]*class="[^"]*\bno-print\b')
        self.assertRegex(self.html, r'<button[^>]*id="credits-button"[^>]*class="[^"]*\bbrutal-button\b')

    def test_credits_copy_names_and_charitable_work(self):
        for copy in (
            "المطورين",
            "الشكر والتقدير",
            "حسام بن محمد بن العبري",
            "محمد بن نعيم الفارسي",
            "عملاً خيرياً",
            "جامعة السلطان قابوس",
            "SQU",
            "المهارات الدراسية والحياتية",
        ):
            self.assertIn(copy, self.html, copy)

    def test_credits_reuses_pinned_visual_system(self):
        for selector in (".credits-button", ".credits-dialog", ".credits-names", ".credits-note", ".credits-course"):
            self.assertIn(selector, self.css, selector)
        self.assertIn(".api-key-dialog, .credits-dialog", self.css)
        self.assertIn("box-shadow: 8px 8px 0 #17151b", self.css)
        self.assertNotIn("clip-path: inset(50%)", self.css)

    def test_credits_dialog_open_and_close(self):
        self.assertIn('const creditsButton = byId("credits-button");', self.js)
        self.assertIn('const creditsDialog = byId("credits-dialog");', self.js)
        self.assertIn('creditsButton.addEventListener("click"', self.js)
        self.assertIn("creditsDialog.showModal()", self.js)
        self.assertIn('byId("credits-close").addEventListener("click"', self.js)
        self.assertIn("creditsDialog.close()", self.js)


if __name__ == "__main__":
    unittest.main()

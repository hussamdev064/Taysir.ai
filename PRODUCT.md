# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML5, CSS, vanilla JavaScript, and Tailwind CSS via CDN, confirmed by the user. No package-manager build step. Google Gemini supplies branding generation through its API.

## Users

Arabic-speaking students building startups and productive families establishing small businesses. They begin with a project idea and need an accessible starting point for a visual identity without hiring a designer.

## Product Purpose

Taysir.ai (تيسير.ai) turns an Arabic project description into a starting visual-brand identity: a verbal slogan, a 3–4 color palette with names and HEX values, a detailed visual logo concept, and 3–4 titled project ideas with one concrete suggestion each. Success is a complete identity the user can copy, open in Coolors for palette refinement, browse Pinterest logo references based on the same prompt, or save as a PDF through browser printing.

## Positioning

A free, natively Arabic, single-page branding tool powered by Gemini, focused on the stated student-startup and productive-family audiences rather than a generic English-first design workflow.

## Operating Context

The user enters a description or selects one of three Arabic suggestions, optionally pastes a Gemini API key through the header dialog, requests generation, waits for Gemini, reviews four result cards, copies individual outputs, opens the generated palette in Coolors, opens prompt-based Pinterest logo references from the logo card, and optionally saves the cards through the browser's print/PDF flow. A pasted key is held only in the current page's JavaScript memory and is never placed in either external URL. V1 is a local/demo static deployment because its Gemini key lives in browser JavaScript.

## Capabilities and Constraints

- Arabic RTL single-page interface with the exact copy and workflows in `the_prompt.txt`.
- Vanilla JavaScript integration with Google Gemini only, returning the specified strict JSON contract.
- Three suggestion pills, dark/light toggle, loading state, empty-input and API/parse errors, copy feedback, tactile press feedback, subtle hero wave, mouse-follow motion and touch color, Coolors deep link, Pinterest reference link, a Gemini-marked shortcut to Google AI Studio's key page inside the header dialog, a «الشكر والتقدير» button crediting the two contributors and the charitable work for the SQU project, and print-friendly output.
- GPLv3 open-source notices are required.
- `GEMINI_API_KEY` remains `YOUR_API_KEY_HERE` in source; the user may paste a real key into the header dialog for the current page only, overriding the placeholder at runtime without browser storage.
- Stable `gemini-3.8-flash` is selected from official documentation. A secure production API proxy is out of V1 scope.

## Brand Commitments

The name is `Taysir.ai` / `تيسير.ai`. The interface must be natively Arabic and use the specified paperish Neo-Brutalist identity: pastel surfaces, thick sharp black borders, and solid hard black shadows without blur. The supplied Arabic hero, control, card, loading, and error text is binding.

## Evidence on Hand

`the_prompt.txt` is the original product and visual brief; `spec/SPEC-taysir-ai.md` is its V1 specification. No testimonials, user metrics, customer claims, production deployment, image assets, or real API credentials are on hand and none should be invented.

## Product Principles

1. Make the first useful identity available with one description and one action.
2. Keep Arabic language and RTL structure native, not an afterthought.
3. Keep generated outputs understandable, copyable, and printable.
4. Fail visibly and recoverably without losing the user's project description.
5. Keep the static V1 small and within the approved Gemini scope.

## Accessibility & Inclusion

Native Arabic RTL and mobile-first responsiveness are required. No additional product-specific accessibility standard has been established.

# Portfolio Design & Cloning Instructions for Antigravity

## Objective

Build my portfolio as a **clean, highly polished, professional and stylish developer portfolio**.

The visual direction MUST be based **strictly and exclusively** on these two reference portfolios:

1. **Aarav Sharma**
   - Live site: https://aarav-sharma-liart.vercel.app/
   - Listed in the `emmabostian/developer-portfolios` repository as Aarav Sharma, described as "Founder at Wensity | Sr. design engineer | UI/UX developer in Rune."

2. **Abdul Rehman Waseem**
   - Live site: https://abdulrehmanwaseem.me/
   - GitHub: https://github.com/abdulrehmanwaseem
   - Abdul's own site states that the portfolio is a minimal, pixel-perfect developer portfolio and identifies its stack as Next.js 15, Tailwind CSS v4, and shadcn/ui.
   - His site also states that the source code is available on GitHub and is licensed under the MIT license.

## STRICT DESIGN RULE

### Use ONLY the design language of these two references.

Do **NOT** introduce unrelated design trends, templates, components, visual effects, layouts, animations, color systems, or UI patterns from other websites.

Do not "improve" the design by adding random creative elements.

Do not add:
- 3D effects unless they are genuinely part of the chosen reference direction
- excessive gradients
- glassmorphism
- random blobs
- excessive glowing effects
- generic AI-generated decorations
- floating cards that aren't supported by the references
- unnecessary particles
- excessive parallax
- flashy cursor effects
- oversized decorative illustrations
- random neon colors
- generic SaaS dashboard aesthetics
- random UI components
- unnecessary animations

**The result should feel like a carefully designed combination of Aarav Sharma + Abdul Rehman Waseem, not a third unrelated design.**

---

# Mobile-First Requirement

## IMPORTANT: Build MOBILE-FIRST.

The implementation must start from the smallest viewport and progressively enhance for larger screens.

Required priority:

1. Mobile
2. Tablet
3. Desktop
4. Large desktop

Do NOT design desktop first and then squeeze it into mobile.

### Mobile requirements

The mobile version must be a first-class design, not an afterthought.

Pay special attention to:

- typography scale
- spacing
- navigation
- project cards
- section hierarchy
- touch targets
- buttons
- text wrapping
- image/media sizing
- animation performance
- scrolling behavior
- accessibility

Avoid horizontal overflow.

Every section must remain visually intentional on small screens.

---

# Reference Analysis

Before implementing anything:

1. Visit both reference websites.
2. Inspect their layout and visual hierarchy.
3. Identify their typography characteristics.
4. Identify their spacing system.
5. Identify navigation behavior.
6. Identify project presentation.
7. Identify card styles.
8. Identify button styles.
9. Identify animation/motion behavior.
10. Identify responsive behavior.
11. Identify color usage.
12. Identify borders, shadows and radius usage.
13. Identify how sections enter/exit the viewport.
14. Identify any smooth scrolling or micro-interactions.
15. Identify the overall visual rhythm.

Then reproduce the **design principles**, not somebody else's personal content.

---

# Important: Do Not Copy Personal Content

The references are inspiration for the visual system.

Do NOT copy:

- names
- biography
- profile information
- employment history
- personal projects
- personal photographs
- social links
- email addresses
- testimonials
- proprietary content
- personal branding
- logos belonging to the reference developers

Replace all of these with my own content.

The goal is an **original portfolio using the same design direction**, not an impersonation or an exact public clone.

---

# Cloning / Reference Inspection Tools

For authorized local inspection and learning, use the following tools when appropriate.

## Option 1 — True Web Clone

GitHub:

https://github.com/SkyNotSilent/true-web-clone

This is a source-first web-cloning workflow designed to preserve real frontend assets and runtime motion. It specifically supports inspection of systems such as:

- GSAP
- ScrollTrigger
- Swiper
- Lenis
- Lottie
- Rive
- Three.js
- Canvas/WebGL
- GLB/GLTF
- WASM
- textures
- fonts
- videos
- SVG
- JSON

It uses Playwright for browser verification.

Repository:

https://github.com/SkyNotSilent/true-web-clone

Use it for **local research and authorized reconstruction**, not for bypassing authentication, paywalls, private APIs, DRM, or protected resources.

## Option 2 — Python Website Downloader

GitHub:

https://github.com/PKHarsimran/website-downloader

This is a Python-based website downloader that can render JavaScript through Playwright.

Install:

```bash
git clone https://github.com/PKHarsimran/website-downloader.git
cd website-downloader

python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Then:

```bash
pip install -e ".[render]"
playwright install chromium
```

For a JavaScript-rendered site:

```bash
website-downloader \
  --url https://example.com \
  --destination example_backup \
  --render-js
```

For the two reference sites, use the downloader only as a **reference/inspection tool**. Do not blindly publish copied proprietary assets or personal content.

---

# Reference URLs

## Aarav Sharma

Live portfolio:

https://aarav-sharma-liart.vercel.app/

Official listing:

https://github.com/emmabostian/developer-portfolios/blob/master/feed.json

## Abdul Rehman Waseem

Live portfolio:

https://abdulrehmanwaseem.me/

GitHub profile:

https://github.com/abdulrehmanwaseem

Portfolio source information:

https://abdulrehmanwaseem.me/blog/welcome

---

# Implementation Direction

Use a modern component-based frontend.

Preferred direction:

- Next.js
- TypeScript
- Tailwind CSS
- shadcn/ui only where it naturally fits the reference design
- Framer Motion / Motion or GSAP only when needed for the reference-style motion
- semantic HTML
- accessible interactions
- responsive design
- optimized images
- optimized fonts
- good SEO

Do NOT add a dependency simply because it is popular.

Every dependency must have a reason.

---

# Animation & Motion Rules

Animations should be:

- subtle
- purposeful
- smooth
- premium
- fast enough to feel responsive
- consistent with the two references

Avoid animation overload.

Do NOT animate everything.

Use motion primarily for:

- page/section entrance
- hover states
- navigation transitions
- project interactions
- subtle scrolling effects
- meaningful micro-interactions

Animation should never interfere with reading or navigation.

Respect:

```css
prefers-reduced-motion
```

---

# Visual Quality Rules

The final portfolio should communicate:

**clean + premium + technical + modern + personal**

It should NOT communicate:

**template + generic + over-designed + AI-generated + flashy**

Whitespace is important.

Typography is important.

Alignment is important.

Consistency is important.

Do not fill empty space just because it exists.

---

# Content Structure

Use a clear portfolio hierarchy.

Suggested structure:

1. Hero
2. Short introduction
3. Selected work/projects
4. Skills / technologies
5. Experience or education
6. Additional work / achievements
7. About
8. Contact
9. Footer

However, the exact section ordering should be adapted to the **visual hierarchy of the two references**.

Do not blindly follow this list if it conflicts with the reference designs.

---

# Quality Gate

Before considering the implementation finished, verify:

### Design

- [ ] Looks clearly inspired by Aarav Sharma
- [ ] Looks clearly inspired by Abdul Rehman Waseem
- [ ] No unrelated visual style has been introduced
- [ ] No unnecessary decorative elements
- [ ] Typography is polished
- [ ] Spacing is consistent
- [ ] Visual hierarchy is clear

### Mobile

- [ ] Mobile-first implementation
- [ ] No horizontal overflow
- [ ] Navigation works perfectly
- [ ] Touch targets are comfortable
- [ ] Typography remains readable
- [ ] Projects work correctly
- [ ] Animations remain smooth
- [ ] No desktop layout simply squeezed onto mobile

### Desktop

- [ ] Desktop layout feels intentional
- [ ] Content width is controlled
- [ ] Whitespace is balanced
- [ ] Animations remain subtle
- [ ] No unnecessary empty areas

### Technical

- [ ] Fast initial load
- [ ] Optimized assets
- [ ] No unnecessary dependencies
- [ ] No console errors
- [ ] No broken links
- [ ] Accessible keyboard navigation
- [ ] Reduced-motion support
- [ ] Good semantic HTML
- [ ] SEO metadata implemented

---

# FINAL INSTRUCTION TO ANTIGRAVITY

**Do not invent a new visual style.**

Treat the Aarav Sharma and Abdul Rehman Waseem portfolios as the **only two visual references allowed**.

Study them carefully first.

Then create an **original, mobile-first portfolio** that combines their strongest design characteristics while using completely original content and branding.

If a proposed design element cannot be justified by one of these two references, **do not add it.**

When uncertain, choose the **simpler, cleaner option**.

The final result should look like:

> **A premium portfolio designed by someone with excellent taste — not a portfolio template.**

And above everything:

> **MOBILE FIRST. CLEAN. STYLISH. PROFESSIONAL. NOTHING EXTRA.**

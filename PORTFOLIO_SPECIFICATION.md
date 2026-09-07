# Portfolio Specification & Master Record

> **Notice:** This document is the permanent single source of truth for **MD Zihaduzzaman's Portfolio**. All personal details, design extractions, architecture decisions, and styling guidelines are preserved here.

---

## 1. Developer Profile & Personal Information

* **Full Name:** MD Zihaduzzaman
* **Primary Roles / Titles:** 
  * Full-Stack Web Developer & Software Engineer
  * Aspiring Data Engineer (Actively learning Data Engineering pipelines, distributed systems & ETL)
* **Current Academic Status:** 
  * B.Sc. in Software Engineering (2nd Year Undergraduate)
* **Academic Honors & Excellence:**
  * **HSC (Higher Secondary Certificate):** Golden GPA 5.00
  * **SSC (Secondary School Certificate):** Golden GPA 5.00
* **Location:** Dhaka, Bangladesh (Timezone: Asia/Dhaka, GMT+6)
* **Availability:** Open for High-Impact Software Engineering Roles, Full-Stack Development, and Data Engineering Internships/Collaborations.

---

## 2. Design System: Synthesis of Two Strict References

Per project rules, **no third-party unrelated styles, 3D canvases, excessive glassmorphism blur, or flashy decorations are allowed**. The portfolio is a clean, minimal, mobile-first blend of:

### Reference A: Aarav Sharma (`https://aarav-sharma-liart.vercel.app/`)
* **Cover Landscape Banner:** Clean architectural/dark landscape with an italic centered motto: *"Engineering reliable systems, analyzing deep data, and refining every detail."*
* **Avatar Presentation:** Circular portrait overlapping the banner bottom edge (`-mt-10`, `w-24 h-24 sm:w-28 sm:h-28`), framed with a crisp border ring.
* **Featured Projects (Proof of Work):** 2-column visual grid (`grid-cols-1 sm:grid-cols-2`), 4:3 preview ratio, title badge, subtle image zoom/translate on hover, concise description, and inset-bordered tech pill tags.
* **Separators:** Subtle dashed dividers (`border-b border-dashed border-zinc-200 dark:border-zinc-800`).
* **Micro-interactions:** Smooth GPU-accelerated hover states (`hover:-translate-y-0.5`).

### Reference B: Abdul Rehman Waseem (`https://abdulrehmanwaseem.me/`)
* **Framed Container Structure:** Centered max-width column (`max-w-3xl`) bounded by continuous vertical border edges (`border-x border-zinc-200 dark:border-zinc-800`).
* **Blueprint Technical Dividers:** Hatched divider strips (`h-6` to `h-8`) with repeating diagonal 45° stripes (`bg-[repeating-linear-gradient(315deg,...)]`).
* **Header Bar:** Sticky top navigation with minimalist site mark, section shortcuts, theme toggle (Dark/Light), and command hint (`Ctrl+K` / `⌘K`).
* **Quick-Info Matrix:** 2-column key-value grid under the hero (Location, Dhaka live clock, academic stage, GitHub/LinkedIn links).
* **Technical Stack:** Categorized icon grid with clean devicons and tooltips.
* **Experience & Education:** Vertical tree timeline with node dots and collapsible accordions.
* **Social Cards:** 2-column grid cards with platform logo, handle, and arrow-up-right link.

---

## 3. Technology Stack & Zero-Lag Architecture

* **Framework:** **Astro 5.x**
  * Outputs 100% static HTML & CSS at build time.
  * 0 kB client-side JavaScript baseline (Islands Architecture).
  * 0 ms Total Blocking Time (TBT) on low-end mobile devices.
* **Styling:** **Tailwind CSS v4**
  * Zero-runtime atomic CSS.
* **Icons:** **Lucide Icons** + inline optimized SVG logos (0 font-loading delay).
* **Animations:**
  * Only composite properties: `transform` (using 3D transforms) and `opacity`.
  * No heavy `backdrop-filter: blur()`.
  * Native `IntersectionObserver` for viewport reveal triggers.
* **Hosting:** **cPanel Ready**
  * Running `npm run build` generates a `dist/` directory with pure static assets ready to upload directly into `public_html/`.

---

## 4. Portfolio Section Architecture

1. **Header Navigation:** Sticky bar with brand mark, anchor navigation links (`About`, `Projects`, `Stack`, `Experience`, `Education`, `Contact`), and Dark/Light mode toggle.
2. **Hero Section:**
   - Landscape banner with inspirational quote.
   - Circular avatar with verified engineer badge.
   - Name: MD Zihaduzzaman.
   - Title: Full Stack Web Developer & Software Engineer | Learning Data Engineering.
   - Quick Info Matrix:
     - 🎓 2nd Year Software Engineering
     - 🏆 Golden GPA 5.00 in both SSC & HSC
     - 📍 Dhaka, Bangladesh
     - 🕒 Live Dhaka Local Clock
3. **About Section:** Narrative on building scalable full-stack applications, problem-solving, and pursuing data engineering systems.
4. **Featured Projects ("Proof of Work"):** 2-column card grid showcasing flagship full-stack & data engineering projects with GitHub & live preview links.
5. **Tech Stack:** Categorized grid:
   - Languages: JavaScript, TypeScript, Python, SQL, C/C++
   - Frontend: React, Astro, Next.js, Tailwind CSS, HTML5/CSS3
   - Backend & Database: Node.js, Express, PostgreSQL, MongoDB, Redis, Prisma
   - Data Engineering & Tools: Python Data Stack (Pandas, NumPy), Git, Docker, Linux, Postman
6. **Experience & Leadership:** Timeline with role, dates, key contributions, and tech tags.
7. **Education & Academic Honors:**
   - B.Sc. in Software Engineering (2nd Year, Ongoing)
   - Higher Secondary Certificate (HSC) — Golden GPA 5.00
   - Secondary School Certificate (SSC) — Golden GPA 5.00
8. **Certifications & Achievements:** Hackathons, technical credentials, problem-solving milestones.
9. **Socials & Contact:** 2-column clean card grid (LinkedIn, GitHub, Email, Discord/Telegram).
10. **Footer:** Technical blueprint footer with copyright and back-to-top button.
11. **Interactive Physics Pull Cord (Abdul Rehman Waseem Component):**
   - Direct reference: `https://github.com/abdulrehmanwaseem/My-Portfolio` (`src/components/pull-cord-theme.tsx`).
   - 16-node Verlet particle physics rope engine with 20 distance-constraint relaxation passes per frame.
   - Smooth midpoint quadratic bezier curve (`M x0 y0 Q xi yi xc yc ... L xn yn`).
   - Natural gravity entrance drop animation with momentum injection into rope physics.
   - Taut mechanical limit (26px max stretch) with 20px trigger threshold and velocity capping.
   - Mechanical click audio playback (`/audio/ui-sounds/click.wav`) with Web Audio and haptic vibration fallback.
   - Hand-drawn "pull the cord!" SVG curved arrow with Google Font `Caveat`.
12. **Header & Navigation:**
   - ZIHAD custom monogram SVG logo (`viewBox="0 0 256 128"`) adapting to light/dark themes.
   - Clean, uncluttered navbar with direct "Download CV" action button.
13. **Continuous Dynamic Role Rotator:**
   - Smooth vanilla JS typing ticker cycling through:
     * Full Stack Developer
     * Software Engineer
     * Mobile App Developer
     * Data Engineer
     * Problem Solver
     * Algorithmist
14. **QuickInfo / Bio Data Grid (Abdul Rehman 1:1 Layout):**
   - Dark rounded-square icon badges (`</>`, 💡, ♂, 📍, 🕒, 📞, ✉, 🌐).
   - 2-column key-value pairs with live Dhaka clock (`GMT+6`).

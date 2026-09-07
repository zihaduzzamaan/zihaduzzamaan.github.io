# Project Roadmap & Progress Tracker

**Project:** MD Zihaduzzaman — High-Performance Static Developer Portfolio  
**Stack:** Astro 5.x + Tailwind CSS v4 + TypeScript + Hardware-Accelerated CSS  
**Target:** 100/100 Lighthouse Performance, 0 ms Total Blocking Time, cPanel Deployable  
**Last Updated:** 2026-09-07

---

## 📌 Phase Overview & Status

| Phase | Description | Status |
| :--- | :--- | :--- |
| **Phase 0** | Context extraction, specification documentation & reference analysis | ✅ Completed |
| **Phase 1** | Astro Project Scaffolding with Tailwind CSS v4 & Lucide Icons | ✅ Completed |
| **Phase 2** | Design Tokens & Global CSS (Dark/Light mode, hatched line patterns) | ✅ Completed |
| **Phase 3** | Core Layout, Sticky Header & Minimalist Theme Switcher | ✅ Completed |
| **Phase 4** | Hero Section, Banner, Avatar, & Live Dhaka Time Matrix | ✅ Completed |
| **Phase 5** | About & Narrative Section | ✅ Completed |
| **Phase 6** | Featured Projects Grid (Aarav Sharma 2-column aesthetic) | ✅ Completed |
| **Phase 7** | Tech Stack Grid (Abdul Rehman categorized layout) | ✅ Completed |
| **Phase 8** | Experience & Timeline Section (Connected tree) | ✅ Completed |
| **Phase 9** | Education & Academic Honors (Software Engineering 2nd Year, Golden GPA 5.00) | ✅ Completed |
| **Phase 10** | Certifications, Achievements & Honors | ✅ Completed |
| **Phase 11** | Contact & Social Cards Grid | ✅ Completed |
| **Phase 12** | Footer, SEO Meta Tags, and Scroll-to-Top | ✅ Completed |
| **Phase 13** | Zero-Lag Validation: 0 kB Framework JS runtime, 0 ms TBT | ✅ Completed |
| **Phase 14** | Production Build (`npm run build`) & cPanel Static Bundle in `dist/` | ✅ Completed |
| **Phase 15** | Exact 16-Node Verlet Rope Physics from Abdul Rehman's Repo | ✅ Completed |

---

## 🛠️ Completed Component Inventory

* [Layout.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/layouts/Layout.astro): Full SEO tags, Open Graph, instant dark/light theme loader, root mounting of interactive physics pull cord.
* [Header.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/Header.astro): Sticky navigation bar with monogram brand mark and mobile scroll navigation.
* [ThemeToggle.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/ThemeToggle.astro): Instant dark/light mode toggle with `localStorage` persistence.
* [PullCord.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/PullCord.astro): **Abdul Rehman Waseem's exact interactive physics pull cord** (`https://github.com/abdulrehmanwaseem/My-Portfolio/blob/main/src/components/pull-cord-theme.tsx`). Built with an authentic 16-node Verlet integration engine, 20 relaxation passes per frame, quadratic midpoint bezier smoothing, gravity entrance drop with momentum transfer, mechanical taut stretch limits, real click sound (`/audio/ui-sounds/click.wav`), and authentic "pull the cord!" SVG curved arrow with Google Font `Caveat`.
* [Hero.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/Hero.astro): Landscape cover banner with centered motto, overlapping avatar, verified developer badge, and quick action buttons.
* [QuickInfo.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/QuickInfo.astro): 2-column metadata matrix featuring Software Engineering 2nd Year, Golden GPA 5.00, and Live Dhaka Clock.
* [SectionDivider.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/SectionDivider.astro): Abdul Rehman's signature 45° diagonal hatched spacer bar.
* [About.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/About.astro): Lead thesis statement with structured engineering bullet cards.
* [Projects.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/Projects.astro) & [ProjectCard.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/ProjectCard.astro): Aarav Sharma's 2-column showcase with 4:3 preview frame, floating badge, and tech tags.
* [TechStack.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/TechStack.astro): Categorized grid of tools with micro-hover scale.
* [Experience.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/Experience.astro): Vertical connected timeline tree with active pulse node dot.
* [Education.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/Education.astro): Prominently displaying 2nd Year SE and Golden GPA 5.00 in SSC & HSC.
* [Certifications.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/Certifications.astro): Verification badges for hackathons and credentials.
* [SocialLinks.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/SocialLinks.astro): 2-column social card links (GitHub, LinkedIn, Email, Telegram/Discord).
* [Footer.astro](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/components/Footer.astro): Minimalist blueprint footer with smooth back-to-top button.
* [portfolioData.ts](file:///c:/Users/ZISHAN/Downloads/Desktop/WORK/PORTFOLIO/src/data/portfolioData.ts): Single source of truth for all content.

---

## ⚡ Key Commands

```bash
# Start development server
npm run dev

# Build production static bundle for cPanel
npm run build

# Preview production build locally
npm run preview
```

---

## 📦 How to Deploy to cPanel

1. Run `npm run build` (already tested and verified!).
2. In your file explorer, go to `c:\Users\ZISHAN\Downloads\Desktop\WORK\PORTFOLIO\dist`.
3. Select all files and folders inside `dist/` (`index.html`, `_astro/`, `favicon.svg`) and create a `.zip` archive.
4. Log into your **cPanel**.
5. Open **File Manager** and navigate to `public_html/`.
6. Click **Upload**, select your zip file, and extract it directly into `public_html/`.
7. Your portfolio is instantly live!

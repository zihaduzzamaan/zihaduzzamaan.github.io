# Portfolio Banner & Mockup Generators 🎨

This directory contains automated Python scripts that generate production-grade, 16:9 widescreen showcase banners and UI mockups for the portfolio projects.

---

## 📁 Directory Structure & Scripts Overview

```text
scripts/
├── build_refc_banner.py                 # Quad-screen 16:9 banner generator for REFC Online
├── build_attenvo_banner.py              # 16:9 high-res banner generator for Attenvo Edge AI
├── render_mockups.py                   # Vector UI mockups generator for system/web projects
├── generate_realistic_contributions.cjs # Multi-year GitHub contribution graph data generator
└── README.md                            # Complete documentation (this file)
```

---

## 🛠️ Prerequisites

All scripts run on **Python 3.8+** with the standard **Pillow (PIL)** library:

```bash
pip install pillow
```

> **Note on Fonts**: The scripts automatically probe standard Windows fonts (`Segoe UI`, `Segoe UI Bold`, `Consolas`, `Arial`). If running in a headless Linux/CI environment, PIL automatically falls back to its default font bitmap without crashing.

---

## 🚀 How to Run

You can run individual scripts or regenerate all project banners in one go from the project root:

### Run All Generators:
```powershell
python scripts/build_refc_banner.py
python scripts/build_attenvo_banner.py
python scripts/render_mockups.py
```

### Run an Individual Generator:
```powershell
# Regenerate REFC banner (1920x1080)
python scripts/build_refc_banner.py

# Regenerate Attenvo banner (1920x1080)
python scripts/build_attenvo_banner.py

# Regenerate other project mockups (1200x675)
python scripts/render_mockups.py
```

---

## 📄 Script-by-Script Technical Documentation

### 1. `build_refc_banner.py`
* **Target Output**: `public/projects/refc.jpg`
* **Aspect Ratio**: `16:9` (1920 × 1080 Full HD)
* **Project**: **REFC Online: Automated Esports Tournament Platform**

#### Features & Composition Architecture:
1. **Multi-Screen Staggered Layout**:
   - Integrates **all 4 authentic project screenshots** from `public/Project_Images/Refc/`:
     1. `WhatsApp Image ... AM3.jpeg`: Tournament Hub & dynamic banner (`refc.online/tournament-hub`)
     2. `WhatsApp Image ... AM11.jpeg`: Live Club Standings & Points Table (`refc.online/standings`)
     3. `WhatsApp Image ... AM1.jpeg`: Match Schedules & Score Submissions (`refc.online/matches`)
     4. `WhatsApp Image ... AM.jpeg`: Admin Control Hub showing real revenue **৳56,930** (`refc.online/admin/overview`)
2. **Browser Chrome & Elevation**:
   - Encapsulates every screenshot in a sleek dark browser window frame (`#0b0f19`) complete with red/amber/emerald traffic light controls and simulated URL address pills with security locks.
   - Computes realistic multi-stage Gaussian drop shadows (`blur_radius=35-40px`) to give each window floating depth.
3. **Typography & Brand Identity**:
   - Incorporates the transparent REFC brand logo floating naturally on the dark canvas without an artificial background box.
   - Headline: *"Automated Esports Tournament Platform"* with electric cyan accent (`#38bdf8`).
   - 4 technical feature cards with custom vector icons (Lightning bolt, Trophy, Bar Chart, Security Shield).
   - Live production verification pill (`LIVE PRODUCTION: 1,180+ PLAYERS • 21 TOURNAMENTS • BDT 56K+ REVENUE`).
   - Visual workflow pipeline (`Match Report → Instant Tiebreaker → Auto Bracket Advancement`).

---

### 2. `build_attenvo_banner.py`
* **Target Output**: `public/projects/attenvo.jpg`
* **Aspect Ratio**: `16:9` (1920 × 1080 Full HD)
* **Project**: **Attenvo: High-Performance Edge AI Facial Attendance**

#### Problem Solved:
- The raw showcase graphic was formatted at `1024 × 682` (1.50:1 aspect ratio). In a responsive 16:9 card, this caused the top of the phones and bottom handwritten text to be cropped off by ~16%.
- `build_attenvo_banner.py` embeds the showcase graphic into a native 16:9 widescreen canvas (`1920 × 1080`) with generous breathing room and zero cropping.

#### Features & Composition Architecture:
1. **Mathematical Wave Slope Continuation**:
   - Attenvo's signature pastel branding features a decorative lavender wave swooping behind the phones that exits the right border at an angle.
   - The script calculates the trajectory slope (`dx/dy ≈ 0.685`) and dynamically extends the lavender gradient from `(1771, 554)` to `(1920, 656)`.
2. **Seamless Edge Blending**:
   - The left boundary transitions flawlessly into the off-white `#f9fafe` tone.
   - The right seam uses a Gaussian anti-aliasing strip so that the extended wave feels completely organic with zero visual seams or hard borders.
3. **Complete Content Integrity**:
   - Preserves 100% of all 4 mobile phone mockups (Scanner camera preview, Section Students, Section Courses, and Attendance History).
   - Retains the full Attenvo logo, typography, feature badges, and handwritten notes.

---

### 3. `render_mockups.py`
* **Target Output**:
  - `public/projects/campus_welfare.jpg` (1200 × 675)
  - `public/projects/roadmap_tracker.jpg` (1200 × 675)
  - `public/projects/hardware_suite.jpg` (1200 × 675)
* **Aspect Ratio**: `16:9` (1.778 ratio)
* **Projects**:
  - **University Student Welfare & Mentorship Portal**
  - **Roadmap & Daily Habit Tracker**
  - **Desktop Hardware & Audio Utilities Suite**

#### Features & Composition Architecture:
1. **Native Dark Theme UI Architecture**:
   - Programmatically renders clean application windows with title bars, system status dots, and subtle borders matching the portfolio's palette (`#0a0f1a`, `#0c0a18`, `#0a0f12`).
2. **CampusCare Portal**:
   - Faculty mentor directory with real DIU professor cards, avatar indicators, and availability status.
   - Meeting booking interface with date/time selectors, agenda tags, and confirmed appointment cards.
3. **DevRoadmap & Habit Tracker**:
   - 3-column dashboard featuring active roadmaps (Full-Stack, Data Eng, Algorithms) with progress bars.
   - 52-week habit streak commit matrix with varying activity heatmaps.
   - Daily milestone checklist with completed and pending task states.
4. **Hardware & Audio Utilities Suite**:
   - Parametric audio equalizer window with 10-band interactive frequency sliders and DSP convolution stream status.
   - Dual-monitor DDC/CI hardware brightness, contrast, and color temperature controller (Primary gaming panel + vertical reading panel).

---

## 📐 Image Specification Standard

| Asset | Source File | Dimensions | Aspect Ratio | Format |
|---|---|---|---|---|
| `refc.jpg` | `scripts/build_refc_banner.py` | `1920 × 1080` | `16:9` | JPEG (Quality 95) |
| `attenvo.jpg` | `scripts/build_attenvo_banner.py` | `1920 × 1080` | `16:9` | JPEG (Quality 96) |
| `campus_welfare.jpg` | `scripts/render_mockups.py` | `1200 × 675` | `16:9` | JPEG (Quality 95) |
| `roadmap_tracker.jpg` | `scripts/render_mockups.py` | `1200 × 675` | `16:9` | JPEG (Quality 95) |
| `hardware_suite.jpg` | `scripts/render_mockups.py` | `1200 × 675` | `16:9` | JPEG (Quality 95) |
| `piecestyle.jpg` | Pre-rendered | `1376 × 768` | `16:9` | JPEG (Quality 95) |

Every banner in `public/projects/` is strictly calibrated for CSS `aspect-video` (16:9), ensuring clean edge-to-edge presentation on mobile, tablet, and ultra-wide displays.

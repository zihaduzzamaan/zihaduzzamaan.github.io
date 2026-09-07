# Engineering Case Studies: Flagship Systems

*Technical breakdown, architectural decisions, and performance benchmarks for production systems engineered by MD Zihaduzzaman.*

---

## 1. REFC Online (`refc.online`)
### Production Automated eFootball Tournament & Esports Platform

| Metric | Detail |
| :--- | :--- |
| **Status** | Live in Production (`https://refc.online`) |
| **Role** | Full-Stack Developer & Systems Architect (Remote) |
| **Timeline** | 2024 - Present |
| **Core Stack** | React, PHP, MySQL/Storage Engine, Automated Data Pipelines |

### 1.1 Problem Statement & Background
Managing competitive esports tournaments for *eFootball* involves significant manual administrative overhead: tracking hundreds of participants, generating single-elimination/double-elimination and round-robin group brackets, calculating goal differences, tracking disciplinary records, and resolving score disputes. Manual scorekeeping across spreadsheets leads to human error, delayed fixtures, and poor player experience.

### 1.2 System Architecture
```
┌──────────────────────────────────────────────────────────┐
│                   React Frontend UI                      │
│   (Interactive Brackets, Live Standings, Match Hub)      │
└────────────────────────────┬─────────────────────────────┘
                             │ REST API / JSON
┌────────────────────────────▼─────────────────────────────┐
│                    PHP Backend Core                      │
│   (Auth, Business Logic, Validation, Storage Handling)   │
└────────────────────────────┬─────────────────────────────┘
                             │
        ┌────────────────────┴────────────────────┐
        ▼                                         ▼
┌───────────────────────────────┐   ┌──────────────────────────────┐
│   Automated Data Pipelines    │   │      Relational Storage      │
│ (Tiebreakers, Goal Difference,│   │  (Players, Matches, Brackets,│
│  Standings & Seeding Engine)  │   │       Historic Stats)        │
└───────────────────────────────┘   └──────────────────────────────┘
```

### 1.3 Key Features & Engineering Implementations
- **Multi-Format Tournament Engine**: Supports solo (1v1), team/group stages, knockout brackets, and hybrid league-into-playoffs formats.
- **Automated Results Pipeline**: When match scores are submitted, automated triggers recalculate points, goal differentials, head-to-head records, and advance winners into subsequent bracket nodes without admin intervention.
- **Dynamic Seeding**: Algorithmic seeding prevents top-tier players from meeting in early rounds based on historical performance data.
- **Low-Latency Dashboard**: Fast-loading participant portal built with React for instant match discovery and real-time standing updates.

---

## 2. Attenvo
### High-Performance On-Device Facial Recognition System: Kotlin Native vs. React Web

| Metric | Detail |
| :--- | :--- |
| **Product Name** | **Attenvo** |
| **Category** | Computer Vision & Edge AI Attendance System |
| **Core Models** | Python InsightFace (ArcFace / RetinaFace 512D embeddings) |
| **Client Platforms** | Native Android (Kotlin) & Web Client (React) |
| **Architecture** | On-Device Local Inference (Privacy-Preserving Edge Computing) |

### 2.1 The Architectural Challenge: Web vs. Native
The system was originally prototyped as a web application using React. However, extracting high-framerate video frames through the browser canvas and communicating with local Python inference bridges introduced perceptible latency, frame drops, and browser memory pressure.

To achieve industrial-grade attendance scanning (sub-second recognition per user in real-time queues), the client layer was re-architected in **Native Kotlin**:

```
[ Camera Stream ]
       │
       ▼
[ Frame Pipeline ] ──► [ RetinaFace Detection ] ──► [ ArcFace 512D Embeddings ]
                                                           │
                                                           ▼
                                               [ Cosine Similarity Match ]
                                               (Threshold: cosine >= 0.68)
                                                           │
                                                           ▼
                                               [ Instant Attendance Logged ]
```

### 2.2 Benchmarks & Architectural Decisions

| Feature | React Web Client | Native Kotlin Client | Performance Impact |
| :--- | :---: | :---: | :--- |
| **Inference Latency** | ~650ms to 1.1s | **~85ms to 140ms** | **~8x Faster** on mobile hardware |
| **Frame Rate** | 8-12 FPS (Jittery) | **30+ FPS (Silky)** | Smooth real-time facial bounding box tracking |
| **Hardware Access** | Sandbox / Canvas APIs | Native CameraX & NPU/GPU | Direct buffer access without base64 transcoding |
| **Memory Footprint** | Heavy (V8 + Canvas) | **Lightweight Native Process** | Eliminates browser tab crashes under sustained load |

### 2.3 Core Engineering Accomplishments
- **Zero-Cloud Privacy Architecture**: Biometric face vectors are computed and matched strictly **on the edge (user device)**. No raw facial images are ever uploaded to a remote cloud server, guaranteeing complete privacy compliance.
- **High-Dimensional Vector Comparison**: Faces are mapped into a 512-dimensional embedding space using InsightFace. Fast nearest-neighbor vector comparison enables instant authentication even under variable lighting and head poses.
- **Pragmatic Engineering Conviction**: Proved technical maturity by identifying the performance ceiling of web-based computer vision and engineering a native Kotlin replacement to solve real-world latency bottlenecks.

---

## 3. University Student Welfare & Faculty Counselling Portal
### Centralized Campus Support, FAQ Knowledge Base & Teacher-Student Mentorship System

| Metric | Detail |
| :--- | :--- |
| **Category** | Campus Web Application & Welfare Infrastructure |
| **Target Users** | University Students, Faculty Advisors & Department Counsellors |
| **Core Stack** | React, Responsive Component Architecture, State Management, REST APIs |

### 3.1 Problem Statement & Solution
University students frequently face academic stress, course selection friction, and administrative barriers without direct access to faculty guidance. Information is often scattered across physical notice boards and disconnected emails.

This platform centralizes student welfare into a single, intuitive portal:
- **Interactive Knowledge Base & FAQ Engine**: Instant-search access to academic guidelines, exam policies, welfare resources, and campus procedures.
- **Faculty Counselling & Mentorship Scheduler**: Direct 1-on-1 appointment booking system connecting students with designated teachers and advisors for academic and personal counselling.
- **Real-Time Availability & Status Tracking**: Transparent slot management preventing double-bookings and keeping students informed about session confirmations.

---

## 4. PieceStyle E-Commerce Platform
### Full-Stack Retail & E-Commerce Web Application (React & PHP)

| Metric | Detail |
| :--- | :--- |
| **Product Name** | **PieceStyle** |
| **Role** | Full-Stack Developer (Remote) |
| **Timeline** | 2023 - 2025 |
| **Core Stack** | React, PHP, MySQL, REST APIs, Tailwind CSS |

### 4.1 Platform Overview & Commercial Architecture
PieceStyle is a full-stack commercial e-commerce platform engineered from the ground up to provide a smooth, low-latency shopping experience:
- **Interactive Product Catalog**: Fast filtering by categories, tags, sizes, and price ranges with instant client-side updates.
- **Cart & Checkout Engine**: Persistent session cart handling, coupon/discount validation, and streamlined multi-step checkout.
- **Admin & Inventory Control**: Backend admin panel in PHP for real-time stock management, order status tracking (Pending, Dispatched, Delivered), and customer transaction logs.
- **Secure Backend Endpoints**: Custom PHP REST endpoints managing database CRUD operations, data sanitization, and payment verification.

---

## 5. Python Desktop Automation & Hardware Utilities
### Low-Level Audio Enhancement & Multi-Monitor Display Calibration Tools

| Metric | Detail |
| :--- | :--- |
| **Category** | Windows System Utilities & Hardware Automation |
| **Technologies** | Python, Equalizer APO Config Engine, DDC/CI & Win32 APIs |
| **Scope** | Audio Processing & Hardware Display Control |

### 5.1 Audio Enhancer with Equalizer APO
A specialized Python automation utility interfacing with Windows Audio Processing Objects (Equalizer APO):
- **Dynamic Parametric EQ Curve Generator**: Automates frequency response calibration, preamp gains, and acoustic profile switching.
- **Acoustic Presets**: Real-time hotkey toggling between neutral studio monitoring, bass enhancement, and voice clarity presets without manual file editing.

### 5.2 Monitor Visual Controller
A lightweight desktop controller for external monitors utilizing DDC/CI (Display Data Channel / Command Interface) and Win32 display APIs:
- **Hardware-Level Display Control**: Directly controls physical monitor brightness, contrast, and RGB color temperature over I2C/VCP without touching physical hardware buttons.
- **Automated Circadian Tinting**: Scripted color profile shifting to reduce eye strain during extended night coding sessions.

---

## 6. Automated Roadmap & Daily Habit Engine
### Web Scraping Curriculum Decomposer & Productivity Tracker (JavaScript, HTML5, CSS3)

| Metric | Detail |
| :--- | :--- |
| **Category** | Productivity Web Application & Data Scraper |
| **Technologies** | Vanilla JavaScript (ES6+), HTML5, CSS3, DOM & Storage APIs |
| **Scope** | Curriculum Ingestion & Habit Formation |

### 6.1 System Overview & Architecture
An end-to-end learning tracker that bridges the gap between long-term technical roadmaps and daily execution:
- **Roadmap Ingestion & Scraping**: Automatically extracts and parses developer roadmap milestones from online sources into structured JSON learning trees.
- **Daily Task Deconstruction**: Converts complex multi-month milestones into manageable, day-by-day actionable to-do items.
- **Dual Habit & Progress Loop**: Merges roadmap tasks with daily habit tracking (streaks, coding practice, study intervals) stored with zero external dependencies via browser persistence.

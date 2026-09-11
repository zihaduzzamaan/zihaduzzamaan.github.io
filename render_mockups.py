




import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 675

def get_font(name="segoeui.ttf", size=18):
    font_paths = [
        f"C:/Windows/Fonts/{name}",
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/consola.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_window_frame(draw, title="Application Hub"):
    # Header bar
    draw.rectangle([(0, 0), (W, 46)], fill=(15, 23, 42))
    draw.line([(0, 46), (W, 46)], fill=(30, 41, 59), width=1)
    # Window dots
    draw.ellipse([(20, 16), (32, 28)], fill=(239, 68, 68))
    draw.ellipse([(40, 16), (52, 28)], fill=(245, 158, 11))
    draw.ellipse([(60, 16), (72, 28)], fill=(16, 185, 129))
    # Title
    f_title = get_font("segoeuib.ttf", 14)
    draw.text((88, 14), title, fill=(203, 213, 225), font=f_title)

# 1. CAMPUS WELFARE & COUNSELLING
def make_campus_welfare():
    img = Image.new("RGB", (W, H), (10, 15, 26))
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, "CampusCare • University Student Welfare & Counselling Infrastructure")

    # Fonts
    f_h1 = get_font("segoeuib.ttf", 22)
    f_sub = get_font("segoeui.ttf", 13)
    f_bold = get_font("segoeuib.ttf", 15)
    f_reg = get_font("segoeui.ttf", 13)
    f_mono = get_font("consola.ttf", 12)
    f_btn = get_font("segoeuib.ttf", 13)

    # Sub-header
    draw.text((30, 64), "Centralized Campus Support & Mentorship Platform", fill=(248, 250, 252), font=f_h1)
    draw.text((30, 94), "Real-time faculty consultation scheduler, instant FAQ knowledge base & welfare grievance routing", fill=(148, 163, 184), font=f_sub)

    # Left Column: Faculty Directory (x: 30 to 390)
    draw.rounded_rectangle([(30, 126), (390, 635)], radius=12, fill=(15, 23, 42), outline=(51, 65, 85), width=1)
    draw.text((48, 142), "AVAILABLE FACULTY MENTORS", fill=(148, 163, 184), font=f_mono)

    professors = [
        ("Dr. Mahfuz Rahman", "Software Engineering Faculty", "Available: Today • 3:30 PM", (14, 165, 233)),
        ("Prof. Syeda Jahan", "Academic Affairs Advisor", "Available: Tomorrow • 11:00 AM", (168, 85, 247)),
        ("Dr. Ahsan Kabir", "Algorithms & Research Mentor", "Available: Wed • 2:00 PM", (16, 185, 129)),
    ]

    y = 175
    for name, dept, slot, color in professors:
        draw.rounded_rectangle([(46, y), (374, y + 130)], radius=10, fill=(30, 41, 59), outline=(51, 65, 85), width=1)
        # Avatar
        draw.rounded_rectangle([(60, y + 14), (96, y + 50)], radius=8, fill=color)
        draw.text((68, y + 21), name[:2].upper(), fill=(255, 255, 255), font=f_bold)
        # Info
        draw.text((108, y + 14), name, fill=(248, 250, 252), font=f_bold)
        draw.text((108, y + 34), dept, fill=(148, 163, 184), font=f_reg)
        # Slot badge
        draw.rounded_rectangle([(60, y + 58), (360, y + 82)], radius=6, fill=(15, 23, 42))
        draw.text((70, y + 62), slot, fill=(56, 189, 248), font=f_mono)
        # Button
        draw.rounded_rectangle([(60, y + 90), (360, y + 118)], radius=6, fill=(2, 132, 199))
        draw.text((130, y + 94), "Request 1-on-1 Session", fill=(255, 255, 255), font=f_btn)
        y += 145

    # Center Column: Knowledge Base & FAQ Search (x: 410 to 810)
    draw.rounded_rectangle([(410, 126), (810, 635)], radius=12, fill=(15, 23, 42), outline=(51, 65, 85), width=1)
    draw.text((428, 142), "CAMPUS FAQ & SMART KNOWLEDGE ENGINE", fill=(148, 163, 184), font=f_mono)

    # Search box
    draw.rounded_rectangle([(426, 175), (794, 218)], radius=8, fill=(30, 41, 59), outline=(56, 189, 248), width=1)
    draw.text((444, 186), "Search: Course retake policy, GPA waivers, counsellor...", fill=(241, 245, 249), font=f_reg)

    # Topic filters
    tags = ["All Topics", "Course Retake", "Welfare Fund", "Exam Rules", "Mental Health"]
    tx = 426
    for i, t in enumerate(tags):
        bg = (14, 165, 233) if i == 0 else (30, 41, 59)
        tc = (255, 255, 255) if i == 0 else (148, 163, 184)
        tw = len(t) * 8 + 16
        draw.rounded_rectangle([(tx, 230), (tx + tw, 254)], radius=12, fill=bg, outline=(51, 65, 85), width=1)
        draw.text((tx + 8, 234), t, fill=tc, font=f_mono)
        tx += tw + 8

    # Q&A Accordion Items
    faqs = [
        ("Q: How does student welfare financial assistance work?",
         "Full-time enrolled students facing unforeseen medical or academic crisis can file an urgent claim through the Welfare Officer portal with department chair signoff."),
        ("Q: Can I book confidential psychological counselling?",
         "Yes. All student wellbeing sessions are strictly encrypted and anonymized. Book directly with certified student advisors."),
        ("Q: What is the deadline for prerequisite course waiver?",
         "Course waiver petitions must be submitted within the first 10 days of semester registration.")
    ]
    fy = 275
    for q, a in faqs:
        draw.rounded_rectangle([(426, fy), (794, fy + 104)], radius=8, fill=(30, 41, 59), outline=(51, 65, 85), width=1)
        draw.text((440, fy + 12), q, fill=(56, 189, 248), font=f_bold)
        # 2 lines of text
        draw.text((440, fy + 38), a[:58], fill=(203, 213, 225), font=f_reg)
        draw.text((440, fy + 58), a[58:116], fill=(203, 213, 225), font=f_reg)
        draw.text((440, fy + 78), a[116:160] + "...", fill=(148, 163, 184), font=f_sub)
        fy += 116

    # Right Column: Confirmed Session (x: 830 to 1170)
    draw.rounded_rectangle([(830, 126), (1170, 635)], radius=12, fill=(15, 23, 42), outline=(51, 65, 85), width=1)
    draw.text((848, 142), "UPCOMING CONFIRMED SESSION", fill=(148, 163, 184), font=f_mono)

    # Active Card
    draw.rounded_rectangle([(846, 175), (1154, 420)], radius=10, fill=(30, 41, 59), outline=(16, 185, 129), width=1)
    draw.rounded_rectangle([(862, 192), (950, 216)], radius=6, fill=(6, 78, 59))
    draw.text((872, 196), "● CONFIRMED", fill=(52, 211, 153), font=f_mono)

    draw.text((862, 230), "Academic Degree Guidance", fill=(248, 250, 252), font=f_bold)
    draw.text((862, 260), "Today • 14:30 PM", fill=(56, 189, 248), font=get_font("segoeuib.ttf", 22))
    draw.text((862, 298), "Advisor: Dr. Mahfuz Rahman", fill=(203, 213, 225), font=f_reg)
    draw.text((862, 322), "Room: CSE Department Faculty Wing B", fill=(148, 163, 184), font=f_sub)

    draw.rounded_rectangle([(862, 360), (1138, 402)], radius=8, fill=(16, 185, 129))
    draw.text((915, 372), "Enter Virtual Consultation", fill=(255, 255, 255), font=f_bold)

    # Notice banner
    draw.rounded_rectangle([(846, 440), (1154, 615)], radius=10, fill=(30, 41, 59), outline=(51, 65, 85), width=1)
    draw.text((862, 455), "CAMPUS ADVISORY", fill=(245, 158, 11), font=f_mono)
    draw.text((862, 480), "Mid-term examination counseling", fill=(248, 250, 252), font=f_bold)
    draw.text((862, 505), "Faculty office hours are extended", fill=(148, 163, 184), font=f_reg)
    draw.text((862, 525), "through Thursday for all engineering", fill=(148, 163, 184), font=f_reg)
    draw.text((862, 545), "departments.", fill=(148, 163, 184), font=f_reg)

    img.save("public/projects/campus_welfare.jpg", quality=95)
    print("campus_welfare.jpg rendered successfully")

# 2. ROADMAP & HABIT TRACKER
def make_roadmap_tracker():
    img = Image.new("RGB", (W, H), (12, 10, 24))
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, "DevRoadmap & Daily Streak Matrix • Automated Curriculum Scraper")

    f_h1 = get_font("segoeuib.ttf", 22)
    f_sub = get_font("segoeui.ttf", 13)
    f_bold = get_font("segoeuib.ttf", 15)
    f_reg = get_font("segoeui.ttf", 13)
    f_mono = get_font("consola.ttf", 12)
    f_btn = get_font("segoeuib.ttf", 13)

    draw.text((30, 64), "Developer Roadmap Scraper & Daily Habit Tracker", fill=(248, 250, 252), font=f_h1)
    draw.text((30, 94), "Automated technical curriculum parser with daily checklist generator and habit streak heatmaps", fill=(192, 132, 252), font=f_sub)

    # Left: Active Roadmaps (x: 30 to 390)
    draw.rounded_rectangle([(30, 126), (390, 635)], radius=12, fill=(19, 16, 38), outline=(63, 43, 99), width=1)
    draw.text((48, 142), "SYNCED CURRICULUM TRACKS", fill=(192, 132, 252), font=f_mono)

    tracks = [
        ("Full-Stack Software Engineer", "84% Completed • 32/38 Topics", 84, (168, 85, 247)),
        ("Data Engineering & Pipelines", "62% Completed • 18/29 Topics", 62, (59, 130, 246)),
        ("Algorithms & LeetCode 75", "92% Completed • 69/75 Problems", 92, (16, 185, 129)),
    ]
    y = 175
    for title, desc, pct, col in tracks:
        draw.rounded_rectangle([(46, y), (374, y + 105)], radius=10, fill=(30, 25, 58), outline=(76, 53, 117), width=1)
        draw.text((60, y + 12), title, fill=(248, 250, 252), font=f_bold)
        draw.text((60, y + 36), desc, fill=(203, 213, 225), font=f_sub)
        # Progress bar
        draw.rounded_rectangle([(60, y + 62), (360, y + 74)], radius=6, fill=(19, 16, 38))
        draw.rounded_rectangle([(60, y + 62), (60 + int(3.0 * pct), y + 74)], radius=6, fill=col)
        y += 125

    # Center: Interactive Roadmap Flow (x: 410 to 810)
    draw.rounded_rectangle([(410, 126), (810, 635)], radius=12, fill=(19, 16, 38), outline=(63, 43, 99), width=1)
    draw.text((428, 142), "CURRICULUM FLOW GRAPH (ROADMAP ENGINE)", fill=(192, 132, 252), font=f_mono)

    nodes = [
        ("RESTful Architecture & HTTP Verbs", "STATUS: COMPLETED (Verified)", (16, 185, 129), (6, 78, 59)),
        ("PostgreSQL Database Normalization", "STATUS: COMPLETED (Verified)", (16, 185, 129), (6, 78, 59)),
        ("B-Tree Indexing & Query Profiling", "STATUS: IN PROGRESS (Daily Target)", (245, 158, 11), (120, 53, 15)),
        ("Message Queues: Redis Streams / Kafka", "STATUS: UPCOMING NEXT", (148, 163, 184), (30, 25, 58)),
    ]
    ny = 175
    for i, (ntitle, nstatus, ncol, nbg) in enumerate(nodes):
        draw.rounded_rectangle([(426, ny), (794, ny + 78)], radius=10, fill=(30, 25, 58), outline=ncol, width=1)
        draw.rounded_rectangle([(440, ny + 12), (720, ny + 32)], radius=4, fill=nbg)
        draw.text((448, ny + 14), nstatus, fill=ncol, font=f_mono)
        draw.text((440, ny + 42), ntitle, fill=(248, 250, 252), font=f_bold)
        # Connecting arrows
        if i < len(nodes) - 1:
            draw.line([(610, ny + 78), (610, ny + 105)], fill=(168, 85, 247), width=2)
        ny += 105

    # Right: Habit Streaks & Daily Todo (x: 830 to 1170)
    draw.rounded_rectangle([(830, 126), (1170, 635)], radius=12, fill=(19, 16, 38), outline=(63, 43, 99), width=1)
    draw.text((848, 142), "TODAY'S HABITS & STREAK MATRIX", fill=(192, 132, 252), font=f_mono)

    # Streak Hero Card
    draw.rounded_rectangle([(846, 175), (1154, 305)], radius=10, fill=(30, 25, 58), outline=(168, 85, 247), width=1)
    draw.text((862, 190), "CONSISTENCY STREAK", fill=(192, 132, 252), font=f_mono)
    draw.text((862, 212), "34 Days Streak", fill=(248, 250, 252), font=get_font("segoeuib.ttf", 26))
    draw.text((862, 252), "Current Velocity: 4.8 Tasks/Day (Top 5%)", fill=(52, 211, 153), font=f_sub)

    # Mini Habit Heatmap Grid (7 cols x 4 rows)
    hx = 862
    hy = 276
    for c in range(16):
        for r in range(2):
            col_val = (168, 85, 247) if (c + r) % 3 != 0 else (59, 40, 95)
            draw.rectangle([(hx + c * 17, hy + r * 10), (hx + c * 17 + 12, hy + r * 10 + 7)], fill=col_val)

    # Daily Checklist
    draw.text((848, 325), "DAILY CHECKLIST", fill=(192, 132, 252), font=f_mono)
    todos = [
        ("[x] Solve 2 LeetCode Tree Problems", True),
        ("[x] Review B-Tree Indexing Specs", True),
        ("[x] Read System Design Primer Chapter", True),
        ("[ ] Implement Redis Stream Worker", False),
        ("[ ] 30m Technical Documentation", False),
    ]
    ty = 350
    for todo, done in todos:
        bg = (16, 70, 50) if done else (30, 25, 58)
        col = (52, 211, 153) if done else (203, 213, 225)
        draw.rounded_rectangle([(846, ty), (1154, ty + 42)], radius=6, fill=bg, outline=(76, 53, 117), width=1)
        draw.text((860, ty + 12), todo, fill=col, font=f_reg)
        ty += 52

    img.save("public/projects/roadmap_tracker.jpg", quality=95)
    print("roadmap_tracker.jpg rendered successfully")

# 3. HARDWARE & AUDIO SUITE
def make_hardware_suite():
    img = Image.new("RGB", (W, H), (10, 15, 18))
    draw = ImageDraw.Draw(img)
    draw_window_frame(draw, "AudioForge Studio & Multi-Display Visual Controller • Win32 & DDC/CI Core")

    f_h1 = get_font("segoeuib.ttf", 22)
    f_sub = get_font("segoeui.ttf", 13)
    f_bold = get_font("segoeuib.ttf", 15)
    f_reg = get_font("segoeui.ttf", 13)
    f_mono = get_font("consola.ttf", 12)
    f_btn = get_font("segoeuib.ttf", 13)

    draw.text((30, 64), "Desktop Hardware Utilities & Audio Calibrator", fill=(248, 250, 252), font=f_h1)
    draw.text((30, 94), "System-level Equalizer APO sound enhancer & dual-monitor DDC/CI visual hardware controller", fill=(45, 212, 191), font=f_sub)

    # Left / Center: Equalizer APO Audio Engine (x: 30 to 680)
    draw.rounded_rectangle([(30, 126), (680, 635)], radius=12, fill=(15, 23, 28), outline=(30, 58, 68), width=1)
    draw.text((48, 142), "EQUALIZER APO 10-BAND PARAMETRIC CALIBRATION", fill=(45, 212, 191), font=f_mono)

    # Equalizer Faders
    bands = ["32Hz", "64Hz", "125Hz", "250Hz", "500Hz", "1kHz", "2kHz", "4kHz", "8kHz", "16kHz"]
    levels = [6, 8, 4, 1, -2, 0, 3, 7, 9, 8] # dB values

    fx = 58
    for i, (band, lvl) in enumerate(zip(bands, levels)):
        # Vertical track
        track_x = fx + i * 62
        draw.line([(track_x + 12, 190), (track_x + 12, 420)], fill=(30, 48, 58), width=6)
        # Center line (0 dB)
        draw.line([(track_x, 305), (track_x + 24, 305)], fill=(51, 65, 85), width=1)
        # Thumb position
        thumb_y = 305 - lvl * 10
        # Active color bar
        draw.line([(track_x + 12, 305), (track_x + 12, thumb_y)], fill=(20, 184, 166), width=6)
        # Slider thumb knob
        draw.rounded_rectangle([(track_x, thumb_y - 8), (track_x + 24, thumb_y + 8)], radius=4, fill=(45, 212, 191), outline=(255, 255, 255), width=1)
        # dB label
        draw.text((track_x - 4, thumb_y - 24), f"+{lvl}dB" if lvl > 0 else f"{lvl}dB", fill=(203, 213, 225), font=f_mono)
        # Band label
        draw.text((track_x - 6, 435), band, fill=(148, 163, 184), font=f_mono)

    # Equalizer Presets
    draw.text((48, 475), "AUDIO PRESET PROFILES", fill=(45, 212, 191), font=f_mono)
    presets = ["Acoustic Studio Reference", "Bass Boost Sub-Harmonic", "Spatial Gaming & Footsteps", "Clear Vocal Podcast"]
    px = 48
    for p in presets:
        draw.rounded_rectangle([(px, 500), (px + 144, 540)], radius=8, fill=(20, 35, 42), outline=(30, 58, 68), width=1)
        draw.text((px + 10, 512), p[:16], fill=(248, 250, 252), font=f_mono)
        px += 154

    # Audio Engine Status
    draw.rounded_rectangle([(48, 560), (662, 615)], radius=8, fill=(10, 28, 30), outline=(20, 184, 166), width=1)
    draw.text((64, 574), "● DSP Status: Active (Low-latency 64-bit float convolution stream • 0.8ms buffer)", fill=(45, 212, 191), font=f_mono)
    draw.text((64, 592), "Output Device: High Definition Audio Device (24-bit / 96000 Hz Studio Quality)", fill=(148, 163, 184), font=f_sub)

    # Right: Multi-Monitor Display Controller (x: 700 to 1170)
    draw.rounded_rectangle([(700, 126), (1170, 635)], radius=12, fill=(15, 23, 28), outline=(30, 58, 68), width=1)
    draw.text((718, 142), "DDC/CI HARDWARE MONITOR CONTROLLER", fill=(45, 212, 191), font=f_mono)

    # Monitor 1 Card
    draw.rounded_rectangle([(718, 175), (1152, 380)], radius=10, fill=(20, 35, 42), outline=(30, 58, 68), width=1)
    draw.text((736, 190), "MONITOR 1 • Primary Display", fill=(45, 212, 191), font=f_mono)
    draw.text((736, 210), "27\" IPS 144Hz Gaming & Color Panel", fill=(248, 250, 252), font=f_bold)
    # Brightness slider
    draw.text((736, 240), "Brightness: 75%", fill=(203, 213, 225), font=f_sub)
    draw.rounded_rectangle([(736, 260), (1134, 272)], radius=6, fill=(10, 18, 24))
    draw.rounded_rectangle([(736, 260), (736 + int(398 * 0.75), 272)], radius=6, fill=(45, 212, 191))
    # Contrast slider
    draw.text((736, 290), "Contrast: 70%", fill=(203, 213, 225), font=f_sub)
    draw.rounded_rectangle([(736, 310), (1134, 322)], radius=6, fill=(10, 18, 24))
    draw.rounded_rectangle([(736, 310), (736 + int(398 * 0.70), 322)], radius=6, fill=(59, 130, 246))
    # Color Profile
    draw.text((736, 342), "Color Profile: D65 sRGB Calibrated (Gamma 2.2)", fill=(148, 163, 184), font=f_mono)

    # Monitor 2 Card
    draw.rounded_rectangle([(718, 400), (1152, 605)], radius=10, fill=(20, 35, 42), outline=(30, 58, 68), width=1)
    draw.text((736, 415), "MONITOR 2 • Secondary Display", fill=(45, 212, 191), font=f_mono)
    draw.text((736, 435), "24\" Vertical Code & Document Panel", fill=(248, 250, 252), font=f_bold)
    # Brightness slider
    draw.text((736, 465), "Brightness: 60% (Reading Mode)", fill=(203, 213, 225), font=f_sub)
    draw.rounded_rectangle([(736, 485), (1134, 497)], radius=6, fill=(10, 18, 24))
    draw.rounded_rectangle([(736, 485), (736 + int(398 * 0.60), 497)], radius=6, fill=(245, 158, 11))
    # Color Profile
    draw.text((736, 520), "Night Shift: 4500K Warm Light Activated", fill=(251, 191, 36), font=f_mono)
    draw.rounded_rectangle([(736, 550), (1134, 585)], radius=6, fill=(13, 148, 136))
    draw.text((880, 560), "Sync Multi-Display Color Balance", fill=(255, 255, 255), font=f_bold)

    img.save("public/projects/hardware_suite.jpg", quality=95)
    print("hardware_suite.jpg rendered successfully")

if __name__ == "__main__":
    make_campus_welfare()
    make_roadmap_tracker()
    make_hardware_suite()

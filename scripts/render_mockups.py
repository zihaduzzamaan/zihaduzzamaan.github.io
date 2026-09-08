"""
Render Mockups: Humanized 16:9 Showcase Banner Generator
Generates production-grade, 16:9 (1920x1080) showcase banners for:
1. PieceStyle (Commercial Fashion E-Commerce)
2. CampusCare (University Student Welfare & Mentorship)
3. DevRoadmap (Curriculum Scraper & Daily Habit Tracker)
4. AudioForge & DisplaySync (Win32 Hardware & Audio Utilities)
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1920, 1080

def get_font(name="segoeuib.ttf", size=24):
    font_paths = [
        f"C:/Windows/Fonts/{name}",
        f"C:/Windows/Fonts/{name.lower()}",
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/georgiab.ttf",
        "C:/Windows/Fonts/georgia.ttf",
        "C:/Windows/Fonts/consola.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def add_drop_shadow(img, blur_radius=38, offset=(0, 22), shadow_color=(0, 0, 0, 220)):
    sw = img.width + blur_radius * 2
    sh = img.height + blur_radius * 2
    shadow = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    
    pad = blur_radius
    box = [
        pad + offset[0],
        pad + offset[1],
        pad + offset[0] + img.width,
        pad + offset[1] + img.height
    ]
    s_draw.rounded_rectangle(box, radius=14, fill=shadow_color)
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur_radius))
    
    result = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    result.paste(shadow, (0, 0))
    result.paste(img, (pad, pad), mask=img)
    return result, pad

def make_browser_frame(content_w, content_h, title_url="app.io", header_bg=(15, 23, 42, 255), frame_radius=12):
    header_h = 36
    frame_w = content_w
    frame_h = content_h + header_h
    
    frame = Image.new("RGBA", (frame_w, frame_h), header_bg)
    draw = ImageDraw.Draw(frame)
    
    # Top bar background
    draw.rounded_rectangle([(0, 0), (frame_w, frame_h)], radius=frame_radius, fill=header_bg)
    draw.rectangle([(0, header_h - 8), (frame_w, header_h)], fill=header_bg)
    
    # Traffic light dots
    draw.ellipse([(14, 13), (22, 21)], fill=(239, 68, 68))
    draw.ellipse([(28, 13), (36, 21)], fill=(245, 158, 11))
    draw.ellipse([(42, 13), (50, 21)], fill=(16, 185, 129))
    
    # URL pill
    pill_w = min(280, frame_w - 180)
    pill_x = 64
    draw.rounded_rectangle([(pill_x, 8), (pill_x + pill_w, 28)], radius=6, fill=(0, 0, 0, 80), outline=(255, 255, 255, 25), width=1)
    # Lock icon
    draw.arc([(pill_x + 10, 13), (pill_x + 16, 20)], 180, 0, fill=(148, 163, 184), width=1)
    draw.rounded_rectangle([(pill_x + 9, 18), (pill_x + 17, 24)], radius=1, fill=(245, 158, 11))
    draw.text((pill_x + 23, 11), title_url, fill=(203, 213, 225), font=get_font("consola.ttf", 11))
    
    return frame, header_h

def draw_vector_arrow(draw, x, y, col=(245, 158, 11)):
    draw.line([(x, y), (x + 14, y)], fill=col, width=2)
    draw.polygon([(x + 14, y - 4), (x + 20, y), (x + 14, y + 4)], fill=col)

def draw_icon(draw, kind, cx, cy, col):
    if kind == "bag":
        # Shopping bag
        draw.rectangle([(cx - 7, cy - 4), (cx + 7, cy + 9)], fill=col)
        draw.arc([(cx - 4, cy - 10), (cx + 4, cy - 2)], 180, 0, fill=col, width=2)
    elif kind == "filter":
        # Sliders / filter
        draw.polygon([(cx - 9, cy - 8), (cx + 9, cy - 8), (cx + 3, cy + 1), (cx + 3, cy + 8), (cx - 3, cy + 8), (cx - 3, cy + 1)], fill=col)
    elif kind == "shield":
        # Shield with check
        draw.polygon([(cx - 8, cy - 9), (cx + 8, cy - 9), (cx + 8, cy + 1), (cx, cy + 11), (cx - 8, cy + 1)], fill=col)
        draw.line([(cx - 4, cy), (cx - 1, cy + 3), (cx + 4, cy - 2)], fill=(15, 23, 42), width=2)
    elif kind == "database":
        # Database cylinder
        draw.ellipse([(cx - 8, cy - 9), (cx + 8, cy - 4)], fill=col)
        draw.rectangle([(cx - 8, cy - 6), (cx + 8, cy + 6)], fill=col)
        draw.ellipse([(cx - 8, cy + 3), (cx + 8, cy + 8)], fill=col)
    elif kind == "calendar":
        # Calendar page
        draw.rounded_rectangle([(cx - 8, cy - 7), (cx + 8, cy + 9)], radius=2, fill=col)
        draw.rectangle([(cx - 8, cy - 7), (cx + 8, cy - 2)], fill=(15, 23, 42))
        draw.ellipse([(cx - 5, cy - 9), (cx - 3, cy - 6)], fill=col)
        draw.ellipse([(cx + 3, cy - 9), (cx + 5, cy - 6)], fill=col)
    elif kind == "search":
        # Magnifying glass
        draw.ellipse([(cx - 7, cy - 8), (cx + 3, cy + 2)], outline=col, width=2)
        draw.line([(cx + 2, cy + 1), (cx + 8, cy + 7)], fill=col, width=2)
    elif kind == "bell":
        # Bell alert
        draw.arc([(cx - 7, cy - 6), (cx + 7, cy + 6)], 180, 0, fill=col, width=2)
        draw.line([(cx - 8, cy + 6), (cx + 8, cy + 6)], fill=col, width=2)
        draw.ellipse([(cx - 2, cy + 7), (cx + 2, cy + 10)], fill=col)
    elif kind == "terminal":
        # Code brackets >_
        draw.line([(cx - 7, cy - 6), (cx - 2, cy - 1), (cx - 7, cy + 4)], fill=col, width=2)
        draw.line([(cx, cy + 4), (cx + 7, cy + 4)], fill=col, width=2)
    elif kind == "grid":
        # Commit grid matrix
        for gx in [-6, 0, 6]:
            for gy in [-6, 0, 6]:
                draw.rectangle([(cx + gx - 2, cy + gy - 2), (cx + gx + 2, cy + gy + 2)], fill=col)
    elif kind == "flame":
        # Flame streak
        draw.polygon([(cx, cy - 10), (cx + 6, cy - 3), (cx + 8, cy + 5), (cx + 4, cy + 9), (cx - 4, cy + 9), (cx - 8, cy + 5), (cx - 6, cy - 2)], fill=col)
    elif kind == "sliders":
        # EQ sliders
        draw.line([(cx - 5, cy - 8), (cx - 5, cy + 8)], fill=col, width=2)
        draw.ellipse([(cx - 8, cy - 3), (cx - 2, cy + 3)], fill=col)
        draw.line([(cx + 5, cy - 8), (cx + 5, cy + 8)], fill=col, width=2)
        draw.ellipse([(cx + 2, cy - 1), (cx + 8, cy + 5)], fill=col)
    elif kind == "monitor":
        # Display monitor
        draw.rounded_rectangle([(cx - 8, cy - 7), (cx + 8, cy + 4)], radius=2, outline=col, width=2)
        draw.line([(cx, cy + 4), (cx, cy + 8)], fill=col, width=2)
        draw.line([(cx - 4, cy + 8), (cx + 4, cy + 8)], fill=col, width=2)
    elif kind == "sun":
        # Sun / color temp
        draw.ellipse([(cx - 4, cy - 4), (cx + 4, cy + 4)], fill=col)
        for d in range(0, 360, 45):
            pass

# ==============================================================================
# 1. PIECESTYLE: Commercial E-Commerce Platform
# ==============================================================================
def make_piecestyle():
    canvas = Image.new("RGBA", (W, H), (11, 13, 18, 255))
    
    # Ambient luxury glows
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([(800, 100), (1700, 950)], fill=(212, 175, 55, 30))
    gd.ellipse([(1200, 50), (1900, 700)], fill=(180, 130, 80, 25))
    glow = glow.filter(ImageFilter.GaussianBlur(140))
    canvas = Image.alpha_composite(canvas, glow)

    # 1. Right Side: Floating E-Commerce Storefront Window
    store_w, store_h = 700, 680
    frame, hdr_h = make_browser_frame(store_w, store_h, "piecestyle.com/collection", (20, 23, 31, 255))
    fd = ImageDraw.Draw(frame)
    
    # Storefront Header
    fd.text((store_w // 2 - 45, hdr_h + 16), "PieceStyle", fill=(245, 235, 225), font=get_font("georgiab.ttf", 20))
    fd.text((32, hdr_h + 20), "NEW ARRIVALS   CLOTHING   SHOES   EDITORIAL", fill=(148, 163, 184), font=get_font("consola.ttf", 10))
    fd.line([(24, hdr_h + 46), (store_w - 24, hdr_h + 46)], fill=(35, 42, 54), width=1)
    
    # Hero Collection Banner inside store
    fd.rounded_rectangle([(24, hdr_h + 56), (store_w - 24, hdr_h + 210)], radius=8, fill=(28, 32, 42))
    fd.text((48, hdr_h + 90), "CURATED ESSENTIALS", fill=(255, 255, 255), font=get_font("georgiab.ttf", 24))
    fd.text((48, hdr_h + 125), "Autumn / Winter Luxury Capsule • Limited Batch Production", fill=(203, 213, 225), font=get_font("segoeui.ttf", 13))
    fd.rounded_rectangle([(48, hdr_h + 155), (180, hdr_h + 188)], radius=4, fill=(212, 175, 55))
    fd.text((62, hdr_h + 163), "SHOP COLLECTION", fill=(15, 23, 42), font=get_font("segoeuib.ttf", 11))
    
    # 3 Product Cards
    card_items = [
        ("The Astreee Silk Blazer", "$890", (45, 50, 65)),
        ("Luna Knit Maxi Dress", "$640", (40, 45, 60)),
        ("Minimalist Trench Coat", "$1,200", (35, 40, 55))
    ]
    cx = 24
    for p_name, p_price, p_col in card_items:
        # Product card
        fd.rounded_rectangle([(cx, hdr_h + 230), (cx + 206, hdr_h + 650)], radius=8, fill=(24, 28, 38), outline=(38, 45, 60), width=1)
        # Image placeholder with luxury dark tones
        fd.rounded_rectangle([(cx + 10, hdr_h + 240), (cx + 196, hdr_h + 490)], radius=6, fill=p_col)
        # Quick view tag
        fd.rounded_rectangle([(cx + 50, hdr_h + 445), (cx + 156, hdr_h + 475)], radius=4, fill=(10, 12, 16, 230))
        fd.text((cx + 64, hdr_h + 453), "QUICK VIEW", fill=(245, 235, 225), font=get_font("segoeuib.ttf", 11))
        # Details
        fd.text((cx + 12, hdr_h + 505), p_name[:18], fill=(248, 250, 252), font=get_font("segoeuib.ttf", 13))
        fd.text((cx + 12, hdr_h + 528), "100% Organic Italian Silk", fill=(148, 163, 184), font=get_font("segoeui.ttf", 11))
        fd.text((cx + 12, hdr_h + 555), p_price, fill=(212, 175, 55), font=get_font("segoeuib.ttf", 14))
        # Add to Bag button
        fd.rounded_rectangle([(cx + 12, hdr_h + 585), (cx + 194, hdr_h + 625)], radius=6, fill=(35, 42, 58), outline=(60, 72, 98), width=1)
        fd.text((cx + 62, hdr_h + 597), "ADD TO BAG", fill=(245, 235, 225), font=get_font("segoeuib.ttf", 11))
        cx += 224

    sh_store, pad_s = add_drop_shadow(frame, blur_radius=40, offset=(0, 25), shadow_color=(0, 0, 0, 210))
    canvas.paste(sh_store, (780 - pad_s, 60 - pad_s), mask=sh_store)

    # 2. Overlaid Staggered Shopping Bag Drawer
    cart_w, cart_h = 420, 520
    cart_card = Image.new("RGBA", (cart_w, cart_h), (18, 21, 28, 255))
    cd = ImageDraw.Draw(cart_card)
    cd.rounded_rectangle([(0, 0), (cart_w, cart_h)], radius=12, fill=(18, 21, 28, 255), outline=(65, 55, 30), width=1)
    
    # Drawer Header
    cd.text((24, 20), "YOUR BAG (3 ITEMS)", fill=(245, 235, 225), font=get_font("georgiab.ttf", 15))
    cd.line([(24, 52), (cart_w - 24, 52)], fill=(38, 44, 56), width=1)
    
    # Cart Items
    items = [
        ("The Astreee Silk Blazer", "Size M • Black", "$890.00"),
        ("Luna Knit Maxi Dress", "Size S • Charcoal", "$640.00"),
        ("Sisak Fine Leather Belt", "Size 34 • Brass", "$150.00")
    ]
    iy = 68
    for iname, isub, iprice in items:
        cd.rounded_rectangle([(24, iy), (74, iy + 60)], radius=4, fill=(32, 37, 50))
        cd.text((86, iy + 8), iname, fill=(248, 250, 252), font=get_font("segoeuib.ttf", 13))
        cd.text((86, iy + 28), isub, fill=(148, 163, 184), font=get_font("segoeui.ttf", 11))
        cd.text((86, iy + 45), iprice, fill=(212, 175, 55), font=get_font("consola.ttf", 12))
        cd.text((cart_w - 60, iy + 20), "Qty: 1", fill=(148, 163, 184), font=get_font("consola.ttf", 11))
        iy += 78

    # Subtotal & Checkout
    cd.line([(24, 330), (cart_w - 24, 330)], fill=(38, 44, 56), width=1)
    cd.text((24, 350), "Subtotal:", fill=(148, 163, 184), font=get_font("segoeui.ttf", 14))
    cd.text((cart_w - 120, 348), "$1,680.00", fill=(245, 235, 225), font=get_font("georgiab.ttf", 18))
    cd.text((24, 380), "Shipping & Taxes:", fill=(100, 116, 139), font=get_font("segoeui.ttf", 12))
    cd.text((cart_w - 120, 380), "Calculated at Step 2", fill=(100, 116, 139), font=get_font("segoeui.ttf", 12))
    
    # Checkout Button
    cd.rounded_rectangle([(24, 420), (cart_w - 24, 475)], radius=8, fill=(212, 175, 55))
    cd.text((cart_w // 2 - 68, 438), "PROCEED TO CHECKOUT", fill=(15, 23, 42), font=get_font("segoeuib.ttf", 12))
    cd.text((cart_w // 2 - 80, 488), "● 256-Bit SSL Encrypted Payment Pipeline", fill=(16, 185, 129), font=get_font("consola.ttf", 10))

    sh_cart, pad_c = add_drop_shadow(cart_card, blur_radius=42, offset=(0, 25), shadow_color=(0, 0, 0, 240))
    canvas.paste(sh_cart, (1430 - pad_c, 360 - pad_c), mask=sh_cart)

    # 3. Left Side: Brand Identity & Feature Callouts
    draw = ImageDraw.Draw(canvas)
    
    # Brand Header
    draw.text((80, 75), "PieceStyle", fill=(245, 235, 225), font=get_font("georgiab.ttf", 36))
    draw.text((82, 128), "COMMERCIAL FASHION E-COMMERCE & SAAS", fill=(212, 175, 55), font=get_font("consola.ttf", 12))
    
    # Headline
    draw.text((80, 168), "Curated Fashion &", fill=(255, 255, 255), font=get_font("segoeuib.ttf", 46))
    draw.text((80, 225), "Scalable Merchandising", fill=(212, 175, 55), font=get_font("segoeuib.ttf", 46))
    
    # Description
    draw.text((80, 292), "Full-stack fashion e-commerce storefront with dynamic catalogs,", fill=(203, 213, 225), font=get_font("segoeui.ttf", 16))
    draw.text((80, 318), "persistent shopping bag drawers, and secure checkout processing.", fill=(148, 163, 184), font=get_font("segoeui.ttf", 16))
    
    # 4 Feature Cards
    features = [
        ("bag", "Dynamic Product Catalog", "Real-time stock counts, size matrices & apparel filter pipelines.", (212, 175, 55)),
        ("filter", "Instant Slide-Out Cart Drawer", "Live subtotal calculation, quantity steppers & promo discount codes.", (56, 189, 248)),
        ("shield", "Secure Order Processing", "PCI-compliant checkout pipeline with automated invoice generation.", (52, 211, 153)),
        ("database", "Commercial Admin Portal", "Centralized inventory manager, order fulfillment & stock alerts.", (192, 132, 252))
    ]
    
    card_y = 365
    for icon_k, f_t, f_d, f_col in features:
        draw.rounded_rectangle([(80, card_y), (700, card_y + 66)], radius=12, fill=(18, 22, 30, 220), outline=(38, 46, 62), width=1)
        draw.rounded_rectangle([(96, card_y + 11), (140, card_y + 55)], radius=10, fill=(f_col[0], f_col[1], f_col[2], 30), outline=f_col, width=1)
        draw_icon(draw, icon_k, 118, card_y + 33, f_col)
        draw.text((156, card_y + 12), f_t, fill=(248, 250, 252), font=get_font("segoeuib.ttf", 15))
        draw.text((156, card_y + 36), f_d, fill=(148, 163, 184), font=get_font("segoeui.ttf", 13))
        card_y += 78

    # Production Metric Pill
    draw.rounded_rectangle([(80, 700), (700, 750)], radius=25, fill=(45, 36, 15, 200), outline=(212, 175, 55, 220), width=1)
    draw.ellipse([(100, 720), (110, 730)], fill=(212, 175, 55))
    draw.text((122, 716), "COMMERCIAL SAAS: DYNAMIC INVENTORY • 100% RESPONSIVE • FAST CHECKOUT", fill=(254, 243, 199), font=get_font("segoeuib.ttf", 13))
    
    # Workflow note
    f_flow = get_font("segoeuib.ttf", 15)
    draw.text((82, 780), "Browse Collection", fill=(148, 163, 184), font=f_flow)
    draw_vector_arrow(draw, 226, 790, (212, 175, 55))
    draw.text((260, 780), "Slide-Out Bag", fill=(248, 250, 252), font=f_flow)
    draw_vector_arrow(draw, 375, 790, (212, 175, 55))
    draw.text((408, 780), "One-Click Secure Order", fill=(212, 175, 55), font=f_flow)

    out_path = os.path.join(PROJECT_ROOT, "public/projects/piecestyle.jpg")
    final_rgb = Image.new("RGB", (W, H), (11, 13, 18))
    final_rgb.paste(canvas, (0, 0), mask=canvas)
    final_rgb.save(out_path, quality=95)
    print("piecestyle.jpg rendered successfully")


# ==============================================================================
# 2. CAMPUSCARE: University Student Welfare & Mentorship Portal
# ==============================================================================
def make_campus_welfare():
    canvas = Image.new("RGBA", (W, H), (6, 15, 26, 255))
    
    # Ambient collegiate glows
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([(850, 80), (1750, 950)], fill=(16, 185, 129, 28))
    gd.ellipse([(1100, 40), (1920, 680)], fill=(6, 182, 212, 35))
    glow = glow.filter(ImageFilter.GaussianBlur(140))
    canvas = Image.alpha_composite(canvas, glow)

    # 1. Right Side: Mentorship Directory Window
    store_w, store_h = 680, 640
    frame, hdr_h = make_browser_frame(store_w, store_h, "campuscare.diu.edu.bd/mentorship", (15, 25, 42, 255))
    fd = ImageDraw.Draw(frame)
    
    # Window Header
    fd.text((30, hdr_h + 18), "AVAILABLE FACULTY MENTORS", fill=(52, 211, 153), font=get_font("consola.ttf", 11))
    fd.text((30, hdr_h + 38), "Select an advisor for 1-on-1 academic or career consultation", fill=(148, 163, 184), font=get_font("segoeui.ttf", 12))
    
    # 3 Faculty Cards
    professors = [
        ("Dr. Mahfuz Rahman", "Software Engineering Faculty", "Today • 3:30 PM", (14, 165, 233)),
        ("Prof. Syeda Jahan", "Academic Affairs Advisor", "Tomorrow • 11:00 AM", (168, 85, 247)),
        ("Dr. Ahsan Kabir", "Algorithms & Research Lead", "Wed • 2:00 PM", (16, 185, 129))
    ]
    py = hdr_h + 75
    for name, dept, slot, col in professors:
        fd.rounded_rectangle([(30, py), (store_w - 30, py + 120)], radius=10, fill=(20, 32, 50), outline=(35, 52, 78), width=1)
        # Avatar
        fd.rounded_rectangle([(46, py + 18), (110, py + 82)], radius=8, fill=col)
        fd.text((58, py + 36), name.split()[-1][:2].upper(), fill=(255, 255, 255), font=get_font("segoeuib.ttf", 20))
        # Info
        fd.text((126, py + 18), name, fill=(248, 250, 252), font=get_font("segoeuib.ttf", 16))
        fd.text((126, py + 42), dept, fill=(148, 163, 184), font=get_font("segoeui.ttf", 13))
        fd.text((126, py + 68), f"● Available: {slot}", fill=(52, 211, 153), font=get_font("consola.ttf", 11))
        # Button
        fd.rounded_rectangle([(store_w - 200, py + 38), (store_w - 46, py + 78)], radius=6, fill=(14, 165, 233))
        fd.text((store_w - 186, py + 48), "Request Session", fill=(255, 255, 255), font=get_font("segoeuib.ttf", 12))
        py += 136

    # FAQ Search bar inside window
    fd.rounded_rectangle([(30, py + 10), (store_w - 30, py + 64)], radius=8, fill=(12, 20, 34), outline=(30, 48, 72), width=1)
    fd.text((50, py + 26), "Search campus policy, course retakes, GPA waivers...", fill=(100, 116, 139), font=get_font("segoeui.ttf", 13))

    sh_store, pad_s = add_drop_shadow(frame, blur_radius=40, offset=(0, 25), shadow_color=(0, 0, 0, 210))
    canvas.paste(sh_store, (780 - pad_s, 60 - pad_s), mask=sh_store)

    # 2. Overlaid Staggered Appointment Confirmed Card
    card_w, card_h = 410, 460
    app_card = Image.new("RGBA", (card_w, card_h), (12, 25, 42, 255))
    cd = ImageDraw.Draw(app_card)
    cd.rounded_rectangle([(0, 0), (card_w, card_h)], radius=12, fill=(12, 25, 42, 255), outline=(16, 185, 129), width=1)
    
    # Status
    cd.rounded_rectangle([(24, 24), (130, 52)], radius=6, fill=(6, 78, 59))
    cd.text((36, 30), "● CONFIRMED", fill=(52, 211, 153), font=get_font("consola.ttf", 11))
    
    cd.text((24, 75), "Academic Degree Guidance", fill=(248, 250, 252), font=get_font("segoeuib.ttf", 18))
    cd.text((24, 110), "Today • 14:30 PM", fill=(56, 189, 248), font=get_font("segoeuib.ttf", 26))
    
    cd.text((24, 160), "Advisor: Dr. Mahfuz Rahman", fill=(203, 213, 225), font=get_font("segoeuib.ttf", 14))
    cd.text((24, 186), "Room: CSE Department Faculty Wing B", fill=(148, 163, 184), font=get_font("segoeui.ttf", 13))
    cd.text((24, 210), "Session Mode: Hybrid (In-Person / Virtual Room)", fill=(148, 163, 184), font=get_font("segoeui.ttf", 12))

    cd.rounded_rectangle([(24, 250), (card_w - 24, 300)], radius=8, fill=(16, 185, 129))
    cd.text((card_w // 2 - 82, 266), "Enter Virtual Consultation", fill=(255, 255, 255), font=get_font("segoeuib.ttf", 13))

    cd.line([(24, 330), (card_w - 24, 330)], fill=(28, 48, 72), width=1)
    cd.text((24, 350), "CAMPUS ADVISORY", fill=(245, 158, 11), font=get_font("consola.ttf", 11))
    cd.text((24, 375), "Mid-term counseling hours extended through", fill=(203, 213, 225), font=get_font("segoeui.ttf", 12))
    cd.text((24, 395), "Thursday for all engineering undergraduates.", fill=(148, 163, 184), font=get_font("segoeui.ttf", 12))

    sh_card, pad_c = add_drop_shadow(app_card, blur_radius=42, offset=(0, 25), shadow_color=(0, 0, 0, 240))
    canvas.paste(sh_card, (1440 - pad_c, 410 - pad_c), mask=sh_card)

    # 3. Left Side: Brand Identity & Feature Callouts
    draw = ImageDraw.Draw(canvas)
    
    # Brand Header
    draw.text((80, 75), "CampusCare", fill=(255, 255, 255), font=get_font("segoeuib.ttf", 36))
    draw.text((82, 128), "UNIVERSITY STUDENT WELFARE & ADVISING", fill=(52, 211, 153), font=get_font("consola.ttf", 12))
    
    # Headline
    draw.text((80, 168), "Empowering Students With", fill=(255, 255, 255), font=get_font("segoeuib.ttf", 46))
    draw.text((80, 225), "Confidential Mentorship", fill=(52, 211, 153), font=get_font("segoeuib.ttf", 46))
    
    # Description
    draw.text((80, 292), "Centralized campus support hub connecting students with faculty advisors,", fill=(203, 213, 225), font=get_font("segoeui.ttf", 16))
    draw.text((80, 318), "confidential welfare grievance routing, and instant policy search.", fill=(148, 163, 184), font=get_font("segoeui.ttf", 16))
    
    # 4 Feature Cards
    features = [
        ("calendar", "1-on-1 Faculty Advisor Scheduler", "Live slot booking with automated calendar sync and room allocation.", (16, 185, 129)),
        ("shield", "Confidential Welfare Routing", "Encrypted student grievance triage routed directly to university deans.", (56, 189, 248)),
        ("search", "Smart Campus Knowledge Engine", "Instant search indexing waiver requirements, credit policies & FAQs.", (245, 158, 11)),
        ("bell", "Real-Time Advisory Broadcasts", "Push notifications for counseling deadlines, emergency aid & events.", (168, 85, 247))
    ]
    
    card_y = 365
    for icon_k, f_t, f_d, f_col in features:
        draw.rounded_rectangle([(80, card_y), (700, card_y + 66)], radius=12, fill=(12, 22, 38, 220), outline=(28, 44, 68), width=1)
        draw.rounded_rectangle([(96, card_y + 11), (140, card_y + 55)], radius=10, fill=(f_col[0], f_col[1], f_col[2], 30), outline=f_col, width=1)
        draw_icon(draw, icon_k, 118, card_y + 33, f_col)
        draw.text((156, card_y + 12), f_t, fill=(248, 250, 252), font=get_font("segoeuib.ttf", 15))
        draw.text((156, card_y + 36), f_d, fill=(148, 163, 184), font=get_font("segoeui.ttf", 13))
        card_y += 78

    # Production Metric Pill
    draw.rounded_rectangle([(80, 700), (700, 750)], radius=25, fill=(6, 78, 59, 190), outline=(16, 185, 129, 220), width=1)
    draw.ellipse([(100, 720), (110, 730)], fill=(52, 211, 153))
    draw.text((122, 716), "CAMPUS INFRASTRUCTURE: 1-ON-1 SESSIONS • ENCRYPTED GRIEVANCES • INSTANT", fill=(209, 250, 229), font=get_font("segoeuib.ttf", 13))
    
    # Workflow note
    f_flow = get_font("segoeuib.ttf", 15)
    draw.text((82, 780), "Search Knowledge Base", fill=(148, 163, 184), font=f_flow)
    draw_vector_arrow(draw, 255, 790, (16, 185, 129))
    draw.text((288, 780), "Select Faculty Advisor", fill=(248, 250, 252), font=f_flow)
    draw_vector_arrow(draw, 452, 790, (16, 185, 129))
    draw.text((485, 780), "Confirmed 1-on-1 Session", fill=(52, 211, 153), font=f_flow)

    out_path = os.path.join(PROJECT_ROOT, "public/projects/campus_welfare.jpg")
    final_rgb = Image.new("RGB", (W, H), (6, 15, 26))
    final_rgb.paste(canvas, (0, 0), mask=canvas)
    final_rgb.save(out_path, quality=95)
    print("campus_welfare.jpg rendered successfully")


# ==============================================================================
# 3. DEVROADMAP: Curriculum Scraper & Daily Habit Tracker
# ==============================================================================
def make_roadmap_tracker():
    canvas = Image.new("RGBA", (W, H), (10, 8, 22, 255))
    
    # Ambient cyberpunk violet glows
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([(850, 80), (1750, 950)], fill=(139, 92, 246, 32))
    gd.ellipse([(1200, 50), (1900, 700)], fill=(6, 182, 212, 28))
    glow = glow.filter(ImageFilter.GaussianBlur(140))
    canvas = Image.alpha_composite(canvas, glow)

    # 1. Right Side: Roadmap Node Graph Window
    store_w, store_h = 680, 640
    frame, hdr_h = make_browser_frame(store_w, store_h, "devroadmap.app/engineer", (22, 18, 38, 255))
    fd = ImageDraw.Draw(frame)
    
    fd.text((30, hdr_h + 18), "SYNCED CURRICULUM TRACKS", fill=(192, 132, 252), font=get_font("consola.ttf", 11))
    
    # 3 Track progress bars
    tracks = [
        ("Full-Stack Software Engineer", 0.84, "32/38 Topics", (168, 85, 247)),
        ("Data Engineering & Pipelines", 0.62, "18/29 Topics", (56, 189, 248)),
        ("Algorithms & LeetCode 75", 0.92, "69/75 Problems", (52, 211, 153))
    ]
    tx = 30
    for tname, tprog, tdetail, tcol in tracks:
        fd.rounded_rectangle([(tx, hdr_h + 45), (tx + 196, hdr_h + 125)], radius=8, fill=(30, 24, 52), outline=(55, 45, 90), width=1)
        fd.text((tx + 12, hdr_h + 55), tname[:16], fill=(248, 250, 252), font=get_font("segoeuib.ttf", 12))
        fd.text((tx + 12, hdr_h + 75), tdetail, fill=(148, 163, 184), font=get_font("segoeui.ttf", 11))
        # Bar
        fd.rounded_rectangle([(tx + 12, hdr_h + 100), (tx + 184, hdr_h + 108)], radius=4, fill=(15, 12, 26))
        fd.rounded_rectangle([(tx + 12, hdr_h + 100), (tx + 12 + int(172 * tprog), hdr_h + 108)], radius=4, fill=tcol)
        tx += 212

    # Roadmap Flow Pipeline
    fd.text((30, hdr_h + 155), "CURRICULUM PROGRESSION GRAPH", fill=(148, 163, 184), font=get_font("consola.ttf", 11))
    
    nodes = [
        ("RESTful Architecture & HTTP Verbs", "COMPLETED (Verified)", (16, 185, 129)),
        ("PostgreSQL Database Normalization", "COMPLETED (Verified)", (16, 185, 129)),
        ("B-Tree Indexing & Query Profiling", "IN PROGRESS (Daily Target)", (245, 158, 11)),
        ("Message Queues: Redis Streams / Kafka", "UPCOMING NEXT", (100, 116, 139))
    ]
    ny = hdr_h + 185
    for n_title, n_status, n_col in nodes:
        fd.rounded_rectangle([(30, ny), (store_w - 30, ny + 70)], radius=8, fill=(28, 22, 50), outline=(50, 40, 85), width=1)
        fd.text((50, ny + 12), n_status, fill=n_col, font=get_font("consola.ttf", 11))
        fd.text((50, ny + 34), n_title, fill=(248, 250, 252), font=get_font("segoeuib.ttf", 14))
        # Connecting line if not last
        if n_status != "UPCOMING NEXT":
            fd.line([(store_w // 2, ny + 70), (store_w // 2, ny + 85)], fill=(139, 92, 246), width=2)
        ny += 85

    sh_store, pad_s = add_drop_shadow(frame, blur_radius=40, offset=(0, 25), shadow_color=(0, 0, 0, 210))
    canvas.paste(sh_store, (780 - pad_s, 60 - pad_s), mask=sh_store)

    # 2. Overlaid Staggered 34-Day Streak & Heatmap Widget
    card_w, card_h = 410, 480
    streak_card = Image.new("RGBA", (card_w, card_h), (25, 18, 48, 255))
    cd = ImageDraw.Draw(streak_card)
    cd.rounded_rectangle([(0, 0), (card_w, card_h)], radius=12, fill=(25, 18, 48, 255), outline=(139, 92, 246), width=1)
    
    cd.text((24, 20), "CONSISTENCY STREAK", fill=(192, 132, 252), font=get_font("consola.ttf", 11))
    cd.text((24, 45), "34 Days Streak", fill=(248, 250, 252), font=get_font("segoeuib.ttf", 26))
    cd.text((24, 82), "Current Velocity: 4.8 Tasks/Day (Top 5% Consistency)", fill=(52, 211, 153), font=get_font("segoeui.ttf", 12))
    
    # 52-week commit grid preview
    cd.text((24, 115), "ANNUAL HABIT COMMIT MATRIX", fill=(148, 163, 184), font=get_font("consola.ttf", 10))
    gy = 138
    import random
    random.seed(42)
    for row in range(5):
        gx = 24
        for col in range(22):
            v = random.choice([0, 1, 2, 3, 4])
            c_fill = [(35, 28, 62), (60, 40, 110), (100, 60, 170), (139, 92, 246), (192, 132, 252)][v]
            cd.rounded_rectangle([(gx, gy), (gx + 12, gy + 12)], radius=2, fill=c_fill)
            gx += 16
        gy += 16

    # Daily checklist
    cd.line([(24, 240), (card_w - 24, 240)], fill=(50, 38, 80), width=1)
    cd.text((24, 255), "TODAY'S HABIT MILESTONES", fill=(192, 132, 252), font=get_font("consola.ttf", 10))
    
    todos = [
        ("[x] Solve 2 LeetCode Tree Problems", True),
        ("[x] Review B-Tree Indexing Specs", True),
        ("[x] Read System Design Primer Chapter", True),
        ("[ ] Implement Redis Stream Worker", False)
    ]
    ty = 280
    for todo, done in todos:
        bg = (16, 70, 50) if done else (35, 26, 60)
        col = (52, 211, 153) if done else (203, 213, 225)
        cd.rounded_rectangle([(24, ty), (card_w - 24, ty + 38)], radius=6, fill=bg, outline=(65, 48, 105), width=1)
        cd.text((38, ty + 10), todo, fill=col, font=get_font("segoeui.ttf", 12))
        ty += 46

    sh_card, pad_c = add_drop_shadow(streak_card, blur_radius=42, offset=(0, 25), shadow_color=(0, 0, 0, 240))
    canvas.paste(sh_card, (1440 - pad_c, 390 - pad_c), mask=sh_card)

    # 3. Left Side: Brand Identity & Feature Callouts
    draw = ImageDraw.Draw(canvas)
    
    # Brand Header
    draw.text((80, 75), "DevRoadmap", fill=(255, 255, 255), font=get_font("segoeuib.ttf", 36))
    draw.text((82, 128), "AUTOMATED CURRICULUM & HABIT ENGINE", fill=(192, 132, 252), font=get_font("consola.ttf", 12))
    
    # Headline
    draw.text((80, 168), "Master Any Tech Stack with", fill=(255, 255, 255), font=get_font("segoeuib.ttf", 46))
    draw.text((80, 225), "Daily Habit Streaks", fill=(192, 132, 252), font=get_font("segoeuib.ttf", 46))
    
    # Description
    draw.text((80, 292), "Curriculum parser scraping technical developer roadmaps into actionable", fill=(203, 213, 225), font=get_font("segoeui.ttf", 16))
    draw.text((80, 318), "daily milestones, habit streaks, and GitHub-style progress heatmaps.", fill=(148, 163, 184), font=get_font("segoeui.ttf", 16))
    
    # 4 Feature Cards
    features = [
        ("terminal", "Automated Roadmap Scraper", "Parses complex full-stack & data engineering curricula into nodes.", (168, 85, 247)),
        ("grid", "52-Week Consistency Heatmap", "GitHub-style interactive commitment matrix tracking annual velocity.", (52, 211, 153)),
        ("check", "Actionable Daily Checklists", "Bite-sized milestone generation with instantaneous LocalStorage sync.", (56, 189, 248)),
        ("flame", "Habit Streaks & Velocity", "Streak protection engine with milestone completion percentage graphs.", (245, 158, 11))
    ]
    
    card_y = 365
    for icon_k, f_t, f_d, f_col in features:
        draw.rounded_rectangle([(80, card_y), (700, card_y + 66)], radius=12, fill=(22, 18, 42, 220), outline=(48, 38, 78), width=1)
        draw.rounded_rectangle([(96, card_y + 11), (140, card_y + 55)], radius=10, fill=(f_col[0], f_col[1], f_col[2], 30), outline=f_col, width=1)
        draw_icon(draw, icon_k, 118, card_y + 33, f_col)
        draw.text((156, card_y + 12), f_t, fill=(248, 250, 252), font=get_font("segoeuib.ttf", 15))
        draw.text((156, card_y + 36), f_d, fill=(148, 163, 184), font=get_font("segoeui.ttf", 13))
        card_y += 78

    # Production Metric Pill
    draw.rounded_rectangle([(80, 700), (700, 750)], radius=25, fill=(45, 22, 75, 190), outline=(168, 85, 247, 220), width=1)
    draw.ellipse([(100, 720), (110, 730)], fill=(192, 132, 252))
    draw.text((122, 716), "PRODUCTIVITY ENGINE: ROADMAP PARSER • 34-DAY STREAK • ZERO DATA LOSS", fill=(243, 232, 255), font=get_font("segoeuib.ttf", 13))
    
    # Workflow note
    f_flow = get_font("segoeuib.ttf", 15)
    draw.text((82, 780), "Scrape Roadmap", fill=(148, 163, 184), font=f_flow)
    draw_vector_arrow(draw, 218, 790, (192, 132, 252))
    draw.text((252, 780), "Generate Daily Tasks", fill=(248, 250, 252), font=f_flow)
    draw_vector_arrow(draw, 426, 790, (192, 132, 252))
    draw.text((458, 780), "Build 365-Day Consistency", fill=(192, 132, 252), font=f_flow)

    out_path = os.path.join(PROJECT_ROOT, "public/projects/roadmap_tracker.jpg")
    final_rgb = Image.new("RGB", (W, H), (10, 8, 22))
    final_rgb.paste(canvas, (0, 0), mask=canvas)
    final_rgb.save(out_path, quality=95)
    print("roadmap_tracker.jpg rendered successfully")


# ==============================================================================
# 4. AUDIOFORGE & DISPLAYSYNC: Win32 Hardware Utilities Suite
# ==============================================================================
def make_hardware_suite():
    canvas = Image.new("RGBA", (W, H), (7, 16, 20, 255))
    
    # Ambient hardware teal glows
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([(850, 80), (1750, 950)], fill=(20, 184, 166, 32))
    gd.ellipse([(1200, 50), (1900, 700)], fill=(245, 158, 11, 24))
    glow = glow.filter(ImageFilter.GaussianBlur(140))
    canvas = Image.alpha_composite(canvas, glow)

    # 1. Right Side: Parametric Equalizer Studio Window
    store_w, store_h = 680, 640
    frame, hdr_h = make_browser_frame(store_w, store_h, "AudioForge DSP Studio • Equalizer APO Win32", (18, 30, 36, 255))
    fd = ImageDraw.Draw(frame)
    
    fd.text((30, hdr_h + 18), "EQUALIZER APO 10-BAND PARAMETRIC CALIBRATION", fill=(45, 212, 191), font=get_font("consola.ttf", 11))
    
    # 10 Vertical EQ Sliders
    bands = [
        ("32Hz", 6), ("64Hz", 8), ("125Hz", 4), ("250Hz", 1), ("500Hz", -2),
        ("1kHz", 0), ("2kHz", 3), ("4kHz", 7), ("8kHz", 9), ("16kHz", 8)
    ]
    sx = 42
    track_top = hdr_h + 55
    track_bot = hdr_h + 380
    track_h = track_bot - track_top
    mid_y = track_top + track_h // 2
    
    for freq, db in bands:
        fd.line([(sx + 24, track_top), (sx + 24, track_bot)], fill=(32, 50, 60), width=3)
        # 0dB line indicator
        fd.line([(sx + 14, mid_y), (sx + 34, mid_y)], fill=(50, 75, 88), width=1)
        # Thumb position
        norm = (db + 12) / 24.0
        thumb_y = int(track_bot - norm * track_h)
        # Active track bar
        fd.line([(sx + 24, mid_y), (sx + 24, thumb_y)], fill=(45, 212, 191), width=4)
        # Thumb handle
        fd.rounded_rectangle([(sx + 8, thumb_y - 8), (sx + 40, thumb_y + 8)], radius=4, fill=(45, 212, 191))
        # dB readout
        fd.text((sx + 12, thumb_y - 24), f"+{db}dB" if db > 0 else f"{db}dB", fill=(248, 250, 252), font=get_font("consola.ttf", 10))
        # Freq label
        fd.text((sx + 8, track_bot + 12), freq, fill=(148, 163, 184), font=get_font("consola.ttf", 10))
        sx += 60

    # DSP Status bar inside window
    fd.rounded_rectangle([(30, hdr_h + 430), (store_w - 30, hdr_h + 500)], radius=8, fill=(12, 22, 28), outline=(25, 45, 55), width=1)
    fd.text((46, hdr_h + 445), "● DSP Status: Active (Low-latency 64-bit float convolution stream • 0.8ms buffer)", fill=(45, 212, 191), font=get_font("consola.ttf", 11))
    fd.text((46, hdr_h + 468), "Output: High Definition Audio Device (24-bit / 96000 Hz Studio Quality Output)", fill=(148, 163, 184), font=get_font("segoeui.ttf", 12))

    # Audio Preset Pills
    px = 30
    for preset in ["Acoustic Studio", "Bass Boost Sub-H", "Spatial Gaming 3D", "Clear Vocal Pod"]:
        fd.rounded_rectangle([(px, hdr_h + 520), (px + 144, hdr_h + 560)], radius=6, fill=(20, 36, 44), outline=(35, 60, 72), width=1)
        fd.text((px + 16, hdr_h + 532), preset, fill=(248, 250, 252), font=get_font("segoeui.ttf", 11))
        px += 156

    sh_store, pad_s = add_drop_shadow(frame, blur_radius=40, offset=(0, 25), shadow_color=(0, 0, 0, 210))
    canvas.paste(sh_store, (780 - pad_s, 60 - pad_s), mask=sh_store)

    # 2. Overlaid Staggered DDC/CI Hardware Monitor Controller Card
    card_w, card_h = 420, 480
    ddc_card = Image.new("RGBA", (card_w, card_h), (14, 25, 30, 255))
    cd = ImageDraw.Draw(ddc_card)
    cd.rounded_rectangle([(0, 0), (card_w, card_h)], radius=12, fill=(14, 25, 30, 255), outline=(45, 212, 191), width=1)
    
    cd.text((24, 20), "DDC/CI HARDWARE MONITOR CONTROLLER", fill=(45, 212, 191), font=get_font("consola.ttf", 10))
    
    # Monitor 1
    cd.rounded_rectangle([(24, 45), (card_w - 24, 205)], radius=8, fill=(20, 36, 44), outline=(32, 58, 68), width=1)
    cd.text((38, 56), "MONITOR 1 • Primary Display", fill=(45, 212, 191), font=get_font("consola.ttf", 10))
    cd.text((38, 76), "27\" IPS 144Hz Gaming & Color Panel", fill=(248, 250, 252), font=get_font("segoeuib.ttf", 13))
    cd.text((38, 102), "Brightness: 75%", fill=(203, 213, 225), font=get_font("segoeui.ttf", 11))
    cd.rounded_rectangle([(38, 120), (card_w - 38, 130)], radius=4, fill=(10, 18, 22))
    cd.rounded_rectangle([(38, 120), (38 + int(344 * 0.75), 130)], radius=4, fill=(45, 212, 191))
    cd.text((38, 145), "Contrast: 70%", fill=(203, 213, 225), font=get_font("segoeui.ttf", 11))
    cd.rounded_rectangle([(38, 162), (card_w - 38, 172)], radius=4, fill=(10, 18, 22))
    cd.rounded_rectangle([(38, 162), (38 + int(344 * 0.70), 172)], radius=4, fill=(59, 130, 246))
    cd.text((38, 185), "Color Profile: D65 sRGB Calibrated (Gamma 2.2)", fill=(100, 116, 139), font=get_font("consola.ttf", 10))

    # Monitor 2
    cd.rounded_rectangle([(24, 220), (card_w - 24, 380)], radius=8, fill=(20, 36, 44), outline=(32, 58, 68), width=1)
    cd.text((38, 230), "MONITOR 2 • Secondary Display", fill=(245, 158, 11), font=get_font("consola.ttf", 10))
    cd.text((38, 250), "24\" Vertical Code & Document Panel", fill=(248, 250, 252), font=get_font("segoeuib.ttf", 13))
    cd.text((38, 276), "Brightness: 60% (Reading Mode)", fill=(203, 213, 225), font=get_font("segoeui.ttf", 11))
    cd.rounded_rectangle([(38, 294), (card_w - 38, 304)], radius=4, fill=(10, 18, 22))
    cd.rounded_rectangle([(38, 294), (38 + int(344 * 0.60), 304)], radius=4, fill=(245, 158, 11))
    cd.text((38, 320), "Night Shift: 4500K Warm Light Activated", fill=(251, 191, 36), font=get_font("consola.ttf", 10))

    # Sync Button
    cd.rounded_rectangle([(24, 400), (card_w - 24, 450)], radius=8, fill=(13, 148, 136))
    cd.text((card_w // 2 - 95, 416), "Sync Multi-Display Color Balance", fill=(255, 255, 255), font=get_font("segoeuib.ttf", 12))

    sh_card, pad_c = add_drop_shadow(ddc_card, blur_radius=42, offset=(0, 25), shadow_color=(0, 0, 0, 240))
    canvas.paste(sh_card, (1440 - pad_c, 390 - pad_c), mask=sh_card)

    # 3. Left Side: Brand Identity & Feature Callouts
    draw = ImageDraw.Draw(canvas)
    
    # Brand Header
    draw.text((80, 75), "AudioForge & DisplaySync", fill=(255, 255, 255), font=get_font("segoeuib.ttf", 36))
    draw.text((82, 128), "WIN32 KERNEL & HARDWARE ENGINE", fill=(45, 212, 191), font=get_font("consola.ttf", 12))
    
    # Headline
    draw.text((80, 168), "Studio Sound Calibration &", fill=(255, 255, 255), font=get_font("segoeuib.ttf", 46))
    draw.text((80, 225), "Multi-Display Precision", fill=(45, 212, 191), font=get_font("segoeuib.ttf", 46))
    
    # Description
    draw.text((80, 292), "Native desktop system utilities pairing an Equalizer APO parametric", fill=(203, 213, 225), font=get_font("segoeui.ttf", 16))
    draw.text((80, 318), "sound calibrator with dual-monitor DDC/CI hardware brightness control.", fill=(148, 163, 184), font=get_font("segoeui.ttf", 16))
    
    # 4 Feature Cards
    features = [
        ("sliders", "10-Band Parametric Equalizer", "Equalizer APO convolution stream with custom frequency Q-factors.", (45, 212, 191)),
        ("monitor", "DDC/CI Hardware I2C Controller", "Direct monitor communication for brightness, contrast & gain sync.", (56, 189, 248)),
        ("shield", "Low-Latency 64-Bit DSP Stream", "Audiophile-grade 0.8ms buffer convolution for glitch-free audio.", (52, 211, 153)),
        ("sun", "Automated Color Temperature Sync", "Harmonizes white point & warm night shift across mismatched panels.", (245, 158, 11))
    ]
    
    card_y = 365
    for icon_k, f_t, f_d, f_col in features:
        draw.rounded_rectangle([(80, card_y), (700, card_y + 66)], radius=12, fill=(16, 28, 36, 220), outline=(30, 52, 64), width=1)
        draw.rounded_rectangle([(96, card_y + 11), (140, card_y + 55)], radius=10, fill=(f_col[0], f_col[1], f_col[2], 30), outline=f_col, width=1)
        draw_icon(draw, icon_k, 118, card_y + 33, f_col)
        draw.text((156, card_y + 12), f_t, fill=(248, 250, 252), font=get_font("segoeuib.ttf", 15))
        draw.text((156, card_y + 36), f_d, fill=(148, 163, 184), font=get_font("segoeui.ttf", 13))
        card_y += 78

    # Production Metric Pill
    draw.rounded_rectangle([(80, 700), (700, 750)], radius=25, fill=(10, 45, 48, 190), outline=(45, 212, 191, 220), width=1)
    draw.ellipse([(100, 720), (110, 730)], fill=(45, 212, 191))
    draw.text((122, 716), "WIN32 HARDWARE SUITE: 64-BIT FLOAT DSP • DDC/CI PROTOCOL • 0.8MS BUFFER", fill=(204, 251, 241), font=get_font("segoeuib.ttf", 13))
    
    # Workflow note
    f_flow = get_font("segoeuib.ttf", 15)
    draw.text((82, 780), "Parametric EQ Tuning", fill=(148, 163, 184), font=f_flow)
    draw_vector_arrow(draw, 252, 790, (45, 212, 191))
    draw.text((285, 780), "DDC/CI Hardware Sync", fill=(248, 250, 252), font=f_flow)
    draw_vector_arrow(draw, 470, 790, (45, 212, 191))
    draw.text((502, 780), "Studio Precision Setup", fill=(45, 212, 191), font=f_flow)

    out_path = os.path.join(PROJECT_ROOT, "public/projects/hardware_suite.jpg")
    final_rgb = Image.new("RGB", (W, H), (7, 16, 20))
    final_rgb.paste(canvas, (0, 0), mask=canvas)
    final_rgb.save(out_path, quality=95)
    print("hardware_suite.jpg rendered successfully")


if __name__ == "__main__":
    make_piecestyle()
    make_campus_welfare()
    make_roadmap_tracker()
    make_hardware_suite()

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Canvas: 1920x1080 (16:9 Full HD)
W, H = 1920, 1080

def get_font(name="segoeuib.ttf", size=24):
    font_paths = [
        f"C:/Windows/Fonts/{name}",
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
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

def create_rounded_mask(size, radius):
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), size], radius=radius, fill=255)
    return mask

def draw_vector_lock(draw, x, y):
    draw.arc([(x + 2, y - 5), (x + 8, y + 3)], 180, 0, fill=(148, 163, 184), width=2)
    draw.rounded_rectangle([(x, y + 1), (x + 10, y + 9)], radius=2, fill=(245, 158, 11))

def draw_vector_arrow(draw, x, y, col=(245, 158, 11)):
    draw.line([(x, y), (x + 14, y)], fill=col, width=2)
    draw.polygon([(x + 14, y - 4), (x + 20, y), (x + 14, y + 4)], fill=col)

def make_browser_frame(content_img, title_url="refc.online", scale_w=600):
    aspect = content_img.height / content_img.width
    cw = scale_w
    ch = int(cw * aspect)
    content_scaled = content_img.resize((cw, ch), Image.Resampling.LANCZOS)
    
    header_h = 36
    frame_w = cw
    frame_h = ch + header_h
    
    frame = Image.new("RGBA", (frame_w, frame_h), (11, 15, 25, 255))
    draw = ImageDraw.Draw(frame)
    
    # Top bar background
    draw.rounded_rectangle([(0, 0), (frame_w, frame_h)], radius=12, fill=(11, 15, 25, 255))
    draw.rectangle([(0, header_h - 8), (frame_w, header_h)], fill=(11, 15, 25, 255))
    
    # Traffic light dots
    draw.ellipse([(14, 13), (22, 21)], fill=(239, 68, 68))
    draw.ellipse([(28, 13), (36, 21)], fill=(245, 158, 11))
    draw.ellipse([(42, 13), (50, 21)], fill=(16, 185, 129))
    
    # URL pill
    url_box = [(72, 7), (frame_w - 72, 29)]
    draw.rounded_rectangle(url_box, radius=6, fill=(20, 26, 38), outline=(45, 55, 75), width=1)
    
    # Vector Lock Icon
    draw_vector_lock(draw, 84, 15)
    
    f_url = get_font("consola.ttf", 11)
    draw.text((100, 11), title_url, fill=(148, 163, 184), font=f_url)
    
    frame.paste(content_scaled, (0, header_h))
    
    # Outer stroke & rounded corners
    final_mask = create_rounded_mask((frame_w, frame_h), 12)
    rounded_frame = Image.new("RGBA", (frame_w, frame_h), (0, 0, 0, 0))
    rounded_frame.paste(frame, (0, 0), mask=final_mask)
    
    r_draw = ImageDraw.Draw(rounded_frame)
    r_draw.rounded_rectangle([(0, 0), (frame_w - 1, frame_h - 1)], radius=12, outline=(65, 75, 95, 220), width=1)
    
    return rounded_frame

def add_drop_shadow(img, blur_radius=35, offset=(0, 20), shadow_color=(0, 0, 0, 210)):
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

def draw_vector_icon(draw, kind, cx, cy):
    if kind == "lightning":
        # Cyan lightning bolt
        pts = [
            (cx + 3, cy - 13),
            (cx - 7, cy + 1),
            (cx - 1, cy + 1),
            (cx - 3, cy + 13),
            (cx + 7, cy - 1),
            (cx + 1, cy - 1)
        ]
        draw.polygon(pts, fill=(56, 189, 248))
    elif kind == "trophy":
        # Gold trophy cup
        draw.polygon([(cx - 8, cy - 10), (cx + 8, cy - 10), (cx + 7, cy + 1), (cx, cy + 6), (cx - 7, cy + 1)], fill=(245, 158, 11))
        draw.rectangle([(cx - 2, cy + 6), (cx + 2, cy + 11)], fill=(245, 158, 11))
        draw.rectangle([(cx - 8, cy + 11), (cx + 8, cy + 13)], fill=(245, 158, 11))
        draw.arc([(cx - 11, cy - 9), (cx - 5, cy - 2)], 90, 270, fill=(245, 158, 11), width=2)
        draw.arc([(cx + 5, cy - 9), (cx + 11, cy - 2)], 270, 90, fill=(245, 158, 11), width=2)
    elif kind == "chart":
        # Emerald bar chart
        draw.rectangle([(cx - 9, cy + 2), (cx - 5, cy + 12)], fill=(52, 211, 153))
        draw.rectangle([(cx - 2, cy - 4), (cx + 2, cy + 12)], fill=(52, 211, 153))
        draw.rectangle([(cx + 5, cy - 10), (cx + 9, cy + 12)], fill=(52, 211, 153))
    elif kind == "shield":
        # Purple security shield with check
        draw.polygon([(cx - 8, cy - 10), (cx + 8, cy - 10), (cx + 8, cy + 1), (cx, cy + 13), (cx - 8, cy + 1)], fill=(192, 132, 252))
        draw.line([(cx - 4, cy + 1), (cx - 1, cy + 4), (cx + 4, cy - 3)], fill=(15, 23, 42), width=2)

def build_banner():
    # 1. Background Canvas (Deep Cinematic Esports Navy)
    canvas = Image.new("RGBA", (W, H), (7, 10, 18, 255))
    
    # Ambient Radial Glows
    glow1 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g1 = ImageDraw.Draw(glow1)
    g1.ellipse([(60, -180), (850, 600)], fill=(37, 99, 235, 52))
    glow1 = glow1.filter(ImageFilter.GaussianBlur(130))
    canvas = Image.alpha_composite(canvas, glow1)
    
    glow2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g2 = ImageDraw.Draw(glow2)
    g2.ellipse([(1150, 220), (1850, 920)], fill=(245, 158, 11, 28))
    g2.ellipse([(1300, 60), (1950, 680)], fill=(6, 182, 212, 35))
    glow2 = glow2.filter(ImageFilter.GaussianBlur(150))
    canvas = Image.alpha_composite(canvas, glow2)
    
    # Subtle Technical Grid Overlay
    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid)
    for x in range(0, W, 48):
        gd.line([(x, 0), (x, H)], fill=(255, 255, 255, 6), width=1)
    for y in range(0, H, 48):
        gd.line([(0, y), (W, y)], fill=(255, 255, 255, 6), width=1)
    canvas = Image.alpha_composite(canvas, grid)

    # 2. Load ALL 4 REFC Screenshots
    img_hero = Image.open(os.path.join(PROJECT_ROOT, 'public/Project_Images/Refc/WhatsApp Image 2026-09-09 at 2.17.03 AM3.jpeg'))
    img_table = Image.open(os.path.join(PROJECT_ROOT, 'public/Project_Images/Refc/WhatsApp Image 2026-09-09 at 2.17.03 AM11.jpeg'))
    img_matches = Image.open(os.path.join(PROJECT_ROOT, 'public/Project_Images/Refc/WhatsApp Image 2026-09-09 at 2.17.03 AM1.jpeg'))
    img_admin = Image.open(os.path.join(PROJECT_ROOT, 'public/Project_Images/Refc/WhatsApp Image 2026-09-09 at 2.17.03 AM.jpeg'))

    # Quad-Display Layout (Harmonious Staggered 2x2 Showcase):
    # Top-Left: Hero Landing Hub (refc.online)
    frame_hero = make_browser_frame(img_hero, title_url="refc.online/tournament-hub", scale_w=580)
    shadow_hero, pad_h = add_drop_shadow(frame_hero, blur_radius=35, offset=(0, 20), shadow_color=(0, 0, 0, 190))
    canvas.paste(shadow_hero, (740 - pad_h, 55 - pad_h), mask=shadow_hero)
    
    # Top-Right: Points Table & Standings (refc.online/standings)
    frame_table = make_browser_frame(img_table, title_url="refc.online/standings", scale_w=560)
    shadow_table, pad_t = add_drop_shadow(frame_table, blur_radius=35, offset=(0, 20), shadow_color=(0, 0, 0, 190))
    canvas.paste(shadow_table, (1330 - pad_t, 55 - pad_t), mask=shadow_table)
    
    # Bottom-Left: Tournament Fixtures & Schedules (refc.online/matches)
    frame_matches = make_browser_frame(img_matches, title_url="refc.online/matches", scale_w=520)
    shadow_matches, pad_m = add_drop_shadow(frame_matches, blur_radius=35, offset=(0, 20), shadow_color=(0, 0, 0, 210))
    canvas.paste(shadow_matches, (740 - pad_m, 440 - pad_m), mask=shadow_matches)
    
    # Bottom-Right: Admin Control Hub with Revenue ৳56,930 (refc.online/admin)
    frame_admin = make_browser_frame(img_admin, title_url="refc.online/admin/overview", scale_w=620)
    shadow_admin, pad_a = add_drop_shadow(frame_admin, blur_radius=40, offset=(0, 25), shadow_color=(0, 0, 0, 230))
    canvas.paste(shadow_admin, (1270 - pad_a, 500 - pad_a), mask=shadow_admin)

    # 3. Left Side: Typography, Brand Identity & Feature Callouts
    draw = ImageDraw.Draw(canvas)
    
    # Brand Header: Clean 100% Transparent REFC Logo Floating on Canvas (No Box!)
    logo_clean = Image.open(os.path.join(PROJECT_ROOT, 'public/Project_Images/Refc/refc_logo_clean.png'))
    lw, lh = int(logo_clean.width * 1.5), int(logo_clean.height * 1.5)
    logo_scaled = logo_clean.resize((lw, lh), Image.Resampling.LANCZOS)
    canvas.paste(logo_scaled, (80, 60), mask=logo_scaled)
    
    # Brand Sub-label directly beneath logo (Matching Attenvo "FACIAL RECOGNITION ATTENDANCE")
    f_sub_brand = get_font("consola.ttf", 12)
    draw.text((82, 134), "AUTOMATED ESPORTS INFRASTRUCTURE", fill=(245, 158, 11), font=f_sub_brand)
    
    # Headline (Bold, Clean, Punchy)
    f_h1 = get_font("segoeuib.ttf", 46)
    draw.text((80, 168), "Automated Esports", fill=(255, 255, 255), font=f_h1)
    draw.text((80, 225), "Tournament Platform", fill=(56, 189, 248), font=f_h1)
    
    # Description
    f_desc = get_font("segoeui.ttf", 16)
    draw.text((80, 292), "End-to-end competition infrastructure for eFootball managing live match", fill=(203, 213, 225), font=f_desc)
    draw.text((80, 318), "submissions, automated brackets, tiebreakers, and club standings.", fill=(148, 163, 184), font=f_desc)
    
    # 4 Feature Badges (Matching the Attenvo style with real vector icons!)
    features = [
        ("lightning", "Real-Time Data Pipelines", "Instant score submission & automated tiebreaker logic.", (14, 165, 233)),
        ("trophy", "Automated Bracket Progression", "Solo (1v1), double-elimination & multi-tier group stages.", (245, 158, 11)),
        ("chart", "Live Team Standings Table", "Real-time goal difference & dynamic club ranking matrices.", (16, 185, 129)),
        ("shield", "Production Admin Control Hub", "Complete audit logs, payment tracking & player rosters.", (168, 85, 247))
    ]
    
    card_y = 365
    for icon_kind, f_title, f_detail, f_accent in features:
        # Card container
        draw.rounded_rectangle([(80, card_y), (700, card_y + 66)], radius=12, fill=(15, 23, 42, 220), outline=(35, 45, 65), width=1)
        
        # Icon badge
        badge_box = [(96, card_y + 11), (140, card_y + 55)]
        draw.rounded_rectangle(badge_box, radius=10, fill=(f_accent[0], f_accent[1], f_accent[2], 30), outline=f_accent, width=1)
        
        # Vector Icon
        draw_vector_icon(draw, icon_kind, 118, card_y + 33)
        
        # Text
        draw.text((156, card_y + 12), f_title, fill=(248, 250, 252), font=get_font("segoeuib.ttf", 15))
        draw.text((156, card_y + 36), f_detail, fill=(148, 163, 184), font=get_font("segoeui.ttf", 13))
        
        card_y += 78
        
    # Production Metric Pill at Bottom
    draw.rounded_rectangle([(80, 700), (700, 750)], radius=25, fill=(6, 78, 59, 190), outline=(16, 185, 129, 220), width=1)
    # Pulsing live dot
    draw.ellipse([(100, 720), (110, 730)], fill=(52, 211, 153))
    f_pill = get_font("segoeuib.ttf", 13)
    draw.text((122, 716), "LIVE PRODUCTION: 1,180+ PLAYERS • 21 TOURNAMENTS • BDT 56K+ REVENUE", fill=(209, 250, 229), font=f_pill)
    
    # Workflow Progression Arrow Note with clean Vector Arrows
    f_flow = get_font("segoeuib.ttf", 15)
    draw.text((82, 780), "Match Report", fill=(148, 163, 184), font=f_flow)
    draw_vector_arrow(draw, 192, 790)
    draw.text((226, 780), "Instant Tiebreaker", fill=(248, 250, 252), font=f_flow)
    draw_vector_arrow(draw, 385, 790)
    draw.text((418, 780), "Auto Bracket Advancement", fill=(56, 189, 248), font=f_flow)
    
    # Save the master banner image
    output_path = os.path.join(PROJECT_ROOT, "public/projects/refc.jpg")
    final_rgb = Image.new("RGB", (W, H), (7, 10, 18))
    final_rgb.paste(canvas, (0, 0), mask=canvas)
    final_rgb.save(output_path, quality=95)
    print(f"REFC 4-Screen banner with 100% transparent logo generated successfully at: {output_path}")

if __name__ == "__main__":
    build_banner()

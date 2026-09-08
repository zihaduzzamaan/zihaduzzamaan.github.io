"""
Attenvo Mockup Banner Builder
Converts the Attenvo showcase graphic into a crisp 16:9 (1920x1080) high-resolution banner.
Seamlessly continues the branded pastel lavender wave and ensures zero clipping of phones or typography.
"""

import os
from PIL import Image, ImageFilter

def build_attenvo_banner():
    # Source image candidates
    possible_sources = [
        os.path.abspath("C:/Users/ZISHAN/.gemini/antigravity-ide/brain/8de61dd1-6528-4b76-bb02-62e290992a26/.user_uploaded/media_1788899147097.jpg"),
        os.path.abspath("scratch/user_banner_copy.png"),
        os.path.abspath("public/projects/attenvo.jpg")
    ]
    
    src = None
    for p in possible_sources:
        if os.path.exists(p):
            src = p
            break
            
    if not src:
        raise FileNotFoundError("Attenvo source image not found.")

    orig = Image.open(src).convert("RGB")
    tw, th = 1920, 1080

    scale = th / orig.height
    nw = int(orig.width * scale)
    scaled = orig.resize((nw, th), Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (tw, th), (249, 250, 254))
    ox = (tw - nw) // 2

    # 1. Fill left margin (0 to ox) seamlessly with base tone
    for x in range(ox):
        for y in range(th):
            canvas.putpixel((x, y), scaled.getpixel((0, y)))

    # 2. Fill right margin (ox + nw to tw) by continuing the wave slope and pastel gradient
    right_edge_x = ox + nw
    for x in range(right_edge_x, tw):
        dx = x - right_edge_x
        # Natural continuation of the wave boundary slope (~0.685)
        boundary_y = int(554 + dx * 0.685)
        for y in range(th):
            if y < boundary_y:
                # Vertical lavender gradient
                t = y / max(1, boundary_y)
                r = int(232 * (1 - t) + 216 * t)
                g = int(233 * (1 - t) + 221 * t)
                b = int(253 * (1 - t) + 251 * t)
                canvas.putpixel((x, y), (r, g, b))
            else:
                canvas.putpixel((x, y), (249, 250, 254))

    # 3. Composite scaled image onto canvas
    canvas.paste(scaled, (ox, 0))

    # 4. Soft anti-aliasing along the right seam
    box = (right_edge_x - 5, 0, right_edge_x + 5, th)
    strip = canvas.crop(box).filter(ImageFilter.GaussianBlur(2))
    canvas.paste(strip, box)

    # Save to public/projects/attenvo.jpg
    out_dir = os.path.abspath("public/projects")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "attenvo.jpg")
    canvas.save(out_path, "JPEG", quality=96, optimize=True)
    print(f"Generated Attenvo 16:9 banner: {out_path} ({tw}x{th})")

if __name__ == "__main__":
    build_attenvo_banner()

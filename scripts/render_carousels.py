import os, sys, base64
sys.path.insert(0, "/home/claude/work")
from content import POSTS
from slides import carousel_pages, story
from playwright.sync_api import sync_playwright

OUT = "/home/claude/repos/raquetada-posts/semana-2"
only = sys.argv[1:]

def shot(pg, html, path, w, h):
    tmp = "/home/claude/work/tmp.html"
    open(tmp, "w").write(html)
    pg.set_viewport_size({"width": w, "height": h})
    pg.goto("file://" + tmp)
    pg.wait_for_function("window.__fit===true")
    pg.wait_for_timeout(150)
    pg.screenshot(path=path + ".png")
    from PIL import Image
    Image.open(path + ".png").convert("RGB").save(path, quality=92)
    os.remove(path + ".png")

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    for post in POSTS:
        if post["tipo"] != "carrossel": continue
        if only and not any(o in post["pasta"] for o in only): continue
        d = os.path.join(OUT, post["pasta"]); os.makedirs(d, exist_ok=True)
        pages = carousel_pages(post)
        for i, h in enumerate(pages, 1):
            shot(pg, h, f"{d}/slide-{i:02d}.jpg", 1080, 1350)
        thumb = "data:image/jpeg;base64," + base64.b64encode(open(f"{d}/slide-01.jpg", "rb").read()).decode()
        shot(pg, story(post, thumb), f"{d}/story.jpg", 1080, 1920)
        print("ok", post["pasta"], len(pages))
    b.close()

import re, base64, html as H

FONTDIR = "/home/claude/work/package/files"
BG = "#0B2D49"; LINE = "#153753"; PANEL = "#08243A"; CARD = "#12324F"; CARDB = "#24476A"
MUTED = "#8FA3B6"; WHITE = "#F4F6F8"
ACC = {"tenis": "#DAFF01", "bt": "#FF8A3D"}
ACC_DARK = {"tenis": "#7A9A1E", "bt": "#B85F28"}

def b64(p):
    return base64.b64encode(open(p, "rb").read()).decode()

LOGO_S = "data:image/png;base64," + b64(""+__import__("os").path.dirname(__file__)+"/assets/logo-small.png")
LOGO_B = "data:image/png;base64," + b64(""+__import__("os").path.dirname(__file__)+"/assets/logo-big-name.png")

def fontface():
    out = []
    for w in (500, 600, 700, 800, 900):
        out.append(f"@font-face{{font-family:M;font-weight:{w};src:url(file://{FONTDIR}/montserrat-latin-{w}-normal.woff2)}}")
        out.append(f"@font-face{{font-family:M;font-weight:{w};src:url(file://{FONTDIR}/montserrat-latin-ext-{w}-normal.woff2);unicode-range:U+0100-024F}}")
    return "\n".join(out)

def em(s):
    """*texto* -> destaque na cor de acento"""
    s = H.escape(s, quote=False)
    return re.sub(r"\*(.+?)\*", r'<span class="a">\1</span>', s)

def lines(arr):
    return "<br>".join(em(x) for x in arr)

# ---------------- ícones ----------------
def ic_ball(c, size=96):
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100"><circle cx="50" cy="50" r="46" fill="{c}"/>
<path d="M14 22 C38 34 38 66 14 78" stroke="{BG}" stroke-width="7" fill="none" stroke-linecap="round"/>
<path d="M86 22 C62 34 62 66 86 78" stroke="{BG}" stroke-width="7" fill="none" stroke-linecap="round"/></svg>'''

def ic_speedball(c, size=96):
    return f'''<div style="display:flex;align-items:center;gap:8px">
<svg width="{int(size*0.75)}" height="{size}" viewBox="0 0 75 100"><g stroke="{c}" stroke-width="9" stroke-linecap="round">
<line x1="6" y1="30" x2="64" y2="30"/><line x1="22" y1="50" x2="70" y2="50"/><line x1="34" y1="70" x2="70" y2="70"/></g></svg>{ic_ball(c,size)}</div>'''

def ic(name, c, size=40, sw=3.2):
    paths = {
      "bookmark": '<path d="M7 3h10v18l-5-4-5 4z"/>',
      "heart": f'<path d="M12 20s-7-4.4-8.6-9A4.6 4.6 0 0 1 12 6.6 4.6 4.6 0 0 1 20.6 11C19 15.6 12 20 12 20z" fill="{c}"/>',
      "send": '<path d="M21 3 3 10.5l7 2.5 2.5 7z"/><path d="M21 3 10 13"/>',
      "user": '<circle cx="9" cy="8" r="4"/><path d="M2 21c0-4 3-6 7-6s7 2 7 6"/><path d="M19 8v6M16 11h6"/>',
      "bulb": '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
      "check": f'<circle cx="12" cy="12" r="10" fill="{c}" stroke="none"/><path d="m7 12.5 3.2 3L17 8.8" stroke="{BG}" stroke-width="2.6"/>',
      "x": '<circle cx="12" cy="12" r="9.5"/><path d="m8.5 8.5 7 7M15.5 8.5l-7 7"/>',
      "info": f'<circle cx="12" cy="12" r="10" fill="{c}" stroke="none"/><path d="M12 11v6M12 7.2v.1" stroke="{BG}" stroke-width="2.6"/>',
      "ok": f'<path d="m5 12.5 4.5 4.5L19 7.5" stroke="{c}" stroke-width="3"/>',
      "arrowr": '<path d="M3 12h17M14 6l6 6-6 6"/>',
      "arrowd": '<path d="M12 3v17M6 14l6 6 6-6"/>',
      "chat": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 10.5h.1M12 10.5h.1M16 10.5h.1" stroke-width="3.2"/>',
    }
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{sw*24/size if size>40 else 2.2}" stroke-linecap="round" stroke-linejoin="round">{paths[name]}</svg>'

def big_icon(kind, acc):
    w = WHITE
    if kind == "raquete":
        strings = "".join(f'<line x1="{x}" y1="10" x2="{x}" y2="190" />' for x in range(30, 200, 18)) + \
                  "".join(f'<line x1="10" y1="{y}" x2="210" y2="{y}" />' for y in range(25, 200, 18))
        return f'''<svg width="400" height="640" viewBox="0 0 260 420"><g transform="rotate(-28 130 210)">
<defs><clipPath id="hd"><ellipse cx="110" cy="100" rx="88" ry="98"/></clipPath></defs>
<g clip-path="url(#hd)" stroke="{w}" stroke-width="3" opacity=".9">{strings}</g>
<ellipse cx="110" cy="100" rx="88" ry="98" fill="none" stroke="{w}" stroke-width="13"/>
<path d="M88 194 L100 236 M132 194 L120 236" stroke="{w}" stroke-width="11" fill="none"/>
<rect x="96" y="232" width="28" height="160" rx="10" fill="{w}"/>
<g stroke="{BG}" stroke-width="4">{"".join(f'<line x1="96" y1="{y}" x2="124" y2="{y+10}"/>' for y in range(290,390,16))}</g></g>
<g transform="translate(150 300)">{ic_ball(acc,90).replace("<svg ","<svg x='0' y='0' ")}</g></svg>'''
    if kind == "bola":
        return f'<div style="display:flex;flex-direction:column;align-items:center;gap:30px">{ic_ball(acc,300)}<div style="width:260px;height:26px;border-radius:50%;background:#061d30"></div></div>'
    if kind == "placar":
        cell = lambda t, c: f'<div style="width:96px;height:120px;border-radius:14px;background:{CARD};border:2px solid {CARDB};display:flex;align-items:center;justify-content:center;font:900 76px M;color:{c}">{t}</div>'
        row = lambda n, a, b, c: f'<div style="display:flex;gap:14px;align-items:center"><div style="width:90px;font:800 26px M;color:{MUTED};letter-spacing:2px">{n}</div>{cell(a,WHITE)}{cell(b,c)}</div>'
        return f'''<div style="display:flex;flex-direction:column;gap:22px;align-items:center">
<div style="font:800 24px M;letter-spacing:5px;color:{acc}">SET · TIE-BREAK</div>
{row("VOCÊ","6","6",acc)}{row("ADV","6","5",WHITE)}</div>'''
    if kind == "dupla":
        p = lambda c: f'<svg width="150" height="230" viewBox="0 0 150 230"><circle cx="75" cy="50" r="40" fill="{c}"/><path d="M5 225c0-60 30-100 70-100s70 40 70 100z" fill="{c}"/></svg>'
        bub = lambda t, c: f'<div style="padding:14px 22px;border-radius:22px;background:{c};font:900 30px M;color:{BG}">{t}</div>'
        return f'''<div style="display:flex;flex-direction:column;align-items:center;gap:26px">
<div style="display:flex;gap:30px">{bub("MINHA!",acc)}{bub("SUA!",WHITE)}</div>
<div style="display:flex;gap:40px">{p(acc)}{p(WHITE)}</div></div>'''
    if kind == "tenis":
        return f'''<svg width="400" height="300" viewBox="0 0 400 300">
<path d="M30 230 C30 170 60 120 120 110 L170 60 C190 45 215 50 225 70 L250 130 C300 140 360 160 375 200 L380 232 Z" fill="{w}"/>
<path d="M22 232 H388 V256 C388 266 380 272 370 272 H40 C30 272 22 266 22 256 Z" fill="{acc}"/>
<g stroke="{BG}" stroke-width="7" stroke-linecap="round"><line x1="160" y1="95" x2="200" y2="110"/><line x1="148" y1="118" x2="190" y2="133"/><line x1="136" y1="141" x2="178" y2="156"/></g>
<g stroke="{BG}" stroke-width="5">{"".join(f'<line x1="{x}" y1="240" x2="{x+12}" y2="266"/>' for x in range(50,380,26))}</g></svg>'''
    return ""

# ---------------- quadra ----------------
def court(elems, acc, w=400, h=740, label=True, show_net=True):
    # quadra vertical; margem interna
    mx, my = 36, 34
    cw, ch = w - 2*mx, h - 2*my
    X = lambda x: mx + x*cw
    Y = lambda y: my + y*ch
    s = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" overflow="visible">']
    s.append(f'<rect x="{mx}" y="{my}" width="{cw}" height="{ch}" fill="none" stroke="{WHITE}" stroke-width="3"/>')
    al = 0.125
    s.append(f'<line x1="{X(al)}" y1="{my}" x2="{X(al)}" y2="{my+ch}" stroke="{WHITE}" stroke-width="2.5"/>')
    s.append(f'<line x1="{X(1-al)}" y1="{my}" x2="{X(1-al)}" y2="{my+ch}" stroke="{WHITE}" stroke-width="2.5"/>')
    s.append(f'<line x1="{X(al)}" y1="{Y(0.23)}" x2="{X(1-al)}" y2="{Y(0.23)}" stroke="{WHITE}" stroke-width="2.5"/>')
    s.append(f'<line x1="{X(al)}" y1="{Y(0.77)}" x2="{X(1-al)}" y2="{Y(0.77)}" stroke="{WHITE}" stroke-width="2.5"/>')
    s.append(f'<line x1="{X(.5)}" y1="{Y(0.23)}" x2="{X(.5)}" y2="{Y(0.77)}" stroke="{WHITE}" stroke-width="2.5"/>')
    s.append(f'<line x1="{X(.5)}" y1="{my}" x2="{X(.5)}" y2="{my+12}" stroke="{WHITE}" stroke-width="2.5"/>')
    s.append(f'<line x1="{X(.5)}" y1="{my+ch-12}" x2="{X(.5)}" y2="{my+ch}" stroke="{WHITE}" stroke-width="2.5"/>')
    # zonas primeiro
    for e in elems:
        if e[0] == "zona":
            _, x1, y1, x2, y2, t = e
            s.append(f'<rect x="{X(x1)}" y="{Y(y1)}" width="{X(x2)-X(x1)}" height="{Y(y2)-Y(y1)}" fill="{acc}" fill-opacity=".22" stroke="{acc}" stroke-width="2.5" stroke-dasharray="7 5"/>')
            if label:
                s.append(f'<text x="{X(x1)+8}" y="{Y(y1)+24}" font-family="M" font-weight="800" font-size="17" fill="{acc}">{H.escape(t)}</text>')
    # rede
    if show_net:
        s.append(f'<line x1="{mx-22}" y1="{Y(.5)}" x2="{mx+cw+22}" y2="{Y(.5)}" stroke="{WHITE}" stroke-width="3" stroke-dasharray="2 4"/>')
        s.append(f'<circle cx="{mx-22}" cy="{Y(.5)}" r="5" fill="{WHITE}"/><circle cx="{mx+cw+22}" cy="{Y(.5)}" r="5" fill="{WHITE}"/>')
    for i, e in enumerate(elems):
        if e[0] == "bola":
            _, x1, y1, x2, y2 = e
            ax, ay, bx, by = X(x1), Y(y1), X(x2), Y(y2)
            s.append(f'<defs><marker id="ah{i}" markerWidth="10" markerHeight="10" refX="5" refY="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="{acc}"/></marker></defs>')
            s.append(f'<line class="ball" x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{acc}" stroke-width="4" stroke-dasharray="12 8" marker-end="url(#ah{i})"/>')
    for e in elems:
        if e[0] == "eu":
            s.append(f'<circle cx="{X(e[1])}" cy="{Y(e[2])}" r="21" fill="{acc}"/>')
        elif e[0] == "par":
            s.append(f'<circle cx="{X(e[1])}" cy="{Y(e[2])}" r="21" fill="{acc}" fill-opacity=".55"/>')
        elif e[0] == "adv":
            s.append(f'<circle cx="{X(e[1])}" cy="{Y(e[2])}" r="20" fill="none" stroke="{WHITE}" stroke-width="4"/>')
    s.append("</svg>")
    return "".join(s)

def legend(acc):
    return f'''<div class="legend"><span><i style="background:{acc}"></i>Você</span><span><i style="border:3px solid {WHITE}"></i>Adversário</span><span><b style="border-top:3px dashed {acc}"></b>Bola</span></div>'''

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:%(W)dpx;height:%(Hh)dpx;overflow:hidden}
body{background:%(BG)s;font-family:M;color:%(WHITE)s;position:relative;-webkit-font-smoothing:antialiased}
.a{color:var(--acc)}
[data-fit]{white-space:nowrap}
.frame{position:absolute;inset:40px;border:2px solid %(LINE)s;pointer-events:none}
.gv{position:absolute;left:540px;top:40px;bottom:40px;width:2px;background:%(LINE)s}
.gh{position:absolute;top:%(GH)dpx;left:40px;right:40px;height:2px;background:%(LINE)s}
.logo{position:absolute;left:64px;top:52px;width:93px}
.cnt{position:absolute;right:66px;top:72px;font:700 24px M;color:#6E859B}
.tag{font:800 25px M;letter-spacing:5px;color:var(--acc)}
.foot{position:absolute;left:64px;right:66px;bottom:52px;display:flex;justify-content:space-between;align-items:center;font:800 25px M;letter-spacing:1px}
.foot .mid{font:700 19px M;color:#6E859B;letter-spacing:3px}
.foot .sv{display:flex;align-items:center;gap:10px;color:var(--acc);letter-spacing:3px}
.legend{display:flex;gap:18px;justify-content:flex-end;font:600 16px M;color:%(MUTED)s;margin-top:10px}
.legend span{display:flex;align-items:center;gap:7px}
.legend i{display:inline-block;width:14px;height:14px;border-radius:50%%}
.legend b{display:inline-block;width:22px}
.panel{background:%(PANEL)s;border-radius:22px;display:flex;align-items:center;justify-content:center}
.card{background:%(CARD)s;border:2px solid %(CARDB)s;border-radius:16px;padding:26px 30px}
.card h4{font:800 33px M;letter-spacing:.5px;margin-bottom:12px}
.card p{font:500 29px/1.42 M;color:#C9D4DF}
.card{padding:30px 34px}
.tipbox{border:3px solid var(--acc);border-radius:16px;padding:26px 30px;display:flex;gap:22px;align-items:center;font:600 29px/1.4 M}
"""

def page(body, esporte, W=1080, Hh=1350, grid=True):
    css = CSS % dict(W=W, Hh=Hh, BG=BG, WHITE=WHITE, LINE=LINE, PANEL=PANEL, CARD=CARD, CARDB=CARDB, MUTED=MUTED, GH=Hh//2)
    g = '<div class="frame"></div><div class="gv"></div><div class="gh"></div>' if grid else '<div class="frame"></div>'
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{fontface()}{css}</style></head>
<body style="--acc:{ACC[esporte]}">{g}{body}
<script>
// encolhe títulos que estouram a largura (depois de carregar as fontes)
document.fonts.ready.then(()=>{{document.querySelectorAll('[data-fit]').forEach(el=>{{const max=+el.dataset.fit;el.style.display='inline-block';let fs=parseFloat(getComputedStyle(el).fontSize);
while(el.getBoundingClientRect().width>max&&fs>20){{fs-=2;el.style.fontSize=fs+'px';}}}});window.__fit=true;}});
</script></body></html>'''

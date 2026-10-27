import sys, os, subprocess, base64, wave
import numpy as np
sys.path.insert(0, "/home/claude/work")
from content import POSTS
from tpl import *
from slides import story
from playwright.sync_api import sync_playwright

OUT = "/home/claude/repos/raquetada-posts/semana-2"
FPS = 30
T_INTRO, T_STEP, T_END = 5.0, 5.5, 4.5

def reel_html(p, capa=False):
    e = p["esporte"]; acc = ACC[e]
    steps = []
    for s in p["passos"]:
        if "errado" in s:
            body = f'''<div class="card it" style="display:flex;gap:22px;align-items:flex-start;padding:30px 32px">{ic("x",MUTED,52)}<div><div style="font:800 22px M;letter-spacing:3px;color:{MUTED}">ERRADO</div><div style="font:700 38px/1.3 M;margin-top:6px">{em(s["errado"])}</div></div></div>
<div class="it" style="display:flex;gap:22px;align-items:flex-start;padding:30px 32px;border-radius:16px;background:{acc};color:{BG};margin-top:24px">{ic("ok",BG,52)}<div><div style="font:800 22px M;letter-spacing:3px">POR QUÊ</div><div style="font:800 38px/1.3 M;margin-top:6px">{em(s["porque"]).replace('class="a"','')}</div></div></div>'''
        else:
            body = f'''<div class="card it" style="display:flex;gap:24px;align-items:flex-start;padding:34px 34px">{ic("info",acc,54)}<div><div style="font:800 22px M;letter-spacing:3px;color:{acc}">{s["rotulo"]}</div><div style="font:600 40px/1.35 M;margin-top:8px">{em(s["texto"])}</div></div></div>'''
        steps.append(f'''<div class="scene" data-k="{s["n"]}">
 <div class="it" style="display:flex;justify-content:center"><div style="width:150px;height:150px;border-radius:50%;background:{acc};display:flex;align-items:center;justify-content:center;font:900 92px M;color:{BG}">{s["n"]}</div></div>
 <div class="it" style="text-align:center;font:900 62px M;margin:44px 0 54px">{em(s["titulo"])}</div>
 {body}</div>''')
    intro = f'''<div class="scene" data-k="0" style="text-align:center">
 <div class="it" style="display:flex;justify-content:center">{ic_speedball(acc,140)}</div>
 <div class="it tag" style="font-size:32px;letter-spacing:6px;margin-top:50px">{em(p["tag"])}</div>
 <div class="it" data-fit="940" style="font:900 104px/1.04 M;margin-top:30px">{lines(p["titulo"])}</div>
 <div class="it" style="display:flex;justify-content:center;margin-top:46px"><div style="border:4px solid {acc};border-radius:60px;padding:18px 40px;font:700 40px M;background:rgba(0,0,0,.12)">{em(p["selo"])}</div></div>
</div>'''
    end = f'''<div class="scene" data-k="9" style="text-align:center">
 <div class="it" style="display:flex;justify-content:center"><img src="{LOGO_B}" style="width:470px"></div>
 <div class="it" data-fit="940" style="font:900 60px/1.15 M;margin-top:70px">{lines(p["pergunta"])}</div>
 <div class="it" style="font:800 40px/1.9 M;margin-top:50px"><span class="a">Curta</span> se a dica ajudou<br><span class="a">Compartilhe</span> com sua dupla<br><span class="a">Siga</span> @raquetada.br</div>
</div>'''
    css = f'''.scene{{position:absolute;left:80px;right:80px;top:400px;opacity:0}}
.bar{{position:absolute;left:70px;right:70px;top:70px;height:8px;border-radius:4px;background:{LINE}}}
.bar i{{display:block;height:100%;border-radius:4px;background:{acc};width:0}}'''
    body = f'''<style>{css}</style><div class="bar"><i id="pb"></i></div>
<div style="position:absolute;left:0;right:0;top:130px;display:flex;justify-content:center"><img src="{LOGO_S}" style="width:130px"></div>
{intro}{"".join(steps)}{end}
<div style="position:absolute;left:0;right:0;bottom:330px;text-align:center;font:800 28px M;letter-spacing:3px;color:#7C93A8">RAQUETADA<span class="a">.BR</span></div>
<script>
const TI={T_INTRO},TS={T_STEP},TE={T_END},N={len(steps)};const TOT=TI+N*TS+TE;
const ease=x=>1-Math.pow(1-Math.min(Math.max(x,0),1),3);
function render(t){{
 document.getElementById('pb').style.width=(100*Math.min(t/TOT,1))+'%';
 const sc=[...document.querySelectorAll('.scene')];
 sc.forEach((el,idx)=>{{
   let a,b; if(idx==0){{a=0;b=TI}} else if(idx<=N){{a=TI+(idx-1)*TS;b=a+TS}} else {{a=TI+N*TS;b=TOT+1}}
   const vis=t>=a-0.001&&t<b; el.style.opacity=vis?1:0;
   if(!vis)return; const lt=t-a, out=(idx<=N)?Math.max(0,(lt-(b-a-0.35))/0.35):0;
   [...el.querySelectorAll('.it')].forEach((it,j)=>{{const k=ease((lt-0.12-j*0.16)/0.45);
     it.style.opacity=(k*(1-out)).toFixed(3); it.style.transform=`translateY(${{(1-k)*50 - out*30}}px)`;}});
 }});
}}
window.render=render; window.TOT=TOT;
</script>'''
    h = page(body, e, 1080, 1920, grid=False)
    return h.replace('<div class="frame"></div>', '<div class="frame"></div><div class="gh" style="top:960px"></div><div class="gv"></div>')

def music(path, dur, seed=1):
    sr = 44100; n = int(sr*dur); t = np.arange(n)/sr
    out = np.zeros(n)
    bpm = 118; beat = 60/bpm
    rng = np.random.default_rng(seed)
    def env(L, a=0.004, d=0.25):
        x = np.arange(L)/sr; return np.minimum(x/a, 1)*np.exp(-x/d)
    def add(at, sig):
        i = int(at*sr); j = min(n, i+len(sig)); out[i:j] += sig[:j-i]
    # progressão (A m, F, C, G) em frequências
    chords = [[220.0, 261.63, 329.63], [174.61, 220.0, 261.63], [130.81, 196.0, 261.63], [196.0, 246.94, 293.66]]
    bass = [110.0, 87.31, 65.41, 98.0]
    nb = int(dur/beat)+1
    for b in range(nb):
        at = b*beat; bar = (b//4) % 4
        L = int(0.35*sr); x = np.arange(L)/sr
        # kick
        f = 50+70*np.exp(-x*35); kick = np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-x*9)
        add(at, 0.55*kick)
        # clap no 2 e 4
        if b % 2 == 1:
            Lc = int(0.18*sr); add(at, 0.18*rng.standard_normal(Lc)*env(Lc, 0.002, 0.05))
        # hats nos contratempos
        Lh = int(0.06*sr); hh = rng.standard_normal(Lh); hh = np.diff(np.concatenate([[0], hh]))
        add(at+beat/2, 0.07*hh*env(Lh, 0.001, 0.015))
        # baixo
        Lb = int(beat*0.9*sr); xb = np.arange(Lb)/sr
        add(at, 0.22*np.sin(2*np.pi*bass[bar]*xb)*env(Lb, 0.005, 0.35))
        # arpejo pluck em semicolcheias (2 por tempo)
        for k in range(2):
            fq = chords[bar][(b*2+k) % 3]*2
            Lp = int(0.3*sr); xp = np.arange(Lp)/sr
            pl = (np.sin(2*np.pi*fq*xp)+0.4*np.sin(2*np.pi*2*fq*xp)+0.15*np.sin(2*np.pi*3*fq*xp))*env(Lp, 0.003, 0.12)
            add(at+k*beat/2, 0.11*pl)
    # fade
    fi = np.minimum(t/0.4, 1); fo = np.minimum((dur-t)/1.5, 1)
    out *= fi*fo
    out = out/np.max(np.abs(out))*0.8
    st = np.stack([out, out], 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((st*32767).astype("<i2").tobytes())

def build(post, pg):
    d = os.path.join(OUT, post["pasta"]); os.makedirs(d, exist_ok=True)
    html = reel_html(post)
    tmp = "/home/claude/work/reel_tmp.html"; open(tmp, "w").write(html)
    pg.set_viewport_size({"width": 1080, "height": 1920})
    pg.goto("file://" + tmp); pg.wait_for_function("window.__fit===true")
    tot = pg.evaluate("window.TOT")
    # capa: cena de abertura completa
    pg.evaluate("render(3.0)"); pg.screenshot(path=f"{d}/capa-reel.png")
    from PIL import Image
    Image.open(f"{d}/capa-reel.png").convert("RGB").save(f"{d}/capa-reel.jpg", quality=92); os.remove(f"{d}/capa-reel.png")
    wav = f"/home/claude/work/{post['pasta']}.wav"; music(wav, tot, seed=len(post["pasta"]))
    nfr = int(tot*FPS)
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                           "-i", wav, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-crf", "20", "-r", str(FPS),
                           "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", f"{d}/reel.mp4"], stdin=subprocess.PIPE)
    for f in range(nfr):
        pg.evaluate(f"render({f/FPS})")
        ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
    ff.stdin.close(); ff.wait()
    thumb = "data:image/jpeg;base64," + base64.b64encode(open(f"{d}/capa-reel.jpg", "rb").read()).decode()
    open(tmp, "w").write(story(post, thumb)); pg.goto("file://" + tmp); pg.wait_for_function("window.__fit===true")
    pg.screenshot(path=f"{d}/story.png"); Image.open(f"{d}/story.png").convert("RGB").save(f"{d}/story.jpg", quality=92); os.remove(f"{d}/story.png")
    print("ok", post["pasta"], round(tot, 1), "s")

if __name__ == "__main__":
    only = sys.argv[1:]
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        for post in POSTS:
            if post["tipo"] != "reels": continue
            if only and not any(o in post["pasta"] for o in only): continue
            build(post, pg)
        b.close()

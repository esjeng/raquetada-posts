from tpl import *

def footer(esporte, mid="", salve=True):
    sv = f'<div class="sv">{ic("bookmark", ACC[esporte], 30)}SALVE</div>' if salve else '<div style="font:500 19px M;color:#6E859B;letter-spacing:0">Seu jogo começa aqui</div>'
    return f'<div class="foot"><div>RAQUETADA<span class="a">.BR</span></div><div class="mid">{mid}</div>{sv}</div>'

def header(i, n):
    return f'<img class="logo" src="{LOGO_S}"><div class="cnt">{i}/{n}</div>'

def cover(p, n):
    e = p["esporte"]; acc = ACC[e]
    if p.get("capa_diagrama"):
        right = f'<div class="panel" style="position:absolute;left:625px;top:170px;width:398px;height:776px">{court(p["capa_diagrama"], acc, 360, 740, label=False)}</div>'
        tw = 545
    else:
        right = f'<div style="position:absolute;left:590px;top:150px;width:460px;height:820px;display:flex;align-items:center;justify-content:center">{big_icon(p["capa_icone"], acc)}</div>'
        tw = 500
    nt = len(p["titulo"])
    fs = 78 if nt <= 3 else 68
    body = f'''{header(1,n)}
<div style="position:absolute;left:64px;top:170px;width:{tw}px">
 <div class="tag">{em(p["tag"])}</div>
 <div data-fit="{tw}" style="font:900 {fs}px/1.04 M;margin-top:30px;letter-spacing:-.5px">{lines(p["titulo"])}</div>
 <div style="font:500 33px/1.4 M;margin-top:34px;color:#E3E9EF">{em(p["sub"])}</div>
</div>{right}
<div style="position:absolute;left:64px;top:1020px">{ic_speedball(acc,100)}</div>
<div style="position:absolute;left:64px;top:1170px;display:flex;align-items:center;gap:18px" class="tag">ARRASTE PARA VER AS DICAS {ic("arrowr",acc,54)}</div>
{footer(e)}'''
    return page(body, e)

def tip(p, s, i, n, ntips):
    e = p["esporte"]; acc = ACC[e]
    body = f'''{header(i,n)}
<div style="position:absolute;left:64px;top:162px" class="tag" ><span style="font-size:21px;letter-spacing:4px">{em(s["over"])}</span></div>
<div style="position:absolute;left:64px;top:225px;display:flex;gap:26px;align-items:center">
 <div style="width:96px;height:96px;border-radius:50%;border:5px solid {acc};display:flex;align-items:center;justify-content:center;font:800 54px M;color:{acc}">{s["n"]}</div>
 <div data-fit="840" style="font:900 56px/1.04 M">{lines(s["titulo"])}</div>
</div>
<div style="position:absolute;left:64px;top:420px;width:470px">
 {"".join(f'<p style="font:500 32px/1.45 M;margin-bottom:30px;color:#E7EDF2">{em(t)}</p>' for t in s["texto"])}
 <div style="border:3px solid {acc};border-radius:14px;padding:22px 24px;font:800 25px/1.35 M;color:{acc};letter-spacing:.5px;margin-top:20px">{em(s["destaque"])}</div>
</div>
<div style="position:absolute;left:580px;top:420px;width:440px">
 <div class="panel" style="height:640px">{court(s["diagrama"], acc, 330, 610)}</div>{legend(acc)}
</div>
<div style="position:absolute;left:64px;right:64px;top:1135px;height:86px;border-radius:14px;background:{acc};display:flex;align-items:center;justify-content:center;font:900 29px M;color:{BG};letter-spacing:1px">{em(s["barra"]).replace('class="a"','')}</div>
{footer(e, f"DICA {s['n']} DE {ntips}")}'''
    return page(body, e)

def cards(p, s, i, n):
    e = p["esporte"]; acc = ACC[e]
    cs = "".join(f'<div class="card"><h4>{em(t)}</h4><p>{em(d)}</p></div>' for t, d in s["cards"])
    body = f'''{header(i,n)}
<div style="position:absolute;left:64px;right:66px;top:150px;bottom:130px;display:flex;flex-direction:column;justify-content:center">
 <div class="tag" style="font-size:24px;letter-spacing:4px">{em(s["over"])}</div>
 <div data-fit="950" style="font:900 76px/1.04 M;margin:24px 0 50px">{lines(s["titulo"])}</div>
 <div style="display:flex;flex-direction:column;gap:22px">{cs}</div>
 <div class="tipbox" style="margin-top:34px">{ic("bulb",acc,46)}<div>{em(s["dica"])}</div></div>
</div>
{footer(e, salve=False)}'''
    return page(body, e)

def check(p, s, i, n):
    e = p["esporte"]; acc = ACC[e]
    li = "".join(f'<div style="display:flex;gap:24px;align-items:flex-start;margin-bottom:38px">{ic("check",acc,50)}<div style="font:600 34px/1.4 M">{em(t)}</div></div>' for t in s["itens"])
    body = f'''{header(i,n)}
<div style="position:absolute;left:64px;right:80px;top:150px;bottom:130px;display:flex;flex-direction:column;justify-content:center">
 <div class="tag" style="font-size:24px;letter-spacing:4px">{em(s["over"])}</div>
 <div data-fit="950" style="font:900 76px/1.04 M;margin:24px 0 64px">{lines(s["titulo"])}</div>
 {li}
</div>
{footer(e, salve=False)}'''
    return page(body, e)

def final(p, i, n):
    e = p["esporte"]; acc = ACC[e]
    it = lambda icn, t: f'<div style="display:flex;flex-direction:column;align-items:center;gap:14px;width:210px;text-align:center">{ic(icn,acc,52)}<div style="font:800 21px/1.25 M">{t}</div></div>'
    body = f'''<div style="position:absolute;left:0;right:0;top:110px;display:flex;justify-content:center"><img src="{LOGO_B}" style="width:420px"></div>
<div style="position:absolute;left:80px;right:80px;top:540px;text-align:center">
 <div style="display:flex;justify-content:center;margin-bottom:26px">{ic("chat",acc,64)}</div>
 <div data-fit="920" style="font:900 52px/1.12 M">{lines(p["pergunta"])}</div>
 <div style="font:500 28px M;margin-top:22px;color:#DCE4EB">{em(p["pergunta_sub"])}</div>
</div>
<div style="position:absolute;left:60px;right:60px;top:930px;display:flex;justify-content:space-between">
 {it("bookmark","Salve<br>este post")}{it("heart","Curta")}{it("send","Compartilhe")}{it("user",f'Siga<br><span class="a">@raquetada.br</span>')}
</div>
{footer(e, salve=False)}'''
    return page(body, e)

def carousel_pages(p):
    n = 1 + len(p["slides"]) + 1
    ntips = sum(1 for s in p["slides"] if s["kind"] == "tip")
    out = [cover(p, n)]
    for k, s in enumerate(p["slides"], start=2):
        if s["kind"] == "tip": out.append(tip(p, s, k, n, ntips))
        elif s["kind"] == "cards": out.append(cards(p, s, k, n))
        else: out.append(check(p, s, k, n))
    out.append(final(p, n, n))
    return out

def story(p, thumb_data):
    e = p["esporte"]; acc = ACC[e]; st = p["story"]
    body = f'''<div style="position:absolute;left:0;right:0;top:120px;display:flex;justify-content:center"><img src="{LOGO_S}" style="width:130px"></div>
<div style="position:absolute;left:70px;right:70px;top:300px;text-align:center">
 <div class="tag" style="font-size:30px;letter-spacing:6px">{st["over"]}</div>
 <div data-fit="940" style="font:900 98px/1.04 M;margin-top:30px">{lines(st["titulo"])}</div>
</div>
<div style="position:absolute;left:0;right:0;top:860px;display:flex;justify-content:center">
 <div style="transform:rotate(-5deg);padding:14px;border-radius:44px;background:#E9EEF3;box-shadow:0 30px 60px rgba(0,0,0,.45)">
  <div style="width:{372 if p['tipo']=='carrossel' else 330}px;height:{465 if p['tipo']=='carrossel' else 586}px;border-radius:32px;overflow:hidden;background:{BG};position:relative">
   <img src="{thumb_data}" style="width:100%;height:100%;object-fit:cover">
   {'' if p['tipo']=='carrossel' else f'<div style="position:absolute;inset:0;display:flex;align-items:flex-end;padding-bottom:110px;justify-content:center"><div style="width:110px;height:110px;border-radius:50%;background:rgba(11,45,73,.75);border:4px solid {acc};display:flex;align-items:center;justify-content:center"><svg width="44" height="44" viewBox="0 0 24 24"><path d="M7 4v16l13-8z" fill="{acc}"/></svg></div></div>'}
  </div></div>
</div>
<div style="position:absolute;left:60px;right:60px;top:1560px;text-align:center;font:800 40px/1.35 M">{lines(st["cta"])}</div>
<div style="position:absolute;left:0;right:0;top:1700px;display:flex;justify-content:center">{ic("arrowd",acc,60)}</div>'''
    return page(body, e, 1080, 1920, grid=False).replace('<div class="frame"></div>', '<div class="frame"></div><div class="gh" style="top:960px"></div><div class="gv"></div>')

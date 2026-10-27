# Conteúdo da semana 2 do @raquetada.br (28/10 a 03/11/2026)
# esporte: "tenis" (acento lime) | "bt" (acento laranja)
# Diagramas: lista de elementos em coordenadas de quadra (x 0..1, y 0..1; rede em y=0.5; você embaixo)
#   ("eu",x,y) ponto cheio | ("par",x,y) parceiro (cheio, mais escuro) | ("adv",x,y) adversário (vazado)
#   ("bola",x1,y1,x2,y2) seta tracejada | ("zona",x1,y1,x2,y2,"rótulo") área destacada

POSTS = [
# ---------------- QUA 28/10 ----------------
dict(
  pasta="1-qua-28-backhand-tenis", data="2026-10-28", dia="QUA", hora="12h", esporte="tenis", tipo="carrossel",
  tag="TÊNIS · TÉCNICA", titulo=["BACKHAND DE", "*UMA* OU *DUAS*", "MÃOS?"],
  sub="Vantagens de cada um e como escolher o seu.",
  capa_icone="raquete",
  slides=[
    dict(kind="cards", over="AS DUAS OPÇÕES · 1/2", titulo=["DUAS MÃOS", "*ESTABILIDADE*"], cards=[
      ("A FAVOR", "Mais firmeza e força em bolas altas e na devolução de saque. Costuma ser mais fácil de aprender."),
      ("CONTRA", "Menos alcance: exige chegar mais perto da bola e se deslocar mais."),
    ], dica="Escolha comum para *iniciantes* e crianças."),
    dict(kind="cards", over="AS DUAS OPÇÕES · 2/2", titulo=["UMA MÃO", "*ALCANCE E VARIAÇÃO*"], cards=[
      ("A FAVOR", "Mais alcance e facilidade para variar: slice, ângulos e subidas à rede."),
      ("CONTRA", "Sofre mais com bolas altas e com muito spin. Pede mais força e tempo de bola."),
    ], dica="Combina com quem gosta de *variar* e *subir à rede*."),
    dict(kind="cards", over="QUAL É A SUA?", titulo=["COMO", "*ESCOLHER*"], cards=[
      ("COMEÇANDO AGORA", "Duas mãos costuma dar resultado mais rápido."),
      ("JOGO DE FUNDO", "Duas mãos ajuda a segurar trocas longas e bolas altas."),
      ("JOGO VARIADO", "Uma mão abre espaço para slice e aproximação."),
    ], dica="Na dúvida, teste os dois com um *professor*."),
    dict(kind="check", over="DICA EXTRA", titulo=["APRENDA O", "*SLICE*"], itens=[
      "Mesmo quem bate com duas mãos usa o slice de uma mão",
      "Bom para defender bolas abertas e ganhar tempo",
      "Bola baixa e cortada atrapalha o ataque do adversário",
      "Ótimo para aproximar e subir à rede",
    ]),
  ],
  pergunta=["QUAL É O SEU", "*BACKHAND*?"], pergunta_sub="Uma ou duas mãos? Conta nos comentários",
  story=dict(over="NOVO POST", titulo=["UMA OU DUAS", "*MÃOS* NO", "BACKHAND?"], cta=["Arraste pro post e veja", "*qual combina com você*"]),
  adesivo='enquete "Uma mão / Duas mãos"',
  caption="""Backhand de uma ou duas mãos? 🎾

Duas mãos dá mais firmeza e é mais fácil de aprender. Uma mão dá mais alcance e variação. Não existe certo ou errado: existe o que combina com o seu jogo.

Arraste e veja as vantagens de cada um e como escolher 👉

E o seu, é de uma ou de duas mãos? 👇

❤️ Curta, compartilhe com quem joga com você e siga @raquetada.br para mais dicas

#tênis #tenis #backhand #tecnicadetenis #dicasdetenis #tenisbrasil #raquetada""",
),
dict(
  pasta="1b-qua-28-voleio-bt", data="2026-10-28", dia="QUA", hora="18h", esporte="bt", tipo="reels",
  tag="BEACH TENNIS · REDE", titulo=["VOLEIO NO", "*BEACH TENNIS*"], selo="4 dicas na rede",
  passos=[
    dict(n=1, titulo="RAQUETE ALTA", rotulo="A REGRA", texto="Raquete na frente do peito, sempre pronta. Na rede não dá tempo de levantar o braço."),
    dict(n=2, titulo="PASSO À FRENTE", rotulo="COMO", texto="Encontre a bola na frente do corpo, com um passo curto. Nada de esperar a bola chegar."),
    dict(n=3, titulo="MIRE NOS PÉS", rotulo="ONDE", texto="Bola nos pés de quem está na rede ou no meio da dupla. Difícil de devolver."),
    dict(n=4, titulo="ERRO CLÁSSICO", errado="Bater forte e girar o corpo todo", porque="Na rede, é só bloquear e direcionar. Movimento curto."),
  ],
  pergunta=["MARQUE QUEM", "*MANDA NA REDE*"],
  story=dict(over="NOVO REEL", titulo=["VOCÊ VAI", "*PRA REDE*", "OU FOGE DELA?"], cta=["Toque no Reel e veja", "*as 4 dicas*"]),
  adesivo='enquete "Adoro a rede / Prefiro o fundo"',
  caption="""Voleio no beach tennis: 4 dicas na rede 🏖️

Raquete alta, passo à frente, mire nos pés e nada de bater forte. Na rede, quem bloqueia bem ganha o ponto.

Qual dessas você precisa treinar? 👇

❤️ Curta, compartilhe com sua dupla e siga @raquetada.br para mais dicas

#beachtennis #beachtennisbrasil #voleio #rede #dicasbeachtennis #raquetada""",
),
# ---------------- QUI 29/10 ----------------
dict(
  pasta="2b-qui-29-regras-bt", data="2026-10-29", dia="QUI", hora="12h", esporte="bt", tipo="carrossel",
  tag="BEACH TENNIS · REGRAS", titulo=["REGRAS DO", "*BEACH TENNIS*", "EM 1 MINUTO"],
  sub="O básico para entrar na quadra sem dúvida.",
  capa_icone="bola",
  slides=[
    dict(kind="cards", over="SAQUE", titulo=["SÓ UM", "*SAQUE*"], cards=[
      ("SEM SEGUNDO SAQUE", "Errou o saque, perdeu o ponto. Por isso vale mais acertar do que forçar."),
      ("BOLA NA REDE", "Se a bola do saque tocar a fita e passar, o ponto segue normalmente."),
    ], dica="Saque seguro e *bem colocado* vale ouro."),
    dict(kind="cards", over="PONTUAÇÃO", titulo=["CONTAGEM", "*DO TÊNIS*"], cards=[
      ("15, 30, 40, GAME", "A contagem dos pontos é a mesma do tênis."),
      ("40 A 40", "Não tem vantagem: é ponto decisivo. Quem recebe escolhe quem vai devolver."),
      ("SET", "Em geral, 6 games, com tie-break no 6 a 6."),
    ], dica="Formatos podem mudar conforme o *torneio*."),
    dict(kind="check", over="BOLA EM JOGO", titulo=["A BOLA", "*NÃO QUICA*"], itens=[
      "A bola não pode tocar a areia do seu lado",
      "Cada dupla tem um toque só para devolver",
      "Encostar o corpo ou a raquete na rede é ponto perdido",
      "Bola na linha é bola boa",
    ]),
  ],
  pergunta=["ALGUMA REGRA TE", "*PEGOU DE SURPRESA*?"], pergunta_sub="Conte nos comentários",
  story=dict(over="NOVO POST", titulo=["NO 40 A 40", "QUEM", "*ESCOLHE*?"], cta=["Arraste pro post e veja", "*as regras básicas*"]),
  adesivo='quiz "No 40 a 40: tem vantagem? Sim / Não, ponto decisivo"',
  caption="""Regras do beach tennis em 1 minuto 🏖️

Só um saque, contagem igual à do tênis, ponto decisivo no 40 a 40 e bola que não pode quicar na areia. O básico para entrar na quadra sem dúvida.

Arraste e confira 👉

Qual regra te pegou de surpresa no começo? 👇

❤️ Curta, compartilhe com quem está começando e siga @raquetada.br para mais dicas

#beachtennis #beachtennisbrasil #regras #iniciantes #dicasbeachtennis #raquetada""",
),
dict(
  pasta="2-qui-29-split-step-tenis", data="2026-10-29", dia="QUI", hora="18h", esporte="tenis", tipo="reels",
  tag="TÊNIS · MOVIMENTAÇÃO", titulo=["SPLIT STEP:", "*O PASSINHO*", "QUE MUDA TUDO"], selo="Chegue antes na bola",
  passos=[
    dict(n=1, titulo="O QUE É", rotulo="A REGRA", texto="Um pequeno salto com os dois pés, para sair rápido para qualquer lado."),
    dict(n=2, titulo="QUANDO FAZER", rotulo="QUANDO", texto="No instante em que o adversário bate na bola. Você aterrissa já sabendo a direção."),
    dict(n=3, titulo="COMO FAZER", rotulo="COMO", texto="Pés na largura dos ombros, joelhos flexionados e peso na ponta dos pés."),
    dict(n=4, titulo="ERRO CLÁSSICO", errado="Pular cedo demais ou alto demais", porque="Você aterrissa atrasado. Salto baixo e no tempo certo."),
  ],
  pergunta=["VOCÊ JÁ FAZ O", "*SPLIT STEP*?"],
  story=dict(over="NOVO REEL", titulo=["O PASSINHO", "QUE TE FAZ", "*CHEGAR ANTES*"], cta=["Toque no Reel e", "*aprenda o split step*"]),
  adesivo='enquete "Já faço / Vou começar"',
  caption="""Split step: o passinho que muda tudo 🎾

Um saltinho no momento em que o adversário bate na bola. Parece pouco, mas é o que faz você sair rápido e chegar antes.

Você já faz ou vai começar hoje? 👇

❤️ Curta, compartilhe com quem joga com você e siga @raquetada.br para mais dicas

#tênis #tenis #splitstep #movimentacao #dicasdetenis #tenisbrasil #raquetada""",
),
# ---------------- SEX 30/10 ----------------
dict(
  pasta="3-sex-30-devolucao-tenis", data="2026-10-30", dia="SEX", hora="12h", esporte="tenis", tipo="carrossel",
  tag="TÊNIS · DEVOLUÇÃO", titulo=["DEVOLUÇÃO", "DE SAQUE:", "*4 AJUSTES*"],
  sub="Pare de entregar o ponto logo na primeira bola.",
  capa_diagrama=[("adv",0.62,0.05),("bola",0.62,0.06,0.30,0.74),("eu",0.26,0.86)],
  slides=[
    dict(kind="tip", n=1, titulo=["AJUSTE A", "*DISTÂNCIA*"], over="DEVOLUÇÃO · TÊNIS",
         texto=["Saque forte? Dê um ou dois passos para trás.", "Saque mais lento? Avance e tome a bola mais cedo."],
         destaque="LEIA O SAQUE ANTES DE SE POSICIONAR.", barra="POSIÇÃO CERTA, BOLA MAIS FÁCIL",
         diagrama=[("adv",0.62,0.05),("zona",0.10,0.88,0.52,0.98,"SAQUE FORTE"),("zona",0.10,0.72,0.52,0.82,"SAQUE LENTO"),("eu",0.72,0.93)]),
    dict(kind="tip", n=2, titulo=["SPLIT STEP", "*NO SAQUE*"], over="DEVOLUÇÃO · TÊNIS",
         texto=["Dê o saltinho quando o sacador bater na bola.", "Você aterrissa pronto para ir para qualquer lado."],
         destaque="PÉS ATIVOS, NUNCA PARADOS.", barra="O TEMPO CERTO É O DO CONTATO",
         diagrama=[("adv",0.62,0.05),("bola",0.62,0.06,0.30,0.74),("eu",0.28,0.86)]),
    dict(kind="tip", n=3, titulo=["ENCURTE O", "*MOVIMENTO*"], over="DEVOLUÇÃO · TÊNIS",
         texto=["Contra saque rápido, não faça o golpe inteiro.", "Use a força da bola: preparação curta, quase um bloqueio."],
         destaque="MENOS BRAÇO, MAIS TIMING.", barra="CURTO E FIRME",
         diagrama=[("adv",0.62,0.05),("bola",0.62,0.06,0.32,0.80),("eu",0.28,0.86),("bola",0.30,0.84,0.48,0.14)]),
    dict(kind="tip", n=4, titulo=["FUNDO E", "*NO MEIO*"], over="DEVOLUÇÃO · TÊNIS",
         texto=["Na dúvida, devolva alto e fundo no meio da quadra.", "Bola funda no meio tira os ângulos do sacador."],
         destaque="DEVOLVEU, JÁ ESTÁ NO PONTO.", barra="SEGURANÇA PRIMEIRO",
         diagrama=[("adv",0.82,0.05),("zona",0.28,0.03,0.72,0.16,"ALVO"),("eu",0.28,0.86),("bola",0.30,0.84,0.50,0.10)]),
  ],
  pergunta=["QUAL SUA MAIOR", "*DIFICULDADE NA DEVOLUÇÃO*?"], pergunta_sub="Conte nos comentários",
  story=dict(over="NOVO POST", titulo=["VOCÊ", "*DEVOLVE BEM*", "O SAQUE?"], cta=["Arraste pro post e veja", "*os 4 ajustes*"]),
  adesivo='enquete "Devolvo bem / Sofro com saque forte"',
  caption="""Devolução de saque: 4 ajustes 🎾

Ajustar a distância, fazer o split step no contato, encurtar o movimento e devolver fundo no meio. Simples, e já muda o seu próximo jogo.

Arraste e veja cada ajuste no diagrama 👉

Qual é a sua maior dificuldade na devolução? 👇

❤️ Curta, compartilhe com quem joga com você e siga @raquetada.br para mais dicas

#tênis #tenis #devolucao #saque #dicasdetenis #tenisbrasil #raquetada""",
),
dict(
  pasta="3b-sex-30-lob-bt", data="2026-10-30", dia="SEX", hora="18h", esporte="bt", tipo="carrossel",
  tag="BEACH TENNIS · TÁTICA", titulo=["LOB NO", "*BEACH TENNIS*:", "QUANDO E COMO"],
  sub="A jogada que tira a dupla adversária da rede.",
  capa_diagrama=[("adv",0.35,0.40),("adv",0.65,0.40),("eu",0.40,0.86),("bola",0.40,0.84,0.55,0.06)],
  slides=[
    dict(kind="tip", n=1, titulo=["QUANDO", "*USAR*"], over="LOB · BEACH TENNIS",
         texto=["A dupla adversária está colada na rede?", "É a hora do lob: o espaço livre está lá atrás."],
         destaque="REDE CHEIA, FUNDO VAZIO.", barra="LEIA ONDE ESTÁ O ESPAÇO",
         diagrama=[("adv",0.35,0.42),("adv",0.65,0.42),("zona",0.08,0.02,0.92,0.18,"ESPAÇO LIVRE"),("eu",0.40,0.86)]),
    dict(kind="tip", n=2, titulo=["ALTO", "*O SUFICIENTE*"], over="LOB · BEACH TENNIS",
         texto=["A bola precisa passar da raquete esticada de quem está na rede.", "Lob baixo vira smash do adversário."],
         destaque="NA DÚVIDA, MAIS ALTO.", barra="ALTURA É SEGURANÇA",
         diagrama=[("adv",0.50,0.40),("bola",0.45,0.84,0.55,0.08),("eu",0.45,0.86)]),
    dict(kind="tip", n=3, titulo=["MIRE NO", "*FUNDO*"], over="LOB · BEACH TENNIS",
         texto=["Busque a bola perto da linha de fundo.", "Quanto mais fundo, mais o adversário corre para trás."],
         destaque="FUNDO OBRIGA A RECUAR.", barra="PROFUNDIDADE ANTES DE FORÇA",
         diagrama=[("adv",0.35,0.40),("adv",0.65,0.40),("zona",0.10,0.02,0.90,0.10,"ALVO"),("eu",0.40,0.86),("bola",0.40,0.84,0.60,0.06)]),
    dict(kind="tip", n=4, titulo=["DEPOIS,", "*SUBAM JUNTOS*"], over="LOB · BEACH TENNIS",
         texto=["Lob bem feito obriga a dupla a recuar.", "É a deixa para vocês dois avançarem para a rede."],
         destaque="O LOB ABRE A PORTA DA REDE.", barra="LOB + SUBIDA = PONTO",
         diagrama=[("adv",0.35,0.12),("adv",0.65,0.12),("eu",0.35,0.62),("par",0.65,0.62),("zona",0.10,0.55,0.90,0.70,"SUBAM JUNTOS")]),
  ],
  pergunta=["VOCÊ USA O", "*LOB* NOS SEUS JOGOS?"], pergunta_sub="Conte nos comentários",
  story=dict(over="NOVO POST", titulo=["A DUPLA", "COLOU NA REDE?", "*LOB NELES*"], cta=["Arraste pro post e veja", "*quando e como usar*"]),
  adesivo='enquete "Uso sempre / Quase nunca"',
  caption="""Lob no beach tennis: quando e como 🏖️

Dupla colada na rede? O espaço livre está lá atrás. Alto o suficiente, fundo perto da linha e, depois, os dois sobem juntos.

Arraste e veja os 4 passos no diagrama 👉

Você usa o lob nos seus jogos? 👇

❤️ Curta, compartilhe com sua dupla e siga @raquetada.br para mais dicas

#beachtennis #beachtennisbrasil #lob #tatica #dicasbeachtennis #raquetada""",
),
# ---------------- SÁB 31/10 ----------------
dict(
  pasta="4b-sab-31-cuidados-areia-bt", data="2026-10-31", dia="SÁB", hora="12h", esporte="bt", tipo="reels",
  tag="BEACH TENNIS · BEM-ESTAR", titulo=["4 CUIDADOS", "PARA JOGAR", "*NA AREIA*"], selo="Antes de entrar na quadra",
  passos=[
    dict(n=1, titulo="AQUEÇA ANTES", rotulo="POR QUÊ", texto="A areia exige mais de tornozelos e panturrilhas. Cinco minutos de aquecimento fazem diferença."),
    dict(n=2, titulo="HIDRATE-SE", rotulo="COMO", texto="Beba água antes, durante e depois do jogo. Não espere sentir sede."),
    dict(n=3, titulo="PROTEJA-SE DO SOL", rotulo="COMO", texto="Protetor solar, boné ou viseira e óculos. Evite o sol mais forte do meio do dia."),
    dict(n=4, titulo="ERRO CLÁSSICO", errado="Jogar no sol forte sem água por perto", porque="Calor e esforço cansam mais rápido. Pausa e garrafinha sempre por perto."),
  ],
  pergunta=["MARQUE SUA", "*DUPLA DE AREIA*"],
  story=dict(over="NOVO REEL", titulo=["VOCÊ", "*AQUECE*", "ANTES DE JOGAR?"], cta=["Toque no Reel e veja", "*os 4 cuidados*"]),
  adesivo='enquete "Sempre / Vou direto pro jogo"',
  caption="""4 cuidados para jogar na areia 🏖️☀️

Aquecer, se hidratar, se proteger do sol e não jogar sem água por perto. Cuidados simples para aproveitar o jogo do começo ao fim.

Qual desses você costuma esquecer? 👇

❤️ Curta, compartilhe com sua dupla e siga @raquetada.br para mais dicas

#beachtennis #beachtennisbrasil #praia #aquecimento #dicasbeachtennis #raquetada""",
),
dict(
  pasta="4-sab-31-tie-break-tenis", data="2026-10-31", dia="SÁB", hora="18h", esporte="tenis", tipo="carrossel",
  tag="TÊNIS · REGRAS", titulo=["TIE-BREAK:", "*COMO FUNCIONA*"],
  sub="Contagem, saque e troca de lado sem confusão.",
  capa_icone="placar",
  slides=[
    dict(kind="cards", over="QUANDO ACONTECE", titulo=["NO", "*6 A 6*"], cards=[
      ("QUANDO", "O set empatou em 6 games a 6? O tie-break decide."),
      ("COMO GANHA", "Vence quem fizer 7 pontos primeiro, com 2 de diferença. Se empatar no 6 a 6, segue até abrir 2."),
      ("NO PLACAR", "O set termina 7 a 6."),
    ], dica="A contagem é *1, 2, 3...*, não 15, 30, 40."),
    dict(kind="cards", over="SAQUE E LADO", titulo=["QUEM", "*SACA*"], cards=[
      ("1º PONTO", "Saca quem seria o próximo a sacar no set. Só 1 ponto."),
      ("DEPOIS", "O saque alterna a cada 2 pontos."),
      ("TROCA DE LADO", "A cada 6 pontos somados (6, 12, 18...)."),
    ], dica="No set seguinte, *começa recebendo* quem sacou primeiro no tie-break."),
    dict(kind="check", over="E O SUPER TIE-BREAK?", titulo=["SUPER", "*TIE-BREAK*"], itens=[
      "Muito usado em duplas e torneios amadores",
      "Substitui o 3º set",
      "Vence quem fizer 10 pontos, com 2 de diferença",
      "Saque e troca de lado seguem a mesma regra",
    ]),
  ],
  pergunta=["VOCÊ JÁ SE PERDEU", "*NA CONTAGEM*?"], pergunta_sub="Salve para o próximo jogo",
  story=dict(over="NOVO POST", titulo=["TIE-BREAK", "AINDA TE", "*CONFUNDE*?"], cta=["Arraste pro post e", "*tire a dúvida*"]),
  adesivo='quiz "Quantos pontos vence o tie-break? 7 com 2 de diferença / 10"',
  caption="""Tie-break: como funciona 🎾

Acontece no 6 a 6, vence quem fizer 7 pontos com 2 de diferença, o saque alterna a cada 2 pontos e os jogadores trocam de lado a cada 6. E ainda tem o super tie-break, até 10.

Arraste e salve para o próximo jogo 👉

Você já se perdeu na contagem? Conta aqui 👇

❤️ Curta, compartilhe com quem joga com você e siga @raquetada.br para mais dicas

#tênis #tenis #tiebreak #regrasdotenis #dicasdetenis #tenisbrasil #raquetada""",
),
# ---------------- DOM 01/11 ----------------
dict(
  pasta="5-dom-01-aquecimento-tenis", data="2026-11-01", dia="DOM", hora="12h", esporte="tenis", tipo="reels",
  tag="TÊNIS · PREPARAÇÃO", titulo=["AQUECIMENTO", "EM *5 MINUTOS*"], selo="Antes de entrar no jogo",
  passos=[
    dict(n=1, titulo="ATIVE O CORPO", rotulo="1 MINUTO", texto="Corrida leve ou polichinelos para aquecer e acelerar a respiração."),
    dict(n=2, titulo="SOLTE AS ARTICULAÇÕES", rotulo="2 MINUTOS", texto="Círculos de ombros, quadril e tornozelos. Movimentos amplos e sem pressa."),
    dict(n=3, titulo="MOVIMENTE OS PÉS", rotulo="1 MINUTO", texto="Passos laterais, deslocamentos curtos e alguns split steps."),
    dict(n=4, titulo="NA QUADRA", rotulo="1 MINUTO", texto="Comece com bolas curtas perto da rede, depois vá para o fundo."),
  ],
  pergunta=["QUANTO TEMPO VOCÊ", "*AQUECE*?"],
  story=dict(over="NOVO REEL", titulo=["5 MINUTOS", "QUE SALVAM", "*SEU JOGO*"], cta=["Toque no Reel e", "*aqueça do jeito certo*"]),
  adesivo='enquete "Aqueço sempre / Vou direto pro jogo"',
  caption="""Aquecimento em 5 minutos antes do tênis 🎾

Ative o corpo, solte as articulações, movimente os pés e comece com bolas curtas. Cinco minutos que deixam você pronto desde o primeiro ponto.

Você aquece antes de jogar? 👇

❤️ Curta, compartilhe com quem joga com você e siga @raquetada.br para mais dicas

#tênis #tenis #aquecimento #preparacaofisica #dicasdetenis #tenisbrasil #raquetada""",
),
dict(
  pasta="5b-dom-01-comunicacao-dupla-bt", data="2026-11-01", dia="DOM", hora="18h", esporte="bt", tipo="carrossel",
  tag="BEACH TENNIS · DUPLA", titulo=["5 COMBINADOS", "COM A SUA", "*DUPLA*"],
  sub="Comunicação que evita bola no meio e discussão.",
  capa_icone="dupla",
  slides=[
    dict(kind="cards", over="DURANTE O PONTO · 1/2", titulo=["FALE", "*NA HORA*"], cards=[
      ("1 · \"MINHA!\" / \"SUA!\"", "Quem vai na bola avisa alto. Acaba com a bola que passa entre os dois."),
      ("2 · \"ATRÁS!\"", "Viu o lob passando por cima do parceiro? Avise para ele virar ou trocar de lado."),
    ], dica="Fala *curta e alta*: uma palavra basta."),
    dict(kind="cards", over="ANTES DO PONTO · 2/2", titulo=["COMBINE", "*ANTES*"], cards=[
      ("3 · BOLA DO MEIO", "Definam quem pega a bola do meio, por exemplo quem está do lado do forehand."),
      ("4 · PLANO DO SAQUE", "Antes de sacar, combinem onde vai a bola e quem cobre cada lado."),
      ("5 · DEPOIS DO ERRO", "Um \"vamos!\" ou um toque de raquete. Dupla que se apoia joga mais solta."),
    ], dica="Combinado bom é o que *os dois* lembram."),
  ],
  pergunta=["QUAL COMBINADO", "*FALTA NA SUA DUPLA*?"], pergunta_sub="Marque seu parceiro nos comentários",
  story=dict(over="NOVO POST", titulo=["SUA DUPLA", "*CONVERSA*", "EM QUADRA?"], cta=["Arraste pro post e veja", "*os 5 combinados*"]),
  adesivo='menção "Marque sua dupla"',
  caption="""5 combinados com a sua dupla 🏖️

"Minha!", "Atrás!", quem pega a bola do meio, o plano do saque e o apoio depois do erro. Dupla que conversa erra menos e se diverte mais.

Arraste e veja os 5 👉

Qual desses falta na sua dupla? Marque seu parceiro 👇

❤️ Curta, compartilhe com sua dupla e siga @raquetada.br para mais dicas

#beachtennis #beachtennisbrasil #dupla #comunicacao #dicasbeachtennis #raquetada""",
),
# ---------------- SEG 02/11 ----------------
dict(
  pasta="6b-seg-02-smash-bt", data="2026-11-02", dia="SEG", hora="12h", esporte="bt", tipo="carrossel",
  tag="BEACH TENNIS · ATAQUE", titulo=["SMASH NO", "*BEACH TENNIS*:", "4 DICAS"],
  sub="Para transformar bola alta em ponto.",
  capa_diagrama=[("eu",0.45,0.60),("bola",0.45,0.58,0.30,0.30),("adv",0.35,0.22),("adv",0.65,0.22)],
  slides=[
    dict(kind="tip", n=1, titulo=["POSICIONE-SE", "*EMBAIXO*"], over="SMASH · BEACH TENNIS",
         texto=["Vire de lado e ande para trás com passos curtos.", "A bola deve cair um pouco à frente do seu corpo."],
         destaque="CHEGUE ANTES, BATA COM CALMA.", barra="PÉS PRIMEIRO, BRAÇO DEPOIS",
         diagrama=[("eu",0.45,0.70),("bola",0.45,0.69,0.45,0.82),("zona",0.30,0.58,0.60,0.66,"PONTO DE CONTATO")]),
    dict(kind="tip", n=2, titulo=["APONTE", "*PARA A BOLA*"], over="SMASH · BEACH TENNIS",
         texto=["O braço livre aponta para a bola enquanto ela desce.", "Ajuda a medir a distância e a girar o corpo."],
         destaque="BRAÇO LIVRE É A SUA MIRA.", barra="MIRA ANTES DO GOLPE",
         diagrama=[("eu",0.45,0.70),("zona",0.30,0.58,0.60,0.66,"BOLA DESCENDO")]),
    dict(kind="tip", n=3, titulo=["BATA NO", "*ALTO*"], over="SMASH · BEACH TENNIS",
         texto=["Encontre a bola no ponto mais alto, braço esticado.", "Bola baixa demais vira golpe sem ângulo."],
         destaque="BRAÇO ESTICADO, BOLA NA FRENTE.", barra="ALTURA DÁ ÂNGULO",
         diagrama=[("eu",0.45,0.66),("bola",0.45,0.64,0.40,0.22)]),
    dict(kind="tip", n=4, titulo=["MIRE, NÃO", "*SÓ FORCE*"], over="SMASH · BEACH TENNIS",
         texto=["Pés de quem está na rede ou o espaço entre os dois.", "Colocação ganha mais pontos que força pura."],
         destaque="LUGAR CERTO > BOLA FORTE.", barra="COLOCAÇÃO GANHA O PONTO",
         diagrama=[("adv",0.32,0.22),("adv",0.68,0.22),("zona",0.42,0.12,0.58,0.32,"MEIO"),("eu",0.45,0.66),("bola",0.45,0.64,0.50,0.22)]),
  ],
  pergunta=["SEU SMASH É MAIS", "*FORÇA OU COLOCAÇÃO*?"], pergunta_sub="Conte nos comentários",
  story=dict(over="NOVO POST", titulo=["BOLA ALTA", "É *PONTO*", "PRA VOCÊ?"], cta=["Arraste pro post e veja", "*as 4 dicas de smash*"]),
  adesivo='enquete "Força / Colocação"',
  caption="""Smash no beach tennis: 4 dicas 🏖️

Posicione-se embaixo da bola, aponte com o braço livre, bata no ponto mais alto e mire em vez de só forçar. Bola alta vira ponto.

Arraste e veja cada dica no diagrama 👉

Seu smash é mais força ou colocação? 👇

❤️ Curta, compartilhe com sua dupla e siga @raquetada.br para mais dicas

#beachtennis #beachtennisbrasil #smash #ataque #dicasbeachtennis #raquetada""",
),
dict(
  pasta="6-seg-02-calcado-tenis", data="2026-11-02", dia="SEG", hora="18h", esporte="tenis", tipo="carrossel",
  tag="TÊNIS · EQUIPAMENTO", titulo=["TÊNIS DE", "CORRIDA NA", "*QUADRA*?"],
  sub="Por que o calçado certo faz diferença.",
  capa_icone="tenis",
  slides=[
    dict(kind="cards", over="A DIFERENÇA", titulo=["FEITO PARA", "*IR DE LADO*"], cards=[
      ("TÊNIS DE CORRIDA", "Pensado para correr para a frente. Solado alto e macio, pouco apoio lateral."),
      ("TÊNIS DE QUADRA", "Pensado para frear, mudar de direção e deslizar. Mais firme nas laterais."),
    ], dica="No tênis, quase todo movimento é *lateral*."),
    dict(kind="cards", over="SOLADO", titulo=["UM PARA", "*CADA PISO*"], cards=[
      ("SAIBRO", "Solado tipo espinha de peixe: segura no pó e não acumula tanto saibro."),
      ("QUADRA DURA", "Solado mais resistente ao desgaste do piso áspero."),
      ("ALL COURT", "Bom meio-termo para quem joga em pisos diferentes."),
    ], dica="Use o calçado do *piso em que você mais joga*."),
    dict(kind="check", over="DICAS FINAIS", titulo=["CUIDE DO", "*SEU CALÇADO*"], itens=[
      "Troque quando o solado estiver liso ou gasto",
      "Calcanhar firme: o pé não pode escorregar dentro",
      "Use meias próprias para esporte",
      "Experimente no fim do dia, com o pé mais inchado",
    ]),
  ],
  pergunta=["COM QUE CALÇADO", "*VOCÊ JOGA*?"], pergunta_sub="Conte nos comentários",
  story=dict(over="NOVO POST", titulo=["VOCÊ JOGA", "DE TÊNIS", "*DE CORRIDA*?"], cta=["Arraste pro post e veja", "*por que trocar*"]),
  adesivo='enquete "Calçado de quadra / Tênis de corrida"',
  caption="""Tênis de corrida na quadra? Melhor não 🎾👟

O tênis de corrida é feito para ir para a frente. Na quadra, você freia, muda de direção e se desloca de lado o tempo todo. Calçado de quadra dá esse apoio.

Arraste e veja como escolher o seu 👉

Com que calçado você joga hoje? 👇

❤️ Curta, compartilhe com quem joga com você e siga @raquetada.br para mais dicas

#tênis #tenis #calcadodetenis #equipamentodetenis #dicasdetenis #tenisbrasil #raquetada""",
),
# ---------------- TER 03/11 ----------------
dict(
  pasta="7-ter-03-voleio-tenis", data="2026-11-03", dia="TER", hora="12h", esporte="tenis", tipo="carrossel",
  tag="TÊNIS · REDE", titulo=["VOLEIO:", "*4 ERROS*", "QUE TE FAZEM", "PERDER O PONTO"],
  sub="E como corrigir cada um.",
  capa_diagrama=[("eu",0.45,0.58),("adv",0.60,0.92-0.86),("bola",0.60,0.08,0.47,0.56),("bola",0.47,0.56,0.20,0.20)],
  slides=[
    dict(kind="tip", n=1, titulo=["BALANÇAR", "*DEMAIS*"], over="VOLEIO · TÊNIS",
         texto=["Voleio não é golpe de fundo.", "Use um movimento curto, de soco, e deixe a bola trabalhar."],
         destaque="CURTO E FIRME, SEM BALANÇO.", barra="SOCO, NÃO SWING",
         diagrama=[("adv",0.60,0.06),("bola",0.60,0.08,0.47,0.56),("eu",0.45,0.60)]),
    dict(kind="tip", n=2, titulo=["RAQUETE", "*CAÍDA*"], over="VOLEIO · TÊNIS",
         texto=["Cabeça da raquete acima do punho.", "Raquete caída manda a bola para a rede ou para o alto."],
         destaque="CABEÇA DA RAQUETE PARA CIMA.", barra="PUNHO FIRME, RAQUETE ALTA",
         diagrama=[("eu",0.45,0.60),("zona",0.30,0.50,0.60,0.56,"NA FRENTE DO CORPO")]),
    dict(kind="tip", n=3, titulo=["FICAR", "*PARADO*"], over="VOLEIO · TÊNIS",
         texto=["Faça o split step quando o adversário bater.", "Depois, um passo à frente para encontrar a bola."],
         destaque="NA REDE, OS PÉS NÃO PARAM.", barra="SPLIT STEP + PASSO À FRENTE",
         diagrama=[("adv",0.60,0.06),("eu",0.45,0.66),("bola",0.45,0.66,0.45,0.58)]),
    dict(kind="tip", n=4, titulo=["PEGADA", "*ERRADA*"], over="VOLEIO · TÊNIS",
         texto=["Use a pegada continental, a de \"martelo\".", "Serve para forehand e backhand sem trocar a mão."],
         destaque="UMA PEGADA PARA OS DOIS LADOS.", barra="CONTINENTAL NA REDE",
         diagrama=[("eu",0.45,0.60),("bola",0.45,0.58,0.20,0.18),("bola",0.45,0.58,0.80,0.18)]),
  ],
  pergunta=["QUAL DESSES", "*VOCÊ COMETE*?"], pergunta_sub="Comente o número",
  story=dict(over="NOVO POST", titulo=["SEU VOLEIO", "*VAI NA REDE*", "COM FREQUÊNCIA?"], cta=["Arraste pro post e veja", "*os 4 erros*"]),
  adesivo='enquete "1 / 2 / 3 / 4"',
  caption="""Voleio: 4 erros que te fazem perder o ponto 🎾

Balançar demais, raquete caída, ficar parado e pegada errada. Corrija esses detalhes e a rede vira o seu lugar.

Arraste e veja como corrigir cada um 👉

Qual desses você comete? Comenta o número 👇

❤️ Curta, compartilhe com quem joga com você e siga @raquetada.br para mais dicas

#tênis #tenis #voleio #rede #dicasdetenis #tenisbrasil #raquetada""",
),
dict(
  pasta="7b-ter-03-bola-bt", data="2026-11-03", dia="TER", hora="18h", esporte="bt", tipo="carrossel",
  tag="BEACH TENNIS · EQUIPAMENTO", titulo=["A BOLA DO", "*BEACH TENNIS*", "É DIFERENTE?"],
  sub="Sim, e isso muda o seu jogo.",
  capa_icone="bola",
  slides=[
    dict(kind="cards", over="A DIFERENÇA", titulo=["PRESSÃO", "*REDUZIDA*"], cards=[
      ("MAIS LENTA", "A bola oficial tem menos pressão que a de tênis. Anda mais devagar no ar."),
      ("TROCAS MAIS LONGAS", "Mais tempo para chegar na bola e mais pontos disputados."),
    ], dica="Por isso o jogo na rede é tão *rápido e divertido*."),
    dict(kind="cards", over="E A BOLA DE TÊNIS?", titulo=["POR QUE", "*NÃO USAR*"], cards=[
      ("RÁPIDA DEMAIS", "A bola de tênis comum é mais viva e muda o ritmo do jogo."),
      ("MAIS IMPACTO", "Bola mais dura transmite mais impacto para o braço."),
    ], dica="Use bola *própria para beach tennis*."),
    dict(kind="check", over="DICAS FINAIS", titulo=["CUIDE DAS", "*SUAS BOLAS*"], itens=[
      "Ficou murcha e sem vida? É hora de trocar",
      "Guarde na embalagem, longe do sol e do calor",
      "Tire a areia antes de guardar",
      "Leve bolas extras para o jogo",
    ]),
  ],
  pergunta=["DE QUANTO EM QUANTO TEMPO", "*VOCÊ TROCA AS BOLAS*?"], pergunta_sub="Conte nos comentários",
  story=dict(over="NOVO POST", titulo=["VOCÊ JOGA", "COM BOLA DE", "*TÊNIS*?"], cta=["Arraste pro post e veja", "*a diferença*"]),
  adesivo='quiz "A bola de beach tennis é mais lenta? Sim / Não"',
  caption="""A bola do beach tennis é diferente? 🏖️🎾

Sim! Ela tem pressão reduzida, é mais lenta que a de tênis e deixa as trocas mais longas. Usar bola de tênis comum muda o ritmo do jogo e sobrecarrega mais o braço.

Arraste e veja como cuidar das suas bolas 👉

De quanto em quanto tempo você troca as bolas? 👇

❤️ Curta, compartilhe com sua dupla e siga @raquetada.br para mais dicas

#beachtennis #beachtennisbrasil #boladebeachtennis #equipamento #dicasbeachtennis #raquetada""",
),
]

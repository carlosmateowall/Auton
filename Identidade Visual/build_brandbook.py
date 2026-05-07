from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import math

W, H = A4  # 595 x 842

# Brand colors
NOITE      = HexColor("#1C1028")
ROXO_PRINC = HexColor("#7F77DD")
ROXO_VIB   = HexColor("#9B7FE8")
LILAS      = HexColor("#CECBF6")
NEVOA      = HexColor("#EEEDFE")
BRANCO     = white
CINZA_TEXT = HexColor("#8B8FA8")
ESCURO_TXT = HexColor("#26215C")

import os
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Auton — Brand Book.pdf")

c = canvas.Canvas(OUTPUT, pagesize=A4)
c.setTitle("Auton — Brand Book")
c.setAuthor("Auton")
c.setSubject("Identidade Visual Auton")

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def draw_logo(c, x, y, size=36, color=ROXO_VIB, opacity=1.0, text_color=None, label="Auton", font_size=22):
    """Draw the Auton logo (4 squares + connector lines + wordmark)."""
    sq = size * 0.39   # square size
    gap = size * 0.22  # gap between squares
    step = sq + gap

    positions = [(x, y + step), (x + step, y + step), (x, y), (x + step, y)]
    opacities = [1.0, 0.35, 0.35, 1.0]

    for i, (px, py) in enumerate(positions):
        alpha = opacities[i] * opacity
        col = HexColor(f"#{int(color.red*255):02x}{int(color.green*255):02x}{int(color.blue*255):02x}")
        c.setFillColor(col)
        c.setFillAlpha(alpha)
        c.roundRect(px, py, sq, sq, radius=sq*0.2, fill=1, stroke=0)

    # Connector lines
    c.setFillAlpha(1)
    c.setStrokeColor(color)
    c.setStrokeAlpha(0.7)
    c.setLineWidth(1.2)
    cx_l = x + sq;  cy_top = y + step + sq/2; cy_bot = y + sq/2
    cx_r = x + step; cx_mid_l = x + sq; cx_mid_r = x + step
    # horizontal top
    c.line(x + sq, y + step + sq/2, x + step, y + step + sq/2)
    # horizontal bottom
    c.line(x + sq, y + sq/2, x + step, y + sq/2)
    # vertical left
    c.line(x + sq/2, y + sq, x + sq/2, y + step)
    # vertical right
    c.line(x + step + sq/2, y + sq, x + step + sq/2, y + step)
    c.setStrokeAlpha(1)

    # Wordmark
    if label:
        c.setFillColor(text_color or BRANCO)
        c.setFillAlpha(1)
        c.setFont("Helvetica-Bold", font_size)
        c.drawString(x + size + 6, y + sq - 2, label)

def page_footer(c, page_num, total=8):
    c.setFillColor(HexColor("#444060"))
    c.setFillAlpha(0.5)
    c.setFont("Helvetica", 8)
    c.drawString(20*mm, 10*mm, "Auton — Brand Book")
    c.drawRightString(W - 20*mm, 10*mm, f"{page_num} / {total}")
    c.setFillAlpha(1)

def section_tag(c, x, y, text):
    c.setFillColor(ROXO_VIB)
    c.setFillAlpha(0.12)
    c.roundRect(x, y, len(text)*6.5 + 16, 16, radius=8, fill=1, stroke=0)
    c.setFillAlpha(1)
    c.setFillColor(ROXO_VIB)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(x + 8, y + 4.5, text.upper())

def divider(c, y, margin=20*mm):
    c.setStrokeColor(LILAS)
    c.setStrokeAlpha(0.25)
    c.setLineWidth(0.5)
    c.line(margin, y, W - margin, y)
    c.setStrokeAlpha(1)

# ─────────────────────────────────────────────
# PAGE 1 — CAPA
# ─────────────────────────────────────────────
c.setFillColor(NOITE)
c.rect(0, 0, W, H, fill=1, stroke=0)

# Subtle grid
c.setStrokeColor(ROXO_PRINC)
c.setStrokeAlpha(0.06)
c.setLineWidth(0.5)
for i in range(0, int(W)+1, 20):
    c.line(i, 0, i, H)
for j in range(0, int(H)+1, 20):
    c.line(0, j, W, j)
c.setStrokeAlpha(1)

# Big logo in center
draw_logo(c, W/2 - 80, H/2 + 20, size=80, color=ROXO_VIB, text_color=BRANCO, font_size=52)

# Tagline
c.setFillColor(LILAS)
c.setFillAlpha(0.7)
c.setFont("Helvetica", 12)
c.drawCentredString(W/2 + 20, H/2 - 10, "Process & Flow")
c.setFillAlpha(1)

# Bottom strip
c.setFillColor(ROXO_VIB)
c.setFillAlpha(0.08)
c.rect(0, 0, W, 70, fill=1, stroke=0)
c.setFillAlpha(1)

c.setFillColor(BRANCO)
c.setFont("Helvetica-Bold", 9)
c.drawString(20*mm, 30, "BRAND BOOK")
c.setFillColor(LILAS)
c.setFillAlpha(0.6)
c.setFont("Helvetica", 9)
c.drawString(20*mm, 18, "Identidade Visual · 2025")
c.setFillAlpha(1)

c.setFillColor(LILAS)
c.setFillAlpha(0.4)
c.setFont("Helvetica", 9)
c.drawRightString(W - 20*mm, 24, "autoncy.com")
c.setFillAlpha(1)

c.showPage()

# ─────────────────────────────────────────────
# PAGE 2 — ÍNDICE / SUMÁRIO
# ─────────────────────────────────────────────
c.setFillColor(NOITE)
c.rect(0, 0, W, H, fill=1, stroke=0)

# Left accent bar
c.setFillColor(ROXO_VIB)
c.rect(0, 0, 4, H, fill=1, stroke=0)

margin = 28*mm
y = H - 52*mm

section_tag(c, margin, y, "Sumário")
y -= 22

c.setFillColor(BRANCO)
c.setFont("Helvetica-Bold", 26)
c.drawString(margin, y, "O que está")
y -= 32
c.setFillColor(ROXO_VIB)
c.drawString(margin, y, "neste guia.")
y -= 50

items = [
    ("01", "Personalidade da marca", "03"),
    ("02", "Logo e variações",       "04"),
    ("03", "Paleta de cores",        "05"),
    ("04", "Tipografia",             "06"),
    ("05", "Cartão de visita",       "07"),
    ("06", "Camiseta",               "08"),
]

for num, title, pg in items:
    c.setFillColor(ROXO_VIB)
    c.setFillAlpha(0.15)
    c.roundRect(margin, y - 4, W - margin*2, 34, radius=6, fill=1, stroke=0)
    c.setFillAlpha(1)

    c.setFillColor(ROXO_VIB)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin + 12, y + 9, num)

    c.setFillColor(BRANCO)
    c.setFont("Helvetica", 13)
    c.drawString(margin + 38, y + 9, title)

    c.setFillColor(LILAS)
    c.setFillAlpha(0.5)
    c.setFont("Helvetica", 10)
    c.drawRightString(W - margin - 12, y + 9, f"p.{pg}")
    c.setFillAlpha(1)

    y -= 44

page_footer(c, 2)
c.showPage()

# ─────────────────────────────────────────────
# PAGE 3 — PERSONALIDADE
# ─────────────────────────────────────────────
c.setFillColor(NOITE)
c.rect(0, 0, W, H, fill=1, stroke=0)
c.setFillColor(ROXO_VIB)
c.rect(0, 0, 4, H, fill=1, stroke=0)

y = H - 52*mm
section_tag(c, margin, y, "01 · Personalidade")
y -= 22
c.setFillColor(BRANCO)
c.setFont("Helvetica-Bold", 26)
c.drawString(margin, y, "Quem é a Auton.")
y -= 14
c.setFillColor(LILAS)
c.setFillAlpha(0.5)
c.setFont("Helvetica", 10)
c.drawString(margin, y, "A essência que guia cada decisão visual e de comunicação.")
c.setFillAlpha(1)
y -= 36

divider(c, y, margin)
y -= 28

# Personality traits
traits = [
    ("Tecnológica",  "Linguagem precisa, interfaces limpas, referências ao universo de dados e sistemas."),
    ("Futurista",    "Visão de longo prazo, estética que aponta para o amanhã, não para o passado."),
    ("Confiável",    "Consistência visual, tom direto, sem exageros. Promessas que cabem na realidade."),
    ("Inovadora",    "Soluções sob medida, não enlatadas. Disposição para ir além do óbvio."),
    ("Sólida",       "Presença marcante, identidade coesa, marca que transmite seriedade e competência."),
]

for trait, desc in traits:
    # dot
    c.setFillColor(ROXO_VIB)
    c.circle(margin + 5, y + 6, 4, fill=1, stroke=0)

    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(margin + 18, y + 2, trait)

    c.setFillColor(LILAS)
    c.setFillAlpha(0.65)
    c.setFont("Helvetica", 10)
    c.drawString(margin + 18, y - 12, desc)
    c.setFillAlpha(1)
    y -= 44

y -= 10
divider(c, y, margin)
y -= 28

# Tone of voice
section_tag(c, margin, y, "Tom de voz")
y -= 22
tone_pairs = [
    ("Direto",      "Prolixo"),
    ("Técnico",     "Superficial"),
    ("Próximo",     "Frio"),
    ("Confiante",   "Arrogante"),
]
col_w = (W - margin*2) / 2 - 10
for pair in tone_pairs:
    for i, (word, anti) in enumerate([(pair[0], pair[1])]):
        # positive
        c.setFillColor(ROXO_VIB)
        c.setFillAlpha(0.15)
        c.roundRect(margin, y - 4, col_w, 26, radius=5, fill=1, stroke=0)
        c.setFillAlpha(1)
        c.setFillColor(ROXO_VIB)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(margin + 10, y + 6, f"✓  {word}")
        # negative
        c.setFillColor(HexColor("#ffffff"))
        c.setFillAlpha(0.04)
        c.roundRect(margin + col_w + 20, y - 4, col_w, 26, radius=5, fill=1, stroke=0)
        c.setFillAlpha(1)
        c.setFillColor(LILAS)
        c.setFillAlpha(0.35)
        c.setFont("Helvetica", 11)
        c.drawString(margin + col_w + 30, y + 6, f"✗  {anti}")
        c.setFillAlpha(1)
    y -= 36

page_footer(c, 3)
c.showPage()

# ─────────────────────────────────────────────
# PAGE 4 — LOGO
# ─────────────────────────────────────────────
c.setFillColor(NOITE)
c.rect(0, 0, W, H, fill=1, stroke=0)
c.setFillColor(ROXO_VIB)
c.rect(0, 0, 4, H, fill=1, stroke=0)

y = H - 52*mm
section_tag(c, margin, y, "02 · Logo")
y -= 22
c.setFillColor(BRANCO)
c.setFont("Helvetica-Bold", 26)
c.drawString(margin, y, "Logo e variações.")
y -= 14
c.setFillColor(LILAS)
c.setFillAlpha(0.5)
c.setFont("Helvetica", 10)
c.drawString(margin, y, "Quatro nós conectados — processos interligados, fluxo de dados, automação.")
c.setFillAlpha(1)
y -= 36
divider(c, y, margin)
y -= 28

logo_variants = [
    ("#1C1028", ROXO_VIB, BRANCO,    "Versão escura",   "Uso principal · redes sociais · apresentações"),
    ("#F5F3FF", ROXO_PRINC, ESCURO_TXT, "Versão clara", "Slides · documentos internos"),
    ("#FFFFFF", ROXO_PRINC, ESCURO_TXT, "Versão branca","E-mail · documentos formais · PDF"),
]

card_w = (W - margin*2 - 16) / 3
for i, (bg, lcolor, tcolor, name, desc) in enumerate(logo_variants):
    cx = margin + i * (card_w + 8)
    card_h = 100

    # bg card
    c.setFillColor(HexColor(bg))
    if bg == "#FFFFFF":
        c.setStrokeColor(LILAS)
        c.setStrokeAlpha(0.4)
        c.setLineWidth(0.5)
        c.roundRect(cx, y - card_h, card_w, card_h, radius=8, fill=1, stroke=1)
        c.setStrokeAlpha(1)
    else:
        c.roundRect(cx, y - card_h, card_w, card_h, radius=8, fill=1, stroke=0)

    draw_logo(c, cx + card_w/2 - 55, y - card_h/2 - 12, size=28, color=lcolor, text_color=tcolor, font_size=18)

    # label
    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(cx, y - card_h - 18, name)
    c.setFillColor(LILAS)
    c.setFillAlpha(0.55)
    c.setFont("Helvetica", 8)
    c.drawString(cx, y - card_h - 30, desc)
    c.setFillAlpha(1)

y -= card_h + 52

# Icon only — section tag
section_tag(c, margin, y, "Ícone isolado")
y -= 22

icon_bg_x = margin
icon_bg_y = y - 80
c.setFillColor(NOITE)
c.roundRect(icon_bg_x, icon_bg_y, 80, 80, radius=10, fill=1, stroke=0)
# draw icon only (no wordmark)
c.setFillColor(ROXO_VIB)
sq = 18; gap = 9; step = sq + gap
positions_i = [(icon_bg_x+11, icon_bg_y+11+step), (icon_bg_x+11+step, icon_bg_y+11+step),
               (icon_bg_x+11, icon_bg_y+11),       (icon_bg_x+11+step, icon_bg_y+11)]
opacities_i = [1.0, 0.35, 0.35, 1.0]
for i2, (px, py) in enumerate(positions_i):
    c.setFillAlpha(opacities_i[i2])
    c.roundRect(px, py, sq, sq, radius=sq*0.2, fill=1, stroke=0)
c.setFillAlpha(1)
c.setStrokeColor(ROXO_VIB); c.setStrokeAlpha(0.6); c.setLineWidth(1.2)
cx0 = icon_bg_x+11
c.line(cx0+sq, icon_bg_y+11+step+sq/2, cx0+step, icon_bg_y+11+step+sq/2)
c.line(cx0+sq, icon_bg_y+11+sq/2,      cx0+step, icon_bg_y+11+sq/2)
c.line(cx0+sq/2, icon_bg_y+11+sq,      cx0+sq/2, icon_bg_y+11+step)
c.line(cx0+step+sq/2, icon_bg_y+11+sq, cx0+step+sq/2, icon_bg_y+11+step)
c.setStrokeAlpha(1)

# Icon labels — directly below the icon box
c.setFillColor(BRANCO)
c.setFont("Helvetica-Bold", 10)
c.drawString(margin, icon_bg_y - 16, "Ícone isolado")
c.setFillColor(LILAS); c.setFillAlpha(0.55)
c.setFont("Helvetica", 8)
c.drawString(margin, icon_bg_y - 28, "Favicon · foto de perfil · WhatsApp · app icon")
c.setFillAlpha(1)

# ── REGRAS DE USO — posicionadas na parte inferior da página ──
rules_bottom_y = 38*mm  # ancora no rodapé, acima do footer

rules = [
    ("✓", "Manter proporções originais"),
    ("✓", "Usar versão de contraste adequado ao fundo"),
    ("✓", "Espaçamento mínimo equivalente à altura do ícone"),
    ("✗", "Não distorcer ou rotacionar"),
    ("✗", "Não alterar as cores da paleta"),
    ("✗", "Não usar sobre fundos sem contraste"),
]

# Calcula altura total do bloco de regras para posicionar de cima pra baixo
rule_block_h = 20 + len(rules) * 16
rule_start_y = rules_bottom_y + rule_block_h

section_tag(c, margin, rule_start_y + 2, "Regras de uso")

ry = rule_start_y - 16
for sym, rule in rules:
    color = ROXO_VIB if sym == "✓" else HexColor("#FF6B6B")
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin, ry, sym)
    c.setFillColor(LILAS if sym == "✓" else HexColor("#FFB3B3"))
    c.setFillAlpha(0.7)
    c.setFont("Helvetica", 10)
    c.drawString(margin + 16, ry, rule)
    c.setFillAlpha(1)
    ry -= 16

page_footer(c, 4)
c.showPage()

# ─────────────────────────────────────────────
# PAGE 5 — CORES
# ─────────────────────────────────────────────
c.setFillColor(NOITE)
c.rect(0, 0, W, H, fill=1, stroke=0)
c.setFillColor(ROXO_VIB)
c.rect(0, 0, 4, H, fill=1, stroke=0)

y = H - 52*mm
section_tag(c, margin, y, "03 · Cores")
y -= 22
c.setFillColor(BRANCO)
c.setFont("Helvetica-Bold", 26)
c.drawString(margin, y, "Paleta de cores.")
y -= 14
c.setFillColor(LILAS); c.setFillAlpha(0.5)
c.setFont("Helvetica", 10)
c.drawString(margin, y, "Cinco cores que sustentam toda a identidade visual.")
c.setFillAlpha(1)
y -= 36
divider(c, y, margin)
y -= 20

palette = [
    (NOITE,      "#1C1028", "Noite",        "Fundo principal, fundo do logo",          "bg-noite"),
    (ROXO_PRINC, "#7F77DD", "Roxo principal","Versão clara do logo, bordas, detalhes",  "brand-primary"),
    (ROXO_VIB,   "#9B7FE8", "Roxo vibrante","Ícone do logo, CTAs, destaques",          "brand-accent"),
    (LILAS,      "#CECBF6", "Lilás",         "Textos sobre fundo escuro, labels",       "text-light"),
    (NEVOA,      "#EEEDFE", "Névoa",         "Fundos claros, badges, tags",             "bg-light"),
]

swatch_h = 90
swatch_w = (W - margin*2 - 16) / 5

for i, (col, hex_, name, usage, var) in enumerate(palette):
    sx = margin + i * (swatch_w + 4)
    sy = y - swatch_h

    # Main swatch
    c.setFillColor(col)
    if col == NEVOA:
        c.setStrokeColor(LILAS); c.setStrokeAlpha(0.4); c.setLineWidth(0.5)
        c.roundRect(sx, sy, swatch_w, swatch_h, radius=8, fill=1, stroke=1)
        c.setStrokeAlpha(1)
    else:
        c.roundRect(sx, sy, swatch_w, swatch_h, radius=8, fill=1, stroke=0)

    # Name label
    txt_color = NOITE if col in [NEVOA, LILAS] else BRANCO
    c.setFillColor(txt_color)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(sx + 8, sy + 14, name)
    c.setFont("Helvetica", 8)
    c.drawString(sx + 8, sy + 5, hex_)

    # Below swatch
    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(sx, sy - 16, name)
    c.setFillColor(LILAS); c.setFillAlpha(0.55)
    c.setFont("Helvetica", 7.5)
    # wrap usage text
    words = usage.split(", ")
    line_y = sy - 27
    for w in words:
        c.drawString(sx, line_y, w)
        line_y -= 10
    c.setFillAlpha(1)

    # Token
    c.setFillColor(ROXO_VIB); c.setFillAlpha(0.12)
    c.roundRect(sx, sy - 80, swatch_w, 14, radius=4, fill=1, stroke=0)
    c.setFillAlpha(1)
    c.setFillColor(ROXO_VIB); c.setFont("Helvetica", 7)
    c.drawString(sx + 4, sy - 75, var)

y -= swatch_h + 110
divider(c, y, margin)
y -= 28

# Color combos
section_tag(c, margin, y, "Combinações aprovadas")
y -= 22

combos = [
    (NOITE, BRANCO,    "#1C1028", "#FFFFFF",  "Texto principal sobre fundo escuro"),
    (NOITE, LILAS,     "#1C1028", "#CECBF6",  "Labels e tags sobre fundo escuro"),
    (NOITE, ROXO_VIB,  "#1C1028", "#9B7FE8",  "Destaque / CTA sobre fundo escuro"),
    (NEVOA, ESCURO_TXT,"#EEEDFE", "#26215C",  "Texto sobre fundo claro"),
]

combo_w = (W - margin*2 - 12) / 4
for i, (bg, fg, bgh, fgh, label) in enumerate(combos):
    cx2 = margin + i * (combo_w + 4)
    c.setFillColor(bg)
    if bg == NEVOA:
        c.setStrokeColor(LILAS); c.setStrokeAlpha(0.4); c.setLineWidth(0.5)
        c.roundRect(cx2, y - 50, combo_w, 50, radius=6, fill=1, stroke=1)
        c.setStrokeAlpha(1)
    else:
        c.roundRect(cx2, y - 50, combo_w, 50, radius=6, fill=1, stroke=0)
    c.setFillColor(fg)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(cx2 + combo_w/2, y - 22, "Aa")
    c.setFont("Helvetica", 7)
    c.drawCentredString(cx2 + combo_w/2, y - 34, f"{bgh} · {fgh}")
    c.setFillColor(LILAS); c.setFillAlpha(0.55)
    c.setFont("Helvetica", 7)
    # wrap label
    words2 = label.split(" / ") if " / " in label else [label[:22], label[22:]] if len(label) > 22 else [label]
    ly2 = y - 60
    for w2 in words2:
        c.drawCentredString(cx2 + combo_w/2, ly2, w2)
        ly2 -= 10
    c.setFillAlpha(1)

page_footer(c, 5)
c.showPage()

# ─────────────────────────────────────────────
# PAGE 6 — TIPOGRAFIA
# ─────────────────────────────────────────────
c.setFillColor(NOITE)
c.rect(0, 0, W, H, fill=1, stroke=0)
c.setFillColor(ROXO_VIB)
c.rect(0, 0, 4, H, fill=1, stroke=0)

y = H - 52*mm
section_tag(c, margin, y, "04 · Tipografia")
y -= 22
c.setFillColor(BRANCO)
c.setFont("Helvetica-Bold", 26)
c.drawString(margin, y, "Tipografia.")
y -= 14
c.setFillColor(LILAS); c.setFillAlpha(0.5)
c.setFont("Helvetica", 10)
c.drawString(margin, y, "Fonte primária: Inter · Pesos: 400 Regular · 500 Medium · 600 SemiBold · 700 Bold")
c.setFillAlpha(1)
y -= 36
divider(c, y, margin)
y -= 30

type_specs = [
    ("Inter Bold",     "Helvetica-Bold", 36, "Inter Bold",     "28px · 700 · LH 1.2 · Headlines, capas"),
    ("Inter SemiBold", "Helvetica-Bold", 22, "Inter SemiBold", "18px · 600 · LH 1.3 · Subtítulos"),
    ("Inter Regular",  "Helvetica",      14, "Inter Regular",  "15px · 400 · LH 1.6 · Texto corrido"),
    ("Inter Medium",   "Helvetica-Bold",  9, "Inter Medium",   "11px · 500 · LH 1.4 · Tags, categorias"),
]

for role, font, size, sample, spec in type_specs:
    # row bg
    c.setFillColor(ROXO_VIB)
    c.setFillAlpha(0.04)
    c.roundRect(margin, y - size - 16, W - margin*2, size + 32, radius=6, fill=1, stroke=0)
    c.setFillAlpha(1)

    # nome da fonte no tamanho real do estilo
    c.setFillColor(BRANCO)
    c.setFont(font, size)
    c.drawString(margin + 10, y - size + 6, role)

    # spec
    c.setFillColor(LILAS); c.setFillAlpha(0.45)
    c.setFont("Helvetica", 8)
    c.drawRightString(W - margin - 10, y - size + 6, spec)
    c.setFillAlpha(1)

    y -= size + 44

y -= 10
divider(c, y, margin)
y -= 28

# Spacing
section_tag(c, margin, y, "Espaçamento e ritmo")
y -= 20
spacing_items = ["4px → micro espaço", "8px → espaço padrão", "16px → separação de elementos",
                 "32px → separação de seções", "64px → separação de blocos"]
for sp in spacing_items:
    val = int(sp.split("px")[0])
    c.setFillColor(ROXO_VIB)
    c.rect(margin, y - 6, min(val * 1.2, 80), 8, fill=1, stroke=0)
    c.setFillColor(LILAS); c.setFillAlpha(0.65)
    c.setFont("Helvetica", 9)
    c.drawString(margin + 90, y - 2, sp)
    c.setFillAlpha(1)
    y -= 18

page_footer(c, 6)
c.showPage()

# ─────────────────────────────────────────────
# PAGE 7 — CARTÃO DE VISITA
# ─────────────────────────────────────────────
c.setFillColor(NOITE)
c.rect(0, 0, W, H, fill=1, stroke=0)
c.setFillColor(ROXO_VIB)
c.rect(0, 0, 4, H, fill=1, stroke=0)

y = H - 52*mm
section_tag(c, margin, y, "05 · Cartão de visita")
y -= 22
c.setFillColor(BRANCO)
c.setFont("Helvetica-Bold", 26)
c.drawString(margin, y, "Cartão de visita.")
y -= 14
c.setFillColor(LILAS); c.setFillAlpha(0.5)
c.setFont("Helvetica", 10)
c.drawString(margin, y, "Medidas padrão: 85 × 55 mm · Frente e verso")
c.setFillAlpha(1)
y -= 36
divider(c, y, margin)
y -= 30

# Card dimensions at 3x scale
card_W = 85*mm * 1.6
card_H = 55*mm * 1.6

# ── FRENTE ──
label_x = margin
c.setFillColor(LILAS); c.setFillAlpha(0.4)
c.setFont("Helvetica", 8)
c.drawString(label_x, y, "FRENTE")
c.setFillAlpha(1)
y -= 12

# Card frente — dark bg
c.setFillColor(NOITE)
c.setStrokeColor(ROXO_VIB); c.setStrokeAlpha(0.25); c.setLineWidth(0.5)
c.roundRect(margin, y - card_H, card_W, card_H, radius=10, fill=1, stroke=1)
c.setStrokeAlpha(1)

# Subtle grid on card
c.setStrokeColor(ROXO_PRINC); c.setStrokeAlpha(0.05); c.setLineWidth(0.4)
for gi in range(0, int(card_W)+1, 15):
    c.line(margin + gi, y - card_H, margin + gi, y)
c.setStrokeAlpha(1)

# Logo on card
draw_logo(c, margin + 16, y - 42, size=26, color=ROXO_VIB, text_color=BRANCO, font_size=17)

# Bottom info
c.setFillColor(BRANCO)
c.setFont("Helvetica-Bold", 11)
c.drawString(margin + 16, y - card_H + 34, "Pedro Henrique")
c.setFillColor(LILAS); c.setFillAlpha(0.6)
c.setFont("Helvetica", 9)
c.drawString(margin + 16, y - card_H + 22, "Fundador · Auton")
c.setFillAlpha(1)
c.setFillColor(ROXO_VIB)
c.setFont("Helvetica", 9)
c.drawString(margin + 16, y - card_H + 10, "pedro@autoncy.com")

# Right side — contact
c.setFillColor(LILAS); c.setFillAlpha(0.5)
c.setFont("Helvetica", 8)
c.drawRightString(margin + card_W - 16, y - card_H + 34, "autoncy.com")
c.drawRightString(margin + card_W - 16, y - card_H + 22, "+55 61 98236-5437")
c.setFillAlpha(1)

# Accent line at bottom of card
c.setFillColor(ROXO_VIB)
c.roundRect(margin, y - card_H, card_W, 4, radius=2, fill=1, stroke=0)

# ── VERSO ──
verso_x = margin + card_W + 20
c.setFillColor(LILAS); c.setFillAlpha(0.4)
c.setFont("Helvetica", 8)
c.drawString(verso_x, y, "VERSO")
c.setFillAlpha(1)

c.setFillColor(NOITE)
c.setStrokeColor(ROXO_VIB); c.setStrokeAlpha(0.25); c.setLineWidth(0.5)
c.roundRect(verso_x, y - card_H, card_W, card_H, radius=10, fill=1, stroke=1)
c.setStrokeAlpha(1)

# Big centered icon on verso
sq2 = 30; gap2 = 14; step2 = sq2 + gap2
ix = verso_x + card_W/2 - sq2 - gap2/2
iy = y - card_H/2 - sq2 - gap2/2
pos2 = [(ix, iy + step2), (ix + step2, iy + step2), (ix, iy), (ix + step2, iy)]
op2  = [1.0, 0.3, 0.3, 1.0]
for i2, (px2, py2) in enumerate(pos2):
    c.setFillColor(ROXO_VIB); c.setFillAlpha(op2[i2])
    c.roundRect(px2, py2, sq2, sq2, radius=6, fill=1, stroke=0)
c.setFillAlpha(1)
c.setStrokeColor(ROXO_VIB); c.setStrokeAlpha(0.5); c.setLineWidth(1.5)
c.line(ix + sq2, iy + step2 + sq2/2, ix + step2, iy + step2 + sq2/2)
c.line(ix + sq2, iy + sq2/2,         ix + step2, iy + sq2/2)
c.line(ix + sq2/2, iy + sq2,         ix + sq2/2, iy + step2)
c.line(ix + step2 + sq2/2, iy + sq2, ix + step2 + sq2/2, iy + step2)
c.setStrokeAlpha(1)

c.setFillColor(ROXO_VIB); c.setFillAlpha(1)
c.roundRect(verso_x, y - card_H, card_W, 4, radius=2, fill=1, stroke=0)

# Tagline below icon
c.setFillColor(LILAS); c.setFillAlpha(0.45)
c.setFont("Helvetica", 8)
c.drawCentredString(verso_x + card_W/2, iy - 12, "Process & Flow")
c.setFillAlpha(1)

y -= card_H + 40
divider(c, y, margin)
y -= 22

# Print specs
section_tag(c, margin, y, "Especificações para gráfica")
y -= 20
specs = [
    "Formato: 85 × 55 mm + 3mm de sangria (91 × 61 mm final)",
    "Resolução: 300 dpi mínimo",
    "Modo de cor: CMYK",
    "Frente: Noite #1C1028 → CMYK(72, 83, 44, 53) aprox.",
    "Roxo vibrante #9B7FE8 → CMYK(38, 49, 0, 9) aprox.",
    "Acabamento sugerido: couchê 300g + laminação fosca",
]
for sp in specs:
    c.setFillColor(LILAS); c.setFillAlpha(0.6)
    c.circle(margin + 4, y + 3, 2, fill=1, stroke=0)
    c.setFillColor(LILAS); c.setFillAlpha(0.7)
    c.setFont("Helvetica", 9)
    c.drawString(margin + 12, y, sp)
    c.setFillAlpha(1)
    y -= 14

page_footer(c, 7)
c.showPage()

# ─────────────────────────────────────────────
# PAGE 8 — CAMISETA
# ─────────────────────────────────────────────
c.setFillColor(NOITE)
c.rect(0, 0, W, H, fill=1, stroke=0)
c.setFillColor(ROXO_VIB)
c.rect(0, 0, 4, H, fill=1, stroke=0)

y = H - 52*mm
section_tag(c, margin, y, "06 · Camiseta")
y -= 22
c.setFillColor(BRANCO)
c.setFont("Helvetica-Bold", 26)
c.drawString(margin, y, "Camiseta.")
y -= 14
c.setFillColor(LILAS); c.setFillAlpha(0.5)
c.setFont("Helvetica", 10)
c.drawString(margin, y, "Duas versões: escura (principal) e clara (alternativa)")
c.setFillAlpha(1)
y -= 36
divider(c, y, margin)
y -= 20

def draw_tshirt(c, cx, cy, shirt_color, logo_color, text_color, label):
    """Draw a simple t-shirt outline with Auton branding."""
    bw = 130  # body width
    bh = 160  # body height
    sw = 50   # sleeve width
    sh = 55   # sleeve height
    nc = 30   # neck width

    bx = cx - bw/2
    by = cy - bh

    # Body
    c.setFillColor(shirt_color)
    body_path = c.beginPath()
    body_path.moveTo(bx, by + bh)  # top-left shoulder
    body_path.lineTo(bx - sw, by + bh - sh)  # sleeve tip left
    body_path.lineTo(bx - sw + 20, by + bh - sh - 10)
    body_path.lineTo(bx + 18, by + bh - 28)  # armpit left
    body_path.lineTo(bx, by)  # bottom-left
    body_path.lineTo(bx + bw, by)  # bottom-right
    body_path.lineTo(bx + bw - 18, by + bh - 28)  # armpit right
    body_path.lineTo(bx + bw + sw - 20, by + bh - sh - 10)
    body_path.lineTo(bx + bw + sw, by + bh - sh)  # sleeve tip right
    body_path.lineTo(bx + bw, by + bh)  # top-right shoulder
    # Neck
    body_path.arcTo(bx + bw/2 - nc/2, by + bh - nc/2,
                    bx + bw/2 + nc/2, by + bh + nc/2, 0, 180)
    body_path.close()
    c.drawPath(body_path, fill=1, stroke=0)

    # Subtle shirt texture
    c.setStrokeColor(logo_color)
    c.setStrokeAlpha(0.05)
    c.setLineWidth(0.3)
    for li in range(int(by), int(by + bh), 8):
        c.line(bx, li, bx + bw, li)
    c.setStrokeAlpha(1)

    # Logo on chest
    logo_size = 38
    draw_logo(c, cx - logo_size * 1.1, by + bh * 0.55, size=logo_size,
              color=logo_color, text_color=text_color, font_size=24)

    # Label below shirt
    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(cx, by - 20, label)

# Dark shirt
draw_tshirt(c, W/2 - 110, y - 30,
            shirt_color=HexColor("#1C1028"),
            logo_color=ROXO_VIB,
            text_color=BRANCO,
            label="Versão escura")

# Light shirt
draw_tshirt(c, W/2 + 110, y - 30,
            shirt_color=NEVOA,
            logo_color=ROXO_PRINC,
            text_color=ESCURO_TXT,
            label="Versão clara")

y -= 230
divider(c, y, margin)
y -= 22

section_tag(c, margin, y, "Variações adicionais")
y -= 20

# Small badges
extras = [
    ("Só ícone — costas",  NOITE,  ROXO_VIB),
    ("Tagline — manga",    NOITE,  LILAS),
    ("Monocromático",      HexColor("#2D2D2D"), BRANCO),
]
badge_w = (W - margin*2 - 16) / 3
for i2, (name, bg, fg) in enumerate(extras):
    bx2 = margin + i2 * (badge_w + 8)
    c.setFillColor(bg)
    if bg == NEVOA:
        c.setStrokeColor(LILAS); c.setStrokeAlpha(0.3); c.setLineWidth(0.5)
        c.roundRect(bx2, y - 50, badge_w, 50, radius=8, fill=1, stroke=1)
        c.setStrokeAlpha(1)
    else:
        c.roundRect(bx2, y - 50, badge_w, 50, radius=8, fill=1, stroke=0)
    # small logo
    draw_logo(c, bx2 + 10, y - 38, size=18, color=fg, text_color=fg,
              label="" if "ícone" in name.lower() else "Auton", font_size=12)
    c.setFillColor(BRANCO if bg != NEVOA else NOITE)
    c.setFont("Helvetica", 8)
    c.drawCentredString(bx2 + badge_w/2, y - 62, name)

y -= 80
divider(c, y, margin)
y -= 22

# Print specs
section_tag(c, margin, y, "Especificações para confecção")
y -= 20
shirt_specs = [
    "Estampa: serigrafia ou DTF (recomendado para pequenas tiragens)",
    "Posição: peito esquerdo (logo) — 8 × 8 cm aprox.",
    "Cor de fundo escuro: usar Pantone 2755C (aprox. do Roxo vibrante)",
    "Tecido recomendado: malha 100% algodão 30.1 penteado",
    "Cores CMYK para estampa clara: C38 M49 B0 K9 (Roxo vibrante)",
]
for sp in shirt_specs:
    c.setFillColor(LILAS); c.setFillAlpha(0.6)
    c.circle(margin + 4, y + 3, 2, fill=1, stroke=0)
    c.setFillColor(LILAS); c.setFillAlpha(0.7)
    c.setFont("Helvetica", 9)
    c.drawString(margin + 12, y, sp)
    c.setFillAlpha(1)
    y -= 14

page_footer(c, 8)
c.showPage()

c.save()
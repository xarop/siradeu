#!/usr/bin/env python3
"""Genera els contenidors fotogràfics SVG (placeholders) de la web siradeu.com."""
import os

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(DIR, exist_ok=True)

TPL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800" preserveAspectRatio="xMidYMid slice" role="img" aria-label="{label}">
<defs>
<linearGradient id="a" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
<linearGradient id="b" x1="0" y1="0" x2="0.6" y2="1"><stop offset="0" stop-color="{c3}" stop-opacity="0.95"/><stop offset="1" stop-color="{c4}" stop-opacity="0.55"/></linearGradient>
</defs>
<rect width="1200" height="800" fill="url(#a)"/>
<rect width="1200" height="46" fill="{c2}" opacity="0.6"/>
<g fill="none" stroke="{c3}" stroke-width="10" opacity="0.45">
<path d="M70 640V330a80 80 0 0 1 160 0v310"/><path d="M310 640V330a80 80 0 0 1 160 0v310"/>
<path d="M550 640V330a80 80 0 0 1 160 0v310"/><path d="M790 640V330a80 80 0 0 1 160 0v310"/>
<path d="M1030 640V330a80 80 0 0 1 160 0v310"/></g>
<g fill="url(#b)">
<rect x="80" y="360" width="140" height="270" rx="4"/><rect x="320" y="360" width="140" height="270" rx="4"/>
<rect x="560" y="360" width="140" height="270" rx="4"/><rect x="800" y="360" width="140" height="270" rx="4"/>
<rect x="1040" y="360" width="140" height="270" rx="4"/></g>
<g stroke="{c3}" stroke-width="6" opacity="0.4">
<line x1="80" y1="480" x2="220" y2="480"/><line x1="320" y1="480" x2="460" y2="480"/>
<line x1="560" y1="480" x2="700" y2="480"/><line x1="800" y1="480" x2="940" y2="480"/>
<line x1="1040" y1="480" x2="1180" y2="480"/></g>
<rect y="640" width="1200" height="160" fill="{c2}" opacity="0.85"/>
<g fill="{c3}" opacity="0.3"><circle cx="150" cy="700" r="46"/><circle cx="1060" cy="712" r="38"/></g>
<g fill="none" stroke="{c4}" stroke-width="9" opacity="0.75"><rect x="470" y="596" width="270" height="204"/><line x1="605" y1="596" x2="605" y2="800"/></g>
<rect x="24" y="24" width="1152" height="752" fill="none" stroke="{c4}" stroke-width="3" opacity="0.25"/>
</svg>
"""

SHOTS = [
    ("portada-facade", "#EFE7DA", "#E2D7C6", "#C89662", "#2D5A40", "Façana de Verdi 85 amb els arcs originals"),
    ("portada-interior", "#2D5A40", "#1F3F2C", "#C89662", "#FDFBF7", "Interior de l'espai amb els arcs"),
    ("portada-carrer", "#FDFBF7", "#E0DDD5", "#C89662", "#2D5A40", "Carrer de Verdi a primera hora"),
    ("coworking-llum", "#FDFBF7", "#EFE7DA", "#2D5A40", "#C89662", "Sala de coworking amb llum natural"),
    ("coworking-taula", "#EAF0EA", "#DCE6DD", "#2D5A40", "#C89662", "Taules de treball compartides"),
    ("despatxos", "#F1E9DE", "#E2D7C6", "#2D5A40", "#C89662", "Despatx privat amb finestres al carrer"),
    ("despatxos-reunio", "#EAF0EA", "#D6E2D8", "#C89662", "#1A1A1A", "Sala de reunions de l'espai"),
    ("tallers", "#FDFBF7", "#E7DFD2", "#C89662", "#2D5A40", "Taller impartint un workshop"),
    ("tallers-eines", "#EFE7DA", "#DFD2BE", "#2D5A40", "#C89662", "Eines i taules de taller"),
    ("activitats", "#2D5A40", "#244733", "#C89662", "#FDFBF7", "Xerrada a la sala del barri"),
    ("activitats-public", "#FDFBF7", "#E0DDD5", "#2D5A40", "#C89662", "Trobada veïnal al carrer"),
    ("botiga", "#F5E9DC", "#EADCC8", "#C89662", "#2D5A40", "Botiga efímera a Verdi 85"),
    ("botiga-shooting", "#EAF0EA", "#D9E4DA", "#2D5A40", "#C89662", "Rodatge d'un pop-up store"),
    ("associacio", "#FDFBF7", "#EDEAE2", "#2D5A40", "#C89662", "Sala de l'EspaiGràcia Associació"),
    ("mapa", "#F1EDE4", "#E4DED2", "#2D5A40", "#C89662", "Mapa esquemàtic del carrer de Verdi"),
]

for name, c1, c2, c3, c4, label in SHOTS:
    with open(os.path.join(DIR, name + ".svg"), "w", encoding="utf-8") as fh:
        fh.write(TPL.format(label=label, c1=c1, c2=c2, c3=c3, c4=c4))
    print("ok", name)

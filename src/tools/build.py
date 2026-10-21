#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Constructor del lloc siradeu.com.

El contingut viu als mòduls Python de `src/tools/page_*.py`. Aquest script
compon cada pàgina amb la capçalera i el peu de `common.py` i escriu el resultat
a `dist/`, que és el directori que es publica al servidor.

Ús:
    python3 src/tools/build.py [--out dist] [--check]
"""

import argparse
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
ROOT = os.path.dirname(SRC)
sys.path.insert(0, HERE)

import common  # noqa: E402
import validate  # noqa: E402

# Pàgina -> (títol, descripció, mòdul)
PAGES = [
    ("index.html", "Portada", "Espai Sira10 al carrer de Verdi 85 de Vila de Gràcia: coworking, despatxos, tallers, activitats i botiga efímera. Economia de proximitat i Km 0.", "page_index"),
    ("coworking.html", "Coworking", "Taules de treball i espais de concentració a Vila de Gràcia per hores, dies o setmanes. Sense contracte de llarg termini, a pocs passos del mercat.", "page_coworking"),
    ("despatxos.html", "Despatxos", "Despatxos privats per a equips i autònoms al carrer de Verdi 85. Sala de reunions, connectivitat i preus de barri.", "page_despatxos"),
    ("tallers.html", "Tallers", "Espai per impartir tallers, cursos i formació veïnal. Sales equipades, tarifes socials i suport de l'associació.", "page_tallers"),
    ("activitats.html", "Activitats", "Agenda d'activitats, xerrades i formació al barri. Escull el teu propi taller o proposa una activitat de comunitat.", "page_activitats"),
    ("botiga.html", "Botiga", "Botiga efímera a Verdi 85: el teu producte exposat a peu de carrer, amb campanyes per a comerços Km 0 i economia de proximitat.", "page_botiga"),
    ("associacio.html", "Associació", "Qui som: EspaiGràcia Associació, entitat sense ànim de lucre que gestiona l'Espai Sira10 per l'economia de proximitat de Vila de Gràcia.", "page_associacio"),
]


def build_page(filename, title, desc, module_name, base_url=None, robots=None):
    """Compon una pàgina completa a partir del cos del mòdul.

    base_url: URL pública on viu la pàgina (p. ex. https://siradeu.com/2026/).
              Si és None, no s'emet cap canonical.
    robots:   valor del meta robots.
    """
    module = __import__(module_name)
    body = module.BODY.strip()

    canonical = None
    if base_url:
        canonical = base_url.rstrip("/") + "/" + filename

    # El mòdul ja inclou <main id="main">…</main>; el peu el tanca.
    parts = [
        common.head(title, desc, canonical=canonical, robots=robots),
        common.header(filename),
        body,
        common.footer(),
    ]
    return "\n".join(parts)


def copy_assets(out_dir):
    """Copia css/, js/ i img/ al directori de sortida."""
    for folder in ("css", "js", "img"):
        src = os.path.join(SRC, folder)
        dst = os.path.join(out_dir, folder)
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)


def build(out_dir, check=False, base_url=None, robots=None):
    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)

    for filename, title, desc, module_name in PAGES:
        html = build_page(filename, title, desc, module_name,
                          base_url=base_url, robots=robots)
        path = os.path.join(out_dir, filename)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        print("  ✓ %-20s %6d bytes" % (filename, len(html.encode("utf-8"))))

    copy_assets(out_dir)
    print("  ✓ actius copiats (css, js, img)")

    if check:
        errors, pages = validate.check_dist(out_dir)
        if errors:
            print("\n✗ %d problema/es detectat/s:" % len(errors))
            for err in errors:
                print("   - %s" % err)
            return 1
        print("  ✓ validació OK (%d pàgines)" % len(pages))

    return 0


def main():
    parser = argparse.ArgumentParser(description="Construeix el lloc siradeu.com")
    parser.add_argument("--out", default=os.path.join(ROOT, "dist"), help="directori de sortida")
    parser.add_argument("--check", action="store_true", help="valida l'HTML generat")
    parser.add_argument("--base-url", default=None,
                        help="URL pública de la publicació, per als metadats canonical")
    parser.add_argument("--robots", default=None,
                        help="valor del meta robots (p. ex. 'noindex, nofollow')")
    args = parser.parse_args()

    print("Construint %s" % args.out)
    code = build(args.out, check=args.check, base_url=args.base_url, robots=args.robots)
    return code


if __name__ == "__main__":
    sys.exit(main())

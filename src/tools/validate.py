# -*- coding: utf-8 -*-
"""Comprovacions de qualitat sobre l'HTML generat: estructura, enllaços i actius."""

import os
import re
from html.parser import HTMLParser

VOID = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}

# Etiquetes que es poden tancar sol, encara que l'HTML original les deixi obertes.
OPTIONAL_CLOSE = {"li", "dt", "dd", "p", "thead", "tbody", "tfoot", "tr", "th", "td", "option"}


class Balance(HTMLParser):
    """Comprova que les etiquetes estiguin anidades correctament."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.ids = []
        self.h1 = 0
        self.images = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if d.get("id"):
            self.ids.append(d["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "img":
            self.images.append(d)
        if tag in VOID:
            return
        self.stack.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        d = dict(attrs)
        if d.get("id"):
            self.ids.append(d["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "img":
            self.images.append(d)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append("</%s> sobrant (línia %d)" % (tag, self.getpos()[0]))
            return
        if self.stack[-1][0] == tag:
            self.stack.pop()
            return
        if tag in [t for t, _ in self.stack]:
            while self.stack and self.stack[-1][0] != tag:
                t, ln = self.stack.pop()
                self.errors.append("<%s> no tancada (línia %d)" % (t, ln))
            if self.stack:
                self.stack.pop()
        else:
            self.errors.append("</%s> sobrant (línia %d)" % (tag, self.getpos()[0]))

    def close(self):
        super().close()
        for t, ln in self.stack:
            self.errors.append("<%s> no tancada (línia %d)" % (t, ln))
        self.stack = []


def check_page(path, out_dir):
    """Retorna una llista d'errors per a una pàgina HTML."""
    errors = []
    html = open(path, encoding="utf-8").read()

    parser = Balance()
    parser.feed(html)
    parser.close()
    errors.extend(parser.errors)

    # Un únic h1 per pàgina
    if parser.h1 != 1:
        errors.append("s'hauria de tenir exactament un h1 (n'hi ha %d)" % parser.h1)

    # Identificadors duplicats
    dupes = sorted({i for i in parser.ids if parser.ids.count(i) > 1})
    if dupes:
        errors.append("id duplicat(s): %s" % ", ".join(dupes))

    # imgs sense alt
    for img in parser.images:
        if not img.get("alt"):
            errors.append("imatge sense alt: %s" % img.get("src", "?"))

    # Enllaços i actius interns
    for attr, value in re.findall(r'(href|src)="([^"]+)"', html):
        if value.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
            continue
        target = value.split("#")[0].split("?")[0]
        if not target:
            continue
        resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
        if not os.path.exists(resolved):
            errors.append("enllaç trencat: %s -> %s" % (attr, value))
        elif os.path.isdir(resolved):
            errors.append("enllaç a directori: %s -> %s" % (attr, value))

    # marcadors interns (#id) que existeixin
    for anchor in re.findall(r'href="#([^"]+)"', html):
        if anchor and anchor not in parser.ids:
            errors.append("marcador intern inexistent: #%s" % anchor)

    # referències aria-labelledby / aria-describedby / aria-controls cap a ids reals
    for attr in ("aria-labelledby", "aria-describedby", "aria-controls"):
        for ref in re.findall(r'%s="([^"]+)"' % attr, html):
            for one in ref.split():
                if one not in parser.ids:
                    errors.append("%s apunta a un id inexistent: %s" % (attr, one))

    # etiqueta <label for="..."> associada a un control existent
    for target in re.findall(r'<label[^>]*\bfor="([^"]+)"', html):
        if target not in parser.ids:
            errors.append('<label for="%s"> sense control associat' % target)

    # ids referenciats des de l'atribut href="#..."
    for anchor in re.findall(r'<a[^>]*\bname="([^"]+)"', html):
        if anchor not in parser.ids:
            errors.append("<a name> duplicat o inexistent: %s" % anchor)

    return errors


def check_dist(out_dir):
    """Comprova totes les pàgines d'un directori de sortida. Retorna (errors, resum)."""
    errors = []
    pages = sorted(
        os.path.join(out_dir, f) for f in os.listdir(out_dir) if f.endswith(".html")
    )
    for page in pages:
        for err in check_page(page, out_dir):
            errors.append("%s: %s" % (os.path.basename(page), err))
    return errors, pages

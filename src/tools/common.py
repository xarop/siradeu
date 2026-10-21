# -*- coding: utf-8 -*-
"""Plantilles comunes (capçalera, navegació i peu) per a siradeu.com."""

SITE = "siradeu.com"
ADDR = "Carrer de Verdi, 85 · 08012 Vila de Gràcia, Barcelona"
MAIL = "hola@siradeu.com"
PHONE = "+34 933 000 085"
IG = "@siradeu"
IG_URL = "https://instagram.com/siradeu"

NAV = [
    ("index.html", "Portada"),
    ("coworking.html", "Coworking"),
    ("despatxos.html", "Despatxos"),
    ("tallers.html", "Tallers"),
    ("activitats.html", "Activitats"),
    ("botiga.html", "Botiga"),
    ("associacio.html", "Associació"),
]


def head(title, desc, depth=0, canonical=None, robots=None):
    """depth: 0 = arrel, 1 = carpeta.

    canonical: URL pública de la pàgina (per als metadats i les xarxes socials).
    robots:    valor del meta robots; "noindex, nofollow" a la previsió.
    """
    up = "../" if depth else ""
    canonical_tag = ""
    if canonical:
        # La imatge social es refereix a l'arrel del lloc, no a la pàgina.
        site_root = canonical.rsplit("/", 1)[0] if canonical.endswith(".html") else canonical.rstrip("/")
        canonical_tag = (
            '<link rel="canonical" href="{canon}">\n'
            '<meta property="og:type" content="website">\n'
            '<meta property="og:site_name" content="{site}">\n'
            '<meta property="og:title" content="{title} · {site}">\n'
            '<meta property="og:description" content="{desc}">\n'
            '<meta property="og:url" content="{canon}">\n'
            '<meta property="og:image" content="{canon_img}">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
        ).format(canon=canonical, site=SITE, title=title, desc=desc,
                 canon_img=site_root.rstrip("/") + "/img/portada-facade.svg")
    robots_tag = ""
    if robots:
        robots_tag = '<meta name="robots" content="{robots}">\n'.format(robots=robots)
    return """<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {site}</title>
<meta name="description" content="{desc}">
<meta name="author" content="EspaiGràcia Associació">
<meta name="theme-color" content="#2D5A40">
{canonical_tag}{robots_tag}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}css/style.css">
<link rel="icon" href="{up}img/mapa.svg" type="image/svg+xml">
</head>
<body>
<a class="skip-link" href="#main">Saltar al contingut principal</a>
""".format(title=title, site=SITE, desc=desc, up=up,
           canonical_tag=canonical_tag, robots_tag=robots_tag)


def header(active, depth=0):
    up = "../" if depth else ""
    menu_items = "\n".join(
        '        <li><a href="{up}{href}">{label}</a></li>'.format(up=up, href=href, label=label)
        for href, label in NAV
    )
    return """
<header class="site-header">
  <div class="topbar">
    <div class="wrap topbar__inner">
      <span class="topbar__tagline">Espai Sira10 · Vila de Gràcia</span>
      <span class="topbar__tagline" aria-hidden="true">|</span>
      <span>Economia de proximitat &amp; Km 0</span>
      <div class="topbar__links">
        <a href="mailto:{mail}">{mail}</a>
        <a href="{up}associacio.html">Qui som</a>
        <a href="{ig_url}" rel="noopener noreferrer" target="_blank">{ig}</a>
      </div>
    </div>
  </div>

  <div class="masthead">
    <div class="wrap masthead__inner">
      <div class="masthead__side masthead__side--left">
        <strong>{addr1}</strong>
        <span>{addr2}</span>
      </div>
      <div class="masthead__brand">
        <a class="masthead__logo" href="{up}index.html">siradeu</a>
        <span class="masthead__sub">La Gazeta de Verdi 85</span>
      </div>
      <div class="masthead__side masthead__side--right">
        <span class="small">Espai Sira10</span>
        <div class="masthead__actions">
          <button type="button" class="btn btn--ghost btn--sm print-btn" data-print>
            <span aria-hidden="true">&#128424;</span>
            <span>Imprimir Full de Premsa<span class="print-btn__full"> A4</span></span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <nav class="nav" aria-label="Navegació principal">
    <div class="wrap nav__inner">
      <button type="button" class="nav__toggle" data-nav-toggle aria-expanded="false" aria-controls="nav-menu">
        <span class="nav__toggle-bars" aria-hidden="true"><span></span><span></span><span></span></span>
        <span data-nav-label>Menú</span>
      </button>
      <ul class="nav__menu" id="nav-menu" data-nav-menu>
{menu_items}
      </ul>
      <div class="nav__cta">
        <a class="btn btn--green btn--sm" href="mailto:{mail}">Contacta'ns</a>
      </div>
    </div>
  </nav>
</header>
""".format(
        up=up, mail=MAIL, ig=IG, ig_url=IG_URL,
        addr1="Carrer de Verdi, 85",
        addr2="08012 Vila de Gràcia · Barcelona",
        menu_items=menu_items,
    )


def footer(depth=0):
    up = "../" if depth else ""
    nav_links = "\n".join(
        '            <li><a href="{up}{href}">{label}</a></li>'.format(up=up, href=href, label=label)
        for href, label in NAV
    )
    return """
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <a class="footer__brand" href="{up}index.html">siradeu</a>
        <p class="small">Espai Sira10 · Carrer de Verdi, 85<br>08012 Vila de Gràcia, Barcelona</p>
        <p class="small">Un projecte de <a href="{up}associacio.html">EspaiGràcia Associació</a>, entitat sense ànim de lucre que treballa per l’economia de proximitat del barri.</p>
      </div>
      <div>
        <p class="footer__title">Seccions</p>
        <ul class="footer__list">
{nav_links}
        </ul>
      </div>
      <div>
        <p class="footer__title">Contacte</p>
        <ul class="footer__list">
          <li><a href="mailto:{mail}">{mail}</a></li>
          <li><a href="tel:{phone_clean}">{phone}</a></li>
          <li>{addr}</li>
        </ul>
      </div>
      <div>
        <p class="footer__title">Horari d’atenció</p>
        <ul class="footer__list">
          <li>Dilluns – divendres · 9:00 – 19:00</li>
          <li>Dissabte · 10:00 – 14:00 (cita prèvia)</li>
          <li>Diumenge · tancat</li>
        </ul>
        <p class="small"><a href="https://instagram.com/siradeu" rel="noopener noreferrer" target="_blank">{ig}</a> · Segueix l’activitat diària</p>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> EspaiGràcia Associació · <span class="small">Llicència Creative Commons BY-NC-SA</span></span>
      <span class="small">Full de premsa imprès / PDF A4 · Fet al barri, per al barri</span>
    </div>
  </div>
</footer>
<script src="{up}js/main.js" defer></script>
</body>
</html>
""".format(
        up=up, mail=MAIL, phone=PHONE, phone_clean=PHONE.replace(" ", ""),
        addr=ADDR, ig=IG, nav_links=nav_links,
    )

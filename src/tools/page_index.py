# -*- coding: utf-8 -*-
"""Contingut de la portada (index.html) — estil diari de barri."""

BODY = """
<main id="main">

  <!-- Capçalera de diari -->
  <div class="wrap">
    <div class="newspaper-head">
      <div class="newspaper-head__edition">
        <span>Any XII</span>
        <span>Núm. 085</span>
        <span>Carrer de Verdi, 85</span>
      </div>
      <div class="newspaper-head__edition">
        <span>Vila de Gràcia</span>
        <span>Barcelona</span>
        <span>Economia de proximitat</span>
      </div>
    </div>
  </div>

  <!-- Portada / hero -->
  <section class="hero" aria-labelledby="hero-title">
    <div class="hero__media">
      <img src="img/portada-facade.svg" alt="Façana del local d’Espai Sira10 al carrer de Verdi, 85, amb els arcs originals de l’edifici." width="1200" height="800">
      <div class="hero__overlay">
        <div class="wrap hero__inner">
          <span class="kicker">Espai Sira10 · Vila de Gràcia</span>
          <h1 id="hero-title">Un espai per treballar, compartir i fer barri</h1>
          <p class="hero__lead">Al carrer de Verdi, 85, hi ha llum, taules i gent. Coworking, despatxos, tallers, botiga efímera i una agenda oberta al barri — tot regit per una associació sense ànim de lucre.</p>
          <div class="hero__actions">
            <a class="btn btn--clay" href="coworking.html">Troba el teu espai</a>
            <a class="btn btn--ghost" href="activitats.html">Agenda del barri</a>
            <button type="button" class="btn btn--ghost print-btn" data-print>
              <span aria-hidden="true">&#128424;</span>
              <span>Imprimir Full de Premsa<span class="print-btn__full"> A4</span></span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Manifest -->
  <section class="section" aria-labelledby="manifest-title">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <article>
          <span class="kicker">Manifest</span>
          <h2 id="manifest-title">“La Gazeta de Verdi 85”</h2>
          <p class="lead-story__text">SIRADEU és un projecte que vol <strong>ajudar</strong>: un espai de treball comunitari al carrer de Verdi, 85, gestionat per l’EspaiGràcia Associació, una entitat sense ànim de lucre que creu en l’economia de proximitat, el Km 0 i la vida de barri.</p>
          <p>No és només un coworking. És un lloc on es pot venir a treballar a primera hora, impartir un taller el dissabte, muntar un pop-up durant una setmana o participar en una assemblea veïnal. Un únic edifici, moltes maneres d’estar-hi.</p>
          <blockquote>
            “El barri no es fa només de comerç. Es fa de gent que es troba, que treballa plegada i que es queda.”
            <cite>EspaiGràcia Associació</cite>
          </blockquote>
          <p>Cada euro que entra a l’espai torna al barri: en descomptes per a comerços de proximitat, en tallers gratuïts per a veïns i en espais cedits a col·lectius sense recursos. La transparència és el nostre llibre de registre.</p>
          <p><a class="btn btn--green" href="associacio.html">Qui som i com treballem</a></p>
        </article>

        <aside aria-labelledby="sumari-title">
          <div class="section-head">
            <h2 id="sumari-title">Sumari</h2>
            <span class="section-head__meta">Aquest número</span>
          </div>
          <ol class="contents">
            <li>
              <h3 class="contents__title"><a href="coworking.html">Coworking: taules flex i despatxos fixos</a></h3>
              <p class="contents__meta">Tarifes socials · fibra · llum natural</p>
            </li>
            <li>
              <h3 class="contents__title"><a href="despatxos.html">Despatxos privats per a equips</a></h3>
              <p class="contents__meta">De 2 a 12 persones · sala de reunions</p>
            </li>
            <li>
              <h3 class="contents__title"><a href="tallers.html">Espai per a talleristes</a></h3>
              <p class="contents__meta">Formulari de proposta obert</p>
            </li>
            <li>
              <h3 class="contents__title"><a href="activitats.html">Agenda: cursos, xerrades i trobades</a></h3>
              <p class="contents__meta">Activitat oberta al barri</p>
            </li>
            <li>
              <h3 class="contents__title"><a href="botiga.html">Botiga efímera i pop-up</a></h3>
              <p class="contents__meta">Rodatges, gravacions, celebracions</p>
            </li>
            <li>
              <h3 class="contents__title"><a href="associacio.html">EspaiGràcia Associació</a></h3>
              <p class="contents__meta">Història, transparència, compromís</p>
            </li>
          </ol>
        </aside>
      </div>
    </div>
  </section>

  <!-- Destacat + imatges -->
  <section class="section section--paper" aria-labelledby="destacat-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="destacat-title">Destacat</h2>
        <span class="section-head__meta">El carrer, la llum, l’espai</span>
      </div>
      <div class="grid grid--editorial">
        <div class="col-7">
          <figure>
            <div class="photo photo--wide photo--frame">
              <img src="img/portada-interior.svg" alt="Interior de l’Espai Sira10 amb els arcs de l’edifici i taules de treball." width="1200" height="800">
              <span class="photo__credit">@siradeu</span>
            </div>
            <figcaption>La sala principal: llum de matí, arcs originals i taules que es comparteixen. Foto: @siradeu</figcaption>
          </figure>
        </div>
        <div class="col-5 stack">
          <article class="card card--green">
            <div class="card__body">
              <span class="kicker">Km 0</span>
              <h3 class="card__title">Comprem al barri, treballem al barri</h3>
              <p class="card__text">Els membres de l’espai tenen descomptes a comerços de Verdi, Sant Antoni i el centre de Gràcia. Comprem a pocs metres, sense índexs ni grams de transport.</p>
              <div class="card__foot"><span>Més de 40 comerços adherits</span></div>
            </div>
          </article>
          <figure>
            <div class="photo photo--tall photo--frame">
              <img src="img/portada-carrer.svg" alt="El carrer de Verdi a primera hora del matí, amb els comerços oberts." width="1200" height="800">
            </div>
            <figcaption>Verdi de matinada: el barri treballa i nosaltres hi som.</figcaption>
          </figure>
        </div>
      </div>
    </div>
  </section>

  <!-- Valors -->
  <section class="section" aria-labelledby="valors-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="valors-title">Què defensem</h2>
        <span class="section-head__meta">Valors de l’espai</span>
      </div>
      <div class="grid grid--4">
        <article class="card">
          <div class="card__body">
            <span class="tag tag--green">Proximitat</span>
            <h3 class="card__title">Treballar a cinc minuts de casa</h3>
            <p class="card__text">Reduceix el trànsit, estalvia temps i fa que l’economia de proximitat funcioni de debò. El barri és la nostra zona de servei.</p>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag tag--green">Solidaritat</span>
            <h3 class="card__title">Sense ànim de lucre</h3>
            <p class="card__text">L’EspaiGràcia Associació no es reparteix dividends: els excedents es reinverteixen en tarifes socials, en tallers i en espais cedits.</p>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag tag--green">Comunitat</span>
            <h3 class="card__title">Un lloc per trobar-se</h3>
            <p class="card__text">Assemblees, xerrades, trobades de comerçants i festes. L’espai es comparteix, no només es lloga.</p>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag tag--green">Transparència</span>
            <h3 class="card__title">Comptes oberts</h3>
            <p class="card__text">Publiquem les finances, les tarifes i els criteris de cessió d’espais. La comunitat hi pot mirar i opinar.</p>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- Cifres -->
  <section class="section section--green" aria-labelledby="cifres-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="cifres-title">L’espai en xifres</h2>
        <span class="section-head__meta">Dades de la comunitat</span>
      </div>
      <ul class="stats grid grid--4">
        <li><span class="stats__value">85</span><span class="stats__label">Verdi, número</span></li>
        <li><span class="stats__value">320 m²</span><span class="stats__label">De planta baixa</span></li>
        <li><span class="stats__value">48</span><span class="stats__label">Places de treball</span></li>
        <li><span class="stats__value">40+</span><span class="stats__label">Comerços Km 0</span></li>
      </ul>
    </div>
  </section>

  <!-- Seccions -->
  <section class="section" aria-labelledby="seccions-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="seccions-title">Totes les seccions</h2>
        <span class="section-head__meta">On trobar què</span>
      </div>
      <div class="grid grid--3">
        <article class="card">
          <div class="card__body">
            <h3 class="card__title"><a href="coworking.html">Coworking</a></h3>
            <p class="card__text">Taules compartides (Flex) i places fixes, amb fibra òptica, wifi, sala de reunions i cafè de barri.</p>
            <div class="card__foot"><span>Des de 12 € / dia</span><a href="coworking.html">Més info</a></div>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <h3 class="card__title"><a href="despatxos.html">Despatxos privats</a></h3>
            <p class="card__text">Sales amb clàssula, finestres al carrer i accés 24 h per a equips i projectes que volen la seva seu al barri.</p>
            <div class="card__foot"><span>Des de 420 € / mes</span><a href="despatxos.html">Més info</a></div>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <h3 class="card__title"><a href="tallers.html">Tallers</a></h3>
            <p class="card__text">Si imparteixes un workshop o un curs, tenim sala, material i public al barri. Presenta la teva proposta.</p>
            <div class="card__foot"><span>Propostes obertes</span><a href="tallers.html">Més info</a></div>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <h3 class="card__title"><a href="activitats.html">Activitats</a></h3>
            <p class="card__text">Agenda setmanal amb xerrades, formacions, tallers i trobades veïnals. Entrada lliure o a preu de barri.</p>
            <div class="card__foot"><span>Agenda oberta</span><a href="activitats.html">Més info</a></div>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <h3 class="card__title"><a href="botiga.html">Botiga efímera</a></h3>
            <p class="card__text">A peu de carrer per a pop-up stores, shootings, gravacions i celebracions. Deu dies o el que necessitis.</p>
            <div class="card__foot"><span>Consulta preus</span><a href="botiga.html">Més info</a></div>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <h3 class="card__title"><a href="associacio.html">L’A associació</a></h3>
            <p class="card__text">Història, govern, comptes i compromís amb el barri. Una entitat veïnal sense ànim de lucre al servei de Gràcia.</p>
            <div class="card__foot"><span>Transparència oberta</span><a href="associacio.html">Més info</a></div>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- Ubicació -->
  <section class="section section--paper" aria-labelledby="ubicacio-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="ubicacio-title">On som</h2>
        <span class="section-head__meta">Vila de Gràcia</span>
      </div>
      <div class="location">
        <div>
          <address class="location__address">Carrer de Verdi, 85<br>08012 Vila de Gràcia<br>Barcelona</address>
          <ul class="location__list">
            <li><span>Metro</span> <span>L2 Lesseps · L5 Verdi (5 min)</span></li>
            <li><span>Bus</span> <span>39, 50, 51, H6, V21</span></li>
            <li><span>Bicing</span> <span>Estació 268 · Verdi – Ros de la Purificació</span></li>
            <li><span>Parking</span> <span>Parking Verdi (a 120 m)</span></li>
          </ul>
          <p><a class="btn btn--green" href="https://www.openstreetmap.org/search?query=Carrer%20de%20Verdi%2085%20Barcelona" rel="noopener noreferrer" target="_blank">Obre al mapa</a></p>
        </div>
        <figure>
          <div class="photo photo--wide photo--frame">
            <img src="img/mapa.svg" alt="Mapa esquemàtic del carrer de Verdi amb la ubicació d’Espai Sira10 al número 85." width="1200" height="800">
          </div>
          <figcaption>Verdi 85, a pocs passos de la plaça de la Virreina i del mercat de la Llibertat.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <!-- Crida -->
  <section class="cta-band" aria-labelledby="crida-title">
    <div class="wrap-narrow">
      <h2 id="crida-title">Vine al Verdi 85</h2>
      <p>Passa un dia, una setmana o un mes. Pregunta per les tarifes socials, porta el teu taller o proposa una xerrada. L’espai és del barri i el barri en fa res.</p>
      <p><a class="btn" href="mailto:hola@siradeu.com">Escriu-nos</a></p>
    </div>
  </section>

</main>
"""



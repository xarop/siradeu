# -*- coding: utf-8 -*-
"""Contingut de despatxos.html — espais privats per a equips."""

BODY = """
<main id="main">

  <section class="page-head">
    <div class="wrap">
      <nav class="breadcrumb" aria-label="Fil d’Ari">
        <ol>
          <li><a href="index.html">Portada</a></li>
          <li aria-current="page">Despatxos</li>
        </ol>
      </nav>
      <span class="kicker">Espai Sira10 · Secció 02</span>
      <h1>Despatxos privats: la vostra seu al barri</h1>
      <p class="page-head__lead">Sales tancades de 2 a 12 persones, amb finestres al carrer, clàssula de fusta i accés 24 h. Per a equips i projectes que busquen arrelar a la Vila de Gràcia sense renunciar a la proximitat.</p>
      <div class="page-head__meta">
        <span><strong>Superfícies</strong> 12 – 34 m²</span>
        <span><strong>Capacitat</strong> 2 – 12 persones</span>
        <span><strong>Contracte mínim</strong> 3 mesos</span>
        <span><strong>Accés</strong> 24 h amb clau</span>
      </div>
    </div>
  </section>

  <!-- Introducció -->
  <section class="section" aria-labelledby="intro-title">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <article>
          <span class="kicker">Per a qui</span>
          <h2 id="intro-title">Una porta tancada, un barri obert</h2>
          <p>Un despatx privat al Verdi 85 no és un coworking gran: és un espai de 20 m² amb la teva clàssula, la teva llum i el soroll de fons d’un barri viu. És el punt de trobada d’una col·lectiva, d’un petit equip tècnic, d’un taller professional o d’una empresa que vol ADDRESS al carrer on viuen els seus clients.</p>
          <p>Tots els despatxos comparteixen la cuina, la sala de reunions, la sala de trobades i l’entrada de la planta baixa. Això és intencionat: preferim un barri on es creuen els vincles abans que unes oficines aïllades on no es coneix ningú.</p>
          <blockquote>
            “Vam triar Verdi perquè aquí la gent surt a la porta i encara s’ha creuat amb tres veïns. Això no passa a la Meridiana.”
            <cite>Núria A., membre des de 2023</cite>
          </blockquote>
        </article>
        <aside aria-labelledby="resum-title">
          <div class="section-head">
            <h2 id="resum-title">En un cop d’ull</h2>
          </div>
          <ul class="checklist">
            <li>Accés 24 h amb clau o unintelligible</li>
            <li>Wifi i fibra inclosos, sense consum</li>
            <li>Mobiliari bàsic: taules, cadires, armaris</li>
            <li>Sala de reunions inclosa (10 h/mes)</li>
            <li>Correu electrònic professional</li>
            <li>Accésibilitat sense escales</li>
            <li>Contracte flexible des de 3 mesos</li>
          </ul>
        </aside>
      </div>
    </div>
  </section>

  <!-- Catàleg -->
  <section class="section section--paper" aria-labelledby="cataleg-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="cataleg-title">Els espais</h2>
        <span class="section-head__meta">Preus mensuals indicatius</span>
      </div>
      <div class="grid grid--3">
        <article class="card">
          <div class="card__body">
            <span class="tag tag--green">Petit</span>
            <h3 class="card__title">El Verdi</h3>
            <p class="card__text">14 m² amb finestres interiors i llum natural. Ideal per a autònoms, consultants o una col·lectiva de dues persones.</p>
            <ul class="checklist">
              <li>2 places de treball</li>
              <li>1 taula de reunions de 4</li>
              <li>Armari de paret</li>
            </ul>
            <div class="card__foot"><span class="card__price">420 € / mes</span><span>Des de 3 mesos</span></div>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag tag--green">Mitjà</span>
            <h3 class="card__title">La Virreina</h3>
            <p class="card__text">22 m² amb finestres al carrer i la volta original. Per a equips de 4 a 6 persones o una escola taller.</p>
            <ul class="checklist">
              <li>6 places de treball</li>
              <li>Taula de reunions de 8</li>
              <li>Armari i prestatge</li>
            </ul>
            <div class="card__foot"><span class="card__price">680 € / mes</span><span>Des de 3 mesos</span></div>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag tag--green">Gran</span>
            <h3 class="card__title">El 85</h3>
            <p class="card__text">34 m², la sala més ampla de la planta baixa, amb finestra de galeria i espai per a presentacions de fins a 15 persones.</p>
            <ul class="checklist">
              <li>12 places de treball</li>
              <li>Sala de reunions de 8 inclosa</li>
              <li>Zona de recepció</li>
            </ul>
            <div class="card__foot"><span class="card__price">1.050 € / mes</span><span>Des de 6 mesos</span></div>
          </div>
        </article>
      </div>
      <figure>
        <div class="photo photo--wide photo--frame">
          <img src="img/despatxos.svg" alt="Despatx privat amb finestres al carrer i mobiliari de fusta." width="1200" height="800">
          <span class="photo__credit">@siradeu</span>
        </div>
        <figcaption>El 85, la sala més gran de la planta baixa. Foto: @siradeu</figcaption>
      </figure>
    </div>
  </section>

  <!-- Serveis inclosos -->
  <section class="section" aria-labelledby="serveis-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="serveis-title">Què hi ha a la planta baixa</h2>
        <span class="section-head__meta">Compartit per tothom</span>
      </div>
      <div class="grid grid--editorial">
        <div class="col-6">
          <figure>
            <div class="photo photo--square photo--frame">
              <img src="img/despatxos-reunio.svg" alt="Sala de reunions de l’espai amb taula i finestres." width="1200" height="800">
            </div>
            <figcaption>La sala de reunions: deu hores al mes incloses en el lloguer.</figcaption>
          </figure>
        </div>
        <div class="col-6">
          <ul class="checklist">
            <li><strong>Sala de reunions</strong> per a 4 i 8 persones, amb pantalla i videotrucalla.</li>
            <li><strong>Sala de trobades</strong> per a assemblees i col·lectives (fins a 30 persones).</li>
            <li><strong>Cuina compartida</strong> amb cafè de barri i microones.</li>
            <li><strong>Cabina de trucades</strong> i espai de focus.</li>
            <li><strong>Material imprimible</strong> i gestió de residus.</li>
            <li><strong>Magatzem</strong> d’equips de materials per a talleristes.</li>
            <li><strong>Lavabos accessibles</strong> i Dutxa per a la sala de tallers.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Prohibicions -->
  <section class="section section--green" aria-labelledby="normes-title">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <div>
          <span class="kicker">Normes de convivència</span>
          <h2 id="normes-title">Un barri viu té regles</h2>
          <p>Perquè l’espai funcioni bé per a tothom, els despatxos comparteixen un petit reglament de barri: horari sorollós fins a les 21 h, cuina neta, sala de reunions reservada i cap activitat que molesti els veïns de Verdi 85 ni els del carrer.</p>
          <p>El reglament el va discutir l’assemblea de veïns i s’aplica igual per a tots els llogaters, sense tarifes ni tractes especials.</p>
        </div>
        <aside aria-labelledby="normes-list-title">
          <div class="section-head">
            <h2 id="normes-list-title">En quatre línies</h2>
          </div>
          <ul class="checklist">
            <li>Silenci absolut a partir de les 21 h</li>
            <li>Sala de reunions: 10 h/mes, reserves a l’aplicació</li>
            <li>No es permet fumar a l’interior de l’espai</li>
            <li>Els animals d’assistència són benvinguts</li>
          </ul>
        </aside>
      </div>
    </div>
  </section>

  <!-- Taula comparativa -->
  <section class="section" aria-labelledby="comparativa-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="comparativa-title">Comparativa</h2>
        <span class="section-head__meta">Despatx privat vs. plaça fixa</span>
      </div>
      <div class="table-wrap">
        <table class="table">
          <caption>Què obteniu en cada modalitat</caption>
          <thead>
            <tr>
              <th scope="col">Concepte</th>
              <th scope="col">Plaça fixa de coworking</th>
              <th scope="col">Despatx privat</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">Espai tancat</th>
              <td>No</td>
              <td>Sí, amb clàssula</td>
            </tr>
            <tr>
              <th scope="row">Accés 24 h</th>
              <td>Sí</td>
              <td>Sí</td>
            </tr>
            <tr>
              <th scope="row">Sala de reunions</th>
              <td>10 h / mes</td>
              <td>10 h / mes</td>
            </tr>
            <tr>
              <th scope="row">Adreça de correu electrònic</th>
              <td>Sí</td>
              <td>Sí</td>
            </tr>
            <tr>
              <th scope="row">Rebuda postal</th>
              <td>Sí</td>
              <td>Sí</td>
            </tr>
            <tr>
              <th scope="row">Preu</th>
              <td><span class="price">165 € / mes</span></td>
              <td><span class="price">Des de 420 € / mes</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="cta-band" aria-labelledby="cta-title">
    <div class="wrap-narrow">
      <h2 id="cta-title">Voleu la vostra sala?</h2>
      <p>Expliqueu-nos què feu i quanta gent sou. Us enviem les condicions i us fem lloc per veure l’espai en horari, amb cafè de barri.</p>
      <p><a class="btn" href="mailto:hola@siradeu.com?subject=Despatx%20privat">Escriu-nos</a></p>
    </div>
  </section>

</main>
"""


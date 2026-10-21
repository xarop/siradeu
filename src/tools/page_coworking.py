# -*- coding: utf-8 -*-
"""Contingut de coworking.html — espais de treball Flex i Fix."""

BODY = """
<main id="main">

  <section class="page-head">
    <div class="wrap">
      <nav class="breadcrumb" aria-label="Fil d’Ari">
        <ol>
          <li><a href="index.html">Portada</a></li>
          <li aria-current="page">Coworking</li>
        </ol>
      </nav>
      <span class="kicker">Espai Sira10 · Secció 01</span>
      <h1>Coworking: treballa al barri, sense contracte de llarg termini</h1>
      <p class="page-head__lead">Taules compartides per a dies solts i places fixes per a qui vol una taula seva. Llum natural, fibra òptica i tarifes pensades per a autònoms, col·lectius i petites equipe del barri.</p>
      <div class="page-head__meta">
        <span><strong>Horari</strong> 8:00 – 21:00 (dilluns a divendres)</span>
        <span><strong>Places</strong> 48</span>
        <span><strong>Wifi</strong> Fibra 1 Gbps</span>
        <span><strong>Tarifa social</strong> −30 % a sense ànim de lucre</span>
      </div>
    </div>
  </section>

  <!-- Flex vs Fix -->
  <section class="section" aria-labelledby="modalitats-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="modalitats-title">Dos maneres de treballar-hi</h2>
        <span class="section-head__meta">Flex · Fix</span>
      </div>
      <div class="grid grid--2">
        <article class="card">
          <div class="card__body">
            <span class="tag">Modalitat Flex</span>
            <h3 class="card__title">Taula compartida, dia a dia</h3>
            <p class="card__text">Una taula a la sala principal per a una jornada. Arribes, treballes entre veïns i te'n vas sense haver de contractar res a llarg termini.</p>
            <ul class="checklist">
              <li>Taula compartida d’estil compartit</li>
              <li>Wifi i fibra inclosos</li>
              <li>Cafè i aigua de la cuina del barri</li>
              <li>Accés a la sala de reunions (30 min)</li>
              <li>Armari per deixar material</li>
            </ul>
            <div class="card__foot">
              <span class="card__price">12 € / dia</span>
              <span>10 % de descompte per packs de 10 dies</span>
            </div>
          </div>
        </article>

        <article class="card card--green">
          <div class="card__body">
            <span class="tag tag--solid">Modalitat Fix</span>
            <h3 class="card__title">La teva taula, sempre hi</h3>
            <p class="card__text">Una plaça fixa amb armari propi, correu, adreça de correu electrònic i prioritat a les sales de reunions. Per a autònoms i equips petits que volen arrelar al barri.</p>
            <ul class="checklist">
              <li>Taula i armari personalitzats</li>
              <li>Correu electrònic professional (verdi85.cat)</li>
              <li>Accés 24 h amb clau</li>
              <li>10 h de sala de reunions al mes</li>
              <li>Esdeveniments i tallers de la comunitat</li>
            </ul>
            <div class="card__foot">
              <span class="card__price">165 € / mes</span>
              <span>Plaça reduïda a 130 € amb compromís social</span>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- Serveis -->
  <section class="section section--paper" aria-labelledby="serveis-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="serveis-title">Què hi trobaràs</h2>
        <span class="section-head__meta">Serveis inclosos</span>
      </div>
      <div class="grid grid--editorial">
        <div class="col-6">
          <figure>
            <div class="photo photo--wide photo--frame">
              <img src="img/coworking-llum.svg" alt="Sala de coworking amb taules i llum natural entrant per les finestres del carrer." width="1200" height="800">
              <span class="photo__credit">@siradeu</span>
            </div>
            <figcaption>La sala de matí: finestres a Verdi i llum de nord. Foto: @siradeu</figcaption>
          </figure>
        </div>
        <div class="col-6 stack">
          <ul class="checklist">
            <li><strong>Fibra òptica de 1 Gbps</strong> amb Wi-Fi mesh per a tot l’espai i xarxa cablejada a les taules.</li>
            <li><strong>Llum natural</strong> a les sales de cara al carrer, amb persians que protegeixen del sol de migdia.</li>
            <li><strong>Sala de reunions</strong> per a 4 i 8 persones, equipada amb pantalla, pissarra i targeta de projecció.</li>
            <li><strong>Cabina de trucades</strong> dues, insonoritzades, gratuïtes.</li>
            <li><strong>Cruita i cafè</strong> de comerços del barri, amb descompte del 10 % per als membres.</li>
            <li><strong>Armaris, material d’oficina</strong> i espai de material imprimible.</li>
            <li><strong>Accessibilitat</strong> sense escales, WC adaptat i entrada a ras de carrer.</li>
          </ul>
          <p><a class="btn btn--ghost" href="despatxos.html">Necessito un espai tancat →</a></p>
        </div>
      </div>
    </div>
  </section>

  <!-- Tarifes -->
  <section class="section" aria-labelledby="tarifes-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="tarifes-title">Tarifes</h2>
        <span class="section-head__meta">Sense IVA · cancel·lació flexible</span>
      </div>
      <div class="table-wrap">
        <table class="table">
          <caption>Plaçaments, preus i condicions d’un simple full</caption>
          <thead>
            <tr>
              <th scope="col">Modalitat</th>
              <th scope="col">Inclou</th>
              <th scope="col">Durada mínima</th>
              <th scope="col" class="num">Preu</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">Flex · dia</th>
              <td>Taula, wifi, cafè, armari temporal</td>
              <td>1 dia</td>
              <td class="num"><span class="price">12 €</span></td>
            </tr>
            <tr>
              <th scope="row">Flex · setmana</th>
              <td>Taula, wifi, cafè, 1 sala de reunions</td>
              <td>1 setmana</td>
              <td class="num"><span class="price">50 €</span></td>
            </tr>
            <tr>
              <th scope="row">Flex · pack 10 dies</th>
              <td>Taula, wifi, cafè, armari temporal</td>
              <td>10 dies</td>
              <td class="num"><span class="price">110 €</span></td>
            </tr>
            <tr>
              <th scope="row">Fix · plaça reduïda</th>
              <td>Taula fixa, armari, correu, 5 h de sala</td>
              <td>1 mes</td>
              <td class="num"><span class="price">130 €</span></td>
            </tr>
            <tr>
              <th scope="row">Fix · plaça estàndard</th>
              <td>Taula fixa, armari, correu, 10 h de sala, accés 24 h</td>
              <td>1 mes</td>
              <td class="num"><span class="price">165 €</span></td>
            </tr>
            <tr>
              <th scope="row">Targeta social</th>
              <td>Comanda de la modalitat escollida</td>
              <td>1 mes</td>
              <td class="num"><span class="price">−30 %</span></td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="small muted">Preu indicatiu per a la versió de proves. Les condicions finals s’acorden amb l’equip de l’espai segons l’activitat i els compromisos socials.</p>
    </div>
  </section>

  <!-- Tarifa social -->
  <section class="section section--green" aria-labelledby="social-title">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <div>
          <span class="kicker">Tarifa social</span>
          <h2 id="social-title">Treballar no hauria de ser un luxe</h2>
          <p>Si formes part d’una entitat sense ànim de lucre, d’una col·lectiva veïnal, d’un col·lectiu cultural o d’un projecte sense beneficis, et donem un descompte del 30 % i sempre tenim taules gratuïtes reservades per a initiatives del barri.</p>
          <p>Demana la <strong>tarifa social</strong> escrivint-nos una línia explica qui ets i què fas. Som una entitat veïnal: confiem en la bona fe del barri.</p>
          <p><a class="btn btn--clay" href="mailto:hola@siradeu.com?subject=Tarifa%20social">Sol·licita la tarifa social</a></p>
        </div>
        <aside aria-labelledby="social-cond">
          <div class="section-head">
            <h2 id="social-cond">Condicions</h2>
          </div>
          <ul class="checklist">
            <li>Entitats, col·lectives i cooperatives sense ànim de lucre</li>
            <li>Projectes de barri, culturals o comunitaris</li>
            <li>Estudiants i personnes en cerca de feina amb justificació</li>
            <li>Valoració trimestral: l’espace s’adapta a qui hi ve</li>
          </ul>
        </aside>
      </div>
    </div>
  </section>

  <!-- Ubicació i CTA -->
  <section class="section" aria-labelledby="on-som-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="on-som-title">On som</h2>
        <span class="section-head__meta">Verdi 85 · Vila de Gràcia</span>
      </div>
      <div class="location">
        <figure>
          <div class="photo photo--wide photo--frame">
            <img src="img/coworking-taula.svg" alt="Taules de treball compartides a la sala de coworking d’Espai Sira10." width="1200" height="800">
            <span class="photo__credit">@siradeu</span>
          </div>
          <figcaption>Les taules compartides: sempre hi ha algú al costat, i sempre hi ha un qui fa de veí.</figcaption>
        </figure>
        <div>
          <address class="location__address">Carrer de Verdi, 85<br>08012 Vila de Gràcia, Barcelona</address>
          <p>Metro L5 Verdi a 4 minuts a peu, L2 Lesseps a 6 minuts, i 25 places de bicing davant del local. Al barri, però sense quedar-hi tancat: el carrer és a la porta.</p>
          <p><a class="btn btn--green" href="mailto:hola@siradeu.com?subject=Reserva%20coworking">Reserva una taula</a></p>
          <p><a class="btn btn--ghost" href="despatxos.html">Vol un despatx tancat</a></p>
        </div>
      </div>
    </div>
  </section>

</main>
"""


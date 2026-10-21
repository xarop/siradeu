# -*- coding: utf-8 -*-
"""Contingut de botiga.html — pop-up, botiga efímera, shootings i celebracions."""

BODY = """
<main id="main">

  <section class="page-head">
    <div class="wrap">
      <nav class="breadcrumb" aria-label="Fil d’Ari">
        <ol>
          <li><a href="index.html">Portada</a></li>
          <li aria-current="page">Botiga</li>
        </ol>
      </nav>
      <span class="kicker">Espai Sira10 · Secció 05</span>
      <h1>Botiga efímera: la teva marca, a peu de carrer</h1>
      <p class="page-head__lead">Vint-i-cinc metres quadrats amb entrada oberta al carrer de Verdi, al costat de la plaça de la Virreina. Per a pop-up stores, llançaments, shootings, gravacions i celebracions.</p>
      <div class="page-head__meta">
        <span><strong>Superfície</strong> 25 m² amb façana</span>
        <span><strong>Capacitat</strong> Fins a 30 persones</span>
        <span><strong>Durada mínima</strong> 3 dies</span>
        <span><strong>Ubicació</strong> Verdi 85, planta baixa</span>
      </div>
    </div>
  </section>

  <!-- Intro -->
  <section class="section" aria-labelledby="intro-title">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <article>
          <span class="kicker">Per a què serveix</span>
          <h2 id="intro-title">Una botiga que només hi és durant un temps</h2>
          <p>Una botiga efímera és una oportunitat: obrir al carrer sense signar un lloguer de cinc anys, provar un producte amb gent real i veure què funciona abans d’invertir-hi. A Verdi 85 entrem al món real de la proximitat: hi passen veïns, famílies, turistes i gent que treballa al barri.</p>
          <p>L’espai està a planta baixa, amb façana al carrer i accès sense escales. Això permet obrir al carrer, muntar un mostrador, fer fotografies amb llum natural i tancar la caixa cada dia.</p>
          <ul class="checklist">
            <li>Façana de 6 metres amb possibilitat de rètol provisional</li>
            <li>Llum natural directe i instal·lació elèctrica reforçada</li>
            <li>Accés a lavabos i a la sala gran per a esdeveniments</li>
            <li>Wifi, caixa i sistema de targetes</li>
            <li>Armaris i prestatges per exposar</li>
            <li>Cartelleria i difusió al barri inclosos en els packs llargs</li>
          </ul>
        </article>
        <aside aria-labelledby="tipus-title">
          <div class="section-head">
            <h2 id="tipus-title">Formats habituals</h2>
          </div>
          <ul class="checklist">
            <li>Pop-up store de marca emergent</li>
            <li>Botiga efímera de temporització limitada</li>
            <li>Shooting o sessió de fotos</li>
            <li>Gravació d’un pòdcast, un documental o un videoclip</li>
            <li>Celebració: llançaments, comiats, exposicions</li>
            <li>Presentació de llibre o exposició fotogràfica</li>
            <li>Trobada de comunitat o assemblea</li>
          </ul>
          <p class="small">També fem espais per a <a href="activitats.html">activitats de l’agenda</a> i <a href="tallers.html">tallers de talleristes</a>.</p>
        </aside>
      </div>
    </div>
  </section>

  <!-- Imatges -->
  <section class="section section--paper" aria-labelledby="espai-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="espai-title">L’espai</h2>
        <span class="section-head__meta">25 m² amb façana</span>
      </div>
      <div class="grid grid--editorial">
        <div class="col-7">
          <figure>
            <div class="photo photo--wide photo--frame">
              <img src="img/botiga.svg" alt="Botiga efímera amb mostrador i productes exposats al local de Verdi 85." width="1200" height="800">
              <span class="photo__credit">@siradeu</span>
            </div>
            <figcaption>Un pop-up de roba i objectes de Km 0. Foto: @siradeu</figcaption>
          </figure>
        </div>
        <div class="col-5">
          <figure>
            <div class="photo photo--square photo--frame">
              <img src="img/botiga-shooting.svg" alt="Rodatge d’una sessió de fotos dins de la botiga efímera." width="1200" height="800">
            </div>
            <figcaption>Rodatges i sessions de fotos amb llum de matí.</figcaption>
          </figure>
        </div>
      </div>
    </div>
  </section>

  <!-- Preus -->
  <section class="section" aria-labelledby="preus-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="preus-title">Preus i durada</h2>
        <span class="section-head__meta">Sense IVA · material a part</span>
      </div>
      <div class="table-wrap">
        <table class="table">
          <caption>Modalitats d’ocupació de la botiga efímera</caption>
          <thead>
            <tr>
              <th scope="col">Modalitat</th>
              <th scope="col">Durada</th>
              <th scope="col">Inclou</th>
              <th scope="col" class="num">Preu</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">Esdeveniment puntual</th>
              <td>1 dia</td>
              <td>Espai, wifi, caixa, publicitat al barri</td>
              <td class="num"><span class="price">180 €</span></td>
            </tr>
            <tr>
              <th scope="row">Micro pop-up</th>
              <td>3 – 6 dies</td>
              <td>Espai, wifi, caixa, publicitat al barri</td>
              <td class="num"><span class="price">90 € / dia</span></td>
            </tr>
            <tr>
              <th scope="row">Pop-up estacional</th>
              <td>2 – 4 setmanes</td>
              <td>Tot el anterior + cartelleria a Verdi i difusió al barri</td>
              <td class="num"><span class="price">70 € / dia</span></td>
            </tr>
            <tr>
              <th scope="row">Rodatge o gravació</th>
              <td>1 – 2 dies</td>
              <td>Espai, energia, material auxiliar</td>
              <td class="num"><span class="price">220 € / dia</span></td>
            </tr>
            <tr>
              <th scope="row">Celebració o llançament</th>
              <td>1 – 3 dies</td>
              <td>Espai, sala gran, neteja i material bàsic</td>
              <td class="num"><span class="price">A consultar</span></td>
            </tr>
            <tr>
              <th scope="row">Projecte veïnal</th>
              <td>Variable</td>
              <td>Espai cedit per a iniciatives del barri sense ànim de lucre</td>
              <td class="num"><span class="price">0 €</span></td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="small muted">Els preus són indicatius per a la versió de proves. Les condicions finals depenen de la durada, l’activitat i si l’esdeveniment és obert al barri.</p>
    </div>
  </section>

  <!-- Condicions -->
  <section class="section section--green" aria-labelledby="cond-title">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <div>
          <span class="kicker">Condicions</span>
          <h2 id="cond-title">Què demanem a canvi</h2>
          <p>La botiga és a la planta baixa d’un edifici amb veïns al costat. Això ens fa ser cuants amb el soroll, l’accés i l’orden, i ens fa posar una condició clara: <strong>l’activitat ha de ser real i oberta al barri</strong>.</p>
          <p>No volem un local buit amb el rètol apagat. Volem que s’hi faci gent, que els veïns hi passin i que l’activitat deixi alguna cosa al barri.</p>
        </div>
        <aside aria-labelledby="req-title">
          <div class="section-head">
            <h2 id="req-title">Requisits</h2>
          </div>
          <ul class="checklist">
            <li>Horari comercial coherent amb el barri (de 9:00 a 21:00)</li>
            <li>Volum de música auditable per als veïns</li>
            <li>Neteja de l’espai en deixar-lo</li>
            <li>Assegurança de responsabilitat civil si hi ha public</li>
            <li>Rètol provisional autoritzat per la comunitat</li>
            <li>Cap producte no autoritzat ni venda sense llicència corresponent</li>
          </ul>
        </aside>
      </div>
    </div>
  </section>

  <!-- Com contractar -->
  <section class="section" aria-labelledby="pas-title">
    <div class="wrap-narrow">
      <div class="section-head">
        <h2 id="pas-title">Com es contracta</h2>
        <span class="section-head__meta">Tres passos</span>
      </div>
      <ol class="contents">
        <li>
          <h3 class="contents__title">Escriu-nos el concepte</h3>
          <p class="contents__meta">Què vols fer, quan i quanta gent hi haurà a l’espai.</p>
        </li>
        <li>
          <h3 class="contents__title">Reps una proposta tancada</h3>
          <p class="contents__meta">Preu, durada, condicions i material disponible.</p>
        </li>
        <li>
          <h3 class="contents__title">Firmes i obres</h3>
          <p class="contents__meta">Pagament del 50 % per reservar dates i el dia abans tens la clau.</p>
        </li>
      </ol>
      <p><a class="btn btn--green" href="mailto:hola@siradeu.com?subject=Botiga%20efimera">Reserva la botiga</a></p>
    </div>
  </section>

</main>
"""


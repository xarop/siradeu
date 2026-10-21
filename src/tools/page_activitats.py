# -*- coding: utf-8 -*-
"""Contingut de activitats.html — agenda, xerrades, formacions i trobades."""

BODY = """
<main id="main">

  <section class="page-head">
    <div class="wrap">
      <nav class="breadcrumb" aria-label="Fil d’Ari">
        <ol>
          <li><a href="index.html">Portada</a></li>
          <li aria-current="page">Activitats</li>
        </ol>
      </nav>
      <span class="kicker">Espai Sira10 · Secció 04</span>
      <h1>Agenda del barri</h1>
      <p class="page-head__lead">Xerrades, cursos, tallers i trobades veïnals. L’agenda d’Espai Sira10 és oberta: hi podem encabir el que el barri vulgui aprendre o celebrar.</p>
      <div class="page-head__meta">
        <span><strong>Programació</strong> Setmanal</span>
        <span><strong>Entrada</strong> Lliure o preu de barri</span>
        <span><strong>Seu</strong> Carrer de Verdi, 85</span>
        <span><strong>Propostes</strong> <a href="tallers.html">Obertes</a></span>
      </div>
    </div>
  </section>

  <!-- Agenda -->
  <section class="section" aria-labelledby="agenda-title">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <div>
          <div class="section-head">
            <h2 id="agenda-title">Properament</h2>
            <span class="section-head__meta">Programació d’hivern</span>
          </div>

          <ol class="agenda">
            <li class="agenda__item">
              <div class="agenda__date"><span class="agenda__day">07</span><span class="agenda__month">Feb</span></div>
              <div>
                <h3 class="agenda__title">Xerrada: “El barri que volem”, què hi ha després de la plaça</h3>
                <p class="agenda__meta">Dijous · 19:00 – 20:30 · Sala Veri · Entrada lliure</p>
                <p class="agenda__excerpt">Una conversa oberta entre veïns, comerçants i l’Ajuntament de Barri sobre el futur de la Vila de Gràcia. Moderada per l’equip de l’espai.</p>
              </div>
              <div class="agenda__cta"><a class="btn btn--ghost btn--sm" href="mailto:hola@siradeu.com?subject=Xerrada%20El%20barri%20que%20volem">Reserva</a></div>
            </li>

            <li class="agenda__item">
              <div class="agenda__date"><span class="agenda__day">12</span><span class="agenda__month">Feb</span></div>
              <div>
                <h3 class="agenda__title">Taller: estampació de teixits amb tints naturals</h3>
                <p class="agenda__meta">Dissabte · 10:30 – 13:30 · 10 places · 35 €</p>
                <p class="agenda__excerpt">Treball de tints vegetals sobre llana i lli, de la preparació del teixit a la fixació del color. Impartit per una tallerista del barri.</p>
              </div>
              <div class="agenda__cta"><a class="btn btn--ghost btn--sm" href="mailto:hola@siradeu.com?subject=Taller%20estampacio">Reserva</a></div>
            </li>

            <li class="agenda__item">
              <div class="agenda__date"><span class="agenda__day">19</span><span class="agenda__month">Feb</span></div>
              <div>
                <h3 class="agenda__title">Formació: finances per a autònoms i col·lectives</h3>
                <p class="agenda__meta">Dimecres · 18:00 – 20:00 · Sala Veri · 45 € · Tarifa social: 20 €</p>
                <p class="agenda__excerpt">Compondre pressupostos, fiscalitat i facturació sense complicar-se. Sessió pràctica amb casos reals del barri i material editable.</p>
              </div>
              <div class="agenda__cta"><a class="btn btn--ghost btn--sm" href="mailto:hola@siradeu.com?subject=Formacio%20finances">Reserva</a></div>
            </li>

            <li class="agenda__item">
              <div class="agenda__date"><span class="agenda__day">26</span><span class="agenda__month">Feb</span></div>
              <div>
                <h3 class="agenda__title">Trobada veïnal: assemblea oberta de l’Espai Sira10</h3>
                <p class="agenda__meta">Dijous · 19:00 – 21:00 · Sala gran · Entrada lliure</p>
                <p class="agenda__excerpt">Presentació de comptes de l’exercici, tarifes de l’any vinent i espais per a les propostes veïnals. Obert a tothom del barri.</p>
              </div>
              <div class="agenda__cta"><a class="btn btn--ghost btn--sm" href="mailto:hola@siradeu.com?subject=Assemblea%20oberta">Vine-hi</a></div>
            </li>

            <li class="agenda__item">
              <div class="agenda__date"><span class="agenda__day">05</span><span class="agenda__month">Mar</span></div>
              <div>
                <h3 class="agenda__title">Festa de Nadal del barri: mercat de Nadal i música</h3>
                <p class="agenda__meta">Dijous · 18:00 – 22:00 · A la botiga i la sala gran · Entrada lliure</p>
                <p class="agenda__excerpt">Productes de Km 0, parades de veïns i una vetllada musical a la porta de Verdi 85. L’espai es queda obert tota la nit.</p>
              </div>
              <div class="agenda__cta"><a class="btn btn--ghost btn--sm" href="mailto:hola@siradeu.com?subject=Festa%20de%20Nadal">Més info</a></div>
            </li>

            <li class="agenda__item">
              <div class="agenda__date"><span class="agenda__day">14</span><span class="agenda__month">Mar</span></div>
              <div>
                <h3 class="agenda__title">Cicle: fotografia analògica i revelat a casa</h3>
                <p class="agenda__meta">Dissabte · 11:00 – 14:00 · 8 places · 45 €</p>
                <p class="agenda__excerpt">Tres sessions per aprendre a revelar i a muntar fotografies, amb material compartit. Cicle obert a persones que mai han fet una còpia.</p>
              </div>
              <div class="agenda__cta"><a class="btn btn--ghost btn--sm" href="mailto:hola@siradeu.com?subject=Cicle%20fotografia">Reserva</a></div>
            </li>
          </ol>
        </div>

        <aside aria-labelledby="filtres-title">
          <div class="section-head">
            <h2 id="filtres-title">Filtres</h2>
          </div>
          <ul class="checklist checklist--cross">
            <li>Totes les activitats</li>
            <li>Xerrades i converses</li>
            <li>Formacions professionals</li>
            <li>Tallers d’ofici</li>
            <li>Trobades veïnals</li>
            <li>Festes i celebracions</li>
          </ul>

          <div class="section-head">
            <h2>Com participar</h2>
          </div>
          <ul class="checklist">
            <li>Reserva amb un correu electrònic</li>
            <li>Pagament al girar, en efectiu o amb targeta</li>
            <li>Places limitades a 20 per respecte a l’espai</li>
            <li>Si no podeu venir, aviseu i alliberem la plaça</li>
          </ul>
          <p><a class="btn btn--green btn--block" href="tallers.html">Proposa un taller</a></p>
        </aside>
      </div>
    </div>
  </section>



  <!-- Tipus d'activitat -->
  <section class="section section--paper" aria-labelledby="tipus-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="tipus-title">Què hi fem</h2>
        <span class="section-head__meta">Cicles de l’espai</span>
      </div>
      <div class="grid grid--3">
        <article class="card">
          <div class="card__body">
            <span class="tag tag--green">Xerrades</span>
            <h3 class="card__title">Pensar en veu alta</h3>
            <p class="card__text">Converses sobre economia de proximitat, ciutat, cultura i drets al barri. Sempre amb moderació veïnal i entrada lliure.</p>
            <div class="card__foot"><span>Cada dijous</span><span>19:00</span></div>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag tag--green">Formacions</span>
            <h3 class="card__title">Aprendre un ofici</h3>
            <p class="card__text">Cicles curts de 3 o 4 sessions: finances, comunicació, gestió de col·lectives, logística de Km 0 o eines digitals per a autònoms.</p>
            <div class="card__foot"><span>3 – 4 sessions</span><span>Tarifa social</span></div>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag tag--green">Trobades</span>
            <h3 class="card__title">Fes-te comú</h3>
            <p class="card__text">Assemblees de l’espai, trobades de comerçants, festivals de barri i taules de treball on sortir de l’aïllament.</p>
            <div class="card__foot"><span>Mensual</span><span>Obert al barri</span></div>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- Imatges -->
  <section class="section" aria-labelledby="imatges-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="imatges-title">L’espai, de veritat</h2>
        <span class="section-head__meta">Galeria del barri</span>
      </div>
      <div class="grid grid--editorial">
        <div class="col-7">
          <figure>
            <div class="photo photo--wide photo--frame">
              <img src="img/activitats.svg" alt="Xerrada a la sala del barri amb el públic assegut." width="1200" height="800">
              <span class="photo__credit">@siradeu</span>
            </div>
            <figcaption>Les xerrades de dijous, a la sala Veri. Foto: @siradeu</figcaption>
          </figure>
        </div>
        <div class="col-5">
          <figure>
            <div class="photo photo--tall photo--frame">
              <img src="img/activitats-public.svg" alt="Trobada veïnal al carrer de Verdi amb gent reunida." width="1200" height="800">
            </div>
            <figcaption>Les trobades s’estenen al carrer: la plaça és tan nostra com la sala.</figcaption>
          </figure>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="cta-band" aria-labelledby="cta-title">
    <div class="wrap-narrow">
      <h2 id="cta-title">Hi ha lloc a la teva agenda</h2>
      <p>Si tens una idea per a l’agenda —una xerrada, un cicle, una celebració— digues-nos-ho. L’espai es crea amb la gent que hi participa.</p>
      <p><a class="btn" href="tallers.html">Proposa una activitat</a></p>
    </div>
  </section>

</main>
"""

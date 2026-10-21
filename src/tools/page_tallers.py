# -*- coding: utf-8 -*-
"""Contingut de tallers.html — espai per a talleristes + formulari de proposta."""

BODY = """
<main id="main">

  <section class="page-head">
    <div class="wrap">
      <nav class="breadcrumb" aria-label="Fil d’Ari">
        <ol>
          <li><a href="index.html">Portada</a></li>
          <li aria-current="page">Tallers</li>
        </ol>
      </nav>
      <span class="kicker">Espai Sira10 · Secció 03</span>
      <h1>Un espai per impartir el teu taller</h1>
      <p class="page-head__lead">Ets tallerista, artesà, formador o empresa que organitza formacions? Tenim sales, material, public al barri i un equip que t’ajuda a dissenyar la sessió. Presenta la teva proposta: la valorem de debò.</p>
      <div class="page-head__meta">
        <span><strong>Capacitat</strong> 6 – 20 persones</span>
        <span><strong>Sales</strong> 2 (amb piano i taules)</span>
        <span><strong>Materials</strong> Bàsics i específics</span>
        <span><strong>Resposta</strong> En 7 dies</span>
      </div>
    </div>
  </section>

  <!-- Per a què serveix -->
  <section class="section" aria-labelledby="per-que-title">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <article>
          <span class="kicker">Per a talleristes</span>
          <h2 id="per-que-title">Feu el taller al Verdi i trobeu el vostreitat</h2>
          <p>Donem-vos la sala, el material, el projector, la publicitat al barri i el cafè. A canvi, ens interessa una cosa: que l’activitat sigui de qualitat, tingui un preu accessible i es faci aquí, al barri, on la gent pot arribar-hi caminant.</p>
          <p>Els tallers que funcionen són aquells que ofereixen alguna cosa que no es troba a cap altre lloc de Barcelona: un ofici concret, una tècnica que es transmet, una mirada local. Si la vostra proposta té un component Km 0, la tarifació social és una opció real.</p>
          <h3>Què us fem possible</h3>
          <ul class="checklist">
            <li>Sala per a 6 a 20 persones, amb taules movibles i aules</li>
            <li>Material bàsic: pissarra, projector, altaveus, taula departicipants</li>
            <li>Material específic a petita escala, si cal (guillotina, forn, banc de treball)</li>
            <li>Publicitat al barri: newsletter, cartells, xarxes i agenda del web</li>
            <li>Gestió d’inscripcions i cobraments si la necessiteu</li>
            <li>Cafè, te i aigua per a la pausa</li>
          </ul>
        </article>
        <aside aria-labelledby="tipus-title">
          <div class="section-head">
            <h2 id="tipus-title">Tipus de taller</h2>
            <span class="section-head__meta">Exemples</span>
          </div>
          <ul class="checklist">
            <li>Ceràmica, fusta, pintura i PAPER</li>
            <li>Cocina de barri i conserves</li>
            <li>Cicle i costura, reparació de roba</li>
            <li>Fotografia analògica i printing</li>
            <li>Impressió 3D, electrònica i prototipatge</li>
            <li>Història del barri i arxiu veïnal</li>
            <li>Formació professional: gestió, finances, comunicació</li>
            <li>Cursos de llengua per a veïns nouvinguts</li>
          </ul>
        </aside>
      </div>
    </div>
  </section>

  <!-- Imatges -->
  <section class="section section--paper" aria-labelledby="espai-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="espai-title">L’espai on treballarem</h2>
        <span class="section-head__meta">Sala Veri</span>
      </div>
      <div class="grid grid--editorial">
        <div class="col-7">
          <figure>
            <div class="photo photo--wide photo--frame">
              <img src="img/tallers.svg" alt="Sala de tallers amb taules, participants i material." width="1200" height="800">
              <span class="photo__credit">@siradeu</span>
            </div>
            <figcaption>Tallers de cap de setmana a la sala Veri. Foto: @siradeu</figcaption>
          </figure>
        </div>
        <div class="col-5 stack">
          <figure>
            <div class="photo photo--square photo--frame">
              <img src="img/tallers-eines.svg" alt="Eines de treball ordenades sobre una taula de taller." width="1200" height="800">
            </div>
            <figcaption>Eines i materials compartits al magatzem.</figcaption>
          </figure>
          <article class="card card--green">
            <div class="card__body">
              <span class="kicker">Tarifa solidària</span>
              <h3 class="card__title">El taller és del barri</h3>
              <p class="card__text">Si el teu taller és sense ànim de lucre, de formació veïnal o de reinserció, no pagues la sala: només el material consumible. Ho decidim l’assemblea de la comunitat.</p>
            </div>
          </article>
        </div>
      </div>
    </div>
  </section>

  <!-- Formulari de proposta -->
  <section class="section" aria-labelledby="form-title">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <div>
          <div class="section-head">
            <h2 id="form-title">Presenta la teva proposta</h2>
            <span class="section-head__meta">Resposta en 7 dies</span>
          </div>
          <p class="muted">Omple el formulari i l’equip de l’espai ho revisa en la comissió d’activitats. Si hi ha places, et contactem per tancar dates, preu i material.</p>

          <form class="form" id="proposta" data-validate novalidate>
            <div class="form__row">
              <div class="field">
                <label for="nom">Nom i cognoms <span aria-hidden="true">*</span></label>
                <input type="text" id="nom" name="nom" autocomplete="name" required>
              </div>
              <div class="field">
                <label for="contacte">Correu electrònic <span aria-hidden="true">*</span></label>
                <input type="email" id="contacte" name="contacte" autocomplete="email" required>
                <span class="hint">Només per respondre’t. No compartim dades.</span>
              </div>
            </div>

            <div class="form__row">
              <div class="field">
                <label for="telefon">Telèfon (opcional)</label>
                <input type="tel" id="telefon" name="telefon" autocomplete="tel">
              </div>
              <div class="field">
                <label for="tipus">Tipus d’activitat <span aria-hidden="true">*</span></label>
                <select id="tipus" name="tipus" required>
                  <option value="">Tria una opció…</option>
                  <option>Workshop d’ofici o tècnica</option>
                  <option>Curs o formació</option>
                  <option>Tallers de cap de setmana</option>
                  <option>Xerrada o conversa</option>
                  <option>Presentació de llibre o projecte</option>
                  <option>Altres activitats formatives</option>
                </select>
              </div>
            </div>

            <div class="form__row">
              <div class="field">
                <label for="titol">Títol del taller <span aria-hidden="true">*</span></label>
                <input type="text" id="titol" name="titol" required>
              </div>
              <div class="field">
                <label for="participants">Places aproximades <span aria-hidden="true">*</span></label>
                <input type="number" id="participants" name="participants" min="1" max="30" step="1" required>
                <span class="hint">Entre 6 i 20, segons la sala.</span>
              </div>
            </div>

            <div class="form__row">
              <div class="field">
                <label for="data">Data o període preferit <span aria-hidden="true">*</span></label>
                <input type="text" id="data" name="data" placeholder="p. ex. dissabte 14 de març al matí" required>
              </div>
              <div class="field">
                <label for="preu">Preu per participant</label>
                <input type="text" id="preu" name="preu" placeholder="p. ex. 25 €, gratuït o a preu de barri">
              </div>
            </div>

            <div class="field">
              <label for="descripcio">Descripció del taller <span aria-hidden="true">*</span></label>
              <textarea id="descripcio" name="descripcio" required placeholder="Què aprendran els participants? Què necessites de l’espai?"></textarea>
            </div>

            <div class="field">
              <label for="material">Material que necessites</label>
              <textarea id="material" name="material" placeholder="Eines, consumibles, equipament tècnic…"></textarea>
            </div>

            <div class="field checkbox-field">
              <input type="checkbox" id="comunitat" name="comunitat">
              <label for="comunitat">És una activitat sense ànim de lucre, de comunitat o de formació veïnal (tarifa solidària)</label>
            </div>

            <div class="field checkbox-field">
              <input type="checkbox" id="privacidad" name="privacidad" required>
              <label for="privacidad">He llegit i accepto que les dades es facin servir per respondre aquesta proposta <span aria-hidden="true">*</span></label>
            </div>

            <div>
              <button type="submit" class="btn btn--green">Enviar proposta</button>
              <p class="form__note">Versió de proves: el formulari no envia cap correu real.</p>
            </div>

            <p class="form__status" data-form-status role="status" hidden></p>
          </form>
        </div>

        <aside aria-labelledby="passos-title">
          <div class="section-head">
            <h2 id="passos-title">Com funciona</h2>
          </div>
          <ol class="contents">
            <li>
              <h3 class="contents__title">Envies la proposta</h3>
              <p class="contents__meta">Amb el formulari d’aquesta pàgina, en un minut.</p>
            </li>
            <li>
              <h3 class="contents__title">La comissió la valora</h3>
              <p class="contents__meta">Reunió setmanal de l’equip de l’espai.</p>
            </li>
            <li>
              <h3 class="contents__title">Tancem la data</h3>
              <p class="contents__meta">Sales, preu, material i publicació a l’agenda.</p>
            </li>
            <li>
              <h3 class="contents__title">Fem el taller</h3>
              <p class="contents__meta">Nosaltres ens ocupem de la logística, tu de l’ofici.</p>
            </li>
          </ol>
          <p class="small"><a href="activitats.html">Consulta l’agenda de tallers ja publicats →</a></p>
        </aside>
      </div>
    </div>
  </section>

  <!-- Tarifes -->
  <section class="section section--paper" aria-labelledby="tarifes-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="tarifes-title">Què costa la sala</h2>
        <span class="section-head__meta">Preus indicatius</span>
      </div>
      <div class="grid grid--3">
        <article class="card">
          <div class="card__body">
            <span class="tag">Sala Veri</span>
            <h3 class="card__title">Mitja jornada</h3>
            <p class="card__text">Fins a 4 hores, fins a 12 participants. Material bàsic i projector inclosos.</p>
            <div class="card__foot"><span class="card__price">90 €</span><span>+ consumibles</span></div>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag">Sala Veri</span>
            <h3 class="card__title">Jornada completa</h3>
            <p class="card__text">Fins a 8 hores, fins a 20 participants, amb pausa de cafè per a tothom.</p>
            <div class="card__foot"><span class="card__price">160 €</span><span>Material específic a part</span></div>
          </div>
        </article>
        <article class="card card--green">
          <div class="card__body">
            <span class="tag tag--solid">Comunitat</span>
            <h3 class="card__title">Tarifa solidària</h3>
            <p class="card__text">Per a entitats i col·lectives sense ànim de lucre: només pagues el material consumible que utilitzis.</p>
            <div class="card__foot"><span class="card__price">0 €</span><span>Decidit per l’assemblea</span></div>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section" aria-labelledby="faq-title">
    <div class="wrap-narrow">
      <div class="section-head">
        <h2 id="faq-title">Preguntes freqüents</h2>
      </div>
      <div class="faq">
        <details class="faq__item">
          <summary>Qui pot proposar un taller?</summary>
          <div class="faq__body">
            <p>Qualsevol persona, col·lectiva o empresa. No cal cap acreditar res: valorem que l’activitat sigui de qualitat, útil i accessible per al barri. Els tallers d’ofici en què calguin eines especials s’han de valorar una mica més per raons de seguretat i d’ocupació de l’espai.</p>
          </div>
        </details>
        <details class="faq__item">
          <summary>Què passa si no es venen totes les places?</summary>
          <div class="faq__body">
            <p>No passes res: la sala es factura igual. Per això recomanem una inscripció prudent i, si vols, podem ajudar-te a fixar un preu que faci que la gent s’apunti sense por.</p>
          </div>
        </details>
        <details class="faq__item">
          <summary>Podem repartir l’activitat en diverses sessions?</summary>
          <div class="faq__body">
            <p>Sí. Els cicles curts de quatre setmanes funcionen molt bé i deixen l’espai lliure per a altres activitats entre setmana.</p>
          </div>
        </details>
        <details class="faq__item">
          <summary>Emporteu els materials que feu servir?</summary>
          <div class="faq__body">
            <p>Sí, t’has d’emportar allò que portis. El material que ofereix l’espai (pissarra, projector, taules) es queda a l’espai i no es ven.</p>
          </div>
        </details>
        <details class="faq__item">
          <summary>Es pot contractar la sala per a un esdeveniment privat?</summary>
          <div class="faq__body">
            <p>Sí, sempre que no sigui una explotació comercial. Si el teu esdeveniment és obert al barri, et donem un preu millor. Consulta la secció <a href="botiga.html">botiga efímera</a> o escriu-nos.</p>
          </div>
        </details>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="cta-band" aria-labelledby="cta-title">
    <div class="wrap-narrow">
      <h2 id="cta-title">Teniu una idea al cap?</h2>
      <p>No cal que estigui acabada. Expliqueu-nos què sabeu fer i qui ho voldria aprendre. Nosaltres fem la resta.</p>
      <p><a class="btn" href="#form-title">Omple el formulari</a></p>
    </div>
  </section>

</main>
"""

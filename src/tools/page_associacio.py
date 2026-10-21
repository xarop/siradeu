# -*- coding: utf-8 -*-
"""Contingut de associacio.html — història, govern, transparència i equip."""

BODY = """
<main id="main">

  <section class="page-head">
    <div class="wrap">
      <nav class="breadcrumb" aria-label="Fil d’Ari">
        <ol>
          <li><a href="index.html">Portada</a></li>
          <li aria-current="page">Associació</li>
        </ol>
      </nav>
      <span class="kicker">Espai Sira10 · Secció 06</span>
      <h1>Qui som</h1>
      <p class="page-head__lead">L’Asociació Sira10 és una entitat veïnal sense ànim de lucre que gestiona l’espai comunitari de Verdi 85: sales, coworking, botiga efímera i agenda. Som una comunitat de persones, no una empresa.</p>
      <div class="page-head__meta">
        <span><strong>Forma jurídica</strong> Associació sense afany de lucre</span>
        <span><strong>Seu</strong> Verdi 85, Barcelona</span>
        <span><strong>Assemblea</strong> Oberta als socis</span>
        <span><strong>Contacte</strong> hola@siradeu.com</span>
      </div>
    </div>
  </section>

  <!-- Història -->
  <section class="section" aria-labelledby="historia-title">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <article>
          <span class="kicker">La nostra història</span>
          <h2 id="historia-title">De local buit a espai del barri</h2>
          <p>L’any 2018, l’immòbil de Verdi 85 portava dos anys tancat. Un dia de gener, un grup de veïns va sortir a l’hora de dinar i va entrar a mirar què passava amb el local. En van sortir tres mesos després amb un acord: comprar l’equip de l’antic comerç, deixar-lo a càrrec de l’Ajuntament i obrir-lo com a espai comunitari.</p>
          <p>El nom ve del carrer i del número: Sira, com el cant de l’avinguda, i 10, perquè hi havia deu places. El nom va quedar perquè tothom el trobava fàcil de dir i de recordar, i perquè ningú no sabia explicar exactament què volia dir. Avui és el que tothom diu.</p>
          <p>La primera activitat va ser una assemblea veïnal sobre el futur de la plaça de la Virreina. Hi van venir quaranta persones i vam haver d’esgotar les cadires. Des de llavors, l’espai ha funcionat amb la mateixa lògica: el barri proposa, l’espai acull, i la comunitat decideix.</p>
          <h3>On som avui</h3>
          <p>Avui l’espai aparta una sala per al coworking, una botiga efímera que acull projectes de Km 0, una agenda de tallers i xerrades, un punt de trobada per a col·lectives i una programació de formació per a autònoms i veïns. Tot plegat en un edifici i una comunitat que creix a poc a poc.</p>
        </article>
        <aside aria-labelledby="fets-title">
          <div class="section-head">
            <h2 id="fets-title">Fets i xifres</h2>
            <span class="section-head__meta">Des de 2018</span>
          </div>
          <dl class="stats">
            <div class="stats__row">
              <dt>Activitats organitzades</dt>
              <dd>420</dd>
            </div>
            <div class="stats__row">
              <dt>Persones que han passat</dt>
              <dd>18.500</dd>
            </div>
            <div class="stats__row">
              <dt>Espais cedits a col·lectives</dt>
              <dd>96</dd>
            </div>
            <div class="stats__row">
              <dt>Comerços de Km 0 al barri</dt>
              <dd>34</dd>
            </div>
            <div class="stats__row">
              <dt>Voluntaris de l’espai</dt>
              <dd>57</dd>
            </div>
          </dl>
        </aside>
      </div>
    </div>
  </section>

  <!-- Govern -->
  <section class="section section--paper" aria-labelledby="govern-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="govern-title">Com es governa</h2>
        <span class="section-head__meta">Estatuts i assemblea</span>
      </div>
      <div class="grid grid--3">
        <article class="card">
          <div class="card__body">
            <span class="tag tag--green">1</span>
            <h3 class="card__title">L’assemblea de socis</h3>
            <p class="card__text">L’òrgan de govern. Aprova comptes, tarifes, pressupostos i les grans decisions de l’espai. Es reuneix com a mínim dues vegades l’any i hi pot assistir tothom que en sigui membre.</p>
            <div class="card__foot"><span>Ordinària</span><span>2 cops l’any</span></div>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag tag--green">2</span>
            <h3 class="card__title">La junta de govern</h3>
            <p class="card__text">Executa els acords de l’assemblea i respon dia a dia de la gestió. Tota la informació de l’activitat es publica al web i a l’assemblea oberta.</p>
            <div class="card__foot"><span>Els socis</span><span>5 membres</span></div>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag tag--green">3</span>
            <h3 class="card__title">Les comissions</h3>
            <p class="card__text">Grups de treball oberts a qualsevol voluntari: agenda, espai, comunicació, botiga i economia de proximitat. Es coordinen des de la junta.</p>
            <div class="card__foot"><span>Voluntariat</span><span>Obertes</span></div>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- Transparència -->
  <section class="section" aria-labelledby="transp-title">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <div>
          <span class="kicker">Transparència</span>
          <h2 id="transp-title">Els diners, a la vista</h2>
          <p>Una associació veïnal que demana confiança l’ha de guanyar amb transparència. Publiquem els comptes anuals, els criteris de tarifa i els resultats de les activitats. Si algú pregunta, li responem.</p>
          <ul class="checklist">
            <li>Comptes anuals aprovats per l’assemblea i publicats al web</li>
            <li>Tarifes vigents i criteris per a la tarifa solidària</li>
            <li>Relació de les activitats i del seu resultat econòmic</li>
            <li>Actes de les assemblees, resumits i disponibles per a les sòcies</li>
            <li>Contractes de lloguer i de serveis, resumits</li>
            <li>Cap donatiu privat condiciona l’activitat de l’espai</li>
          </ul>
        </div>
        <aside aria-labelledby="fin-title">
          <div class="section-head">
            <h2 id="fin-title">Dades de l’exercici</h2>
            <span class="section-head__meta">Exercici de proves</span>
          </div>
          <div class="table-wrap">
            <table class="table">
              <caption>Ingressos i despeses de l’exercici</caption>
              <tbody>
                <tr>
                  <th scope="row">Lloguer i despeses fixes</th>
                  <td class="num">32 %</td>
                </tr>
                <tr>
                  <th scope="row">Activitats i tallers</th>
                  <td class="num">28 %</td>
                </tr>
                <tr>
                  <th scope="row">Botiga i espais cedits</th>
                  <td class="num">21 %</td>
                </tr>
                <tr>
                  <th scope="row">Subvencions i donacions</th>
                  <td class="num">14 %</td>
                </tr>
                <tr>
                  <th scope="row">Altres despeses</th>
                  <td class="num">5 %</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p class="small muted">Dades fictícies, únicament per a la maqueta del prototip.</p>
        </aside>
      </div>
    </div>
  </section>

  <!-- Equip -->
  <section class="section section--paper" aria-labelledby="equip-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="equip-title">L’equip que ho fa possible</h2>
        <span class="section-head__meta">Voluntariat</span>
      </div>
      <div class="grid grid--3">
        <article class="card">
          <div class="card__body">
            <span class="tag">Coordinació</span>
            <h3 class="card__title">Marta R.</h3>
            <p class="card__text">Coordina l’agenda, les sales i la relació amb el barri. Fa de pont entre l’assemblea i els tallers.</p>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag">Espai i botiga</span>
            <h3 class="card__title">Pau C.</h3>
            <p class="card__text">S’ocupa de la botiga efímera, els espais cedits i les col·laboracions amb comerços de Km 0.</p>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag">Coworking</span>
            <h3 class="card__title">Laia G.</h3>
            <p class="card__text">Atén les persones que treballen a l’espai, organitza els esdeveniments i els espais compartits.</p>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag">Comunicació</span>
            <h3 class="card__title">Nil B.</h3>
            <p class="card__text">Escriu la newsletter, manté les xarxes i difon l’agenda per tot el barri.</p>
          </div>
        </article>
        <article class="card">
          <div class="card__body">
            <span class="tag">Comissions</span>
            <h3 class="card__title">Comissions de treball</h3>
            <p class="card__text">Vuit persones més mantenen el projecte: agenda, espai, comunicació, botiga i economia de proximitat.</p>
          </div>
        </article>
        <article class="card card--green">
          <div class="card__body">
            <span class="tag tag--solid">Voluntariat</span>
            <h3 class="card__title">Hi faltes tu</h3>
            <p class="card__text">Si vols ajudar a fer que l’espai funcioni, vine a una comissió o proposa un taller. Totes les tasques són benvingudes.</p>
            <p class="card__foot"><a class="btn btn--ghost btn--sm" href="mailto:hola@siradeu.com?subject=Voluntariat">Contacta</a></p>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="cta-band" aria-labelledby="cta-title">
    <div class="wrap-narrow">
      <h2 id="cta-title">Vine a l’assemblea</h2>
      <p>La porta oberta. Si vols saber com funciona l’espai, col·laborar amb el barri o proposar una activitat, el primer pas és passar per Verdi 85.</p>
      <p><a class="btn" href="mailto:hola@siradeu.com?subject=Assemblea">Contacta l’associació</a></p>
    </div>
  </section>

</main>
"""


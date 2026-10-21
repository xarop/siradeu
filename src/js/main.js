/* =============================================================================
   SIRADEU.COM — main.js
   Lògica mínima i progressiva:
   1. Menú responsive (navegació mòbil)
   2. Botó "Imprimir Full de Premsa" (A4)
   3. Any dinàmic al peu
   4. Validació suau del formulari de propostes de taller
   5. Marca de secció activa segons l'URL
   ============================================================================= */
(function () {
  'use strict';

  var doc = document;
  var d = doc.documentElement;

  /* ---------------------------------------------------------------------
     1. Menú responsive
     --------------------------------------------------------------------- */
  function initMenu() {
    var toggle = doc.querySelector('[data-nav-toggle]');
    var menu = doc.querySelector('[data-nav-menu]');
    if (!toggle || !menu) return;

    function setState(open) {
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      menu.classList.toggle('is-open', open);
      var label = toggle.querySelector('[data-nav-label]');
      if (label) label.textContent = open ? 'Tanca' : 'Menú';
    }

    toggle.addEventListener('click', function () {
      setState(toggle.getAttribute('aria-expanded') !== 'true');
    });

    // Tanca en fer clic fora
    doc.addEventListener('click', function (e) {
      if (!menu.contains(e.target) && !toggle.contains(e.target)) setState(false);
    });

    // Tanca amb Escape
    doc.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setState(false);
        toggle.focus();
      }
    });

    // Tanca en passar a escriptori
    window.addEventListener('resize', function () {
      if (window.innerWidth > 900) setState(false);
    });
  }


  /* ---------------------------------------------------------------------
     2. Botó d'impressió — "Full de Premsa" A4
     --------------------------------------------------------------------- */
  function initPrint() {
    var details = doc.querySelectorAll('details');

    // En imprimir, totes les preguntes han d'aparèixer obertes: es
    // recorda l'estat inicial de cada <details> i es restaura després.
    function openAll() {
      Array.prototype.forEach.call(details, function (item) {
        if (item.getAttribute('data-was-open') === null) {
          item.setAttribute('data-was-open', item.hasAttribute('open') ? 'true' : 'false');
        }
        item.setAttribute('open', '');
      });
    }

    function restore() {
      Array.prototype.forEach.call(details, function (item) {
        var was = item.getAttribute('data-was-open');
        if (was === null) return;
        if (was === 'true') {
          item.setAttribute('open', '');
        } else {
          item.removeAttribute('open');
        }
        item.removeAttribute('data-was-open');
      });
    }

    // 'beforeprint'/'afterprint' cobreixen tant el botó com Cmd+P / Ctrl+P,
    // i el menú d'impressió del navegador.
    if (window.addEventListener) {
      window.addEventListener('beforeprint', openAll);
      window.addEventListener('afterprint', restore);
    }

    var buttons = doc.querySelectorAll('[data-print]');
    Array.prototype.forEach.call(buttons, function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        openAll();
        // Petita espera: el navegador aplica els estils @media print
        window.setTimeout(function () {
          window.print();
          // 'afterprint' ja restaura l'estat; el setTimeout és una xarxa
          // de seguretat per a navegadors que no l'emetin.
          window.setTimeout(restore, 400);
        }, 60);
      });
    });
  }

  /* ---------------------------------------------------------------------
     3. Any dinàmic al peu de pàgina
     --------------------------------------------------------------------- */
  function initYear() {
    var year = String(new Date().getFullYear());
    Array.prototype.forEach.call(doc.querySelectorAll('[data-year]'), function (el) {
      el.textContent = year;
    });
  }

  /* ---------------------------------------------------------------------
     4. Validació suau del formulari (client-side, sense backend)
     --------------------------------------------------------------------- */
  function initForms() {
    var forms = doc.querySelectorAll('[data-validate]');
    Array.prototype.forEach.call(forms, function (form) {
      var status = form.querySelector('[data-form-status]');

      form.addEventListener('submit', function (e) {
        var invalid = null;

        Array.prototype.forEach.call(form.querySelectorAll('[required]'), function (field) {
          var value = (field.value || '').trim();
          var empty = field.type === 'checkbox' ? !field.checked : value === '';
          var emailBad = field.type === 'email' && value !== '' &&
            !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value);

          if (empty || emailBad) {
            invalid = invalid || field;
            field.setAttribute('aria-invalid', 'true');
          } else {
            field.removeAttribute('aria-invalid');
          }
        });

        if (invalid) {
          e.preventDefault();
          if (status) {
            status.hidden = false;
            status.classList.add('form__status--error');
            status.textContent = invalid.type === 'email'
              ? 'Si us plau, revisa el correu electrònic.'
              : 'Si us plau, omple els camps obligatoris abans d\'enviar.';
          }
          invalid.focus();
          return;
        }

        // Sense backend en la versió de proves: es mostra un acus de rebut.
        e.preventDefault();
        if (status) {
          status.hidden = false;
          status.classList.remove('form__status--error');
          status.textContent = 'Gràcies! Hem rebut la teva proposta. Aquesta és una versió de proves: en producció s\'enviarà per correu.';
          form.reset();
        }
      });
    });
  }

  /* ---------------------------------------------------------------------
     5. Marca la secció activa a la navegació
     --------------------------------------------------------------------- */
  function initActiveNav() {
    var page = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
    if (!page) page = 'index.html';
    Array.prototype.forEach.call(doc.querySelectorAll('[data-nav-menu] a'), function (link) {
      var href = (link.getAttribute('href') || '').toLowerCase();
      var isActive = href === page || (href === 'index.html' && page === 'index.html');
      if (isActive) {
        link.setAttribute('aria-current', 'page');
      } else {
        link.removeAttribute('aria-current');
      }
    });
  }

  /* ---------------------------------------------------------------------
     Inicialització
     --------------------------------------------------------------------- */
  function init() {
    d.classList.add('js');
    initMenu();
    initPrint();
    initYear();
    initForms();
    initActiveNav();
  }

  if (doc.readyState === 'loading') {
    doc.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

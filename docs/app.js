'use strict';

// ── TEMA (CLARO / OSCURO) ─────────────────────────────────────────────────────
// Aplicamos el tema guardado ANTES de que el navegador pinte la página.
// Al envolverlo en una IIFE (función auto-invocada), evitamos contaminar
// el espacio de nombres global con variables temporales.
(function initTheme() {
  // localStorage.getItem devuelve null si no hay preferencia guardada → usamos 'dark'
  const saved = localStorage.getItem('theme') || 'dark';
  // data-theme en <html> permite que el CSS cambie los colores con selectores como
  // [data-theme="dark"] { --bg: #111; }  y  [data-theme="light"] { --bg: #fff; }
  document.documentElement.setAttribute('data-theme', saved);
})();

/**
 * Alterna el tema entre claro y oscuro y persiste la elección en localStorage.
 *
 * Por qué existe:
 *   El usuario puede preferir un tema claro o uno oscuro. Al guardar su elección
 *   en localStorage, la recordamos entre sesiones sin necesidad de un servidor.
 *
 * Cómo funciona:
 *   1. Lee el atributo data-theme actual del elemento <html>.
 *   2. Calcula el tema opuesto.
 *   3. Aplica el nuevo tema al <html> (el CSS reacciona automáticamente).
 *   4. Lo guarda en localStorage para la próxima visita.
 */
function toggleTheme() {
  const cur = document.documentElement.getAttribute('data-theme');
  const next = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
}
// El operador ?. (optional chaining) evita errores si el botón no existe en la página
document.getElementById('theme-toggle')?.addEventListener('click', toggleTheme);


// ── SIDEBAR DE NAVEGACIÓN ─────────────────────────────────────────────────────
/*
   Módulo completamente independiente que gestiona el panel lateral.

   Responsabilidades:
     1. Abrir / cerrar el panel (botón ☰, botón ✕, overlay, tecla Escape).
     2. Activar el ítem de sección clicado (resalte visual).
     3. Expandir/colapsar los subfiltros de la sección (acordeón).
     4. Comunicar la selección al motor de filtrado de la página de inicio.
     5. Sincronizar el estado de la sidebar con los pills y el nav del header
        cuando el usuario filtra desde esos controles externos.

   Comunicación con el motor de filtrado:
     - openSidebarFilter(cat, tag) es la función pública que recibe la
       sección activa ('Ia', 'Embebidos', 'Linux', 'Todas') y el tag
       de subfiltro adicional ('python', 'llms', etc. o '' para todos).
     - Llama a window.setSidebarFilter(cat, tag) que es proporcionada
       por initIndexPage() una vez que los datos están cargados.
*/
(function initSidebar() {
  const toggle   = document.getElementById('sidebar-toggle');
  const sidebar  = document.getElementById('sidebar');
  const overlay  = document.getElementById('sidebar-overlay');
  const closeBtn = document.getElementById('sidebar-close');

  // Si no existe el sidebar en esta página (ej: detail.html) salimos silenciosamente
  if (!sidebar) return;

  /* ── Abrir / cerrar ─────────────────────────────────────────── */

  function openSidebar() {
    sidebar.classList.add('open');
    overlay.classList.add('open');
    document.body.classList.add('sidebar-open');
    sidebar.setAttribute('aria-hidden', 'false');
  }

  function closeSidebar() {
    sidebar.classList.remove('open');
    overlay.classList.remove('open');
    document.body.classList.remove('sidebar-open');
    sidebar.setAttribute('aria-hidden', 'true');
  }

  toggle?.addEventListener('click', openSidebar);
  closeBtn?.addEventListener('click', closeSidebar);
  overlay.addEventListener('click', closeSidebar);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeSidebar(); });

  /* ── Activación de sección y subfiltros ─────────────────────── */

  const sidebarItems = sidebar.querySelectorAll('.sidebar-item[data-sidebar-cat]');
  const subfilterPanels = sidebar.querySelectorAll('.sidebar-subfilters');

  /**
   * Aplica el estado visual activo al ítem de la sidebar indicado
   * y muestra u oculta su panel de subfiltros (solo en móvil).
   *
   * @param {Element} item  - El botón .sidebar-item clicado
   * @param {boolean} expand - Si se deben mostrar los subfiltros
   */
  function activateSidebarItem(item, expand = true) {
    // Si estamos en layout desktop, los items son todos estáticos, no hacemos toggle
    const isDesktop = window.innerWidth > 1024;
    
    // Quitamos el estado activo de todos los ítems
    sidebarItems.forEach(i => {
      i.classList.remove('active');
      if (!isDesktop) i.classList.remove('expanded');
    });

    // Ocultamos todos los paneles de subfiltros (solo aplica en móvil)
    if (!isDesktop) {
        subfilterPanels.forEach(p => p.classList.remove('visible'));
    }

    // Marcamos el ítem actual como activo
    item.classList.add('active');

    // Si tiene subfiltros, los mostramos y rotamos el chevron (solo en móvil)
    if (!isDesktop) {
      const cat = item.dataset.sidebarCat;
      const subPanel = sidebar.querySelector(`.sidebar-subfilters[data-subfiltros-de="${cat}"]`);
      if (subPanel && expand) {
        item.classList.add('expanded');
        subPanel.classList.add('visible');
      }
    }
  }

  /**
   * Mapa de tags del sidebar → nombre del informe en docs/reports/.
   * Solo los tags listados aquí abren el visor; el resto filtra tarjetas.
   */
  const REPORT_TAGS = {
    'benchmarks': 'benchmarks',
    'agentes':    'agentes',
    'esp32':      'esp32'
  };

  const reportPanel   = document.getElementById('report-panel');
  const reportContent = document.getElementById('report-content');
  const reportBadge   = document.getElementById('report-badge');
  const reportBackBtn = document.getElementById('report-back-btn');
  const newsGridEl    = document.getElementById('news-grid');
  const loadMoreEl    = document.getElementById('load-more-wrap');

  /**
   * Convierte markdown sencillo a HTML para el visor de informes.
   * Cubre los elementos que genera el prompt de weekly_report.py.
   */
  function mdToHtml(md) {
    if (!md) return '';
    md = md.replace(/^<!--.*?-->\s*/s, ''); // eliminar cabecera de generación

    // 1. Tablas
    md = md.replace(/(?:^\|.+\|(?:\n|$))+/gm, match => {
      const lines = match.trim().split('\n');
      let tableHtml = '<div class="table-wrap"><table>\n';
      lines.forEach((line, index) => {
        if (/^\|[:\- |]+\|$/.test(line)) return; // Ignorar fila separadora
        const tag = index === 0 ? 'th' : 'td';
        const cells = line.trim().replace(/^\||\|$/g, '').split('|');
        tableHtml += '  <tr>' + cells.map(c => `<${tag}>${c.trim()}</${tag}>`).join('') + '</tr>\n';
      });
      tableHtml += '</table></div>\n';
      return tableHtml;
    });

    return md
      .replace(/^#### (.*)$/gm, '<h4>$1</h4>')
      .replace(/^### (.*)$/gm,  '<h3>$1</h3>')
      .replace(/^## (.*)$/gm,   '<h2>$1</h2>')
      .replace(/^# (.*)$/gm,    '<h1>$1</h1>')
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.+?)\*/g,     '<em>$1</em>')
      .replace(/`([^`]+)`/g,     '<code>$1</code>')
      .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
      .replace(/^[*-] (.+)$/gm, '<li>$1</li>')
      .replace(/((?:<li>[\s\S]*?<\/li>\n?)+)/g, '<ul>$1</ul>')
      .replace(/^---$/gm, '<hr>')
      .replace(/^(?!<(?:h[1-6]|ul|li|div|table|tr|td|th|p|hr|\/)).+$/gm, '<p>$&</p>')
      .replace(/<p>\s*<\/p>/g, '');
  }

  /**
   * Muestra informes markdown genéricos (agentes, esp32, python).
   */
  function _showMarkdownReport(reportName, label) {
    fetch(`reports/${reportName}.md?t=${Date.now()}`)
      .then(r => { if (!r.ok) throw new Error(r.status); return r.text(); })
      .then(md => { if (reportContent) reportContent.innerHTML = mdToHtml(md); })
      .catch(() => {
        if (reportContent) reportContent.innerHTML = `
          <div class="report-empty">
            <p>📫 El informe <strong>${label}</strong> aún no se ha generado.</p>
            <p>Se actualiza cada lunes o ejecuta:</p>
            <div class="code-block"><code>python scraper/weekly_report.py</code></div>
          </div>`;
      });
  }

  /* ── Visor de benchmarks con Chart.js ────────────────────── */

  /**
   * Carga benchmarks.json y renderiza:
   *   1. Fecha de actualización
   *   2. Gráfica de barras horizontales (Chart.js)
   *   3. Tabla de comparativa con iconos y badge NEW
   *   4. Texto del informe markdown
   */
  function showBenchmarkReport(label) {
    const speedIcon  = { alta: '⚡', media: '🔶', baja: '🐌' };
    const precioIcon = { bajo: '💰', medio: '💰💰', alto: '💰💰💰' };

    fetch(`reports/benchmarks.json?t=${Date.now()}`)
      .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(data => {
        const modelos = data.modelos || [];
        const semana  = data.semana  || '';
        const informe = data.informe || '';

        let html = semana
          ? `<p class="bench-updated">✨ Actualizado: ${semana}</p>` : '';

        /* Gráfica */
        if (modelos.length > 0) {
          html += `<div class="bench-chart-wrap">
            <canvas id="bench-chart"></canvas>
          </div>`;
        }

        /* Tabla */
        if (modelos.length > 0) {
          html += `<div class="bench-table-wrap"><table class="bench-table">
            <thead><tr>
              <th>Modelo</th><th>Puntuación</th>
              <th>Velocidad</th><th>Precio</th><th>Contexto</th>
            </tr></thead><tbody>`;

          modelos.forEach(m => {
            const score   = Number(m.puntuacion) || 0;
            const badge   = m.novedad   ? '<span class="bench-new">NEW</span>' : '';
            const star    = m.destacado ? '<span class="bench-star">★</span>' : '';
            const rowCls  = m.destacado ? ' class="bench-row-top"' : '';

            html += `<tr${rowCls}>
              <td>${star} ${m.nombre || '—'} ${badge}</td>
              <td><div class="bench-score-bar">
                <div class="bench-score-fill${m.destacado ? ' accent' : ''}"
                     style="width:${score}%"></div>
                <span>${score}</span>
              </div></td>
              <td>${speedIcon[m.velocidad]  || m.velocidad  || '—'}</td>
              <td>${precioIcon[m.precio]    || m.precio     || '—'}</td>
              <td><code>${m.contexto || '—'}</code></td>
            </tr>`;
          });

          html += `</tbody></table></div>`;
        }

        /* Markdown del informe */
        if (informe) html += `<div class="bench-analysis">${mdToHtml(informe)}</div>`;

        if (reportContent) reportContent.innerHTML = html;

        /* Render Chart.js */
        if (modelos.length > 0) {
          const doChart = () => {
            const canvas = document.getElementById('bench-chart');
            if (!canvas || !window.Chart) return;
            const accent = getComputedStyle(document.documentElement)
              .getPropertyValue('--accent').trim() || '#00e5ff';
            new window.Chart(canvas, {
              type: 'bar',
              data: {
                labels: modelos.map(m => m.nombre),
                datasets: [{ label: 'Puntuación',
                  data:            modelos.map(m => m.puntuacion),
                  backgroundColor: modelos.map(m => m.destacado ? accent : 'rgba(255,255,255,0.08)'),
                  borderColor:     modelos.map(m => m.destacado ? accent : 'rgba(255,255,255,0.15)'),
                  borderWidth: 1, borderRadius: 4 }],
              },
              options: {
                indexAxis: 'y', responsive: true, maintainAspectRatio: false,
                plugins: { legend: { display: false },
                  tooltip: { callbacks: { label: c => ` ${c.parsed.x}/100` } } },
                scales: {
                  x: { min: 0, max: 100,
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: 'rgba(255,255,255,0.45)', font: { size: 11 } } },
                  y: { grid: { display: false },
                    ticks: { color: 'rgba(255,255,255,0.8)',  font: { size: 12 } } },
                },
              },
            });
          };
          if (window.Chart) { doChart(); }
          else {
            let tries = 0;
            const poll = setInterval(() => {
              if (window.Chart) { clearInterval(poll); doChart(); }
              if (++tries > 30)   clearInterval(poll);
            }, 100);
          }
        }
      })
      .catch(() => _showMarkdownReport('benchmarks', label));
  }

  /**
   * Punto de entrada único para mostrar un informe.
   * Benchmarks usa el visor enriquecido; el resto usa markdown.
   */
  function showReport(reportName, label) {
    if (reportPanel) reportPanel.style.display = 'block';
    if (newsGridEl)  newsGridEl.style.display  = 'none';
    if (loadMoreEl)  loadMoreEl.style.display  = 'none';
    document.getElementById('empty-state').style.display = 'none';
    if (reportBadge)   reportBadge.textContent = label || reportName;
    if (reportContent) reportContent.innerHTML =
      '<div class="report-loading"><div class="spinner"></div><p>Cargando informe…</p></div>';
    if (reportName === 'benchmarks') showBenchmarkReport(label);
    else _showMarkdownReport(reportName, label);
  }

  /** Oculta el panel y vuelve al grid de tarjetas. */
  function hideReport() {
    if (reportPanel) reportPanel.style.display = 'none';
    if (newsGridEl)  newsGridEl.style.display  = '';
  }

  reportBackBtn?.addEventListener('click', hideReport);

  function applyFilter(cat, tag, label) {
    if (tag === 'python') {
      window.location.href = 'python.html';
      return;
    }
    if (tag === 'llms') {
      window.location.href = 'llms.html';
      return;
    }
    const reportName = tag ? REPORT_TAGS[tag] : null;
    if (reportName) {
      showReport(reportName, label || tag);
    } else {
      hideReport();
      if (typeof window.setSidebarFilter === 'function') {
        window.setSidebarFilter(cat, tag);
      }
    }
  }

  // Listener principal de cada ítem de sección
  sidebarItems.forEach(item => {
    item.addEventListener('click', () => {
      const cat = item.dataset.sidebarCat;
      activateSidebarItem(item, true);

      // Reseteamos el subfiltro activo de esta categoría a "Todas"
      const subPanel = sidebar.querySelector(`.sidebar-subfilters[data-subfiltros-de="${cat}"]`);
      if (subPanel) {
        subPanel.querySelectorAll('.subfilter').forEach(b => b.classList.remove('active'));
        subPanel.querySelector('.subfilter[data-tag=""]')?.classList.add('active');
      }

      // Aplicamos el filtro (sin restricción de tag)
      applyFilter(cat, '');

      // En móvil cerramos el sidebar al seleccionar una sección sin subfiltros
      // (Noticias). Las secciones con subfiltros permanecen abiertas para elegir.
      if (cat === 'Todas') {
        closeSidebar();
      }
    });
  });

  // Listeners de subfiltros
  subfilterPanels.forEach(panel => {
    panel.querySelectorAll('.subfilter').forEach(btn => {
      btn.addEventListener('click', e => {
        e.stopPropagation();
        const tag   = btn.dataset.tag;
        const cat   = panel.dataset.subfiltrosDe;
        const label = btn.textContent.trim(); // texto del botón para el badge

        panel.querySelectorAll('.subfilter').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        applyFilter(cat, tag, label);
        closeSidebar();
      });
    });
  });

  /* ── API pública para sincronización externa ─────────────────── */

  /**
   * Permite que el motor de filtrado (pills, nav) actualice el estado
   * visual del sidebar cuando el usuario filtra desde fuera del panel.
   *
   * @param {string} cat - Categoría activa
   */
  window.updateSidebarActive = function(cat) {
    const normCat = cat.charAt(0).toUpperCase() + cat.slice(1).toLowerCase();
    const item = sidebar.querySelector(`.sidebar-item[data-sidebar-cat="${normCat}"]`)
               || sidebar.querySelector('.sidebar-item[data-sidebar-cat="Todas"]');
    if (item) activateSidebarItem(item, normCat !== 'Todas');
  };

  // Exponer showReport globalmente para que loadNews().then() pueda usarlo
  window.showReportByTag = function(tag) {
    const reportName = { 'benchmarks': 'benchmarks', 'agentes': 'agentes', 'esp32': 'esp32' }[tag];
    if (reportName) {
      showReport(reportName, tag);
      // Marcar item activo en sidebar
      sidebar.querySelectorAll('.sidebar-item').forEach(a => a.classList.remove('active'));
      const match = sidebar.querySelector(`.sidebar-item[href*="tag=${tag}"]`);
      if (match) match.classList.add('active');
    }
  };
})();


// ── UTILIDADES COMPARTIDAS ────────────────────────────────────────────────────

/**
 * Mapeo de nombre de categoría → clase CSS correspondiente.
 * Centralizar este mapeo aquí evita duplicar strings en múltiples lugares.
 * La clase CSS controla el color del badge y la tarjeta en el frontend.
 */
let CAT_CLASS = {};

function initCategories(categories) {
  Object.entries(categories).forEach(([id, cat]) => {
    document.documentElement.style.setProperty(
      '--cat-' + id, cat.color
    );
    CAT_CLASS[id.toLowerCase()] = 'cat-' + id;
  });
}

/**
 * Devuelve la clase CSS de color para una categoría dada.
 *
 * @param {string} cat - Nombre de la categoría (ej: "linux", "ia")
 * @returns {string} Clase CSS (ej: "cat-linux") o "cat-default" si no reconoce la categoría
 */
function catClass(cat = '') {
  let c = cat.toLowerCase();
  if (!CAT_CLASS[c] && c === 'diseño-3d') c = 'diseno-3d'; // fallback por si acaso
  return CAT_CLASS[c] || 'cat-default';
}

/**
 * Formatea una fecha "YYYY-MM-DD" en formato largo en español.
 *
 * Por qué existe:
 *   El JSON almacena las fechas en formato ISO (YYYY-MM-DD) para facilitar
 *   la ordenación, pero el usuario debe verlas en formato legible ("8 de marzo de 2025").
 *
 * Cómo funciona:
 *   Construimos un Date con los tres componentes por separado (año, mes, día)
 *   para evitar el problema de las zonas horarias: new Date("2025-03-08") interpreta
 *   la cadena como UTC medianoche, lo que puede mostrar el día anterior en zonas UTC-X.
 *   Al pasar (y, m-1, d) usamos hora local y evitamos ese desfase.
 *
 * @param {string} str - Fecha en formato "YYYY-MM-DD"
 * @returns {string} Fecha formateada (ej: "8 de marzo de 2025") o "" si no hay fecha
 */
function formatDate(str) {
  if (!str) return '';
  const [y, m, d] = str.split('-').map(Number);
  return new Date(y, m - 1, d).toLocaleDateString('es-ES', {
    day: 'numeric', month: 'long', year: 'numeric'
  });
}

/**
 * Escapa un string para usarlo de forma segura como contenido HTML.
 *
 * Por qué existe:
 *   Si insertamos texto del usuario o de una API directamente en innerHTML
 *   sin escapar, cualquier carácter especial como <, >, & o " puede
 *   romper el HTML o crear vulnerabilidades XSS (inyección de scripts).
 *   Esta función convierte esos caracteres en sus entidades HTML seguras.
 *
 * Cómo funciona:
 *   Crea un elemento <div> temporal, asigna el texto como textContent
 *   (que escapa automáticamente) y devuelve el innerHTML resultante.
 *   Es el método más seguro y compatible para escapar HTML.
 *
 * @param {string} str - Texto posiblemente inseguro
 * @returns {string} Texto con caracteres HTML escapados
 */
function esc(str) {
  if (!str) return '';
  const d = document.createElement('div');
  d.textContent = str;
  return d.innerHTML;
}


// ── DETECCIÓN DE PÁGINA ───────────────────────────────────────────────────────
// El mismo archivo app.js sirve tanto para la página de inicio (lista de tarjetas)
// como para la página de detalle de un artículo. La clase CSS "detail-page" en el
// <body> distingue qué tipo de página estamos mostrando.
const isDetailPage = document.body.classList.contains('detail-page');
isDetailPage ? initDetailPage() : initIndexPage();


/* ══════════════════════════════════════════════════════════════════════════════
   PÁGINA DE INICIO (index.html)
   Muestra la cuadrícula de tarjetas con filtros, búsqueda y paginación.
   ══════════════════════════════════════════════════════════════════════════════ */
function initIndexPage() {
  // Restaurar posición de scroll al volver de un artículo
  const savedPos = sessionStorage.getItem('scrollPos');
  if (savedPos) {
    // Esperamos a que las tarjetas carguen antes de hacer scroll
    setTimeout(() => {
      window.scrollTo(0, parseInt(savedPos));
      sessionStorage.removeItem('scrollPos');
    }, 300);
  }
  // Estado de la interfaz: todos los datos y qué filtros están activos
  let allNews = [];             // array completo de artículos del index.json
  let activeCategory = 'Todas'; // categoría seleccionada en el filtro
  let activeTag = '';           // tag de subfiltro del sidebar ('' = sin filtro de tag)
  let searchQuery = '';         // texto que el usuario ha escrito en el buscador
  let visibleCount = 12;        // cuántas tarjetas mostramos actualmente
  const PAGE_SIZE = 12;         // cuántas tarjetas cargar por cada "Ver más"

  // Referencias a los elementos del buscador (pueden no existir en algunas páginas)
  const searchToggle = document.getElementById('search-toggle');
  const searchBar = document.getElementById('search-bar');
  const searchInput = document.getElementById('search-input');
  const searchClose = document.getElementById('search-close');

  // Mostrar/ocultar la barra de búsqueda al pulsar el icono de lupa
  searchToggle?.addEventListener('click', () => {
    searchBar.classList.toggle('open');
    // Si acabamos de abrir la barra, ponemos el foco en el input para que el usuario pueda escribir
    if (searchBar.classList.contains('open')) searchInput.focus();
  });

  // Limpiar búsqueda y ocultar la barra al pulsar la X
  searchClose?.addEventListener('click', () => {
    searchBar.classList.remove('open');
    searchInput.value = '';
    searchQuery = '';
    filterAndRender(); // volvemos a mostrar todos los artículos
  });

  // Filtrar en tiempo real mientras el usuario escribe (evento 'input')
  searchInput?.addEventListener('input', () => {
    searchQuery = searchInput.value.trim().toLowerCase();
    visibleCount = PAGE_SIZE; // reiniciamos la paginación con cada búsqueda nueva
    filterAndRender();
  });

  // Botón "Ver más": aumenta cuántos artículos se muestran
  document.getElementById('load-more-btn')?.addEventListener('click', () => {
    visibleCount += PAGE_SIZE;
    filterAndRender();
  });

  /**
   * Carga index.json y arranca la interfaz.
   *
   * Por qué hace fetch() con ?t=Date.now():
   *   Añadir un parámetro de tiempo como query string ("cache buster") fuerza
   *   al navegador a descargar un index.json fresco en lugar de usar una versión
   *   cacheada. Útil cuando el archivo se actualiza frecuentemente.
   */
  async function loadNews() {
    try {
      const res = await fetch('index.json?t=' + Date.now());
      if (!res.ok) throw new Error('No se pudo cargar index.json');
      const data = await res.json();
      allNews = Array.isArray(data) ? data : (data.news || []);
      
      if (!Array.isArray(data) && data.categories) {
        initCategories(data.categories);
      }
      
      updateStats();         // actualiza los contadores del header
      buildNav();            // construye los enlaces de navegación por categoría
      buildCategoryPills();  // construye los botones de filtro de categoría
      filterAndRender();     // renderiza las tarjetas con el estado inicial
    } catch (err) {
      // Si falla la carga, mostramos un mensaje de error en lugar de la cuadrícula vacía
      document.getElementById('news-grid').innerHTML = `
        <div class="loading-state">
          <p style="color:#f87171">⚠ ${err.message}</p>
          <p style="margin-top:8px;font-size:.85rem">Ejecuta <code>python build_index.py</code></p>
        </div>`;
    }
  }

  /**
   * Actualiza los contadores estadísticos del header (total, categorías, última fecha).
   *
   * Por qué existe:
   *   Da al usuario una vista rápida del volumen de contenido disponible
   *   sin tener que contar las tarjetas manualmente.
   */
  function updateStats() {
    document.getElementById('stat-total').textContent = allNews.length;
    const cats = new Set(allNews.map(n => n.category));
    document.getElementById('stat-cats').textContent = cats.size;
    // Mostramos la fecha del artículo más reciente (el array ya viene ordenado desc.)
    const dated = allNews.find(n => n.date);
    document.getElementById('stat-date').textContent = dated ? formatDate(dated.date) : '—';
  }

  /**
   * Construye los enlaces de navegación por categoría en la barra superior.
   *
   * Por qué las categorías son dinámicas:
   *   En lugar de hardcodear las categorías en el HTML, las generamos desde los
   *   datos reales de index.json. Así, si en el futuro se añade una nueva categoría
   *   a config.json, aparece automáticamente en la navegación sin tocar el HTML.
   */
  function buildNav() {
    const nav = document.getElementById('main-nav');
    if (!nav) return;
    const cats = [...new Set(allNews.map(n => n.category))].sort();
    nav.innerHTML =
      `<a href="#" class="nav-link active" data-cat="Todas">Todas</a>` +
      cats.map(c => `<a href="#" class="nav-link" data-cat="${c}">${c}</a>`).join('') +
      `<a href="about.html" class="nav-link" style="margin-left:auto">Sobre el proyecto</a>`;

    // Añadimos el listener de clic a cada enlace de categoría
    nav.querySelectorAll('.nav-link[data-cat]').forEach(a => {
      a.addEventListener('click', e => {
        e.preventDefault(); // evitamos que el href="#" haga scroll arriba
        activeCategory = a.dataset.cat;
        activeTag = ''; // al filtrar por nav reseteamos el subfiltro de tag
        // Quitamos "active" de todos los enlaces y se lo ponemos al clicado
        nav.querySelectorAll('.nav-link').forEach(x => x.classList.remove('active'));
        a.classList.add('active');
        syncPills(activeCategory); // sincronizamos los pills con el nav
        window.updateSidebarActive?.(activeCategory); // sincronizamos el sidebar
        visibleCount = PAGE_SIZE;   // reiniciamos la paginación
        filterAndRender();
      });
    });
  }

  /**
   * Construye los botones de filtro rápido (pills) bajo el header.
   *
   * Cada pill muestra el nombre de la categoría y el número de artículos en ella.
   * Son una alternativa visual a los enlaces del nav para filtrar por categoría.
   */
  function buildCategoryPills() {
    const container = document.getElementById('category-pills');
    if (!container) return;
    // Contamos cuántos artículos hay en cada categoría
    const counts = {};
    allNews.forEach(n => { counts[n.category] = (counts[n.category] || 0) + 1; });
    // "Todas" siempre va primero con el total de artículos
    container.appendChild(makePill('Todas', allNews.length, true));
    Object.keys(counts).sort().forEach(c => container.appendChild(makePill(c, counts[c], false)));
  }

  /**
   * Crea un botón pill de categoría como elemento DOM.
   *
   * @param {string}  label  - Nombre de la categoría
   * @param {number}  count  - Número de artículos en esa categoría
   * @param {boolean} active - Si el pill debe aparecer como seleccionado
   * @returns {HTMLButtonElement} Botón pill listo para insertar en el DOM
   */
  function makePill(label, count, active) {
    const btn = document.createElement('button');
    btn.className = 'pill' + (active ? ' active' : '');
    btn.dataset.cat = label;
    btn.innerHTML = `${label} <span class="count">${count}</span>`;
    btn.addEventListener('click', () => {
      activeCategory = label;
      activeTag = ''; // al filtrar por pill reseteamos el subfiltro de tag
      syncPills(label);
      // También sincronizamos los enlaces de navegación del header
      document.querySelectorAll('.nav-link[data-cat]').forEach(a => {
        a.classList.toggle('active', a.dataset.cat === label);
      });
      window.updateSidebarActive?.(label); // sincronizamos el sidebar
      visibleCount = PAGE_SIZE;
      filterAndRender();
    });
    return btn;
  }

  /**
   * Sincroniza el estado visual "active" de todos los pills.
   *
   * Por qué existe:
   *   Los pills pueden activarse desde el clic en el nav (buildNav) o desde
   *   el clic en otro pill (makePill). Esta función centraliza la lógica de
   *   actualización visual para no duplicarla en ambos sitios.
   *
   * @param {string} label - Categoría que debe quedar marcada como activa
   */
  function syncPills(label) {
    document.querySelectorAll('.pill').forEach(p =>
      p.classList.toggle('active', p.dataset.cat === label)
    );
  }

  /**
   * Filtra allNews según la categoría activa y el texto de búsqueda,
   * y llama a renderCards() con el resultado.
   *
   * Flujo:
   *   1. Si hay categoría activa (distinta de "Todas"), filtra por ella.
   *   2. Si hay texto en el buscador, filtra sobre el resultado anterior
   *      buscando en título, categoría, tags y preview simultáneamente.
   *   3. Llama a renderCards() con los artículos que pasaron los filtros.
   */
  function filterAndRender() {
    let filtered = allNews;
    if (activeCategory !== 'Todas') {
      filtered = filtered.filter(n => n.category === activeCategory);
    }
    // Subfiltro por tag del sidebar (si hay uno activo)
    if (activeTag) {
      filtered = filtered.filter(n =>
        (n.tags || []).some(t => t.toLowerCase() === activeTag.toLowerCase())
      );
    }
    if (searchQuery) {
      filtered = filtered.filter(n => {
        // Concatenamos los campos buscables en un único string en minúsculas
        const hay = `${n.title} ${n.category} ${(n.tags || []).join(' ')} ${n.preview || ''}`.toLowerCase();
        return hay.includes(searchQuery);
      });
    }
    renderCards(filtered);
  }

  /**
   * Renderiza las tarjetas de noticias en la cuadrícula del DOM.
   *
   * Gestiona también:
   *   - El estado vacío (cuando no hay resultados para los filtros)
   *   - La visibilidad del botón "Ver más" y el texto que muestra
   *
   * @param {Array} items - Lista de artículos filtrados a mostrar
   */
  function renderCards(items) {
    const grid = document.getElementById('news-grid');
    const loadWrap = document.getElementById('load-more-wrap');
    const emptyEl = document.getElementById('empty-state');

    if (items.length === 0) {
      // Sin resultados: mostramos el estado vacío y ocultamos todo lo demás
      grid.innerHTML = '';
      emptyEl.style.display = 'block';
      loadWrap.style.display = 'none';
      return;
    }
    emptyEl.style.display = 'none';
    // slice(0, visibleCount) implementa la "paginación suave" del botón "Ver más"
    grid.innerHTML = items.slice(0, visibleCount).map(cardHTML).join('');
    const hasMore = items.length > visibleCount;
    loadWrap.style.display = hasMore ? 'block' : 'none';
    // Actualizamos el texto del botón con cuántos artículos quedan por ver
    const btn = document.getElementById('load-more-btn');
    if (btn) btn.textContent = `Ver más artículos (${items.length - visibleCount} restantes)`;
  }

  /**
   * Genera el HTML de una tarjeta de noticia.
   *
   * La tarjeta completa es un enlace <a> para que todo el área sea clicable
   * y sea accesible desde teclado y lectores de pantalla.
   * La URL de destino es detail.html?file=<ruta_al_md> para que la página
   * de detalle sepa qué artículo cargar.
   *
   * @param {Object} news - Objeto de metadatos del artículo (del index.json)
   * @returns {string} HTML de la tarjeta como string
   */
  function cardHTML(news) {
    const cc = catClass(news.category);
    // Limitamos a 3 tags para no sobrecargar visualmente la tarjeta
    const tags = (news.tags || []).slice(0, 3).map(t => `<span class="tag">${esc(t)}</span>`).join('');
    const hasCmd = news.has_command ? `<span class="tag tag-code">⌨ código</span>` : '';
    // encodeURIComponent asegura que la ruta del archivo sea válida como query parameter de URL
    const href = `detail.html?file=${encodeURIComponent(news.file_path || '')}`;
    return `
    <a class="news-card ${cc}" href="${href}" onclick="sessionStorage.setItem('scrollPos', window.scrollY)">
      <div class="card-top">
        <span class="cat-badge ${cc}">${esc(news.category)}</span>
        <span class="card-date">${formatDate(news.date)}</span>
      </div>
      <div class="card-body">
        <h2 class="card-title">${esc(news.title)}</h2>
        <p class="card-preview">${esc(news.preview || 'Sin descripción disponible.')}</p>
      </div>
      ${tags || hasCmd ? `<div class="card-tags">${tags}${hasCmd}</div>` : ''}
      <div class="card-footer">
        <span class="read-link">Leer resumen completo →</span>
      </div>
    </a>`;
  }

  /**
   * Resetea todos los filtros activos y vuelve a mostrar todos los artículos.
   *
   * Por qué es global (window.resetFilters):
   *   Se necesita llamar desde el HTML del estado vacío con onclick="resetFilters()".
   *   Asignándola a window la hacemos accesible globalmente desde el HTML
   *   sin necesidad de exponer el módulo completo.
   */
  window.resetFilters = function () {
    activeCategory = 'Todas';
    activeTag = '';
    searchQuery = '';
    visibleCount = PAGE_SIZE;
    if (searchInput) searchInput.value = '';
    syncPills('Todas');
    document.querySelectorAll('.nav-link').forEach(a =>
      a.classList.toggle('active', a.dataset.cat === 'Todas')
    );
    window.updateSidebarActive?.('Todas');
    filterAndRender();
  };

  /**
   * Función pública que expone el motor de filtrado al módulo initSidebar.
   * Permite que la sidebar aplique un filtro de categoría + tag sin necesidad
   * de acceder directamente a las variables de estado de initIndexPage.
   *
   * @param {string} cat - Categoría a activar ('Ia', 'Linux', 'Embebidos', 'Todas')
   * @param {string} tag - Tag adicional ('python', 'llms', etc. o '' para todos)
   */
  window.setSidebarFilter = function(cat, tag) {
    activeCategory = cat;
    activeTag = tag || '';
    visibleCount = PAGE_SIZE;
    // Sincronizamos pills y nav del header con la categoría del sidebar
    syncPills(cat);
    document.querySelectorAll('.nav-link[data-cat]').forEach(a => {
      a.classList.toggle('active', a.dataset.cat === cat);
    });
    filterAndRender();
  };

  // Punto de entrada: cargamos los datos y arrancamos la UI
  loadNews().then(() => {
    const urlParams = new URLSearchParams(location.search);
    const urlTag = urlParams.get('tag');
    if (urlTag) {
      if (typeof window.showReportByTag === 'function') {
        window.showReportByTag(urlTag);
      } else {
        activeTag = urlTag;
        filterAndRender();
      }
    }
  });
}


/* ══════════════════════════════════════════════════════════════════════════════
   PÁGINA DE DETALLE (detail.html)
   Carga y renderiza un artículo completo a partir de su archivo .md.
   ══════════════════════════════════════════════════════════════════════════════ */
function initDetailPage() {
  // Leemos el parámetro "file" de la URL: detail.html?file=content/ia/articulo.md
  const params = new URLSearchParams(location.search);
  const filePath = params.get('file') || '';
  const container = document.getElementById('article-container');

  if (!filePath) {
    container.innerHTML = '<p style="color:#f87171">Artículo no encontrado.</p>';
    return;
  }

  // Cargamos en paralelo el .md del artículo Y el index.json (para artículos relacionados).
  // Promise.all garantiza que esperamos ambas respuestas antes de renderizar.
  Promise.all([
    fetch(filePath).then(r => { if (!r.ok) throw new Error('No se pudo cargar'); return r.text(); }),
    fetch('index.json').then(r => r.ok ? r.json() : [])
  ])
    .then(([md, data]) => {
      const allNews = Array.isArray(data) ? data : (data.news || []);
      if (!Array.isArray(data) && data.categories) {
        initCategories(data.categories);
      }
      const article = parseMarkdown(md);   // parseamos el Markdown a un objeto estructurado
      renderArticle(article, container);   // renderizamos el HTML del artículo
      renderRelated(article, allNews, filePath); // renderizamos artículos relacionados
      document.title = `${article.title} — TechPulse ES`; // actualizamos el título de la pestaña
      updateMetaTags(article);             // actualizamos las meta tags para compartir en redes
    })
    .catch(err => {
      container.innerHTML = `<p style="color:#f87171">⚠ ${err.message}</p>`;
    });
}

/**
 * Parsea un archivo Markdown de artículo y extrae su contenido estructurado.
 *
 * Por qué existe:
 *   Los artículos se almacenan como texto Markdown plano (no hay un servidor
 *   que los parsee). Esta función extrae cada sección del artículo usando
 *   expresiones regulares para poder renderizarlas con HTML personalizado.
 *
 * Cómo funciona:
 *   - get(label): busca una línea "**label:** valor" y devuelve el valor
 *   - section(name): busca el bloque "## name\n\ncontenido" y devuelve el contenido
 *   Las regex son específicas al formato que genera main.py en save_news().
 *
 * @param {string} md - Contenido completo del archivo .md como string
 * @returns {Object} Objeto con todos los campos del artículo extraídos
 */
function parseMarkdown(md) {
  // Extrae el valor de un campo tipo "**Campo:** valor"
  const get = label => {
    const m = md.match(new RegExp(`\\*\\*${label}:\\*\\*\\s*(.+)`));
    return m ? m[1].trim() : '';
  };
  // Extrae el contenido de una sección tipo "## Nombre\n\ncontenido\n\n## Siguiente"
  const section = name => {
    const m = md.match(new RegExp(`## ${name}\\s*\\n+([\\s\\S]+?)(?=\\n##|\\n---|$)`));
    return m ? m[1].trim() : '';
  };

  const titleM = md.match(/^#\s+(.+)$/m);
  const consejoRaw = section('Consejo técnico');
  // Extraemos el bloque de código del consejo si existe (entre ``` ... ```)
  const comandoM = consejoRaw.match(/```(?:bash)?\s*([\s\S]+?)```/);
  // Extraemos URL y texto del enlace "**Fuente original:** [texto](url)"
  const fuenteM = md.match(/\*\*Fuente original:\*\*\s*\[([^\]]+)\]\(([^)]+)\)/);

  return {
    title: titleM ? titleM[1].trim() : 'Sin título',
    category: get('Categoría'),
    date: get('Fecha'),
    tagsRaw: get('Tags'),
    original: get('Título original'),
    intro: section('Introducción'),
    que_es: section('¿Qué es\\?'),          // el \? escapa el ? en la regex
    como_funciona: section('¿Cómo funciona\\?'),
    por_que_importa: section('¿Por qué importa\\?'),
    consejo: consejoRaw.replace(/```[\s\S]*?```/g, '').trim(), // sin el bloque de código
    comando: comandoM ? comandoM[1].trim() : '',
    fuenteUrl: fuenteM ? fuenteM[2] : '',
    fuenteText: fuenteM ? fuenteM[1] : '',
  };
}

/**
 * Genera el HTML del artículo completo y lo inserta en el contenedor DOM.
 *
 * Por qué se usa esc() en todos los textos:
 *   El contenido viene de archivos .md generados por una IA. Aunque en la práctica
 *   no debería haber HTML malicioso, es buena práctica escapar siempre el contenido
 *   antes de insertarlo con innerHTML para prevenir XSS.
 *
 * @param {Object} a         - Objeto de artículo devuelto por parseMarkdown()
 * @param {Element} container - Elemento DOM donde insertar el artículo
 */
function renderArticle(a, container) {
  const cc = catClass(a.category);
  // Convertimos los tags separados por coma en spans individuales
  const tags = a.tagsRaw
    ? a.tagsRaw.split(',').map(t => `<span class="tag">${esc(t.trim())}</span>`).join('')
    : '';
  // El bloque de código solo se renderiza si hay un comando
  const comandoBlock = a.comando
    ? `<div class="code-block"><code>${esc(a.comando)}</code></div>`
    : '';
  // Filtramos las secciones vacías para no mostrar bloques sin contenido
  const sections = [
    { label: '¿Qué es?', content: a.que_es },
    { label: '¿Cómo funciona?', content: a.como_funciona },
    { label: '¿Por qué importa?', content: a.por_que_importa },
  ].filter(s => s.content);

  container.innerHTML = `
    <div class="article-eyebrow">
      <span class="cat-badge ${cc}">${esc(a.category)}</span>
    </div>
    <h1 class="article-title">${esc(a.title)}</h1>
    <div class="article-meta">
      <span class="meta-item">📅 ${formatDate(a.date)}</span>
      ${a.original ? `<span class="meta-item" title="Título original">🔤 ${esc(a.original)}</span>` : ''}
    </div>
    ${tags ? `<div class="article-tags" style="margin-bottom:32px">${tags}</div>` : ''}
    ${a.intro ? `<div class="article-intro"><p>${esc(a.intro)}</p></div>` : ''}
    ${sections.map(s => `
    <div class="article-section">
      <div class="section-label">${s.label}</div>
      <p class="article-text">${esc(s.content)}</p>
    </div>`).join('')}
    ${a.consejo ? `
    <div class="article-section">
      <div class="section-label">Consejo técnico</div>
      <div class="tip-box">
        <p>${esc(a.consejo)}</p>
        ${comandoBlock}
      </div>
    </div>` : ''}
    <div class="source-link-box">
      <div>
        <p>¿Quieres profundizar más?</p>
        <strong style="font-size:.9rem;color:var(--text-2)">Lee el artículo original completo</strong>
      </div>
      <a href="${esc(a.fuenteUrl)}" target="_blank" rel="noopener">
        Ver fuente original ↗
      </a>
    </div>
    <div id="related-section"></div>
  `;
}

/**
 * Busca y renderiza artículos relacionados al final del artículo actual.
 *
 * Estrategia de selección (en orden de preferencia):
 *   1. Hasta 2 artículos de la misma categoría (los más relacionados por tema)
 *   2. Hasta 1 artículo de otra categoría pero con algún tag en común
 *   Total: máximo 3 artículos relacionados para no sobrecargar la página.
 *
 * Por qué comparamos file_path de varias formas:
 *   El parámetro URL puede venir con o sin encodeURIComponent aplicado,
 *   y con barras "/" o "\" según el sistema. Comprobamos ambas variantes
 *   para no mostrar el artículo actual como "relacionado" con sí mismo.
 *
 * @param {Object} current         - Artículo actual (parseado)
 * @param {Array}  allNews         - Todos los artículos del index.json
 * @param {string} currentFilePath - Ruta del archivo actual (del query param)
 */
function renderRelated(current, allNews, currentFilePath) {
  const section = document.getElementById('related-section');
  if (!section || !allNews.length) return;

  // Artículos de la misma categoría excluyendo el actual
  const sameCat = allNews.filter(n =>
    n.category === current.category &&
    n.file_path !== currentFilePath.replace('%2F', '/') &&
    n.file_path !== decodeURIComponent(currentFilePath)
  );

  // Artículos de otra categoría pero con algún tag común
  const currentTags = new Set(
    (current.tagsRaw || '').split(',').map(t => t.trim().toLowerCase()).filter(Boolean)
  );
  const byTags = allNews.filter(n => {
    if (n.file_path === decodeURIComponent(currentFilePath)) return false;
    if (n.category === current.category) return false; // ya está en sameCat
    const nTags = (n.tags || []).map(t => t.toLowerCase());
    return nTags.some(t => currentTags.has(t));
  });

  // Combinamos: 2 de misma categoría + 1 por tags, máximo 3 en total
  const related = [...sameCat.slice(0, 2), ...byTags.slice(0, 1)].slice(0, 3);
  if (!related.length) return;

  section.innerHTML = `
    <div class="related-section">
      <div class="section-label" style="margin-bottom:16px">Artículos relacionados</div>
      <div class="related-grid">
        ${related.map(n => {
    const cc = catClass(n.category);
    const href = `detail.html?file=${encodeURIComponent(n.file_path || '')}`;
    return `
          <a class="related-card ${cc}" href="${href}">
            <span class="cat-badge ${cc}" style="margin-bottom:10px">${esc(n.category)}</span>
            <p class="related-title">${esc(n.title)}</p>
            <span class="read-link" style="font-size:.65rem;margin-top:8px">Leer →</span>
          </a>`;
  }).join('')}
      </div>
    </div>`;
}

/**
 * Actualiza las meta tags de la página para optimizar el compartir en redes sociales.
 *
 * Por qué existe:
 *   Las meta tags Open Graph (og:) controlan cómo se ve el enlace al compartirlo
 *   en Twitter/X, LinkedIn, WhatsApp, etc. (título, descripción, imagen).
 *   Las meta tags Twitter Card hacen lo mismo específicamente para Twitter.
 *   Sin estos tags, las redes sociales muestran un enlace genérico sin contexto.
 *
 * Cómo funciona:
 *   setMeta() busca una meta tag existente con ese nombre; si no existe, la crea.
 *   Así evitamos duplicar tags que el HTML base ya tenga definidos.
 *
 * @param {Object} article - Objeto de artículo devuelto por parseMarkdown()
 */
function updateMetaTags(article) {
  /**
   * Crea o actualiza una meta tag.
   * @param {string}  name    - Nombre o propiedad de la meta tag
   * @param {string}  content - Valor del atributo content
   * @param {boolean} prop    - true para usar property= (Open Graph), false para name=
   */
  const setMeta = (name, content, prop = false) => {
    const sel = prop ? `meta[property="${name}"]` : `meta[name="${name}"]`;
    let el = document.querySelector(sel);
    if (!el) {
      // Si no existe la meta tag, la creamos y la añadimos al <head>
      el = document.createElement('meta');
      prop ? el.setAttribute('property', name) : el.setAttribute('name', name);
      document.head.appendChild(el);
    }
    el.setAttribute('content', content);
  };

  // Meta tag estándar para buscadores (máx. ~160 chars recomendado por Google)
  setMeta('description', article.intro?.slice(0, 160) || article.title);
  // Open Graph: usado por Facebook, LinkedIn, WhatsApp, Telegram...
  setMeta('og:title', article.title, true);
  setMeta('og:description', article.intro?.slice(0, 200) || '', true);
  setMeta('og:type', 'article', true);
  // Twitter Card: usado por Twitter/X
  setMeta('twitter:card', 'summary');
  setMeta('twitter:title', article.title);
  setMeta('twitter:description', article.intro?.slice(0, 200) || '');
}

'use strict';

// ── THEME ────────────────────────────────────────────────────────
(function initTheme() {
  const saved = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
})();

function toggleTheme() {
  const cur  = document.documentElement.getAttribute('data-theme');
  const next = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
}
document.getElementById('theme-toggle')?.addEventListener('click', toggleTheme);

// ── UTILS ────────────────────────────────────────────────────────
const CAT_CLASS = {
  'ia':        'cat-ia',
  'robotica':  'cat-robotica',
  'linux':     'cat-linux',
  'embebidos': 'cat-embebidos',
  'diseño-3d': 'cat-diseno-3d',
  'diseno-3d': 'cat-diseno-3d',
};
function catClass(cat = '') {
  return CAT_CLASS[cat.toLowerCase()] || 'cat-default';
}
function formatDate(str) {
  if (!str) return '';
  const [y, m, d] = str.split('-').map(Number);
  return new Date(y, m - 1, d).toLocaleDateString('es-ES', {
    day: 'numeric', month: 'long', year: 'numeric'
  });
}
function esc(str) {
  if (!str) return '';
  const d = document.createElement('div');
  d.textContent = str;
  return d.innerHTML;
}

// ── DETECT PAGE ──────────────────────────────────────────────────
const isDetailPage = document.body.classList.contains('detail-page');
isDetailPage ? initDetailPage() : initIndexPage();

/* ══════════════════════════════════════════════════════════════
   INDEX PAGE
   ══════════════════════════════════════════════════════════════ */
function initIndexPage() {
  let allNews        = [];
  let activeCategory = 'Todas';
  let searchQuery    = '';
  let visibleCount   = 12;
  const PAGE_SIZE    = 12;

  // Search
  const searchToggle = document.getElementById('search-toggle');
  const searchBar    = document.getElementById('search-bar');
  const searchInput  = document.getElementById('search-input');
  const searchClose  = document.getElementById('search-close');

  searchToggle?.addEventListener('click', () => {
    searchBar.classList.toggle('open');
    if (searchBar.classList.contains('open')) searchInput.focus();
  });
  searchClose?.addEventListener('click', () => {
    searchBar.classList.remove('open');
    searchInput.value = '';
    searchQuery = '';
    filterAndRender();
  });
  searchInput?.addEventListener('input', () => {
    searchQuery = searchInput.value.trim().toLowerCase();
    visibleCount = PAGE_SIZE;
    filterAndRender();
  });

  document.getElementById('load-more-btn')?.addEventListener('click', () => {
    visibleCount += PAGE_SIZE;
    filterAndRender();
  });

  async function loadNews() {
    try {
      const res = await fetch('index.json?t=' + Date.now());
      if (!res.ok) throw new Error('No se pudo cargar index.json');
      allNews = await res.json();
      updateStats();
      buildNav();
      buildCategoryPills();
      filterAndRender();
    } catch (err) {
      document.getElementById('news-grid').innerHTML = `
        <div class="loading-state">
          <p style="color:#f87171">⚠ ${err.message}</p>
          <p style="margin-top:8px;font-size:.85rem">Ejecuta <code>python build_index.py</code></p>
        </div>`;
    }
  }

  function updateStats() {
    document.getElementById('stat-total').textContent = allNews.length;
    const cats = new Set(allNews.map(n => n.category));
    document.getElementById('stat-cats').textContent = cats.size;
    const dated = allNews.find(n => n.date);
    document.getElementById('stat-date').textContent = dated ? formatDate(dated.date) : '—';
  }

  function buildNav() {
    const nav = document.getElementById('main-nav');
    if (!nav) return;
    const cats = [...new Set(allNews.map(n => n.category))].sort();
    nav.innerHTML =
      `<a href="#" class="nav-link active" data-cat="Todas">Todas</a>` +
      cats.map(c => `<a href="#" class="nav-link" data-cat="${c}">${c}</a>`).join('') +
      `<a href="about.html" class="nav-link" style="margin-left:auto">Sobre el proyecto</a>`;

    nav.querySelectorAll('.nav-link[data-cat]').forEach(a => {
      a.addEventListener('click', e => {
        e.preventDefault();
        activeCategory = a.dataset.cat;
        nav.querySelectorAll('.nav-link').forEach(x => x.classList.remove('active'));
        a.classList.add('active');
        syncPills(activeCategory);
        visibleCount = PAGE_SIZE;
        filterAndRender();
      });
    });
  }

  function buildCategoryPills() {
    const container = document.getElementById('category-pills');
    if (!container) return;
    const counts = {};
    allNews.forEach(n => { counts[n.category] = (counts[n.category] || 0) + 1; });
    container.appendChild(makePill('Todas', allNews.length, true));
    Object.keys(counts).sort().forEach(c => container.appendChild(makePill(c, counts[c], false)));
  }

  function makePill(label, count, active) {
    const btn = document.createElement('button');
    btn.className = 'pill' + (active ? ' active' : '');
    btn.dataset.cat = label;
    btn.innerHTML = `${label} <span class="count">${count}</span>`;
    btn.addEventListener('click', () => {
      activeCategory = label;
      syncPills(label);
      document.querySelectorAll('.nav-link[data-cat]').forEach(a => {
        a.classList.toggle('active', a.dataset.cat === label);
      });
      visibleCount = PAGE_SIZE;
      filterAndRender();
    });
    return btn;
  }

  function syncPills(label) {
    document.querySelectorAll('.pill').forEach(p =>
      p.classList.toggle('active', p.dataset.cat === label)
    );
  }

  function filterAndRender() {
    let filtered = allNews;
    if (activeCategory !== 'Todas') {
      filtered = filtered.filter(n => n.category === activeCategory);
    }
    if (searchQuery) {
      filtered = filtered.filter(n => {
        const hay = `${n.title} ${n.category} ${(n.tags||[]).join(' ')} ${n.preview||''}`.toLowerCase();
        return hay.includes(searchQuery);
      });
    }
    renderCards(filtered);
  }

  function renderCards(items) {
    const grid     = document.getElementById('news-grid');
    const loadWrap = document.getElementById('load-more-wrap');
    const emptyEl  = document.getElementById('empty-state');

    if (items.length === 0) {
      grid.innerHTML = '';
      emptyEl.style.display = 'block';
      loadWrap.style.display = 'none';
      return;
    }
    emptyEl.style.display = 'none';
    grid.innerHTML = items.slice(0, visibleCount).map(cardHTML).join('');
    const hasMore = items.length > visibleCount;
    loadWrap.style.display = hasMore ? 'block' : 'none';
    const btn = document.getElementById('load-more-btn');
    if (btn) btn.textContent = `Ver más artículos (${items.length - visibleCount} restantes)`;
  }

  function cardHTML(news) {
    const cc   = catClass(news.category);
    const tags = (news.tags || []).slice(0, 3).map(t => `<span class="tag">${esc(t)}</span>`).join('');
    const hasCmd = news.has_command ? `<span class="tag tag-code">⌨ código</span>` : '';
    const href = `detail.html?file=${encodeURIComponent(news.file_path || '')}`;
    return `
    <a class="news-card ${cc}" href="${href}">
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

  window.resetFilters = function () {
    activeCategory = 'Todas';
    searchQuery    = '';
    visibleCount   = PAGE_SIZE;
    if (searchInput) searchInput.value = '';
    syncPills('Todas');
    document.querySelectorAll('.nav-link').forEach(a =>
      a.classList.toggle('active', a.dataset.cat === 'Todas')
    );
    filterAndRender();
  };

  loadNews();
}

/* ══════════════════════════════════════════════════════════════
   DETAIL PAGE
   ══════════════════════════════════════════════════════════════ */
function initDetailPage() {
  const params    = new URLSearchParams(location.search);
  const filePath  = params.get('file') || '';
  const container = document.getElementById('article-container');

  if (!filePath) {
    container.innerHTML = '<p style="color:#f87171">Artículo no encontrado.</p>';
    return;
  }

  // Load this article AND index for related articles
  Promise.all([
    fetch(filePath).then(r => { if (!r.ok) throw new Error('No se pudo cargar'); return r.text(); }),
    fetch('index.json').then(r => r.ok ? r.json() : [])
  ])
  .then(([md, allNews]) => {
    const article = parseMarkdown(md);
    renderArticle(article, container);
    renderRelated(article, allNews, filePath);
    document.title = `${article.title} — TechPulse ES`;
    updateMetaTags(article);
  })
  .catch(err => {
    container.innerHTML = `<p style="color:#f87171">⚠ ${err.message}</p>`;
  });
}

function parseMarkdown(md) {
  const get = label => {
    const m = md.match(new RegExp(`\\*\\*${label}:\\*\\*\\s*(.+)`));
    return m ? m[1].trim() : '';
  };
  const section = name => {
    const m = md.match(new RegExp(`## ${name}\\s*\\n+([\\s\\S]+?)(?=\\n##|\\n---|$)`));
    return m ? m[1].trim() : '';
  };

  const titleM     = md.match(/^#\s+(.+)$/m);
  const consejoRaw = section('Consejo técnico');
  const comandoM   = consejoRaw.match(/```(?:bash)?\s*([\s\S]+?)```/);
  const fuenteM    = md.match(/\*\*Fuente original:\*\*\s*\[([^\]]+)\]\(([^)]+)\)/);

  return {
    title:           titleM ? titleM[1].trim() : 'Sin título',
    category:        get('Categoría'),
    date:            get('Fecha'),
    tagsRaw:         get('Tags'),
    original:        get('Título original'),
    intro:           section('Introducción'),
    que_es:          section('¿Qué es\\?'),
    como_funciona:   section('¿Cómo funciona\\?'),
    por_que_importa: section('¿Por qué importa\\?'),
    consejo:         consejoRaw.replace(/```[\s\S]*?```/g, '').trim(),
    comando:         comandoM ? comandoM[1].trim() : '',
    fuenteUrl:       fuenteM ? fuenteM[2] : '',
    fuenteText:      fuenteM ? fuenteM[1] : '',
  };
}

function renderArticle(a, container) {
  const cc   = catClass(a.category);
  const tags = a.tagsRaw
    ? a.tagsRaw.split(',').map(t => `<span class="tag">${esc(t.trim())}</span>`).join('')
    : '';
  const comandoBlock = a.comando
    ? `<div class="code-block"><code>${esc(a.comando)}</code></div>`
    : '';
  const sections = [
    { label: '¿Qué es?',          content: a.que_es },
    { label: '¿Cómo funciona?',   content: a.como_funciona },
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

function renderRelated(current, allNews, currentFilePath) {
  const section = document.getElementById('related-section');
  if (!section || !allNews.length) return;

  // Buscar artículos de la misma categoría, excluyendo el actual
  const sameCat = allNews.filter(n =>
    n.category === current.category &&
    n.file_path !== currentFilePath.replace('%2F', '/') &&
    n.file_path !== decodeURIComponent(currentFilePath)
  );

  // También buscar por tags comunes
  const currentTags = new Set(
    (current.tagsRaw || '').split(',').map(t => t.trim().toLowerCase()).filter(Boolean)
  );
  const byTags = allNews.filter(n => {
    if (n.file_path === decodeURIComponent(currentFilePath)) return false;
    if (n.category === current.category) return false; // ya está en sameCat
    const nTags = (n.tags || []).map(t => t.toLowerCase());
    return nTags.some(t => currentTags.has(t));
  });

  const related = [...sameCat.slice(0, 2), ...byTags.slice(0, 1)].slice(0, 3);
  if (!related.length) return;

  section.innerHTML = `
    <div class="related-section">
      <div class="section-label" style="margin-bottom:16px">Artículos relacionados</div>
      <div class="related-grid">
        ${related.map(n => {
          const cc   = catClass(n.category);
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

function updateMetaTags(article) {
  const setMeta = (name, content, prop = false) => {
    const sel  = prop ? `meta[property="${name}"]` : `meta[name="${name}"]`;
    let el = document.querySelector(sel);
    if (!el) {
      el = document.createElement('meta');
      prop ? el.setAttribute('property', name) : el.setAttribute('name', name);
      document.head.appendChild(el);
    }
    el.setAttribute('content', content);
  };

  setMeta('description', article.intro?.slice(0, 160) || article.title);
  setMeta('og:title',       article.title, true);
  setMeta('og:description', article.intro?.slice(0, 200) || '', true);
  setMeta('og:type',        'article', true);
  setMeta('twitter:card',   'summary');
  setMeta('twitter:title',  article.title);
  setMeta('twitter:description', article.intro?.slice(0, 200) || '');
}

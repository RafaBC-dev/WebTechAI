'use strict';

document.addEventListener('DOMContentLoaded', () => {
  // Estado
  let allLibs = [];
  let filteredLibs = [];
  let activeCategory = 'Todas';
  let activeTags = new Set();
  let searchQuery = '';
  
  const predefinedCategories = [
    { id: 'Todas', name: 'Todas' },
    { id: 'datos', name: 'Datos' },
    { id: 'web', name: 'Web & APIs' },
    { id: 'ml', name: 'Machine Learning' },
    { id: 'vision', name: 'Visión Artificial' },
    { id: 'automatizacion', name: 'Automatización' },
    { id: 'db', name: 'Bases de datos' },
    { id: 'devtools', name: 'DevTools' }
  ];
  
  // Mapeo a las variables CSS del site principal
  const categoryColors = {
    'datos': 'var(--cat-ia)',
    'web': 'var(--cat-robotica)',
    'ml': 'var(--cat-linux)',
    'vision': 'var(--cat-ia)',
    'automatizacion': 'var(--cat-embebidos)',
    'db': 'var(--cat-diseno-3d)',
    'devtools': 'var(--cat-robotica)'
  };
  
  const grid = document.getElementById('libs-grid');
  const searchInput = document.getElementById('lib-search');
  const pillsContainer = document.getElementById('lib-pills');
  const listHeader = document.getElementById('list-header');
  const resultsCount = document.getElementById('results-count');
  const buildState = document.getElementById('build-state');
  const emptyState = document.getElementById('empty-state');
  const btnClearFilters = document.getElementById('btn-clear-filters');
  
  // Escapar para evitar inyecciones HTML
  function esc(str) {
    if (!str) return '';
    const d = document.createElement('div');
    d.textContent = str;
    return d.innerHTML;
  }
  
  async function init() {
    try {
      const res = await fetch('data/python-libs.json?t=' + Date.now());
      if (!res.ok) throw new Error('Error de red');
      allLibs = await res.json();
      
      if (!Array.isArray(allLibs)) allLibs = [];
      
      if (allLibs.length === 0) {
        grid.style.display = 'none';
        buildState.style.display = 'block';
        renderPills();
        return;
      }
      
      renderPills();
      applyFilters();
      
    } catch (error) {
      grid.innerHTML = `<div class="empty-state"><p style="color:#f87171">⚠ No se pudo cargar el archivo JSON.</p></div>`;
    }
  }
  
  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value.toLowerCase().trim();
    applyFilters();
  });
  
  btnClearFilters.addEventListener('click', () => {
    activeCategory = 'Todas';
    activeTags.clear();
    searchQuery = '';
    searchInput.value = '';
    renderPills();
    applyFilters();
  });
  
  function renderPills() {
    pillsContainer.innerHTML = '';
    
    predefinedCategories.forEach(cat => {
      let count = 0;
      if (cat.id === 'Todas') {
        count = allLibs.length;
      } else {
        count = allLibs.filter(l => (l.categoria || '').toLowerCase() === cat.id).length;
      }
      
      const btn = document.createElement('button');
      btn.className = `pill ${activeCategory === cat.id ? 'active' : ''}`;
      btn.innerHTML = `${cat.name} <span class="count">${count}</span>`;
      
      if (activeCategory === cat.id && cat.id !== 'Todas') {
          btn.style.backgroundColor = categoryColors[cat.id] || 'var(--text)';
          btn.style.color = '#0a0a0f'; // Alto contraste para los colores de acento pasteles
      } else if (activeCategory === 'Todas' && cat.id === 'Todas') {
          btn.style.backgroundColor = 'var(--text)';
          btn.style.color = 'var(--bg)';
      }
      
      btn.addEventListener('click', () => {
        activeCategory = cat.id;
        activeTags.clear();
        renderPills();
        applyFilters();
      });
      pillsContainer.appendChild(btn);
    });
  }
  
  function toggleTag(tag) {
    if (activeTags.has(tag)) {
      activeTags.delete(tag);
    } else {
      activeTags.add(tag);
    }
    applyFilters();
  }
  
  function applyFilters() {
    if (allLibs.length === 0) return;
    
    filteredLibs = allLibs.filter(lib => {
      if (activeCategory !== 'Todas' && (lib.categoria || '').toLowerCase() !== activeCategory) {
        return false;
      }
      
      if (activeTags.size > 0) {
        const libTags = lib.tags || [];
        const hasAllTags = Array.from(activeTags).every(t => libTags.includes(t));
        if (!hasAllTags) return false;
      }
      
      if (searchQuery) {
        const searchStr = [
          lib.nombre,
          lib.descripcion_corta,
          ...(lib.tags || [])
        ].join(' ').toLowerCase();
        if (!searchStr.includes(searchQuery)) return false;
      }
      
      return true;
    });
    
    renderGrid();
  }
  
  function renderGrid() {
    grid.innerHTML = '';
    
    listHeader.style.display = 'flex';
    resultsCount.textContent = `Mostrando ${filteredLibs.length} de ${allLibs.length} librerías`;
    
    if (activeCategory !== 'Todas' || activeTags.size > 0 || searchQuery !== '') {
      btnClearFilters.style.display = 'inline-flex';
    } else {
      btnClearFilters.style.display = 'none';
    }
    
    if (filteredLibs.length === 0) {
      emptyState.style.display = 'block';
    } else {
      emptyState.style.display = 'none';
      filteredLibs.forEach(lib => {
        const card = createCard(lib);
        grid.appendChild(card);
      });
      
      if (typeof hljs !== 'undefined') {
        document.querySelectorAll('pre code').forEach((block) => {
          hljs.highlightElement(block);
        });
      }
    }
  }
  
  function createCard(lib) {
    const div = document.createElement('div');
    div.className = 'lib-card';
    
    const catLower = (lib.categoria || '').toLowerCase();
    const isActiva = (lib.estado || 'activa').toLowerCase() === 'activa';
    const cssVarCat = categoryColors[catLower] || 'var(--accent)';
    
    div.style.setProperty('--card-color', cssVarCat);
    
    let tagsHtml = (lib.tags || []).map(t => 
       `<button class="lib-tag ${activeTags.has(t) ? 'active' : ''}" data-tag="${esc(t)}">#${esc(t)}</button>`
    ).join('');
    
    let headerHtml = `
      <div class="lib-card-accent"></div>
      <div class="lib-header">
        <div class="lib-title-area">
          <div class="lib-badges">
            <span class="cat-badge" style="color: ${cssVarCat}; background: ${cssVarCat}; background-opacity: 0.1;">${esc(lib.categoria || 'Otro')}</span>
            <span class="status-badge ${isActiva ? 'activa' : 'deprecated'}">${isActiva ? 'Activa' : 'Deprecated'}</span>
          </div>
          <h2 class="lib-name">${esc(lib.nombre)}</h2>
        </div>
      </div>
      <div class="lib-desc">${esc(lib.descripcion_corta)}</div>
      ${tagsHtml ? `<div class="lib-tags">${tagsHtml}</div>` : ''}
      <div class="lib-actions">
        <button class="btn-expand">
          <span>Ver más</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
      </div>
    `;
    
    div.innerHTML = headerHtml;
    
    if (tagsHtml) {
      div.querySelectorAll('.lib-tag').forEach(tagBtn => {
        tagBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          toggleTag(tagBtn.dataset.tag);
        });
      });
    }
    
    const details = document.createElement('div');
    details.className = 'lib-details';
    
    let detailsHtml = '';
    
    if (lib.que_es) {
      detailsHtml += `<div class="detail-section"><div class="detail-label">¿Qué es?</div><div class="detail-text">${esc(lib.que_es)}</div></div>`;
    }
    if (lib.para_que) {
      detailsHtml += `<div class="detail-section"><div class="detail-label">¿Para qué sirve?</div><div class="detail-text">${esc(lib.para_que)}</div></div>`;
    }
    if (lib.cuando_usarla) {
      detailsHtml += `<div class="detail-section"><div class="detail-label">Cuándo usarla</div><div class="detail-text" style="color: #34d399">${esc(lib.cuando_usarla)}</div></div>`;
    }
    if (lib.cuando_no) {
      detailsHtml += `<div class="detail-section"><div class="detail-label">Cuándo NO usarla</div><div class="detail-text" style="color: #f87171">${esc(lib.cuando_no)}</div></div>`;
    }
    
    if (lib.ejemplo && lib.ejemplo.codigo) {
       detailsHtml += `<div class="detail-section">
         <div class="detail-label">${esc(lib.ejemplo.titulo || 'Ejemplo')}</div>
         <div class="lib-code"><pre><code class="language-python">${esc(lib.ejemplo.codigo)}</code></pre></div>
       </div>`;
    }
    
    if (lib.docs) {
       detailsHtml += `<a href="${esc(lib.docs)}" target="_blank" class="docs-link" style="margin-top: 16px;">
         <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
         Documentación oficial
       </a>`;
    }
    
    details.innerHTML = detailsHtml;
    div.appendChild(details);
    
    const expandBtn = div.querySelector('.btn-expand');
    
    function toggleDetails() {
      const isOpen = details.classList.contains('open');
      if (isOpen) {
        details.classList.remove('open');
        expandBtn.classList.remove('open');
        expandBtn.querySelector('span').textContent = 'Ver más';
      } else {
        details.classList.add('open');
        expandBtn.classList.add('open');
        expandBtn.querySelector('span').textContent = 'Ver menos';
      }
    }
    
    expandBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleDetails();
    });
    
    div.addEventListener('click', (e) => {
      if(!e.target.closest('button') && !e.target.closest('a')) {
        toggleDetails();
      }
    });
    
    return div;
  }
  
  init();
});

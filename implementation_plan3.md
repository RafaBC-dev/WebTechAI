# Goal
Redesign the TechPulse ES navigation system to resemble technical documentation on desktop devices (>1024px). The layout will feature a fixed, constantly visible 240px sidebar on the left with the main content taking up the remaining space using CSS Grid/Flexbox. The mobile experience (<1024px) will retain the current hamburger menu and overlay behavior.

## Proposed Changes

### Configuration
- CSS variables will be managed as before, but layout constraints for body, header, hero, and main content will be updated to accommodate the fixed sidebar.

### Frontend

#### [MODIFY] docs/styles.css
- **Desktop Sidebar (`@media (min-width: 1025px)`)**:
  - `body`: Apply `display: flex;` or css grid to separate sidebar (240px) from the `main-content` (`flex: 1`).
  - `.sidebar`: Apply `position: sticky; top: 0; width: 240px; height: 100vh; background: var(--bg-2); border-right: 1px solid var(--border); overflow-y: auto;`
  - `.sidebar-overlay`, `#sidebar-close`, `#sidebar-toggle`: `display: none;`
  - Replace current nested `.sidebar-subfilters` and `.sidebar-item` with a documentation-style nav layout:
    - Section headers (`.nav-section-label`): uppercase, font-size `0.7rem`, color `var(--text-3)`, bold/mono.
    - Simple links (`.doc-nav-link`): color `var(--text-2)`, left padding, block level.
    - Hover on links: color `var(--text)`, subtle background `rgba(...)`
    - Active link state: color `var(--accent)`, `border-left: 2px solid var(--accent);`
- **Mobile Sidebar (`@media (max-width: 1024px)`)**:
  - Keep the fixed sliding sidebar (`transform: translateX(-100%);`), overlay, and close button.  The structure format of the links inside will match the new desktop ones, but the overall drawer behavior remains.
- **Global Layout (`@media (min-width: 1025px)`)**:
  - Remove original category nav (`#main-nav`) from the header or adjust it depending on aesthetics (decided to remove since sidebar replaces it entirely).
  - Adjust `.site-header` padding and width if needed (e.g., `width: calc(100% - 240px); float: right;` vs full width header above the sidebar). Based on traditional doc layouts, usually the sidebar goes all the way up, or the header is full width and the sidebar is below it. The easiest way without restructuring the entire HTML tree too much is letting the header span the remaining width, or keep it inside the right-side flex container. Let's make the wrapper for the right side.

#### [MODIFY] docs/index.html & docs/python.html & docs/llms.html & docs/about.html
- Ensure the `body` is split logically:
  ```html
  <body>
    <aside class="doc-sidebar">...</aside>
    <div class="page-wrapper">
       <header>...</header>
       <main>...</main>
       <footer>...</footer>
    </div>
  </body>
  ```
- Or alternatively, CSS Flex on the body directly.
- The new sidebar HTML structure will be exactly:
  (Logo)
  GENERAL
  - Todas las noticias
  ...
- Apply to all pages so the navigation matches.
- Remove "Librerías" from the Software Dev section.

#### [MODIFY] docs/app.js & docs/python-app.js
- Remove the accordion collapse/expand logic ([activateSidebarItem](file:///c:/Users/rafae/Desktop/WebTech/docs/app.js#92-119), toggle chevron, etc.) for desktop since all sections will be expanded constantly.
- Refactor the sidebar navigation handling to just use active classes and simple links. Since this is an MPA (Multi-Page App), `href="python.html"` will just navigate there. For filtering the index page (agentes, benchmarks, esp32), we can still use query params `/index.html?tag=benchmarks` or rely on `window.location.href`. The current app.js uses `dataset.tag` click events to filter the main grid. We will map the simple `<a>` links to `button` elements or `a` elements with event listeners that trigger [applyFilter(cat, tag, label)](file:///c:/Users/rafae/Desktop/WebTech/docs/app.js#325-344).

## Verification Plan
### Manual Verification
- Resize the browser to >1024px to check that the 240px sidebar is persistently visible and properly styled.
- Check the hover and active states of the navigation links.
- Check that the header hamburger is hidden.
- Resize below 1024px to verify the hamburger menu appears and triggers the siding overlay sidebar correctly.
- Verify the active link state sets a 2px left border in `var(--accent)`.

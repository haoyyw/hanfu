# Huashang Premium Single-Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and publish a premium bilingual single-page Hanfu culture atelier website with dynasty exploration, service packages, jewellery, ceremonial styling, tea, PhDessert crossover and future cultural experiences.

**Architecture:** A no-build static site for GitHub Pages. `index.html` owns semantic structure, `assets/css/styles.css` owns the design system and responsive layout, and `assets/js/app.js` owns language switching, dynasty state, lightweight perspective interaction and enquiry composition. Generated visual assets live under `assets/images/` and can later be replaced without changing interaction contracts.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript ES modules, Node built-in test runner/assertions, GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-09-09-huashang-premium-single-page-design.md`

## Global Constraints
- GitHub Pages-compatible static site with no build step.
- HTML, CSS and vanilla JavaScript only.
- English default with full Chinese language toggle.
- Generated imagery stored locally under `assets/images/`.
- No invented prices, booking inventory, contact address or payment functionality.
- Enquiry interaction must explicitly state that online submission is not yet connected.
- Motion must respect `prefers-reduced-motion`.
- Real `.glb/.gltf` Three.js 3D remains a later extension; version 1 uses restrained perspective and drag depth.

---

### Task 1: Static shell and design system

**Files:**
- Create: `index.html`
- Create: `assets/css/styles.css`
- Create: `README.md`

**Interfaces:**
- Produces semantic section IDs used by navigation and JavaScript: `home`, `dynasties`, `experience`, `jewellery`, `ceremonial`, `tea`, `dessert`, `coming-soon`, `booking`.
- Produces data attributes for bilingual text: `data-i18n`.

- [ ] **Step 1: Write structural tests**
Create `tests/site.test.mjs` using Node `assert` and `fs` to verify the required section IDs, bilingual toggle, PhDessert URL and local asset references exist.

- [ ] **Step 2: Run tests and verify they fail**
Run `node --test tests/site.test.mjs`; expected failure because site files do not exist.

- [ ] **Step 3: Implement semantic HTML and responsive CSS**
Create the navigation, hero, all content sections, booking area, footer, design tokens, editorial typography, cards, grids and responsive breakpoints.

- [ ] **Step 4: Run structural tests**
Run `node --test tests/site.test.mjs`; structural assertions should pass.

### Task 2: Dynasty data and interactive viewer

**Files:**
- Create: `assets/js/app.js`
- Modify: `index.html`
- Modify: `tests/site.test.mjs`

**Interfaces:**
- Produces `DYNASTIES` keyed by `han`, `tang`, `song`, `ming`.
- Produces `setDynasty(key)` and `setLanguage(locale)` browser functions scoped inside the module.
- Consumes DOM elements with `[data-dynasty]`, `#dynasty-visual`, `#dynasty-name`, `#dynasty-period`, `#dynasty-copy`, `#dynasty-details`.

- [ ] **Step 1: Extend tests**
Assert that `app.js` contains the four dynasty keys, the required image paths and language dictionaries.

- [ ] **Step 2: Run tests and verify the new assertions fail**
Run `node --test tests/site.test.mjs`.

- [ ] **Step 3: Implement dynasty switching and 3D-style interaction**
Clicking a dynasty tab updates its visual and copy. Pointer movement/drag applies bounded CSS perspective variables; keyboard buttons rotate/reset in small increments. Reset transforms when changing dynasty and when reduced motion is enabled.

- [ ] **Step 4: Run tests**
Run `node --test tests/site.test.mjs` and confirm all assertions pass.

### Task 3: Bilingual system, package selection and enquiry composer

**Files:**
- Modify: `assets/js/app.js`
- Modify: `index.html`
- Modify: `tests/site.test.mjs`

**Interfaces:**
- `TRANSLATIONS.en` and `TRANSLATIONS.zh` provide matching keys.
- Service choice buttons use `data-service`.
- Booking summary renders into `#enquiry-summary` and copy action uses `#copy-enquiry`.

- [ ] **Step 1: Extend tests**
Assert presence of translation parity markers, service data attributes, enquiry connection-status copy and copy-summary interaction hooks.

- [ ] **Step 2: Run tests and verify failure**
Run `node --test tests/site.test.mjs`.

- [ ] **Step 3: Implement language and enquiry behaviour**
Toggle all tagged copy, update `html[lang]`, persist language in localStorage, allow service selection, build a bilingual plain-text enquiry summary from user fields, copy it to clipboard and show accessible status feedback. Do not imply that the enquiry was sent.

- [ ] **Step 4: Run tests**
Run `node --test tests/site.test.mjs`.

### Task 4: Generated image assets and performance

**Files:**
- Create: `assets/images/hero-tang.webp`
- Create: `assets/images/dynasty-han.webp`
- Create: `assets/images/dynasty-song.webp`
- Create: `assets/images/dynasty-ming.webp`
- Create: `assets/images/styling.webp`
- Create: `assets/images/jewellery.webp`
- Create: `assets/images/ceremonial.webp`
- Create: `assets/images/tea.webp`
- Create: `assets/images/dessert.webp`
- Create: `assets/images/coming-soon.webp`
- Modify: `index.html`

**Interfaces:**
- HTML and JS reference only these stable filenames.

- [ ] **Step 1: Convert generated PNG images to WebP**
Use loss-aware WebP conversion sized for the rendered slots.

- [ ] **Step 2: Verify image references**
Run `node --test tests/site.test.mjs`; all referenced local files must exist.

- [ ] **Step 3: Add lazy loading and decoding hints**
Hero loads eagerly; supporting imagery uses `loading="lazy"` and `decoding="async"`.

### Task 5: Accessibility, responsive and release verification

**Files:**
- Modify: `assets/css/styles.css`
- Modify: `assets/js/app.js`
- Modify: `tests/site.test.mjs`

**Interfaces:**
- Interactive controls have `aria-*` state where needed.
- Focus-visible styles apply consistently.

- [ ] **Step 1: Add accessibility assertions**
Check for landmarks, labelled buttons, alt text, form labels, reduced-motion CSS and viewport meta.

- [ ] **Step 2: Run tests**
Run `node --test tests/site.test.mjs`.

- [ ] **Step 3: Run local static-server smoke test**
Serve the repository locally with `python -m http.server 8000`, request `/index.html`, `/assets/css/styles.css`, `/assets/js/app.js` and all image paths, and require HTTP 200 responses.

- [ ] **Step 4: Final source scan**
Confirm there are no placeholder contact details, broken internal anchors, external image hotlinks, accidental debug logs or invented prices.

- [ ] **Step 5: Commit release files to `main`**
Upload the verified text and WebP assets to the repository and confirm the repository root contains `index.html`.

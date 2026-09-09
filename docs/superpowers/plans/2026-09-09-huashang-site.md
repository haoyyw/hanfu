# 華裳 · HUASHANG Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and deploy the first premium interactive single-page website for the HUASHANG Hanfu culture atelier.

**Architecture:** Dependency-free static GitHub Pages site with a semantic HTML shell, a focused stylesheet, and one JavaScript interaction module. Generated artwork is committed as SVG wrappers containing compressed WebP data so the connected GitHub text API can store it while browsers render it as standard images.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, Node.js built-in test runner for local static-contract tests, GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-09-09-huashang-site-design.md`

## Global Constraints

- English is the default locale; Simplified Chinese is available without reload.
- No runtime framework, package manager dependency, or build step.
- Site must work as a static GitHub Pages deployment at `/hanfu/`.
- Core palette: lacquer black, cinnabar red, rice-paper ivory, muted jade, antique gold.
- Generated imagery is provisional and replaceable without changing section markup.
- Respect `prefers-reduced-motion`.
- PhDessert link must resolve to `https://haoyyw.github.io/PHDESSERT/`.

---

### Task 1: Static contract tests and semantic shell

**Files:**
- Create: `tests/site.test.mjs`
- Create: `index.html`

**Interfaces:**
- Consumes: design spec section IDs and required links.
- Produces: semantic DOM IDs used by styling and JavaScript: `hero`, `dynasties`, `experience`, `jewellery`, `ceremonial`, `tea`, `phdessert`, `coming-soon`, `booking`.

- [ ] **Step 1: Write failing tests** that read `index.html` and assert all required section IDs, the PhDessert URL, the language toggle, dynasty tablist, enquiry form labels, stylesheet reference, and module script reference.
- [ ] **Step 2: Run `node --test tests/site.test.mjs`** and confirm failure because `index.html` is absent.
- [ ] **Step 3: Create the semantic HTML shell** with all required sections and accessibility hooks.
- [ ] **Step 4: Re-run tests** and confirm the shell contract passes.
- [ ] **Step 5: Commit** test and shell.

### Task 2: Styling and premium responsive layout

**Files:**
- Create: `assets/styles.css`
- Modify: `tests/site.test.mjs`

**Interfaces:**
- Consumes: class names and IDs from `index.html`.
- Produces: responsive editorial layout, CSS 3D viewer frame, focus states, reduced-motion overrides.

- [ ] **Step 1: Add failing CSS contract tests** checking design tokens, responsive breakpoint, reduced-motion query, `.dynasty-stage`, `.package-builder`, and `.modal` styles.
- [ ] **Step 2: Run tests** and confirm failure because the stylesheet is absent.
- [ ] **Step 3: Implement the complete stylesheet** with desktop/mobile layouts and motion constraints.
- [ ] **Step 4: Re-run tests** and confirm green.
- [ ] **Step 5: Commit** stylesheet and tests.

### Task 3: Interaction model and bilingual data

**Files:**
- Create: `assets/app.js`
- Modify: `tests/site.test.mjs`

**Interfaces:**
- Produces: `DYNASTIES`, `COPY`, `setLocale(locale)`, `selectDynasty(key)`, `updatePackage()`, and enquiry mailto behaviour.

- [ ] **Step 1: Add failing JavaScript contract tests** asserting four dynasty keys, both locales, reduced-motion-safe pointer interaction hooks, service-builder state, and mailto form handling.
- [ ] **Step 2: Run tests** and confirm failure because `assets/app.js` is absent.
- [ ] **Step 3: Implement minimal interaction code** for tabs, 3D-style pointer tilt, bilingual copy, package builder, reveal-on-scroll, modal controls, and enquiry draft generation.
- [ ] **Step 4: Re-run tests** and confirm green.
- [ ] **Step 5: Commit** interaction code and tests.

### Task 4: Generated visual assets

**Files:**
- Create: `assets/images/hero-tang.svg`
- Create: `assets/images/han.svg`
- Create: `assets/images/song.svg`
- Create: `assets/images/ming.svg`
- Create: `assets/images/styling.svg`
- Create: `assets/images/jewellery.svg`
- Create: `assets/images/bridal.svg`
- Create: `assets/images/tea.svg`
- Create: `assets/images/pastry.svg`
- Create: `assets/images/coming-soon.svg`

**Interfaces:**
- Consumes: generated project artwork compressed locally to WebP.
- Produces: browser-renderable text-safe SVG image wrappers referenced by HTML and JavaScript.

- [ ] **Step 1: Extend tests** to assert every required image reference exists in HTML/JS and every local image file is present.
- [ ] **Step 2: Run tests** and confirm missing assets fail.
- [ ] **Step 3: Convert generated PNG artwork to compressed WebP and wrap each payload inside SVG `<image>` markup.**
- [ ] **Step 4: Re-run tests** and confirm all asset references resolve.
- [ ] **Step 5: Commit** assets.

### Task 5: Deployment and repository documentation

**Files:**
- Create: `.github/workflows/pages.yml`
- Create: `README.md`
- Modify: `tests/site.test.mjs`

**Interfaces:**
- Produces: GitHub Pages deployment workflow and maintainer instructions.

- [ ] **Step 1: Add failing tests** for workflow path, Pages actions, and README target URL.
- [ ] **Step 2: Run tests** and confirm failure.
- [ ] **Step 3: Add static Pages workflow** using `actions/configure-pages`, `actions/upload-pages-artifact`, and `actions/deploy-pages` plus concise README instructions.
- [ ] **Step 4: Run the complete test suite** with `node --test tests/site.test.mjs` and confirm all tests pass.
- [ ] **Step 5: Commit** deployment files and documentation.

### Task 6: Final verification

- [ ] Fetch the committed HTML, CSS, JS, assets, and workflow from GitHub and verify no path drift.
- [ ] Check the public Pages URL if deployment is available.
- [ ] Verify mobile and desktop structural behaviour through source inspection and browser rendering where accessible.
- [ ] Confirm all primary CTA links, PhDessert crossover, dynasty controls, bilingual controls, and booking interaction are present.

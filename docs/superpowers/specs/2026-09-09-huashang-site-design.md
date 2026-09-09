# 華裳 · HUASHANG Premium Interactive Single-Page Design

## Product goal
Create a premium bilingual GitHub Pages website for a Chinese Hanfu culture atelier. The site should present dynastic Hanfu experiences, hair and make-up styling, complete packages, Chinese jewellery, ceremonial and wedding styling, tea, a PhDessert crossover, and future Chinese cultural experiences.

## Brand direction
The visual language should feel related to PhDessert through editorial typography, generous spacing, refined motion, and premium presentation, while establishing its own identity through lacquer black, cinnabar red, rice-paper ivory, muted jade, and antique gold.

Working brand lock-up: `華裳 · HUASHANG` with the descriptor `HANFU CULTURE ATELIER`.

## Architecture
A dependency-free static site deployed from GitHub Pages. The first release uses `index.html`, `assets/styles.css`, and `assets/app.js`. No build step is required. Generated images are stored as text-safe SVG wrappers containing compressed WebP artwork so they can be committed through the connected GitHub text-file API while still rendering as normal images in browsers.

## Core experience

### 1. Header and Hero
Sticky translucent dark navigation with bilingual brand lock-up and anchor links. Hero uses a generated Tang-inspired editorial image, strong left-aligned copy, and calls to action for exploring Hanfu and booking an experience.

### 2. Dress Through the Dynasties
Four selectable dynasties: Han, Tang, Song, Ming. Each tab updates the large visual, dynasty dates, key garments, silhouette description, styling recommendation, and accessories. Han is represented by shenyi-inspired wrapped/cross-collar forms; Tang by high-waisted ruqun and pibo; Song by beizi and restrained vertical layers; Ming by aoqun and mamianqun.

The first release creates a lightweight interactive ‘3D-style’ viewer using CSS perspective, pointer-driven rotation, parallax, and lighting overlays. The component must have an explicit upgrade path for future `.glb/.gltf` Three.js models without changing the surrounding interface.

### 3. Build Your Look
Three service cards: Hanfu, Make-up, Hair. A highlighted Complete Experience combines Hanfu, hair, make-up, and accessories. Interactive service chips update a concise package summary.

### 4. Jewellery
Boutique gallery for hairpins, buyao, earrings, combs, jade details, and ornamental pieces. The first release is enquiry-led rather than transactional ecommerce.

### 5. Chinese Ceremonial Styling
Premium service section covering Chinese wedding bridal styling, bridal hair, engagement and pre-wedding styling, and event styling.

### 6. Tea Experience
Editorial section for Chinese tea tasting, gongfu tea introduction, seasonal tea, and Hanfu + Tea experiences.

### 7. Tea & Pastry × PhDessert
Show peach blossom pastry, osmanthus cake, mung bean cake, and rice cake. Link prominently to `https://haoyyw.github.io/PHDESSERT/`.

### 8. Coming Soon
A visual future-programme section for calligraphy, incense, guqin, Chinese flower art, lantern craft, and seal carving.

### 9. Booking / Enquiry
A front-end enquiry form with service selector, name, email, preferred date, and notes. In the static first release, submitting opens a pre-filled `mailto:` draft so no backend or third-party service is required. The UI must clearly state that the enquiry is not confirmed until the atelier replies.

## Bilingual behaviour
English is the default locale. A language switch toggles all primary interface copy to Simplified Chinese without a page reload. Dynasty garment names retain Chinese characters alongside English transliterations where useful.

## Generated image set
Use the generated visual family created for this project: Tang hero, Han portrait, Song portrait, Ming portrait, complete styling, jewellery, Chinese bridal styling, tea ritual, tea-and-pastry still life, and a Coming Soon cultural still life. Images should be treated as provisional brand imagery and replaceable later with commissioned photography or final 3D renders.

## Interaction and motion
Use subtle reveal-on-scroll, hover transitions, tab fades, pointer tilt on the dynasty viewer, and restrained ambient movement. Respect `prefers-reduced-motion` and keep the site fully usable without animation.

## Accessibility and responsive design
Semantic landmarks, keyboard-operable controls, visible focus states, descriptive alt text, strong contrast, labelled form fields, and responsive layouts down to narrow mobile screens. Interactive dynasty tabs use ARIA tab semantics.

## Deployment
Target URL: `https://haoyyw.github.io/hanfu/`. Add a Pages workflow so the repository can publish directly from the static root. No runtime dependencies or package installation.

## Success criteria
1. The complete service proposition is understandable within one page.
2. Dynasty selection is immediately visible and interactive.
3. Generated imagery establishes a coherent premium brand world.
4. PhDessert crossover is explicit and links correctly.
5. Mobile layout remains elegant and fully functional.
6. Core behaviour passes static integration tests for required sections, links, accessibility hooks, and JavaScript data contracts.

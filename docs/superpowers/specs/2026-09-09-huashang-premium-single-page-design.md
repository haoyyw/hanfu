# Huashang Premium Single-Page Design

## Purpose
Build a premium bilingual single-page website for a Chinese hanfu and cultural experience atelier, visually related to PhDessert while retaining a distinct identity.

## Brand and visual direction
- Working brand: `華裳 · HUASHANG`.
- Positioning: `HANFU · RITUAL · TEA · BEAUTY`.
- Palette: lacquer black, cinnabar red, rice-paper ivory, antique gold, muted celadon.
- Typography: editorial English serif + restrained sans serif + traditional Chinese serif.
- Visual character: luxury cultural atelier, generous whitespace, cinematic imagery, fine borders, subtle motion.
- The website must feel related to PhDessert through typography, pacing and editorial composition, but must not look like a recoloured copy.

## Platform and architecture
- GitHub Pages-compatible static site.
- No build step and no runtime framework.
- HTML, CSS and vanilla JavaScript only.
- Responsive from small mobile to desktop.
- Progressive enhancement: all essential content remains readable if JavaScript is unavailable.
- Generated imagery is stored locally in `assets/images/` to avoid hotlink dependencies.

## Information architecture
1. Sticky bilingual navigation and brand lock-up.
2. Cinematic hero with primary calls to explore hanfu and book an experience.
3. `Dress Through the Dynasties` interactive section for Han, Tang, Song and Ming.
4. Lightweight `3D-style` garment viewer using perspective, drag interaction and layered depth; architecture must allow later replacement with a real `.glb/.gltf` Three.js viewer.
5. `Build Your Look` service cards covering hanfu, make-up and hair.
6. `Complete Experience` package combining hanfu, hair, make-up and accessories.
7. Boutique Chinese jewellery and accessories section.
8. Chinese ceremonial styling covering weddings, bridal hair, engagement/pre-wedding and events.
9. Chinese tea experience section.
10. `Tea & Pastry × PhDessert` crossover linking to `https://haoyyw.github.io/PHDESSERT/`.
11. `Coming Soon` cultural experiences: calligraphy, incense, guqin, flower art, lantern craft and seal carving.
12. Booking/enquiry section with service selection and a non-misleading first-release interaction that does not invent a contact address.
13. Footer with brand and cross-brand link.

## Dynasty content
- Han: shenyi-derived wrapped/cross-collar silhouette, dark red/black ritual palette and restrained geometric/cloud detail.
- Tang: high-waisted ruqun, flowing layered skirt and pibo, with richer colour and movement.
- Song: beizi, slim vertical layering, narrow sleeves and muted celadon/ivory palette.
- Ming: aoqun styling, structured upper garment and pleated mamianqun silhouette.
- Copy should describe these as historically inspired experience looks rather than claim museum-grade reconstruction.

## Language system
- English default, Chinese toggle available in the header.
- Navigation, section headings, descriptive copy, calls to action and interactive labels must switch together.
- Brand name remains bilingual.

## Interactions
- Dynasty tabs update image, dynasty metadata, garment notes and styling recommendations.
- Garment visual reacts to pointer drag and keyboard-accessible controls, using restrained perspective rather than gimmicky rotation.
- Service package cards expose inclusions clearly.
- Enquiry form allows users to select an experience and compose/copy an enquiry summary locally. It must clearly state that online submission is not yet connected.
- Navigation uses smooth scrolling and active/hover feedback.
- Motion respects `prefers-reduced-motion`.

## Accessibility and performance
- Semantic landmarks, headings, labels and descriptive alt text.
- Strong focus-visible states and keyboard-operable controls.
- Sufficient colour contrast over imagery.
- Images converted to efficient web formats and served with explicit dimensions where practical.
- Avoid large external JavaScript dependencies.

## Generated visual assets
Use the generated images as first-release visual material for: hero/Tang, Han, Song, Ming, complete styling, jewellery, ceremonial bridal styling, tea experience, tea-and-pastry crossover and Coming Soon. These are concept visuals and can later be replaced by original photography without changing layout code.

## Release boundary
Version 1 is a premium functional showcase and enquiry website. Real e-commerce checkout, payment, live appointment inventory and true photogrammetric/3D garment models remain later extensions.

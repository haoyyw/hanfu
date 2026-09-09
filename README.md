# 華裳 · HUASHANG

Premium bilingual single-page website for a Hanfu and Chinese cultural experience atelier.

## What is included

- Han, Tang, Song and Ming dynasty-inspired Hanfu exploration
- Lightweight drag-and-perspective garment viewer
- Hanfu, make-up and hair services
- Complete styling package
- Chinese jewellery and hair accessories
- Chinese ceremonial, bridal and event styling
- Chinese tea experience
- Tea and Chinese pastry crossover with [PhDessert](https://haoyyw.github.io/PHDESSERT/)
- Coming Soon Chinese cultural experiences
- English / Chinese language switching
- Local enquiry composer that copies a request without pretending an online booking was submitted

## Preview locally

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/`.

## Tests

The test suite uses only Node's built-in test runner.

```bash
node --test tests/site.test.mjs
```

## Images

First-release images are generated concept visuals stored as optimised WebP files in `assets/images/`. They are deliberately referenced through stable filenames so original photography can replace them later without changing layout or interaction code.

## Future 3D upgrade

Version 1 uses a lightweight perspective interaction that works directly on GitHub Pages. A future true 3D garment viewer can replace the viewer internals with Three.js and `.glb/.gltf` assets while preserving the existing dynasty data and interface.

## GitHub Pages

The site is entirely static and can be served directly from the repository root. In GitHub, enable Pages for the `main` branch / repository root if the repository has not already been configured for Pages.

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
- Local enquiry composer that creates a copyable request

## Preview locally

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/`.

## Images

The first release uses generated concept visuals under `assets/images/`, plus the existing PhDessert Chinese tasting-box visual for the crossover section. Original photography can later replace the stable asset paths without changing the page structure.

## Future 3D upgrade

Version 1 uses a lightweight perspective interaction that works directly on GitHub Pages. A future true 3D garment viewer can replace the viewer internals with Three.js and `.glb/.gltf` assets while preserving the dynasty interface.

## GitHub Pages

The website is a static root-level `index.html` and can be served directly from the `main` branch.

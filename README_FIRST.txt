HUASHANG HD DROP-IN V3

1. Unzip this package.
2. Upload/replace index.html and the assets folder in the ROOT of your haoyyw/hanfu repository.
3. Keep .nojekyll in the repository root.
4. Commit to main. GitHub Pages will rebuild automatically.
5. Open https://haoyyw.github.io/hanfu/ and hard-refresh once.

Why this version is sharper:
- It follows the PhDessert approach: real production WebP files, not 10–20 KB previews.
- Portraits retain the original 1122 x 1402 pixels.
- Hero retains 1448 x 1086 pixels.
- WebP quality is 92; typical files are about 230–440 KB.
- All filenames end in -v3.webp, forcing browsers/CDNs to fetch fresh assets instead of cached low-quality files.
- Old AVIF/preview assets may remain in the repo, but index.html no longer references them.

The EN/ZH visual hierarchy is also retained: EN prioritises English; 中文 prioritises Chinese.

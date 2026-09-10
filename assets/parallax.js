(() => {
  'use strict';

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const desktopMode = () => window.innerWidth > 900;
  const mobileMode = () => window.innerWidth <= 900;
  const clamp = (value, min = 0, max = 1) => Math.min(max, Math.max(min, value));
  let ticking = false;

  const heroScene = document.querySelector('.hero-scene');
  const hero = heroScene?.querySelector('.hero');
  const heroImage = hero?.querySelector(':scope > img');
  const heroContent = hero?.querySelector('.hero-content');
  const heroNote = hero?.querySelector('.hero-note');
  const dynastySection = document.querySelector('#dynasties');
  const ceremonialSection = document.querySelector('#ceremonial');
  const teaSection = document.querySelector('#tea');

  function sectionProgress(section) {
    if (!section) return 0;
    const rect = section.getBoundingClientRect();
    const viewport = window.innerHeight || document.documentElement.clientHeight;
    return clamp((viewport - rect.top) / Math.max(viewport + rect.height, 1));
  }

  function heroProgress() {
    if (!heroScene || !hero) return 0;
    const rect = heroScene.getBoundingClientRect();
    const travel = Math.max(heroScene.offsetHeight - hero.offsetHeight, 1);
    return clamp(-rect.top / travel);
  }

  function reset() {
    document.querySelectorAll('.hero > img,.hero-content,.hero-note,#dynasties .look-card img,#ceremonial figure img,#tea figure img').forEach((el) => {
      el.style.transform = '';
      el.style.opacity = '';
      el.style.willChange = '';
    });
  }

  function setTransform(element, transform, opacity) {
    if (!element) return;
    element.style.willChange = 'transform, opacity';
    element.style.transform = transform;
    if (opacity !== undefined) element.style.opacity = String(opacity);
  }

  function updateDesktop() {
    const hp = heroProgress();
    setTransform(heroImage, `translate3d(0, ${(hp * 30).toFixed(2)}px, 0) scale(${(1.11 - hp * 0.06).toFixed(4)})`);
    setTransform(heroContent, `translate(-50%, -50%) translate3d(0, ${(-hp * 54).toFixed(2)}px, 0)`, (1 - hp * 0.82).toFixed(3));
    setTransform(heroNote, `translateX(-50%) translate3d(0, ${(-hp * 18).toFixed(2)}px, 0)`, (1 - hp * 0.9).toFixed(3));

    const dp = sectionProgress(dynastySection);
    dynastySection?.querySelectorAll('.look-card img').forEach((img, index) => {
      const offset = (0.5 - dp) * (index ? 34 : 46);
      const scale = 1.045 + Math.abs(0.5 - dp) * 0.015;
      setTransform(img, `translate3d(0, ${offset.toFixed(2)}px, 0) scale(${scale.toFixed(4)})`);
    });

    const cp = sectionProgress(ceremonialSection);
    setTransform(ceremonialSection?.querySelector('figure img'), `translate3d(0, ${((0.5 - cp) * 82).toFixed(2)}px, 0) scale(1.105)`);

    const tp = sectionProgress(teaSection);
    setTransform(teaSection?.querySelector('figure img'), `translate3d(0, ${((0.5 - tp) * 68).toFixed(2)}px, 0) scale(1.09)`);
  }

  function updateMobile() {
    if (heroImage && hero) {
      const rect = hero.getBoundingClientRect();
      const viewport = window.innerHeight || document.documentElement.clientHeight;
      const progress = clamp((viewport - rect.top) / Math.max(viewport + rect.height, 1));
      setTransform(heroImage, `translate3d(0, ${((0.5 - progress) * 22).toFixed(2)}px, 0) scale(1.035)`);
    }

    [
      [dynastySection, '.look-card img', 14, 1.025],
      [ceremonialSection, 'figure img', 18, 1.035],
      [teaSection, 'figure img', 16, 1.03]
    ].forEach(([section, selector, strength, scale]) => {
      const progress = sectionProgress(section);
      section?.querySelectorAll(selector).forEach((img) => {
        setTransform(img, `translate3d(0, ${((0.5 - progress) * strength).toFixed(2)}px, 0) scale(${scale})`);
      });
    });
  }

  function update() {
    if (reducedMotion.matches) {
      reset();
      return;
    }
    if (mobileMode()) updateMobile();
    else if (desktopMode()) updateDesktop();
  }

  function queueUpdate() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      update();
      ticking = false;
    });
  }

  function init() {
    queueUpdate();
    window.addEventListener('scroll', queueUpdate, { passive: true });
    window.addEventListener('resize', queueUpdate, { passive: true });
    reducedMotion.addEventListener?.('change', queueUpdate);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
})();

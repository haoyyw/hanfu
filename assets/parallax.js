(() => {
  'use strict';

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const definitions = [
    { selector: '.hero > img', desktop: 46, mobile: 16 },
    { selector: '#dynasties .look-card img', desktop: 22, mobile: 9 },
    { selector: '#ceremonial figure img', desktop: 32, mobile: 13 },
    { selector: '#tea figure img', desktop: 28, mobile: 11 }
  ];

  let targets = [];
  let ticking = false;

  function collectTargets() {
    targets = definitions.flatMap((definition) =>
      Array.from(document.querySelectorAll(definition.selector)).map((element) => ({
        element,
        definition
      }))
    );
  }

  function resetTransforms() {
    targets.forEach(({ element }) => {
      element.style.transform = '';
      element.style.willChange = '';
    });
  }

  function updateParallax() {
    if (reducedMotion.matches) {
      resetTransforms();
      return;
    }

    const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
    const mobile = window.innerWidth <= 620;

    targets.forEach(({ element, definition }) => {
      const rect = element.getBoundingClientRect();
      if (rect.bottom < -120 || rect.top > viewportHeight + 120) return;

      const elementCentre = rect.top + rect.height / 2;
      const travel = viewportHeight / 2 + rect.height / 2;
      const progress = Math.max(-1, Math.min(1, (viewportHeight / 2 - elementCentre) / travel));
      const strength = mobile ? definition.mobile : definition.desktop;
      const y = progress * strength;
      const scale = 1 + Math.min(0.14, (Math.abs(strength) * 2 / Math.max(rect.height, 1)) + 0.025);

      element.style.willChange = 'transform';
      element.style.transform = `translate3d(0, ${y.toFixed(2)}px, 0) scale(${scale.toFixed(4)})`;
    });
  }

  function queueUpdate() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      updateParallax();
      ticking = false;
    });
  }

  function init() {
    collectTargets();
    queueUpdate();
    window.addEventListener('scroll', queueUpdate, { passive: true });
    window.addEventListener('resize', queueUpdate, { passive: true });
    reducedMotion.addEventListener?.('change', queueUpdate);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();

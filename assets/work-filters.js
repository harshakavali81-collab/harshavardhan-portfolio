/* Accessible deterministic portfolio filter, with delegated events. */
(() => {
  "use strict";
  function activate(filter) {
    const buttons = [...document.querySelectorAll("button[data-filter]")];
    const cards = [...document.querySelectorAll(".case-card[data-type]")];
    const selected = buttons.some(b => b.dataset.filter === filter) ? filter : "All";
    let visible = 0;
    for (const b of buttons) b.setAttribute("aria-pressed", String(b.dataset.filter === selected));
    for (const card of cards) {
      const show = selected === "All" || card.dataset.type === selected;
      card.toggleAttribute("hidden", !show);
      if (show) visible++;
    }
    const counter = document.getElementById("count");
    if (counter) counter.textContent = visible + (visible === 1 ? " case study shown" : " case studies shown");
  }
  document.addEventListener("click", event => {
    const button = event.target.closest?.("button[data-filter]");
    if (button) activate(button.dataset.filter);
  }, true);
  function setup() {
    activate("All");
    // Register directly on each real button as well as delegated capture.
    // This guards against browser-specific retargeting and click propagation.
    for (const button of document.querySelectorAll("button[data-filter]")) {
      // A pointer press can precede a browser-level click that gets cancelled
      // when hover/scroll/layout changes the hit target. Respond immediately to
      // the primary press; the click handler remains for keyboard activation.
      const onPrimaryPress = event => {
        if (event.button === 0) activate(button.dataset.filter);
      };
      button.addEventListener("pointerdown", onPrimaryPress);
      button.addEventListener("mousedown", onPrimaryPress);
      button.addEventListener("click", () => activate(button.dataset.filter));
    }
    document.documentElement.dataset.workFiltersReady = "true";
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setup, {once: true});
  } else setup();
})();

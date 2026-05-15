document.addEventListener("DOMContentLoaded", () => {
  const fab = document.querySelector(".share-fab");
  if (!fab) return;

  const toggle = fab.querySelector(".share-fab__toggle");
  const menu = fab.querySelector(".share-fab__menu");
  const items = fab.querySelectorAll(".share-fab__item");

  const closeFab = () => {
    fab.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
  };

  const openFab = () => {
    fab.classList.add("is-open");
    toggle.setAttribute("aria-expanded", "true");
    items[0]?.focus();
  };

  // Toggle via clique
  toggle.addEventListener("click", (e) => {
    e.stopPropagation();

    const isOpen = fab.classList.contains("is-open");
    isOpen ? closeFab() : openFab();
  });

  // Fecha ao clicar fora
  document.addEventListener("click", (e) => {
    if (!fab.contains(e.target)) {
      closeFab();
    }
  });

  // Fecha com ESC
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closeFab();
      toggle.focus();
    }
  });

  // Controle de navegação por teclado
  fab.addEventListener("keydown", (e) => {
    if (!fab.classList.contains("is-open")) return;

    const currentIndex = Array.from(items).indexOf(document.activeElement);

    if (e.key === "ArrowDown") {
      e.preventDefault();
      items[(currentIndex + 1) % items.length]?.focus();
    }

    if (e.key === "ArrowUp") {
      e.preventDefault();
      items[(currentIndex - 1 + items.length) % items.length]?.focus();
    }
  });
});

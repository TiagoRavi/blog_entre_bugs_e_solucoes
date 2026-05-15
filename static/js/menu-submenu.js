document.addEventListener("DOMContentLoaded", () => {
  const submenus = document.querySelectorAll("[data-submenu]");
  const toggle = document.querySelector("[data-menu-toggle]");
  const nav = document.querySelector("[data-nav]");
  
  function closeAllSubmenus() {
    submenus.forEach(item => {
      item.classList.remove("is-open");
      item.querySelector(".menu-button")
        ?.setAttribute("aria-expanded", "false");
    });
  }

  // Submenu: só abre com clique explícito
  submenus.forEach(item => {
    const button = item.querySelector(".menu-button");

    button.addEventListener("click", event => {
      event.stopPropagation();

      const isOpen = item.classList.contains("is-open");

      closeAllSubmenus();

      if (!isOpen) {
        item.classList.add("is-open");
        button.setAttribute("aria-expanded", "true");
      }
    });
  });

  // Clique fora fecha tudo
  if (nav) {
  nav.addEventListener("click", event => {
    event.stopPropagation();
  });
}


  // Menu mobile
  if (toggle && nav) {
    toggle.addEventListener("click", event => {
      event.stopPropagation(); // 🔒 ESSENCIAL

      const isOpen = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", isOpen);

      if (isOpen) {
        closeAllSubmenus(); // garante submenu fechado
      }
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector("[data-nav]");

  if (!nav) return;

  const toggle = document.querySelector("[data-menu-toggle]");
  const submenus = document.querySelectorAll("[data-submenu]");

  const closeAllSubmenus = () => {
    submenus.forEach(submenu => {
      submenu.classList.remove("is-open");
      submenu
        .querySelector(".menu-button")
        ?.setAttribute("aria-expanded", "false");
    });
  };

  submenus.forEach(submenu => {
    const button = submenu.querySelector(".menu-button");

    button?.addEventListener("click", event => {
      event.stopPropagation();

      const isOpen = submenu.classList.contains("is-open");

      closeAllSubmenus();

      if (!isOpen) {
        submenu.classList.add("is-open");
        button.setAttribute("aria-expanded", "true");
      }
    });
  });

  nav.addEventListener("click", event => {
    event.stopPropagation();
  });

  if (!toggle) return;

  toggle.addEventListener("click", event => {
    event.stopPropagation();

    const isOpen = nav.classList.toggle("is-open");

    toggle.setAttribute("aria-expanded", String(isOpen));

    if (isOpen) {
      closeAllSubmenus();
    }
  });
});
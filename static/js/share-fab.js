document.addEventListener("DOMContentLoaded", () => {
  const fab = document.querySelector(".share-fab");
  const toggle = fab.querySelector(".share-fab__toggle");

  toggle.addEventListener("click", () => {
    fab.classList.toggle("is-open");
  });

  // Fecha ao clicar fora
  document.addEventListener("click", (e) => {
    if (!fab.contains(e.target)) {
      fab.classList.remove("is-open");
    }
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const wrapper = document.getElementById("search-wrapper");
  const input = document.getElementById("search-input");
  const toggle = document.getElementById("search-toggle");

  if (!wrapper || !toggle || !input) return;

  const openSearch = () => {
    wrapper.classList.add("is-open");
    input.focus();
  };

  const closeSearch = () => {
    wrapper.classList.remove("is-open");
  };

  toggle.addEventListener("click", event => {
    event.stopPropagation();
    openSearch();
  });

  wrapper.addEventListener("click", event => {
    event.stopPropagation();
  });

  document.addEventListener("click", closeSearch);

  document.addEventListener("keydown", event => {
    if (event.key === "Escape") {
      closeSearch();
    }
  });
});
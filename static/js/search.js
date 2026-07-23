console.log("search.js carregado");

document.addEventListener("DOMContentLoaded", function () {
  const wrapper = document.getElementById("search-wrapper");
  const toggle = document.getElementById("search-toggle");
  const input = document.getElementById("search-input");

  console.log(wrapper, toggle, input);

  if (!wrapper || !toggle || !input) return;

  toggle.addEventListener("click", function (event) {
    event.stopPropagation();
    wrapper.classList.add("active");
    input.focus();
  });

  wrapper.addEventListener("click", function (event) {
    event.stopPropagation();
  });

  document.addEventListener("click", function () {
    wrapper.classList.remove("active");
  });
});

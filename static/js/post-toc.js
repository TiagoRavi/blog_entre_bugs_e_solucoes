document.addEventListener("DOMContentLoaded", () => {
  const content = document.querySelector(".post-content");
  const toc = document.querySelector(".post-toc");
  const tocList = toc?.querySelector("#post-toc-list");
  const tocToggle = toc?.querySelector(".post-toc-toggle");

  if (!content || !toc || !tocList || !tocToggle) {
    return;
  }

  const headings = content.querySelectorAll("h2, h3");

  // Se não houver headings, remove o TOC
  if (headings.length === 0) {
    toc.remove();
    return;
  }

  // Gera os itens do TOC
  headings.forEach((heading, index) => {
    if (!heading.id) {
      heading.id = `section-${index}`;
    }

    const li = document.createElement("li");
    const a = document.createElement("a");

    a.href = `#${heading.id}`;
    a.textContent = heading.textContent;

    if (heading.tagName === "H3") {
      li.style.marginLeft = "1rem";
    }

    li.appendChild(a);
    tocList.appendChild(li);
  });

  // Estado inicial
  toc.dataset.collapsed = "false";
  tocToggle.setAttribute("aria-expanded", "true");

  // Toggle abrir / fechar
  tocToggle.addEventListener("click", () => {
    const isCollapsed = toc.dataset.collapsed === "true";

    toc.dataset.collapsed = String(!isCollapsed);
    tocToggle.setAttribute("aria-expanded", String(isCollapsed));
  });
});

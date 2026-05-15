document.addEventListener("DOMContentLoaded", () => {
  const content = document.querySelector(".post-content");
  const toc = document.querySelector(".post-toc");
  const tocList = toc?.querySelector("#post-toc-list");
  const tocToggle = toc?.querySelector(".post-toc-toggle");

  if (!content || !toc || !tocList || !tocToggle) {
    return;
  }

  const buildTOC = () => {
    const headings = content.querySelectorAll("h2, h3");

    if (!headings.length) {
      return false;
    }

    tocList.innerHTML = "";

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

    return true;
  };

  // 1️⃣ Tentativa imediata (SEM return)
  buildTOC();

  // 2️⃣ Observa mudanças no conteúdo (CMS / imagens / embeds)
  const observer = new MutationObserver(() => {
    if (buildTOC()) {
      observer.disconnect();
    }
  });

  observer.observe(content, {
    childList: true,
    subtree: true,
  });

  // Toggle abrir / fechar (AGORA SEMPRE REGISTRADO)
  tocToggle.addEventListener("click", () => {
    const isCollapsed = toc.dataset.collapsed === "true";

    toc.dataset.collapsed = isCollapsed ? "false" : "true";
    tocToggle.setAttribute("aria-expanded", isCollapsed ? "true" : "false");
  });
});

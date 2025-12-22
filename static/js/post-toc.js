document.addEventListener("DOMContentLoaded", () => {
  const content = document.querySelector(".post-content");
  const toc = document.querySelector(".post-toc");
  const tocList = toc?.querySelector("ul");

  if (!content || !toc || !tocList) return;

  const headings = content.querySelectorAll("h2, h3");

  if (headings.length === 0) {
    toc.style.display = "none";
    return;
  }

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
});

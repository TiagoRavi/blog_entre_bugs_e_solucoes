document.addEventListener("DOMContentLoaded", function () {
  const banner = document.getElementById("cookie-banner");
  const acceptBtn = document.getElementById("cookie-accept");
  const declineBtn = document.getElementById("cookie-decline");
  const settingsBtn = document.getElementById("cookie-settings-btn");

  if (!banner || !acceptBtn || !declineBtn || !settingsBtn) return;

  const STORAGE_KEY = "cookie_consent";
  const consent = localStorage.getItem(STORAGE_KEY);

  // Estado inicial
  if (consent) {
    banner.classList.add("is-hidden");
    settingsBtn.classList.remove("is-hidden");
  } else {
    banner.classList.add("is-hidden");
    settingsBtn.classList.remove("is-hidden");
  }

  // Abrir banner
  settingsBtn.addEventListener("click", () => {
    banner.classList.remove("is-hidden");
    settingsBtn.classList.add("is-hidden");
  });

  function closeBanner(value) {
    localStorage.setItem(STORAGE_KEY, value);
    banner.classList.add("is-hidden");
    settingsBtn.classList.remove("is-hidden");
  }

  acceptBtn.addEventListener("click", () => closeBanner("accepted"));
  declineBtn.addEventListener("click", () => closeBanner("declined"));
});

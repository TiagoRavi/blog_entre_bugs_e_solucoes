document.addEventListener("DOMContentLoaded", function () {
  const banner = document.getElementById("cookie-banner");
  const acceptBtn = document.getElementById("cookie-accept");
  const declineBtn = document.getElementById("cookie-decline");
  const settingsBtn = document.getElementById("cookie-settings-btn");

  if (!banner || !acceptBtn || !declineBtn || !settingsBtn) return;

  const STORAGE_KEY = "cookie_consent";
  const consent = localStorage.getItem(STORAGE_KEY);

  /**
   * Aplica consentimento ao Google Analytics
   */
  function applyConsent(status) {
    if (typeof gtag !== "function") return;

    if (status === "accepted") {
      gtag("consent", "update", {
        analytics_storage: "granted"
      });
      gtag("config", "G-Z2V7ET28GR", { anonymize_ip: true });
    } else {
      gtag("consent", "update", {
        analytics_storage: "denied"
      });
    }
  }

  // Estado inicial
  if (!consent) {
    banner.classList.remove("is-hidden");
    settingsBtn.classList.add("is-hidden");
  } else {
    banner.classList.add("is-hidden");
    settingsBtn.classList.remove("is-hidden");
    applyConsent(consent);
  }

  // Abrir configurações
  settingsBtn.addEventListener("click", () => {
    banner.classList.remove("is-hidden");
    settingsBtn.classList.add("is-hidden");
  });

  function closeBanner(value) {
    localStorage.setItem(STORAGE_KEY, value);
    banner.classList.add("is-hidden");
    settingsBtn.classList.remove("is-hidden");
    applyConsent(value);
  }

  acceptBtn.addEventListener("click", () => closeBanner("accepted"));
  declineBtn.addEventListener("click", () => closeBanner("declined"));
});

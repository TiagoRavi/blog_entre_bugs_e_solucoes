document.addEventListener("DOMContentLoaded", function () {
  const banner = document.getElementById("cookie-banner");
  const acceptBtn = document.getElementById("cookie-accept");
  const declineBtn = document.getElementById("cookie-decline");
  const settingsBtn = document.getElementById("cookie-settings-btn");

  const STORAGE_KEY = "cookie_consent";
  const consent = localStorage.getItem(STORAGE_KEY);

  function applyConsent(status) {
    if (typeof gtag !== "function") return;

    gtag("consent", "update", {
      analytics_storage: status === "accepted" ? "granted" : "denied",
    });

    if (status === "accepted") {
      gtag("config", "G-Z2V7ET28GR", { anonymize_ip: true });
    }
  }

  function closeBanner(value) {
    localStorage.setItem(STORAGE_KEY, value);

    document.cookie = `cookie_consent=${value}; path=/; max-age=31536000; SameSite=Lax`;

    applyConsent(value);

    if (banner && settingsBtn) {
      banner.classList.add("is-hidden");
      settingsBtn.classList.remove("is-hidden");
    }

    if (value === "accepted") {
      location.reload();
    }
  }

  // ============================
  // Banner (se existir)
  // ============================
  if (banner && acceptBtn && declineBtn && settingsBtn) {
    if (!consent) {
      banner.classList.remove("is-hidden");
      settingsBtn.classList.add("is-hidden");
    } else {
      banner.classList.add("is-hidden");
      settingsBtn.classList.remove("is-hidden");
      applyConsent(consent);
    }

    settingsBtn.addEventListener("click", () => {
      banner.classList.remove("is-hidden");
      settingsBtn.classList.add("is-hidden");
    });

    acceptBtn.addEventListener("click", () => closeBanner("accepted"));
    declineBtn.addEventListener("click", () => closeBanner("declined"));
  }

  // ============================
  // Placeholder do vídeo (SEMPRE)
  // ============================
  document.addEventListener("click", function (event) {
    const button = event.target.closest(".accept-cookies-and-load-video");
    if (!button) return;

    closeBanner("accepted");
  });
});

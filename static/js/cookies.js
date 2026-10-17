
document.addEventListener("DOMContentLoaded", function () {
  const banner = document.getElementById("cookie-banner");
  const acceptBtn = document.getElementById("cookie-accept");
  const declineBtn = document.getElementById("cookie-decline");
  const settingsBtn = document.getElementById("cookie-settings-btn");

  const STORAGE_KEY = "cookie_consent";

  function getConsent() {
    try {
      const value = localStorage.getItem(STORAGE_KEY);

      return value === "accepted" || value === "declined"
        ? value
        : null;
    } catch (error) {
      return null;
    }
  }

  function applyConsent(status) {
    if (typeof window.gtag !== "function") return;

    const granted = status === "accepted" ? "granted" : "denied";

    window.gtag("consent", "update", {
      analytics_storage: granted,
      ad_storage: granted,
      ad_user_data: granted,
      ad_personalization: granted
    });
  }

  
  
  function saveConsent(value) {
    try {
      localStorage.setItem(STORAGE_KEY, value);
    } catch (error) {
      console.warn("Não foi possível salvar o consentimento.", error);
    }

    const secure = window.location.protocol === "https:" ? "; Secure" : "";

    document.cookie =
      "cookie_consent=" + value +
      "; path=/; max-age=31536000; SameSite=Lax" + secure;

    applyConsent(value);
  }


  function showBanner() {
    if (banner) banner.classList.remove("is-hidden");
    if (settingsBtn) settingsBtn.classList.add("is-hidden");
  }

  function hideBanner() {
    if (banner) banner.classList.add("is-hidden");
    if (settingsBtn) settingsBtn.classList.remove("is-hidden");
  }

  function closeBanner(value) {
    saveConsent(value);
    hideBanner();
  }

  // O consentimento salvo já é aplicado no base.html.
  // Aqui, apenas definimos a visibilidade do banner.
  const consent = getConsent();

  if (consent) {
    hideBanner();
  } else {
    showBanner();
  }

  // Reabrir as configurações de cookies.
  if (settingsBtn) {
    settingsBtn.addEventListener("click", showBanner);
  }

  // Aceitar cookies.
  if (acceptBtn) {
    acceptBtn.addEventListener("click", function () {
      closeBanner("accepted");
    });
  }

  // Recusar cookies.
  if (declineBtn) {
    declineBtn.addEventListener("click", function () {
      closeBanner("declined");
    });
  }

  // O carregamento de vídeo não aceita cookies automaticamente.
  document.addEventListener("click", function (event) {
    const target = event.target;

    if (!(target instanceof Element)) return;

    const button = target.closest(".accept-cookies-and-load-video");

    if (!button) return;

    // Não altera a preferência de consentimento.
    // O carregamento do vídeo deve ser tratado separadamente.
  });
});

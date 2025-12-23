document.addEventListener("DOMContentLoaded", function () {
  // --------------------------------------------------
  // Elementos do DOM
  // --------------------------------------------------
  const banner = document.getElementById("cookie-banner");
  const acceptBtn = document.getElementById("cookie-accept");
  const declineBtn = document.getElementById("cookie-decline");
  const settingsBtn = document.getElementById("cookie-settings-btn");

  // Se os elementos essenciais não existirem, aborta
  if (!banner || !acceptBtn || !declineBtn) {
    return;
  }

  const STORAGE_KEY = "cookie_consent";
  let consent = null;

  // --------------------------------------------------
  // Leitura segura do localStorage
  // --------------------------------------------------
  try {
    consent = localStorage.getItem(STORAGE_KEY);
  } catch (error) {
    // localStorage indisponível (modo privado, políticas, etc.)
    banner.hidden = false;
    return;
  }

  // Se já existe decisão, o banner começa oculto
  // Caso contrário, ele é exibido
  banner.hidden = !!consent;

  // --------------------------------------------------
  // Ações do banner
  // --------------------------------------------------

  // Aceitar cookies
  acceptBtn.addEventListener("click", function () {
    try {
      localStorage.setItem(STORAGE_KEY, "accepted");
    } catch (error) {
      // Falha silenciosa
    }

    banner.hidden = true;
  });

  // Recusar cookies
  declineBtn.addEventListener("click", function () {
    try {
      localStorage.setItem(STORAGE_KEY, "declined");
    } catch (error) {
      // Falha silenciosa
    }

    banner.hidden = true;
  });

  // --------------------------------------------------
  // Botão flutuante (reabrir configurações)
  // --------------------------------------------------
  if (settingsBtn) {
    settingsBtn.addEventListener("click", function () {
      banner.hidden = false;
    });
  }
});

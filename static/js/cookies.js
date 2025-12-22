document.addEventListener("DOMContentLoaded", function () {
  const banner = document.getElementById("cookie-banner");
  const acceptBtn = document.getElementById("cookie-accept");
  const declineBtn = document.getElementById("cookie-decline");

  // Se o banner não existir, não faz nada
  if (!banner || !acceptBtn || !declineBtn) return;

  let consent = null;

  try {
    consent = localStorage.getItem("cookie_consent");
  } catch (e) {
    // localStorage indisponível (modo privado, políticas, etc.)
    banner.hidden = false;
    return;
  }

  if (!consent) {
    banner.hidden = false;
  }

  acceptBtn.addEventListener("click", function () {
    try {
      localStorage.setItem("cookie_consent", "accepted");
    } catch (e) {}
    banner.hidden = true;
  });

  declineBtn.addEventListener("click", function () {
    try {
      localStorage.setItem("cookie_consent", "declined");
    } catch (e) {}
    banner.hidden = true;
  });
});

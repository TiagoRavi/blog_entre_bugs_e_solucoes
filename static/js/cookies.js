document.addEventListener("DOMContentLoaded", function () {
  const banner = document.getElementById("cookie-banner");
  const acceptBtn = document.getElementById("cookie-accept");
  const declineBtn = document.getElementById("cookie-decline");

  const consent = localStorage.getItem("cookie_consent");

  if (!consent) {
    banner.hidden = false;
  }

  acceptBtn.addEventListener("click", function () {
    localStorage.setItem("cookie_consent", "accepted");
    banner.hidden = true;
  });

  declineBtn.addEventListener("click", function () {
    localStorage.setItem("cookie_consent", "declined");
    banner.hidden = true;
  });
});

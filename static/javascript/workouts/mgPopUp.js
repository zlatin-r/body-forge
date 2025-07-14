document.addEventListener("DOMContentLoaded", function () {
    const openBtn = document.getElementById("openPopupBtn");
    const modal = document.getElementById("popupModal");
    const closeBtn = document.querySelector(".close-btn");

    if (openBtn) {
        openBtn.onclick = function () {
            modal.style.display = "block";
        }
    }

    if (closeBtn) {
        closeBtn.onclick = function () {
            modal.style.display = "none";
        }
    }

    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    }
});

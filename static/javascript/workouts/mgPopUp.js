document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("popupModal");
    const btn = document.getElementById("openPopupBtn");
    const span = document.querySelector(".close-btn");

    btn.onclick = function () {
        modal.style.display = "block";
    }

    span.onclick = function () {
        modal.style.display = "none";
    }

    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    }
});

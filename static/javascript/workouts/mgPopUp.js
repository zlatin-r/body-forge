document.addEventListener("DOMContentLoaded", function () {
    // Muscle Group Modal
    const mgOpenBtn = document.getElementById("openMgPopupBtn");
    const mgModal = document.getElementById("popupModal");
    const mgCloseBtn = document.querySelector(".close-btn");

    if (mgOpenBtn) {
        mgOpenBtn.onclick = () => mgModal.style.display = "block";
    }
    if (mgCloseBtn) {
        mgCloseBtn.onclick = () => mgModal.style.display = "none";
    }

    // Workout Type Modal
    const wtOpenBtn = document.getElementById("openWtPopupBtn");
    const wtModal = document.getElementById("wtTypeModal");
    const wtCloseBtn = document.querySelector(".wt-close-btn");

    if (wtOpenBtn) {
        wtOpenBtn.onclick = () => wtModal.style.display = "block";
    }
    if (wtCloseBtn) {
        wtCloseBtn.onclick = () => wtModal.style.display = "none";
    }

    // Close modals if clicked outside
    window.onclick = function (event) {
        if (event.target === mgModal) {
            mgModal.style.display = "none";
        }
        if (event.target === wtModal) {
            wtModal.style.display = "none";
        }
    }
});

// document.addEventListener("DOMContentLoaded", function () {
//     const openBtn = document.getElementById("openMgPopupBtn");
//     const modal = document.getElementById("popupModal");
//     const closeBtn = document.querySelector(".close-btn");
//
//
//     if (openBtn) {
//         openBtn.onclick = function () {
//             modal.style.display = "block";
//         }
//     }
//
//     if (closeBtn) {
//         closeBtn.onclick = function () {
//             modal.style.display = "none";
//         }
//     }
//
//     window.onclick = function (event) {
//         if (event.target === modal) {
//             modal.style.display = "none";
//         }
//     }
// });

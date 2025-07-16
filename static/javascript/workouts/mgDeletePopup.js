document.addEventListener("DOMContentLoaded", function () {
    const modal2 = document.getElementById("popupModal2");
    const closeBtn = modal2.querySelector(".close-btn");
    const cancelBtn = document.getElementById("cancelDelete");
    const deleteForm = document.getElementById("deleteMgForm");

    document.addEventListener('click', function (e) {
        if (e.target.classList.contains('delete-mg-btn')) {
            const mgName = e.target.getAttribute('data-mg');
            const mgId = e.target.getAttribute('data-mg-id');

            document.getElementById('mgNamePlaceholder').textContent = mgName;

            deleteForm.action = `/workout/delete-mg/${mgId}/`;

            modal2.style.display = "block";
        }
    });

    closeBtn.onclick = function () {
        modal2.style.display = "none";
    };

    cancelBtn.onclick = function (e) {
        e.preventDefault();
        modal2.style.display = "none";
    };

    window.onclick = function (event) {
        if (event.target === modal2) {
            modal2.style.display = "none";
        }
    };
});

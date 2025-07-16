document.addEventListener("DOMContentLoaded", function() {
    const modal2 = document.getElementById("popupModal2");
    const closeBtn = modal2.querySelector(".close-btn");
    const cancelBtn = document.getElementById("cancelDelete");
    const deleteForm = document.getElementById("deleteMgForm");

    // Handle all delete buttons (using event delegation)
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('delete-mg-btn')) {
            // Get the muscle group name from data attribute
            const mgName = e.target.getAttribute('data-mg');
            const mgId = e.target.getAttribute('data-mg-id');

            // Update the modal text
            document.getElementById('mgNamePlaceholder').textContent = mgName;

            // Update the form action URL with the muscle group ID
            deleteForm.action = `/workout/delete-mg/${mgId}/`;

            // Show the modal
            modal2.style.display = "block";
        }
    });

    // Close modal when clicking X, cancel, or outside
    closeBtn.onclick = function() {
        modal2.style.display = "none";
    };

    cancelBtn.onclick = function(e) {
        e.preventDefault();
        modal2.style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target === modal2) {
            modal2.style.display = "none";
        }
    };
});
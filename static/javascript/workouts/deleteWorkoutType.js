document.addEventListener('DOMContentLoaded', function () {
    const delIcon = document.getElementById('del-icon');

    delIcon.addEventListener('click', function (e) {

        const clickedLI = e.target.closest('LI');

        if (clickedLI) clickedLI.remove();
    });
});

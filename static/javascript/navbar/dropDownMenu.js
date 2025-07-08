document.addEventListener('DOMContentLoaded', function () {
    const avatarContainer = document.querySelector('.avatar');
    const dropdownMenuElement = document.querySelector('#dropdown-menu');

    if (avatarContainer) {
        avatarContainer.addEventListener('click', function (e) {
            e.preventDefault();
            dropdownMenuElement.classList.toggle('hidden');
        });
    }

    document.addEventListener('click', function (e) {
        if (!e.target.closest('.avatar') && !e.target.closest('.dropdown-menu')) {
            dropdownMenuElement.classList.add('hidden');
        }
    })
});
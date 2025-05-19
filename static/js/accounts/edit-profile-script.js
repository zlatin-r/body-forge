document.addEventListener('DOMContentLoaded', function () {
    // Handle photo change button
    document.getElementById('change-photo-btn').addEventListener('click', function () {
        document.getElementById('profile-picture-input').click();
    });

    // Handle photo removal button
    document.getElementById('remove-photo-btn').addEventListener('click', function () {
        // Implement your photo removal logic here
        alert('Photo removal functionality would go here');
    });

    // Preview image when selected
    document.getElementById('profile-picture-input').addEventListener('change', function (e) {
        if (e.target.files && e.target.files[0]) {
            const reader = new FileReader();
            reader.onload = function (event) {
                const avatar = document.querySelector('.profile-avatar') ||
                    document.querySelector('.profile-avatar-default');
                if (avatar) {
                    if (avatar.classList.contains('profile-avatar-default')) {
                        // Replace the default avatar with an image
                        const newAvatar = document.createElement('img');
                        newAvatar.src = event.target.result;
                        newAvatar.className = 'profile-avatar rounded-circle mb-3';
                        newAvatar.alt = 'Profile Picture';
                        avatar.parentNode.replaceChild(newAvatar, avatar);
                    } else {
                        // Update existing avatar
                        avatar.src = event.target.result;
                    }
                }
            };
            reader.readAsDataURL(e.target.files[0]);
        }
    });
});
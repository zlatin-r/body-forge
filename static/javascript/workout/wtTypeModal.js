document.addEventListener('DOMContentLoaded', function() {
    const openBtn = document.getElementById('openWtTypeModal');
    const modal = document.getElementById('wtTypeModal');
    const closeBtn = document.querySelector('.wt-close-btn');

    if (openBtn && modal && closeBtn) {
        // Open modal
        openBtn.addEventListener('click', () => {
            modal.style.display = 'flex';
            document.body.style.overflow = 'hidden'; // Prevent scrolling
        });

        // Close modal via close button
        closeBtn.addEventListener('click', () => {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        });

        // Close modal by clicking outside
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.style.display = 'none';
                document.body.style.overflow = 'auto';
            }
        });

        // Close with Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && modal.style.display === 'flex') {
                modal.style.display = 'none';
                document.body.style.overflow = 'auto';
            }
        });
    }
});

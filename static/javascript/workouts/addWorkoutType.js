document.addEventListener('DOMContentLoaded', function () {
    const sourceList = document.getElementById('sourceList');
    const targetList = document.getElementById('targetList');

    sourceList.addEventListener('click', function (e) {
        const clickedLI = e.target.closest('li');
        if (!clickedLI) return;

        const text = clickedLI.textContent.trim();
        const alreadyAdded = Array.from(targetList.children).some(
            li => li.textContent.trim() === text
        );

        if (!alreadyAdded) {
            const newItem = clickedLI.cloneNode(true);

            const icon = newItem.querySelector('i');
            if (icon) icon.remove();

            targetList.appendChild(newItem);
        }
    });

    targetList.addEventListener('click', function (e) {
        const clickedLI = e.target.closest('li');
        if (clickedLI) clickedLI.remove();
    });
});

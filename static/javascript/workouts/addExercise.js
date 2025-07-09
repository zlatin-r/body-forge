document.addEventListener('DOMContentLoaded', function () {
    const sourceList = document.getElementById('sourceList');
    const targetList = document.getElementById('targetList');

    sourceList.addEventListener('click', function (e) {
        if (e.target && e.target.tagName === 'LI') {

            // Optional: prevent duplicates
            const alreadyAdded = Array.from(targetList.children).some(li => li.textContent === e.target.textContent);

            if (!alreadyAdded) {
                const newItem = e.target.cloneNode(true); // clone if you don't want to remove from source
                targetList.appendChild(newItem);
            }
        }
    });

    targetList.addEventListener('click', function (e) {
        if (e.target && e.target.tagName === 'LI') {
            e.target.remove();
        }
    })
});

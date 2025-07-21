document.addEventListener('DOMContentLoaded', function () {
    const deleteBtn = document.getElementById('deleteWorkoutTypeBtn');
    const select = document.getElementById('workoutType');

    if (deleteBtn && select) {
        deleteBtn.addEventListener('click', () => {
            const selectedId = select.value;
            if (!selectedId) return;

            fetch(`/workout/type/delete/${selectedId}/`, {
                method: "POST",
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    if (response.ok) {
                        location.reload();
                    } else {
                        alert("Failed to delete workout type.");
                    }
                });
        });
    }
});

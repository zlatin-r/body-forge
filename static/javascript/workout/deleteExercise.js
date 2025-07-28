document.addEventListener('DOMContentLoaded', function () {
    const deleteExerciseBtn = document.getElementById('deleteExerciseBtn');
    const exerciseSelect = document.getElementById('exercisesList');

    if (deleteExerciseBtn && exerciseSelect) {
        deleteExerciseBtn.addEventListener('click', () => {
            const selectedId = exerciseSelect.value;
            if (!selectedId) return;

            fetch(`/workout/delete-exercise/${selectedId}/`, {
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
                        alert("Failed to delete exercise.");
                    }
                });
        });
    }
});

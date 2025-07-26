document.addEventListener('DOMContentLoaded', function () {
    const deleteBtn = document.getElementById('deleteWorkoutTypeBtn');
    const muscleGroupSelect = document.getElementById('id_muscle_group');

    if (deleteBtn && muscleGroupSelect) {
        deleteBtn.addEventListener('click', () => {
            const selectedId = muscleGroupSelect.value;
            if (!selectedId) return;

            fetch(`/workout/muscle-group/delete/${selectedId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                if (response.ok) {
                    location.reload();
                } else {
                    alert('Failed to delete muscle group.');
                }
            });
        });
    }
});
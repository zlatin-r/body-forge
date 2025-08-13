document.addEventListener('DOMContentLoaded', function () {
    const startExerciseBtn = document.getElementById('startExerciseBtn');
    const exerciseSelect = document.getElementById('exercisesList');

    const workoutPkInput = document.getElementById('workoutPkInput');

    if (startExerciseBtn && exerciseSelect && workoutPkInput) {
        const workoutPk = workoutPkInput.value;

        if (!workoutPk) {
            console.error('Workout PK input found but its value is empty!');
            return;
        }

        startExerciseBtn.addEventListener('click', function () {
            const selectedExerciseId = exerciseSelect.value;

            if (selectedExerciseId) {
                const url = `/workout/${workoutPk}/exercise/${selectedExerciseId}/add-set/`;
                console.log("Navigating to URL:", url);
                window.location.href = url;
            } else {
                alert("Please select an exercise first.");
            }
        });
    } else {
        console.warn('One or more required elements (startExerciseBtn, exercisesList, or workoutPkInput) not found in DOM. Check your HTML IDs and template rendering.');
    }
});
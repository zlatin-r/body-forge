document.addEventListener('DOMContentLoaded', function () {
    const startExerciseBtn = document.getElementById('startExerciseBtn');
    const exerciseSelect = document.getElementById('exercisesList');
    const workoutPk = exerciseSelect ? exerciseSelect.dataset.workoutPk : null;

    if (startExerciseBtn && exerciseSelect) {
        startExerciseBtn.addEventListener('click', function () {
            const selectedExerciseId = exerciseSelect.value;
            if (selectedExerciseId) {
                const url = `/workout/${workoutPk}/exercise/${selectedExerciseId}/add-set/`;
                window.location.href = url;
            } else {
                alert("Please select an exercise first.");
            }
        });
    } else {
        console.warn('startExerciseBtn or exercisesList not found in DOM.');
    }
});

// document.getElementById('startExerciseBtn').addEventListener('click', function () {
//     const select = document.getElementById('exercisesList');
//     const selectedExerciseId = select.value;
//
//     if (selectedExerciseId) {
//         const url = `/workout/exercise/${selectedExerciseId}/add-set`;
//         window.location.href = url;
//     } else {
//         alert("Please select an exercise first.");
//     }
// });
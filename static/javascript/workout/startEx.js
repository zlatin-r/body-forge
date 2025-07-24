document.getElementById('startExerciseBtn').addEventListener('click', function () {
    const select = document.getElementById('exercisesList');
    const selectedExerciseId = select.value;

    if (selectedExerciseId) {
        const url = `/workout/exercise/${selectedExerciseId}/add-set`;
        window.location.href = url;
    } else {
        alert("Please select an exercise first.");
    }
});
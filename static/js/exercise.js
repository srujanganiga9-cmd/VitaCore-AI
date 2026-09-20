// ======================================================
// VitaCore  AI - AI Exercise Detection
// Part 1
// ======================================================

document.addEventListener("DOMContentLoaded", () => {

    console.log("📷 Exercise Detection Loaded");

    // =====================================
    // Elements
    // =====================================

    const startBtn = document.getElementById("startBtn");
    const stopBtn = document.getElementById("stopBtn");
    const resetBtn = document.getElementById("resetBtn");

    const exerciseSelect = document.getElementById("exercise");

    const repCount = document.getElementById("repCount");
    const accuracy = document.getElementById("accuracy");
    const calories = document.getElementById("calories");
    const timer = document.getElementById("timer");

    const sessionExercise = document.getElementById("sessionExercise");
    const sessionReps = document.getElementById("sessionReps");
    const sessionCalories = document.getElementById("sessionCalories");
    const sessionTime = document.getElementById("sessionTime");

    const statusTitle = document.getElementById("statusTitle");
    const statusTips = document.getElementById("statusTips");

    // =====================================
    // Variables
    // =====================================

    let seconds = 0;
    let timerInterval = null;
    let workoutRunning = false;

    // =====================================
    // Timer
    // =====================================

    function updateTimer() {

        seconds++;

        const min = String(Math.floor(seconds / 60)).padStart(2, "0");
        const sec = String(seconds % 60).padStart(2, "0");

        timer.textContent = `${min}:${sec}`;
        sessionTime.textContent = `${min}:${sec}`;

    }

    // =====================================
    // Start Workout
    // =====================================

    startBtn.addEventListener("click", () => {

        if (timerInterval) return;

        fetch("/start_workout");

        sessionExercise.textContent = exerciseSelect.value;

        timerInterval = setInterval(updateTimer, 1000);
        workoutRunning = true;

    });

    // =====================================
    // Stop Workout
    // =====================================

    stopBtn.addEventListener("click", () => {

        fetch("/stop_workout");

        clearInterval(timerInterval);

        timerInterval = null;
        workoutRunning = false;

    });

    // =====================================
    // Reset Workout
    // =====================================

    resetBtn.addEventListener("click", () => {

        clearInterval(timerInterval);

        timerInterval = null;
        workoutRunning = true;

        seconds = 0;

        repCount.textContent = "0";
        accuracy.textContent = "0%";
        calories.textContent = "0 kcal";

        timer.textContent = "00:00";

        sessionReps.textContent = "0";
        sessionCalories.textContent = "0 kcal";
        sessionTime.textContent = "00:00";

        sessionExercise.textContent = exerciseSelect.value;

        fetch("/reset_exercise");

    });

    // =====================================
// Exercise Changed
// =====================================

exerciseSelect.addEventListener("change", () => {

    const newExercise = exerciseSelect.value;

    // Workout is running?
    if (workoutRunning) {

        const confirmSwitch = confirm(

            "⚠ Workout in Progress\n\n" +

            "You are currently doing: " + sessionExercise.textContent + "\n\n" +

            "Switching to: " + newExercise + "\n\n" +

            "This will reset:\n" +
            "• Timer\n" +
            "• Reps\n" +
            "• Calories\n" +
            "• Accuracy\n\n" +

            "Do you want to continue?"

        );

        // User clicked Cancel
        if (!confirmSwitch) {

            exerciseSelect.value = sessionExercise.textContent;

            return;

        }

        // Stop current workout
        clearInterval(timerInterval);
        timerInterval = null;
        workoutRunning = false;

        // Reset timer
        seconds = 0;
        timer.textContent = "00:00";
        sessionTime.textContent = "00:00";

        // Reset stats
        repCount.textContent = "0";
        accuracy.textContent = "0%";
        calories.textContent = "0 kcal";

        sessionReps.textContent = "0";
        sessionCalories.textContent = "0 kcal";

        // Reset backend
        fetch("/reset_exercise");

    }

    // Change exercise
    sessionExercise.textContent = newExercise;

    fetch("/set_exercise/" + encodeURIComponent(newExercise))
        .then(() => fetchExerciseStats());

    // Ready message
    statusTitle.textContent = "✅ Ready to start " + newExercise;

    statusTips.innerHTML = `
        <li>Press Start to begin.</li>
        <li>Stand in the correct position.</li>
    `;

});
    // =====================================
    // Fetch Live Exercise Stats
    // =====================================

    function fetchExerciseStats() {

        fetch("/exercise_stats")

            .then(response => response.json())

            .then(data => {

                // -------------------------
                // Live Stats
                // -------------------------

                repCount.textContent = data.reps;
                accuracy.textContent = data.accuracy + "%";
                calories.textContent = data.calories + " kcal";

                sessionReps.textContent = data.reps;
                sessionCalories.textContent = data.calories + " kcal";

                // -------------------------
                // AI Form Analysis
                // -------------------------

                statusTitle.textContent = data.status;

                statusTips.innerHTML = "";

                if (data.tips && data.tips.length > 0) {

                    data.tips.forEach(tip => {

                        const li = document.createElement("li");

                        li.textContent = tip;

                        statusTips.appendChild(li);

                    });

                } else {

                    statusTips.innerHTML = `
                        <li>Stand in front of the camera.</li>
                        <li>Make sure your body is visible.</li>
                    `;

                }

            })

            .catch(error => {

                console.error(error);

            });

    }

    // Refresh every 500ms

    setInterval(fetchExerciseStats, 500);
        // ==========================================================
    // Workout Summary Modal
    // ==========================================================

    const summaryModal = document.getElementById("summaryModal");

    const summaryExercise = document.getElementById("summaryExercise");
    const summaryReps = document.getElementById("summaryReps");
    const summaryCalories = document.getElementById("summaryCalories");
    const summaryAccuracy = document.getElementById("summaryAccuracy");
    const summaryTime = document.getElementById("summaryTime");
    const summaryDate = document.getElementById("summaryDate");

    const closeSummaryBtn = document.getElementById("closeSummaryBtn");
    const saveWorkoutBtn = document.getElementById("saveWorkoutBtn");

    // =====================================
    // Stop Button → Show Summary
    // =====================================

    stopBtn.addEventListener("click", () => {

        summaryExercise.textContent = exerciseSelect.value;

        summaryReps.textContent = repCount.textContent;

        summaryCalories.textContent = calories.textContent;

        summaryAccuracy.textContent = accuracy.textContent;

        summaryTime.textContent = timer.textContent;

        summaryDate.textContent = new Date().toLocaleDateString();

        summaryModal.style.display = "flex";

    });

    // =====================================
    // Close Summary
    // =====================================

    closeSummaryBtn.addEventListener("click", () => {

        summaryModal.style.display = "none";

    });

    // =====================================
    // Save Workout
    // =====================================

    saveWorkoutBtn.addEventListener("click", () => {

        fetch("/save_workout", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                exercise: summaryExercise.textContent,

                reps: parseInt(summaryReps.textContent),

                calories: parseFloat(
                    summaryCalories.textContent.replace(" kcal", "")
                ),

                accuracy: parseFloat(
                    summaryAccuracy.textContent.replace("%", "")
                ),

                duration: summaryTime.textContent

            })

        })

        .then(response => response.json())

        .then(data => {

            if (data.success) {

                document.getElementById("successPopup").style.display = "flex";

                summaryModal.style.display = "none";

            } else {

                alert("❌ Failed to save workout.");

            }

        })

        .catch(error => {

            console.error(error);

            alert("❌ Error saving workout.");

        });

    });

});
function closePopup() {
    document.getElementById("successPopup").style.display = "none";
}
let cameraOpened = false;

const cameraBtn = document.getElementById("cameraBtn");
const controls = document.getElementById("exerciseControls");

cameraBtn.addEventListener("click", () => {

    cameraOpened = !cameraOpened;

    if (cameraOpened) {

    fetch("/open_camera");

    cameraBtn.innerHTML =
        '<i class="bi bi-camera-video-off-fill"></i> Close Camera';

    cameraBtn.classList.remove("btn-success");
    cameraBtn.classList.add("btn-danger");

    controls.style.display = "inline-block";

    cameraFeed.src = "/video_feed";

    cameraFeed.style.display = "block";

    cameraPlaceholder.style.display = "none";

} else {

    fetch("/close_camera");

    cameraBtn.innerHTML =
        '<i class="bi bi-camera-video-fill"></i> Open Camera';

    cameraBtn.classList.remove("btn-danger");
    cameraBtn.classList.add("btn-success");

    controls.style.display = "none";

    cameraFeed.removeAttribute("src");

    cameraFeed.style.display = "none";

    cameraPlaceholder.style.display = "flex";

}

});
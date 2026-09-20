// ==========================================
// VitaCore  AI Workout Page
// ==========================================

document.addEventListener("DOMContentLoaded", () => {

    console.log("Workout Page Loaded ✅");

    // ======================================
    // Animate Workout Cards
    // ======================================

    const cards = document.querySelectorAll(".workout-card");

    cards.forEach((card, index) => {

        card.style.opacity = "0";

        card.style.transform = "translateY(20px)";

        setTimeout(() => {

            card.style.transition = "0.5s ease";

            card.style.opacity = "1";

            card.style.transform = "translateY(0)";

        }, index * 120);

    });

    // ======================================
    // Complete Workout Button
    // ======================================

    const completeButton = document.querySelector(".bottom-buttons .btn");

    if (completeButton) {

        completeButton.addEventListener("click", () => {

            completeButton.innerHTML =
                '<i class="bi bi-check-circle-fill"></i> Workout Completed';

            completeButton.classList.remove("btn-success");

            completeButton.classList.add("btn-primary");

        });

    }

});
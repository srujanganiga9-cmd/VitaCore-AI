// ==========================================
//  VitaCore  AI - AI Diet Planner
// ==========================================

document.addEventListener("DOMContentLoaded", () => {

    console.log("🥗 AI Diet Planner Loaded");

    // ======================================
    // Fade In Animation
    // ======================================

    const summaryCards = document.querySelectorAll(".summary-item");
    const dietCard = document.querySelector(".diet-card");

    summaryCards.forEach((card, index) => {

        card.style.opacity = "0";
        card.style.transform = "translateY(20px)";

        setTimeout(() => {

            card.style.transition = "0.5s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";

        }, index * 150);

    });

    if (dietCard) {

        dietCard.style.opacity = "0";
        dietCard.style.transform = "translateY(25px)";

        setTimeout(() => {

            dietCard.style.transition = "0.6s ease";
            dietCard.style.opacity = "1";
            dietCard.style.transform = "translateY(0)";

        }, 500);

    }

    // ======================================
    // Generate New Plan Button
    // ======================================

    const generateBtn = document.querySelector(".btn-success");

    if (generateBtn) {

        generateBtn.addEventListener("click", () => {

            generateBtn.disabled = true;

            generateBtn.innerHTML = `
                <span class="spinner-border spinner-border-sm me-2"></span>
                Generating AI Diet...
            `;

        });

    }

    // ======================================
    // Auto Scroll To Diet Plan
    // ======================================

    if (dietCard) {

        setTimeout(() => {

            dietCard.scrollIntoView({

                behavior: "smooth",
                block: "start"

            });

        }, 300);

    }

});
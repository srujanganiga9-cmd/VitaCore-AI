// =======================================================
//  VitaCore  AI - AI Chatbot
// =======================================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("🤖 AI Chatbot Loaded");

    // =====================================
    // Animate Chat Messages
    // =====================================

    const messages = document.querySelectorAll(".chat-message");

    messages.forEach((message, index) => {

        message.style.opacity = "0";
        message.style.transform = "translateY(20px)";

        setTimeout(() => {

            message.style.transition = "0.5s ease";

            message.style.opacity = "1";

            message.style.transform = "translateY(0)";

        }, index * 200);

    });

    // =====================================
    // Ask AI Button Animation
    // =====================================

    const form = document.getElementById("chat-form");
    const askBtn = document.getElementById("askBtn");

    if (form && askBtn) {

        form.addEventListener("submit", function () {

            askBtn.disabled = true;

            askBtn.innerHTML = `
                <span class="spinner-border spinner-border-sm me-2"></span>
                Thinking...
            `;

        });

    }

    // =====================================
    // Press Enter to Send
    // Shift + Enter = New Line
    // =====================================

    const textarea = document.getElementById("question");

    if (textarea) {

        textarea.addEventListener("keydown", function (e) {

            if (e.key === "Enter" && !e.shiftKey) {

                e.preventDefault();

                form.requestSubmit();

            }

        });

    }

    // =====================================
    // Auto Scroll to AI Response
    // =====================================

    const response = document.querySelector(".response");

    if (response) {

        setTimeout(() => {

            response.scrollIntoView({

                behavior: "smooth",

                block: "start"

            });

        }, 300);

    }

    // =====================================
    // Auto Focus
    // =====================================

    if (textarea) {

        textarea.focus();

    }

});
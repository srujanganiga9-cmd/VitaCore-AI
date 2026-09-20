// ==========================================
//  VitaCore  AI - Login Page JavaScript
// ==========================================

// -----------------------------
// Password Show / Hide
// -----------------------------

function togglePassword() {

    const password = document.getElementById("password");
    const eyeIcon = document.getElementById("eyeIcon");

    if (password.type === "password") {

        // Show password
        password.type = "text";

        eyeIcon.classList.remove("bi-eye-slash-fill");
        eyeIcon.classList.add("bi-eye-fill");

    } else {

        // Hide password
        password.type = "password";

        eyeIcon.classList.remove("bi-eye-fill");
        eyeIcon.classList.add("bi-eye-slash-fill");

    }

}

// -----------------------------
// Fade Animation
// -----------------------------

window.addEventListener("load", () => {

    document.body.classList.add("loaded");

});

// -----------------------------
// Input Focus Animation
// -----------------------------

const inputs = document.querySelectorAll(".input-box input");

inputs.forEach(input => {

    input.addEventListener("focus", function () {

        this.parentElement.classList.add("active");

    });

    input.addEventListener("blur", function () {

        if (this.value === "") {

            this.parentElement.classList.remove("active");

        }

    });

});

// -----------------------------
// Login Button Animation
// -----------------------------

const loginBtn = document.querySelector(".login-btn");

if (loginBtn) {

    loginBtn.addEventListener("click", function () {

        this.innerHTML = `
            <span class="spinner-border spinner-border-sm me-2"></span>
            Logging In...
        `;

    });

}

// -----------------------------
// Floating Animation
// -----------------------------

const features = document.querySelectorAll(".feature");

features.forEach((feature, index) => {

    feature.style.animationDelay = `${index * 0.2}s`;

});

const card = document.querySelector(".login-card");

if (card) {

    card.addEventListener("mouseenter", () => {

        card.style.boxShadow =
            "0 30px 70px rgba(0,0,0,.45), 0 0 40px rgba(31,162,255,.25)";

    });

    card.addEventListener("mouseleave", () => {

        card.style.boxShadow =
            "0 25px 60px rgba(0,0,0,.45), 0 0 40px rgba(31,162,255,.12)";

    });

}

// -----------------------------
// Hero Fade In
// -----------------------------

const hero = document.querySelector(".hero-content");

if (hero) {

    hero.animate(

        [
            {
                opacity: 0,
                transform: "translateY(40px)"
            },

            {
                opacity: 1,
                transform: "translateY(0)"
            }

        ],

        {
            duration: 1200,
            easing: "ease-out"
        }

    );

}
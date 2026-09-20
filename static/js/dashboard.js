// ==========================================
//  VitaCore  AI Dashboard JavaScript
// ==========================================

document.addEventListener("DOMContentLoaded", () => {

    // ==========================
    // LIVE CLOCK
    // ==========================

    function updateClock() {

        const now = new Date();

        const options = {
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
            hour12: true
        };

        const clock = document.getElementById("clock");

        if (clock) {
            clock.textContent = now.toLocaleTimeString([], options);
        }

    }

    updateClock();

    setInterval(updateClock, 1000);

    // ==========================
    // DARK / LIGHT MODE
    // ==========================

    const themeButton = document.getElementById("theme-toggle");

    const body = document.body;

    if(localStorage.getItem("theme")==="light"){

        body.classList.add("light");

        if(themeButton){

            themeButton.innerHTML='<i class="bi bi-sun-fill"></i>';

        }

    }

    if(themeButton){

        themeButton.addEventListener("click",()=>{

            body.classList.toggle("light");

            if(body.classList.contains("light")){

                localStorage.setItem("theme","light");

                themeButton.innerHTML='<i class="bi bi-sun-fill"></i>';

            }

            else{

                localStorage.setItem("theme","dark");

                themeButton.innerHTML='<i class="bi bi-moon-fill"></i>';

            }

        });

    }

    // ==========================
    // CARD HOVER EFFECT
    // ==========================

    const cards = document.querySelectorAll(".stat-card, .dashboard-card");

    cards.forEach(card=>{

        card.addEventListener("mouseenter",()=>{

            card.style.transition="0.3s";

        });

    });

    // ==========================
    // PROFILE MODAL
    // ==========================

    const profileCard = document.getElementById("profile-card");
    const profileModal = document.getElementById("profile-modal");
    const closeProfile = document.getElementById("close-profile");

    if(profileCard && profileModal){

        profileCard.addEventListener("click",()=>{

            profileModal.classList.add("active");

        });

    }

    if(closeProfile && profileModal){

        closeProfile.addEventListener("click",()=>{

            profileModal.classList.remove("active");

        });

    }

    window.addEventListener("click",(e)=>{

        if(e.target===profileModal){

            profileModal.classList.remove("active");

        }

    });

});

// ==========================
// SIDEBAR TOGGLE
// ==========================

const menuBtn = document.getElementById("menu-btn");
const closeBtn = document.getElementById("close-sidebar");
const sidebar = document.getElementById("sidebar");
const overlay = document.getElementById("overlay");

if(menuBtn && sidebar && overlay){

    menuBtn.addEventListener("click",()=>{

        sidebar.classList.add("active");

        overlay.classList.add("active");

    });

}

if(closeBtn && sidebar && overlay){

    closeBtn.addEventListener("click",()=>{

        sidebar.classList.remove("active");

        overlay.classList.remove("active");

    });

}

if(overlay && sidebar){

    overlay.addEventListener("click",()=>{

        sidebar.classList.remove("active");

        overlay.classList.remove("active");

    });

}
function closeSidebar() {
    const sidebar = document.getElementById("sidebar");

    if (sidebar) {
        sidebar.classList.remove("active");
    }
}
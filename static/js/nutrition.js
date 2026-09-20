const searchBox = document.getElementById("foodSearch");
const suggestions = document.getElementById("suggestions");
const result = document.getElementById("nutritionResult");

searchBox.addEventListener("input", async () => {

    const query = searchBox.value.trim();

    if (query.length < 1) {
        suggestions.innerHTML = "";
        return;
    }

    const response = await fetch(`/search_food?q=${query}`);
    const foods = await response.json();

    suggestions.innerHTML = "";

    foods.forEach(food => {

        const div = document.createElement("div");

        div.className = "suggestion-item";

        div.innerText = food;

        div.onclick = () => loadFood(food);

        suggestions.appendChild(div);

    });

});

async function loadFood(food) {

    suggestions.innerHTML = "";

    searchBox.value = food;

    const response = await fetch(
        `/food_details?food=${encodeURIComponent(food)}`
    );

    const data = await response.json();

    if (!data) {

        result.innerHTML = `
            <div class="nutrition-info">
                <h3>Food not found</h3>
            </div>
        `;

        return;

    }

    let quantity = 100;

    const original = {

        calories: Number(data.calories),
        protein: Number(data.protein_g),
        carbs: Number(data.carbs_g),
        fat: Number(data.fat_g),
        fiber: Number(data.fiber_g),
        sugar: Number(data.sugar_g),
        sodium: Number(data.sodium_mg),
        calcium: Number(data.calcium_mg),
        iron: Number(data.iron_mg),
        vitamin_c: Number(data.vitamin_c_mg)

    };

    result.innerHTML = `

<div class="nutrition-info">

<h2> ${data.food_name}</h2>

<div class="quantity-section">

    <h3>Quantity</h3>

    <div class="quick-buttons">

        <button class="gram-btn active" data-value="50">50 g</button>

        <button class="gram-btn" data-value="100">100 g</button>

        <button class="gram-btn" data-value="150">150 g</button>

        <button class="gram-btn" data-value="200">200 g</button>

    </div>

    <div class="custom-box">

        <label>Custom Quantity (g)</label>

        <input
            type="number"
            id="customQty"
            placeholder="Example: 175"
            min="1">

    </div>

</div>
</div>
<div class="meal-section">

    <h3>Select Meal</h3>

    <div class="meal-options">

        <button class="meal-btn active"
                data-meal="Breakfast">

            🍳 Breakfast

        </button>

        <button class="meal-btn"
                data-meal="Lunch">

            🍛 Lunch

        </button>

        <button class="meal-btn"
                data-meal="Dinner">

            🍽 Dinner

        </button>

        <button class="meal-btn"
                data-meal="Snacks">

            🥪 Snacks

        </button>

    </div>

</div>

<div class="nutrition-grid">

<div>

<strong>⚖️ Serving Size</strong>

<br>

<span id="servingSize">${data.serving_size}</span>
<small>gm</small>

</div>

<div>

<strong>🔥 Calories</strong>

<br>

<span id="calories">${data.calories}</span>
<small>kcal</small>

</div>

<div>

<strong>🍗 Protein</strong>

<br>

<span id="protein">${data.protein_g}</span>
<small>gm</small>

</div>

<div>

<strong>🍚 Carbohydrates</strong>

<br>

<span id="carbs">${data.carbs_g}</span>
<small>gm</small>

</div>

<div>

<strong>🥑 Fat</strong>

<br>

<span id="fat">${data.fat_g}</span>
<small>g</small>

</div>

<div>

<strong>🌾 Fiber</strong>

<br>

<span id="fiber">${data.fiber_g}</span>
<small>g</small>

</div>

<div>

<strong>🍬 Sugar</strong>

<br>

<span id="sugar">${data.sugar_g}</span> 
<small>g</small>

</div>

<div>

<strong>🧂 Sodium</strong>

<br>

<span id="sodium">${data.sodium_mg}</span>
<small>mg</small>

</div>

<div>

<strong>🥛 Calcium</strong>

<br>

<span id="calcium">${data.calcium_mg}</span> 
<small>mg</small>

</div>

<div>

<strong>🩸 Iron</strong>

<br>

<span id="iron">${data.iron_mg}</span> 
<small>mg</small>

</div>

<div>

<strong>🍊 Vitamin C</strong>

<br>

<span id="vitamin">${data.vitamin_c_mg}</span> 
<small>mg</small>

</div>

<div>

<strong>📂 Category</strong>

<br>

${data.food_category}

</div>

</div>

<button class="add-btn" id="addIntakeBtn">

Add To Today's Intake

</button>

</div>

`;
// -----------------------------
// Meal Selection
// -----------------------------

let selectedMeal = "Breakfast";

document.querySelectorAll(".meal-btn").forEach(button => {

    button.addEventListener("click", () => {

        document.querySelectorAll(".meal-btn").forEach(btn =>
            btn.classList.remove("active")
        );

        button.classList.add("active");

        selectedMeal = button.dataset.meal;

    });

});

    // Part 2 will add all button functionality here

// -----------------------------
// Update Nutrition Values
// -----------------------------
function updateNutrition() {

    const factor = quantity / 100;
    document.getElementById("servingSize").innerText = quantity;

    document.getElementById("calories").innerText =
        (original.calories * factor).toFixed(1);

    document.getElementById("protein").innerText =
        (original.protein * factor).toFixed(1);

    document.getElementById("carbs").innerText =
        (original.carbs * factor).toFixed(1);

    document.getElementById("fat").innerText =
        (original.fat * factor).toFixed(1);

    document.getElementById("fiber").innerText =
        (original.fiber * factor).toFixed(1);

    document.getElementById("sugar").innerText =
        (original.sugar * factor).toFixed(1);

    document.getElementById("sodium").innerText =
        (original.sodium * factor).toFixed(1);

    document.getElementById("calcium").innerText =
        (original.calcium * factor).toFixed(1);

    document.getElementById("iron").innerText =
        (original.iron * factor).toFixed(1);

    document.getElementById("vitamin").innerText =
        (original.vitamin_c * factor).toFixed(1);
}


// -----------------------------
// Quick Buttons
// -----------------------------
document.querySelectorAll(".gram-btn").forEach(button => {

    button.addEventListener("click", () => {

        quantity = parseInt(button.dataset.value);

        document.getElementById("customQty").value = "";

        document.querySelectorAll(".gram-btn").forEach(btn =>
            btn.classList.remove("active")
        );

        button.classList.add("active");

        updateNutrition();

    });

});

// -----------------------------
// Custom Quantity
// -----------------------------
document.getElementById("customQty").addEventListener("input", function () {

    if (this.value === "") return;

    quantity = parseInt(this.value);

    if (quantity < 1)
        quantity = 1;

    document.querySelectorAll(".gram-btn").forEach(btn =>
        btn.classList.remove("active")
    );

    updateNutrition();

});

// Initial Update
updateNutrition();
// -----------------------------
// Add To Today's Intake
// -----------------------------

document
.getElementById("addIntakeBtn")
.addEventListener("click", async () => {

    const payload = {

    meal: selectedMeal,

    food_name: data.food_name,

    quantity: quantity,

    calories: Number(document.getElementById("calories").innerText),

    protein: Number(document.getElementById("protein").innerText),

    carbs: Number(document.getElementById("carbs").innerText),

    fat: Number(document.getElementById("fat").innerText)

};

    const response = await fetch("/add_food", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(payload)

    });

    const responseData = await response.json();

    if(responseData.success){

    showToast(
        data.food_name,
        quantity
    );

}
    else{

        alert("❌ Failed to add food");

    }

});
}
function showToast(food, quantity){

    const toast = document.getElementById("toast");

    toast.innerHTML = `
        <div class="toast-icon">
            🎉
        </div>

        <h3>Added Successfully</h3>

        <div class="toast-food">
            🍌 ${food}
        </div>

        <div class="toast-qty">
            ${quantity} g
        </div>

        <div class="toast-success">
            <i class="bi bi-check-circle-fill"></i>
            Added to Today's Intake
        </div>
    `;

    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 2200);

}
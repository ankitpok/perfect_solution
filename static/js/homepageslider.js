let slider = document.querySelector(".slider .list");
let items = document.querySelectorAll(".slider .list .item");
let next = document.getElementById("next");
let prev = document.getElementById("prev");
let dots = document.querySelectorAll(".slider .dots li");

let lengthItems = items.length - 1;
let active = 0;

next.onclick = function () {
    active = active + 1 <= lengthItems ? active + 1 : 0;
    reloadSlider();
};
prev.onclick = function () {
    active = active - 1 >= 0 ? active - 1 : lengthItems;
    reloadSlider();
};

// Auto-slide every 3 seconds
let refreshInterval = setInterval(() => {
    next.click();
}, 3000);

function reloadSlider() {
    // Shift slider by 100vw per active item
    slider.style.transform = `translateX(-${active * 100}vw)`;

    // Update active dot
    let last_active_dot = document.querySelector(".slider .dots li.active");
    last_active_dot.classList.remove("active");
    dots[active].classList.add("active");

    // Reset interval for auto-sliding
    clearInterval(refreshInterval);
    refreshInterval = setInterval(() => {
        next.click();
    }, 3000);
}

// Dots navigation
dots.forEach((li, key) => {
    li.addEventListener("click", () => {
        active = key;
        reloadSlider();
    });
});

// Resize event to handle window resize
window.onresize = function () {
    reloadSlider();
};

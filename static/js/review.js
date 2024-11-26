const optionsBtns = document.querySelectorAll('.options-btn');

optionsBtns.forEach(btn => {
    btn.addEventListener('click', function () {
        this.classList.toggle('open'); // Toggles the 'open' class on the clicked button
    });
});
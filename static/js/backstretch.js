

$(document).ready(function () {
    $('.hero-slide').backstretch([
        "{% static 'images/slideshow/white-wall-living-room-have-sofa-decoration-3d-rendering.jpg' %}",
        "{% static 'images/slideshow/interior-wall-mockup-with-sofa-cabinet-living-room-with-empty-white-wall-background-3d-rendering.jpg' %}",
        "{% static 'images/slideshow/wood-sideboard-living-room-interior-with-copy-space.jpg' %}"
    ], { duration: 2000, fade: 750 });
});

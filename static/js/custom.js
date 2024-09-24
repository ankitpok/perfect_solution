(function ($) {

  "use strict";


  $('.hero-slide').backstretch([
    "{% static 'static/images/slideshow/white-wall-living-room-have-sofa-decoration-3d-rendering.jpg' %}",
    "{% static 'static/images/slideshow/interior-wall-mockup-with-sofa-cabinet-living-room-with-empty-white-wall-background-3d-rendering.jpg' %}",
    "static/images/slideshow/wood-sideboard-living-room-interior-with-copy-space.jpg"
  ], { duration: 2000, fade: 750 });


  // REVIEWS CAROUSEL
  $('.reviews-carousel').owlCarousel({
    items: 3,
    loop: true,
    dots: false,
    nav: true,
    autoplay: true,
    margin: 30,
    responsive: {
      0: {
        items: 1
      },
      600: {
        items: 2
      },
      1000: {
        items: 3
      }
    }
  })

  // CUSTOM LINK
  $('.smoothscroll').click(function () {
    var el = $(this).attr('href');
    var elWrapped = $(el);
    var header_height = $('.navbar').height();

    scrollToDiv(elWrapped, header_height);
    return false;

    function scrollToDiv(element, navheight) {
      var offset = element.offset();
      var offsetTop = offset.top;
      var totalScroll = offsetTop - navheight;

      $('body,html').animate({
        scrollTop: totalScroll
      }, 300);
    }
  });

})(window.jQuery);


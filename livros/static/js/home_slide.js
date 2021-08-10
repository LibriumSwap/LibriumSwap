const swiper = new Swiper('.swiper-container', {
  // Optional parameters
  slidesPerView: 4,
  spaceBetween: 10,
  autoHeight: true,
  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  //Responsive breakpoints
  breakpoints: {
    // when window width is >= 320px
    426: {
      slidesPerView: 2,
    },
    // when window width is >= 480px
    833: {
      slidesPerView: 3,
    },
    // when window width is >= 640px
    1121: {
      slidesPerView: 4,
    },
    1400: {
      slidesPerView: 5,
    }
  }
});
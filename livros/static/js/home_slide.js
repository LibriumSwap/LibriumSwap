const swiper = new Swiper('.swiper-container', {
  // Optional parameters
  spaceBetween: 10,
  slidesPerView: 3,
  autoHeight: true,
  freeMode: true,

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  // Responsive breakpoints
  breakpoints: {
    416: {
      slidesPerView: 4
    },
    518: {
      slidesPerView: 5,
    },
    520: {
      slidesPerView: 3,
    },
    690: {
      slidesPerView: 4,
    },
    876: {
      slidesPerView: 5,
    },
    1052: {
      slidesPerView: 4,
    },
    1317: {
      slidesPerView: 5,
    },
    1610: {
      slidesPerView: 6,
    }
  }
});
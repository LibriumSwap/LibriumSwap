const swiper = new Swiper('.swiper-container', {
  // Optional parameters
  slidesPerView: 3,
  spaceBetween: 10,
  autoHeight: true,
  freeMode: true,
  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
  },

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
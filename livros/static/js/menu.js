document.addEventListener('DOMContentLoaded', function () {
  const menuBtn = document.querySelector('.menu-btn');
  let menuOpen = false;
  menuBtn.addEventListener('click', () => {
    if(!menuOpen) {
      menuBtn.classList.add('open');
      menuOpen = true;
    } else {
      menuBtn.classList.remove('open');
      menuOpen = false;
    }
    dropdown = document.querySelector('.dropdown-usuario-mobile')
    if (dropdown.style.display == 'grid') {
      dropdown.style.display = 'none'
    } else {
      dropdown.style.display = 'grid'
    }
  });
})
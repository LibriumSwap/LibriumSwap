document.addEventListener('DOMContentLoaded', function () {
  responsiveMenu()
  dropdownGeneros()
  dropdownCategorias()
  menuGeneros()
  menuCategorias()
  voltarMenu()
})

function responsiveMenu () {
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
    dropdownGenerosMobile = document.querySelector('.dropdown-generos-mobile')
    dropdownCategoriasMobile = document.querySelector('.dropdown-categorias-mobile')

    if (dropdown.style.display == 'grid') {
      dropdown.style.display = 'none'
    } else {
      if ( dropdownGenerosMobile.style.display == 'grid' || dropdownCategoriasMobile.style.display == 'grid') {
         dropdownGenerosMobile.style.display = 'none'
         dropdownCategoriasMobile.style.display = 'none'
       } else{
         dropdown.style.display = 'grid'
       }
    }
  });
}

function dropdownGeneros () {
  const generos = document.querySelector('.div-dropdown-generos');
  dropdownGeneros = document.querySelector('.dropdown-generos');

  generos.addEventListener('mouseover', () => {
    dropdownGeneros.style.display = 'grid'
  })

  generos.addEventListener('mouseleave', () => {
    dropdownGeneros.style.display = 'none'
  })
}

function dropdownCategorias () {
  const categorias = document.querySelector('.div-dropdown-categorias');
  dropdownCategorias = document.querySelector('.dropdown-categorias');

  categorias.addEventListener('mouseover', () => {
    dropdownCategorias.style.display = 'grid'
  })

  categorias.addEventListener('mouseleave', () => {
    dropdownCategorias.style.display = 'none'
  })
}

function menuGeneros () {
  const btnGeneros = document.querySelector('#btn-generos')
  dropdownGenerosMobile = document.querySelector('.dropdown-generos-mobile')
  dropdownUsuarioMobile = document.querySelector('.dropdown-usuario-mobile')


  btnGeneros.addEventListener('click', () => {
    dropdownGenerosMobile.style.display = 'grid'
    dropdownUsuarioMobile.style.display = 'none'
  })
}

function menuCategorias () {
  const btnCategorias = document.querySelector('#btn-categorias')
  dropdownCategoriasMobile = document.querySelector('.dropdown-categorias-mobile')
  dropdownUsuarioMobile = document.querySelector('.dropdown-usuario-mobile')


  btnCategorias.addEventListener('click', () => {
    dropdownCategoriasMobile.style.display = 'grid'
    dropdownUsuarioMobile.style.display = 'none'
  })
}

function voltarMenu () {
  const btnVoltar = document.querySelectorAll('#dropdown-voltar')

  dropdownUsuarioMobile = document.querySelector('.dropdown-usuario-mobile')
  dropdownGenerosMobile = document.querySelector('.dropdown-generos-mobile')
  dropdownCategoriasMobile = document.querySelector('.dropdown-categorias-mobile')

  btnVoltar.forEach(btnVoltar => {
    btnVoltar.addEventListener('click', () => {
      dropdownGenerosMobile.style.display = 'none'
      dropdownCategoriasMobile.style.display = 'none'
      dropdownUsuarioMobile.style.display = 'grid'
    })
  })
}
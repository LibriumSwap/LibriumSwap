btnFavorito = document.querySelector('.bi-heart')

btnFavorito.addEventListener('mouseover', () => {
	btnFavorito.classList.remove('bi-heart')
	btnFavorito.classList.add('bi-heart-fill')
})

btnFavorito.addEventListener('mouseout', () => {
	btnFavorito.classList.remove('bi-heart-fill')
	btnFavorito.classList.add('bi-heart')
})
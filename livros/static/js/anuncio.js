btnFavorito = document.querySelector('#favorito')

btnFavorito.addEventListener('click', () => {
	csrf = document.getElementsByName('csrfmiddlewaretoken')

	fetch(`/livro/favorito/`, {
		method: 'POST',
		headers: {"X-CSRFToken": csrf[0].value},
		body: JSON.stringify({
			id: btnFavorito.dataset.id,
		})
	})
	.then(response => response.json())
	.then(result => {
		console.log(result)
		if (result.success == 'adicionado') {
			btnFavorito.classList.remove('bi-heart')
			btnFavorito.classList.add('bi-heart-fill')
		}

		if (result.success == 'removido') {
			btnFavorito.classList.remove('bi-heart-fill')
			btnFavorito.classList.add('bi-heart')
		}
	})
})
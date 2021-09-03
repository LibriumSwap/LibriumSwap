document.addEventListener("DOMContentLoaded", () => {
	favoritar()
	adicionarAoCarrinho()
})

function favoritar () {
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

			if (result.error == 'login') {
				window.location.href = "/login/"
			}
		})
	})
}

function adicionarAoCarrinho () {
	btnAdicionarAoCarrinho = document.querySelector('.btn-carrinho')

	btnAdicionarAoCarrinho.onclick = function () {
		id = document.querySelector('h2').dataset.id
		csrf = document.getElementsByName('csrfmiddlewaretoken')

		fetch(`/carrinho/adicionar/`, {
			method: 'POST',
			headers: {"X-CSRFToken": csrf[0].value},
			body: JSON.stringify({
				anuncio_id: id,
			})
		})
		.then(response => response.json())
		.then(result => {
			if (result.error == 'login') {
				window.location.href = "/login/"
			}
		})
	}
}
document.addEventListener("DOMContentLoaded", () => {
	favoritar()
	adicionarAoCarrinho()
})

function favoritar () {
	btnFavorito = document.querySelector('#favorito')

	btnFavorito.addEventListener('click', (event) => {
		event.preventDefault();
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
			if (result.success == "adicionado") {
				btnFavorito.checked = true
			}

			if (result.success == "removido") {
				btnFavorito.checked = false
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
			} else if (result.error == 'cheio') {
				btnAdicionarAoCarrinho.querySelector('span').innerText = "Carrinho cheio "
				btnAdicionarAoCarrinho.querySelector('.bi-x-circle-fill').style.display = "inline-block"
			} else if (result.error == 'adicionado') {
				btnAdicionarAoCarrinho.querySelector('span').innerText = "Já adicionado "
				btnAdicionarAoCarrinho.querySelector('.bi-check-circle-fill').style.display = "inline-block"
			} else {
				btnAdicionarAoCarrinho.querySelector('span').innerText = "Adicionado "
				btnAdicionarAoCarrinho.querySelector('.bi-check-circle-fill').style.display = "inline-block"
			}
		})
	}
}
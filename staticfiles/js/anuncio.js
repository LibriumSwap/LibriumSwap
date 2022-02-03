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
			} else {
				btnAdicionarAoCarrinho.querySelector('span').innerText = "Adicionado "
				btnAdicionarAoCarrinho.querySelector('i').style.display = "inline-block"
			}
		})
	}
}
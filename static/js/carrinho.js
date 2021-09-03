document.addEventListener('DOMContentLoaded', function () {
	removerDoCarrinho()
})

function removerDoCarrinho () {
	btnsRemover = document.querySelectorAll('.remover')

	btnsRemover.forEach(btnRemover => {
		btnRemover.onclick = () => {
		csrf = document.getElementsByName('csrfmiddlewaretoken')

		fetch(`/carrinho/remover/`, {
			method: 'POST',
			headers: {"X-CSRFToken": csrf[0].value},
			body: JSON.stringify({
				anuncio_id: btnRemover.dataset.id,
			})
		})
		.then(response => response.json())
		.then(result => {
			if (result.success) {
				anuncio = document.querySelector(`.anuncio${btnRemover.dataset.id}`)

				anuncio.remove()
			}
		})
	}
	})
}
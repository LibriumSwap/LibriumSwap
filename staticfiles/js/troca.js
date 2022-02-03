document.addEventListener('DOMContentLoaded', () => {
	resultado()
})

function resultado () {
	btnAceitar = document.querySelector('.aceitar')
	btnRecusar = document.querySelector('.recusar')

	btnAceitar.addEventListener('click', () => {
		csrf = document.getElementsByName('csrfmiddlewaretoken')

		fetch(`/trade/accept`, {
			method: 'POST',
			headers: {"X-CSRFToken": csrf[0].value},
			body: JSON.stringify({
				troca_id: btnAceitar.dataset.id,
			})
		})
		.then(response => response.json())
		.then(result => {
			if (result.success) {
				btnAceitar.style.display = "none"
				btnRecusar.style.display = "none"

				troca_aceita = document.createElement('p')
				troca_aceita.classList.add('troca-aceita')
				troca_aceita.innerText = 'Troca aceita'

				document.querySelector('.troca-resultado').appendChild(troca_aceita)
			}
		})
	})

	btnRecusar.addEventListener('click', () => {
		csrf = document.getElementsByName('csrfmiddlewaretoken')

		fetch(`/trade/refuse`, {
			method: 'POST',
			headers: {"X-CSRFToken": csrf[0].value},
			body: JSON.stringify({
				troca_id: btnRecusar.dataset.id,
			})
		})
		.then(response => response.json())
		.then(result => {
			if (result.success) {
				btnAceitar.style.display = "none"
				btnRecusar.style.display = "none"

				troca_recusada = document.createElement('p')
				troca_recusada.classList.add('troca-recusada')
				troca_recusada.innerText = 'Troca recusada'

				document.querySelector('.troca-resultado').appendChild(troca_recusada)
			}
		})
	})
}
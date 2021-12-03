document.addEventListener('DOMContentLoaded', () => {
	resultado()
})

function resultado () {
	btnAceitar = document.querySelector('.aceitar')
	btnAceitar.addEventListener('click', () => {
		console.log('aceito')
	})
}
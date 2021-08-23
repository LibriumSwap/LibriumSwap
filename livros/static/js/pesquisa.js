document.addEventListener('DOMContentLoaded', () => {
	categoriaFiltro()
})

function categoriaFiltro () {
	categoriaBtns = document.querySelectorAll('.btn-categoria')

	categoriaBtns.forEach(categoriaBtn => {
		categoriaBtn.onclick = function () {
			pesquisa = window.location.search;
			parametro_q = new URLSearchParams(pesquisa)

			parametro_q = parametro_q.get('q')
			categoria = categoriaBtn.innerText.toLowerCase()

			window.location.href = `/livro/pesquisa/?q=${parametro_q}&categoria=${categoria}`
		}
	})
}
document.addEventListener('DOMContentLoaded', () => {
	categoriaFiltro()
	ordenarDropdown()
	ordenar()
})

function categoriaFiltro () {
	categoriaBtns = document.querySelectorAll('.btn-categoria')

	categoriaBtns.forEach(categoriaBtn => {
		categoriaBtn.onclick = function () {
			pesquisa = window.location.search;
			parametros = new URLSearchParams(pesquisa)

			parametro_q = parametros.get('q')
			categoria = categoriaBtn.innerText.toLowerCase()

			window.location.href = `/livro/pesquisa/?q=${parametro_q}&categoria=${categoria}`
		}
	})
}

function ordenarDropdown () {
	ordenarBtn = document.querySelector('.btn-ordenar')

	ordenarBtn.onclick = function () {
		dropdown = document.querySelector('.dropdown-ordenar')
		if (dropdown.style.display == 'none') {
			dropdown.style.display = 'block'
		} else {
			dropdown.style.display = 'none'
		}
	}
}

function ordenar () {
	btnsOrder = document.querySelectorAll('.btn-order')

	btnsOrder.forEach(btnOrder => {
		btnOrder.onclick = function () {
			pesquisa = window.location.search;
			parametros = new URLSearchParams(pesquisa)
			parametros = parametros.entries()

			string = '?'
			
			for (parametro of parametros) {
				if (parametro[0] != "order") {
					string += (`${parametro[0]}=${parametro[1]}&`)
				}
			}

			if (btnOrder.dataset.order) {
				string += `order=${btnOrder.dataset.order}`
			}

			window.location.href = `/livro/pesquisa/${string}`
		}
	})
}
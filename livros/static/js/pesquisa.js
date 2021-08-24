document.addEventListener('DOMContentLoaded', () => {
	categoriaFiltro()
	ordenarDropdown()
	ordenar()
	precoFiltro()
	generoFiltro()
	filtrarMobile()
	ordenarMobile()
})

function urlParametros (parametro_string) {
	string = '?'
	pesquisa = window.location.search;
	parametros = new URLSearchParams(pesquisa)
			
	for (parametro of parametros) {
		if (parametro[0] != parametro_string) {
			string += (`${parametro[0]}=${parametro[1]}&`)
		}
	}

	return string
}

function categoriaFiltro () {
	categoriaBtns = document.querySelectorAll('.btn-categoria')

	categoriaBtns.forEach(categoriaBtn => {
		categoriaBtn.onclick = function () {
			pesquisa = window.location.search;
			parametros = new URLSearchParams(pesquisa)

			parametro_q = parametros.get('q')
			categoria = categoriaBtn.innerText.toLowerCase()

			string = urlParametros('categoria')

			string += `categoria=${categoria}`

			window.location.href = string
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

			string = urlParametros('order')

			if (btnOrder.dataset.order) {
				string += `order=${btnOrder.dataset.order}`
			}

			window.location.href = `/livro/pesquisa/${string}`
		}
	})
}

function precoFiltro () {
	btnFiltroPreco = document.querySelector('.filtro-preco')

	btnFiltroPreco.onclick = function () {
		min = document.getElementsByName('preco-min')[0]
		max = document.getElementsByName('preco-max')[0]

		string = urlParametros('preco_min')
		string = urlParametros('preco_max')

		if (min.value) {
			string += `preco_min=${min.value}`
		}

		if (max.value) {
			string += `preco_max=${max.value}`
		}

		window.location.href = `/livro/pesquisa/${string}`
	}
}

function generoFiltro () {
	generos = document.querySelectorAll('.filtro-genero')

	generos.forEach(genero => {
		genero.onclick = function () {
			string = urlParametros('genero')

			string += `genero=${genero.innerText.toLowerCase()}`

			window.location.href = `/livro/pesquisa/${string}`
		}
	})
}

function filtrarMobile () {
	btnFiltarMobile = document.querySelector('.btn-filtrar-mobile')

	filtroHeader = document.querySelector('.filtro-mobile')
	filtroDiv = document.querySelector('.resultados-filtro')

	btnFiltarMobile.onclick = function () {
		filtroHeader.style.display = "flex"
		filtroDiv.style.display = "block"
	}

	fecharFiltro = document.querySelector('.x-filtro')

	fecharFiltro.onclick = function () {
		filtroDiv.style.display = "none"
	}
}

function ordenarMobile () {
	btnOrdenar = document.querySelector('.btn-ordenar-mobile')

	ordenarDiv = document.querySelector('.resultados-header-mobile')

	btnOrdenar.onclick = function () {
		ordenarDiv.style.display = "block"
	}

	fecharOrdenar = document.querySelector('.x-ordenar')

	fecharOrdenar.onclick = function () {
		ordenarDiv.style.display = "none"
	}
}
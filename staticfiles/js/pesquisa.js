document.addEventListener('DOMContentLoaded', () => {
	obterFiltros()
	excluirFiltro()
	categoriaFiltro()
	ordenarDropdown()
	ordenar()
	precoFiltro()
	generoFiltro()
	localizacaoFiltro()
	filtrarMobile()
	ordenarMobile()
})

function obterFiltros () {
	pesquisa = window.location.search;
	parametros = new URLSearchParams(pesquisa)

	filtros_ativados_div = document.querySelector(".filtros-ativados")

	parametros.forEach((valor, parametro) => {
		button = document.createElement("button")
		button.id = parametro
		icon = document.createElement("i")
		icon.className = "bi bi-x"

		filtro = ""

		valor_parse = valor.split(" ")

		for (let i = 0; i < valor_parse.length; i++) {
		    valor_parse[i] = valor_parse[i][0].toUpperCase() + valor_parse[i].substr(1);
		}

		if (parametro == "q") {
		} 
		else if (parametro == "preco_min") {
			filtro = "Min: R$"+valor_parse.join(" ")
		} 
		else if (parametro == "preco_max") {
			filtro = "Max: R$"+valor_parse.join(" ")
		} else {
			filtro = valor_parse.join(" ")
		}

		if (filtro != "") {
			button.innerText = filtro
			filtros_ativados_div.appendChild(button)
			document.querySelector(`#${parametro}`).appendChild(icon)
		}
	})
}

function excluirFiltro () {
	filtros_btn = document.querySelector(".filtros-ativados").querySelectorAll('button')
	
	filtros_btn.forEach(filtro_btn => {
		filtro_btn.onclick = function () {
			pesquisa = window.location.search;
			parametros = new URLSearchParams(pesquisa)

			parametros.delete(filtro_btn.id)

			window.location.href = `/livro/pesquisa/?${parametros.toString()}`
		}
	})
}

function categoriaFiltro () {
	categoriaBtns = document.querySelectorAll('.btn-categoria')

	categoriaBtns.forEach(categoriaBtn => {
		categoriaBtn.onclick = function () {
			pesquisa = window.location.search;
			parametros = new URLSearchParams(pesquisa)

			parametros.set('categoria', categoriaBtn.innerText.toLowerCase())

			window.location.href = `/livro/pesquisa/?${parametros.toString()}`
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

			if (btnOrder.dataset.order) {
				parametros.set('order', btnOrder.dataset.order)
			}

			window.location.href = `/livro/pesquisa/?${parametros.toString()}`
		}
	})
}

function precoFiltro () {
	btnFiltroPreco = document.querySelector('.filtro-preco')

	btnFiltroPreco.onclick = function () {
		min = document.getElementsByName('preco-min')[0]
		max = document.getElementsByName('preco-max')[0]

		pesquisa = window.location.search;
		parametros = new URLSearchParams(pesquisa)

		parametros.delete('preco_min')
		parametros.delete('preco_max')

		if (min.value) {
			parametros.set('preco_min', min.value)
		}

		if (max.value) {
			parametros.set('preco_max', max.value)
		}

		window.location.href = `/livro/pesquisa/?${parametros.toString()}`
	}
}

function generoFiltro () {
	generos = document.querySelectorAll('.filtro-genero')

	generos.forEach(genero => {
		genero.onclick = function () {
			pesquisa = window.location.search;
			parametros = new URLSearchParams(pesquisa)

			parametros.set('genero', genero.innerText.toLowerCase())

			window.location.href = `/livro/pesquisa/?${parametros.toString()}`
		}
	})
}

function localizacaoFiltro () {
	localizacoes = document.querySelectorAll('.filtro-localizacao')

	localizacoes.forEach(localizacao => {
		localizacao.onclick = function () {
			pesquisa = window.location.search;
			parametros = new URLSearchParams(pesquisa)

			parametros.set('estado', localizacao.innerText.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, ''))

			window.location.href = `/livro/pesquisa/?${parametros.toString()}`
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
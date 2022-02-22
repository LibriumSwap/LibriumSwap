document.addEventListener('DOMContentLoaded', function () {
  sliderImagens()
  categorias()
  efeitosInput()
  detalhes()
  excluirDetalhe()
  preencherDetalhe()
  preencherImagens()
})

function sliderImagens () {
  imageInputs = document.querySelectorAll('.image-input')

  imageInputs.forEach(imageInput => {
    imageInput.addEventListener("change", evt => {
      url = URL.createObjectURL(imageInput.files[0]);
      label = document.querySelector(`#${imageInput.name}`)
      icon = label.querySelector('i')
      if (icon) {
        label.removeChild(icon)
      }
      label.style.backgroundColor = ""
      label.style.background = "url(" + url + ") no-repeat center";
      label.style.backgroundSize = "auto 500px";
    })
  })
}

function preencherImagens () {
  imageInputs = document.querySelectorAll('.image-input')

  imageInputs.forEach(imageInput => {
    url = imageInput.labels[0].dataset.url
    if(url){
      label = document.querySelector(`#${imageInput.name}`)
      icon = label.querySelector('i')
      if (icon) {
        label.removeChild(icon)
      }
      label.style.backgroundColor = ""
      label.style.background = "url(" + url + ") no-repeat center";
      label.style.backgroundSize = "auto 500px";
    }
  })
}

function categorias () {
  categoriaBtns = document.querySelectorAll('.categoria')

  categoriaBtns.forEach(categoriaBtn => {
    categoriaBtn.addEventListener("click", evt => {
      const preco = document.querySelector('.preco')
      if (categoriaBtn == document.querySelector('label[for="id_categoria_0"]') || categoriaBtn == document.querySelector('label[for="id_categoria_1"]')) {
        preco.style.opacity = "1"
        preco.querySelector("input").removeAttribute("disabled")
      } else {
        preco.style.opacity = "0.35"
        preco.querySelector("input").setAttribute("disabled", true)
      }
    })
  })
}

function detalhes () {
  novoDetalheBtn = document.querySelector('#btn-novo-detalhe')

  novoDetalheBtn.addEventListener("click", evt => {

    detalheInputs = document.querySelectorAll('.detalhe-input')
    
    detalheInputs = detalheInputs[0].cloneNode(true)
    detalheInputs.children[0].children[0].children[0].value = ""
    detalheInputs.children[0].children[1].children[0].value = ""
    detalheInputsDiv = document.querySelector('.detalhe-inputs')
    detalheInputsDiv.appendChild(detalheInputs)
    detalheInputs.scrollIntoView({ behavior: 'smooth'})
    excluirDetalhe()
  })
}

function excluirDetalhe () {
  excluirBtns = document.querySelectorAll('.btn-excluir')

  excluirBtns.forEach(excluirBtn => {
    excluirBtn.onclick = function () {
      detalheInputsDiv = document.querySelector('.detalhe-inputs')
      if (detalheInputsDiv.children.length > 1) {
        detalheInputsDiv.removeChild(excluirBtn.parentElement)
      }
    }
  })
}

function preencherDetalhe () {
  detalhes = document.querySelector('.detalhes').value
  detalhes = JSON.parse(detalhes.replace(/'/g, '"'))

  detalheInputs = document.querySelectorAll('.detalhe-input')

  if (Object.keys(detalhes).length > 0) {
    for(i=0; i < Object.keys(detalhes).length; i++){

      detalheInput = detalheInputs[0].cloneNode(true)
      detalheInput.children[0].children[0].children[0].value = Object.keys(detalhes)[i]
      detalheInput.children[0].children[1].children[0].value = Object.values(detalhes)[i]
      detalheInputsDiv = document.querySelector('.detalhe-inputs')
      detalheInputsDiv.appendChild(detalheInput)
    }

    detalheInputs[0].remove()
  }
}

function anunciar () {
  detalheInputs = document.querySelectorAll('.detalhe-input')
  detalhes = new Object()

  for (let i = 0; i < detalheInputs.length; i++) {
    if (detalheInputs[i].children[0].children[0].children[0].value && detalheInputs[i].children[0].children[1].children[0].value) {
      detalhes[detalheInputs[i].children[0].children[0].children[0].value] = detalheInputs[i].children[0].children[1].children[0].value
    }
  }

  detalhesTexto = document.querySelector('.detalhes')
  console.log(detalhesTexto)
  detalhesTexto.value = JSON.stringify(detalhes).replace(/'/g, '"')
  return true;
}

function efeitosInput () {
  $(window).on('load', function(){
    
    $(".input-effect input").focusout(function(){
      if($(this).val() != ""){
        $(this).addClass("has-content");
      }else{
        $(this).removeClass("has-content");
      }
    })
  });
}
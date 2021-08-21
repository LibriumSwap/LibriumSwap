document.addEventListener('DOMContentLoaded', function () {
  sliderImagens()
  categorias()
  efeitosInput()
  detalhes()
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
    evt.preventDefault()

    detalheInputs = document.querySelectorAll('.detalhe-input')
    
    detalheInputs = detalheInputs[0].cloneNode(true)
    detalheInputs.children[0].value = ""
    detalheInputs.children[1].value = ""
    detalheInputsDiv = document.querySelector('.detalhe-inputs')
    detalheInputsDiv.appendChild(detalheInputs)
  })
}

function anunciar () {
  detalheInputs = document.querySelectorAll('.detalhe-input')
  detalhes = new Object()

  for (let i = 0; i < detalheInputs.length; i++) {
    if (detalheInputs[i].children[0].value && detalheInputs[i].children[1].value) {
      detalhes[detalheInputs[i].children[0].value] = detalheInputs[i].children[1].value
    }
  }

  detalhesTexto = document.querySelector('#id_detalhes')
  detalhesTexto.value = JSON.stringify(detalhes)
  console.log(detalhesTexto.value)
  return true;
}

function efeitosInput () {
  $(window).on('load', function(){
    $(".col-3 input").val("");
    
    $(".input-effect input").focusout(function(){
      if($(this).val() != ""){
        $(this).addClass("has-content");
      }else{
        $(this).removeClass("has-content");
      }
    })
  });
}
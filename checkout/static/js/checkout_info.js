document.addEventListener("DOMContentLoaded", () => {
  efeitosInput()
  cep()
})

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

function cep () {
  cep = document.querySelector('.cep')

  inputs = document.querySelectorAll('input')

  inputs.forEach(input => {
    input.addEventListener("focusin", function () {
      if (cep.value) {
        fetch(`https://viacep.com.br/ws/${cep.value}/json/`, {
          method: 'GET'
        })
        .then(response => response.json())
        .then(result => {
          document.querySelector('input[name=estado]').focus()
          document.querySelector('input[name=estado]').value = result.uf

          document.querySelector('input[name=cidade]').focus()
          document.querySelector('input[name=cidade]').value = result.localidade

          document.querySelector('input[name=bairro]').focus()
          document.querySelector('input[name=bairro]').value = result.bairro

          document.querySelector('input[name=rua]').focus()
          document.querySelector('input[name=rua]').value = result.logradouro
        })
      }
    })
  })
}
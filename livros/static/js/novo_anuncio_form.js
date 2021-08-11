document.addEventListener('DOMContentLoaded', function () {
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
})
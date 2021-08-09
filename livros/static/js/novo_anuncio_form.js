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
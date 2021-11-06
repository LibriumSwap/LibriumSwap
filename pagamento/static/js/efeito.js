document.addEventListener('DOMContentLoaded', () => {
  efeitosInput()
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

var maskCPF = IMask(document.getElementById('form-checkout__cardExpirationMonth'), {
    mask: '00/00'
})
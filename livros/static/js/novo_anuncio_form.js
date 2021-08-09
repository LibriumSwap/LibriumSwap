imageInputs = document.querySelectorAll('.image-input')

imageInputs.forEach(imageInput => {
  imageInput.addEventListener("change", evt => {
    url = URL.createObjectURL(imageInput.files[0]);
    label = document.querySelector(`#${imageInput.name}`)
    icon = label.querySelector('i')
    label.removeChild(icon)
    label.style.backgroundColor = ""
    label.style.background = "url(" + url + ") no-repeat center";
    label.style.backgroundSize = "350px 500px";
  })
})
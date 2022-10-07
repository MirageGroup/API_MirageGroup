var seta = document.querySelectorAll('.botão_seta')

seta.forEach(element => {
  element.addEventListener('click', () => {
    element.classList.toggle('seta_cima')
  })
})
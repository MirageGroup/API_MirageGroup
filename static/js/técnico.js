var seta = document.querySelectorAll('.botão_seta')

seta.forEach(element => {
  element.addEventListener('click', () => {
    element.classList.toggle('seta_cima')
  })
})

    // ALTERNANDO VISIBILIDADE DE CHAMADOS


  const abas = document.querySelectorAll('[data-botao]'); 

  esconderConteudos = () => {
    const conteudos = document.querySelectorAll('[data-conteudo]')

    conteudos.forEach(conteudo => conteudo.classList.add('none'))
  }
  inativarAbas = () => {
    abas.forEach(aba => aba.classList.remove('aba-ativa'))
  }
  ativarConteudo = (valor) => {
    const conteudo = document.querySelector(`[data-conteudo="${valor}"]`)
    console.log(conteudo)
    conteudo.classList.remove('none')
  }
  ativarAba = (aba) => {
    aba.classList.add('aba-ativa')
    console.log(aba)
  }
  abas.forEach(aba => aba.addEventListener('click', () => {
      const valor = aba.dataset.botao
      console.log(valor)

      esconderConteudos()
      inativarAbas()
      ativarConteudo(valor)
      ativarAba(aba)
})) 



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
    const conteudo = document.querySelectorAll(`[data-conteudo="${valor}"]`)

    conteudo.forEach(conteudo=> conteudo.classList.remove('none'))
  }
  ativarAba = (aba) => {
    aba.classList.add('aba-ativa')
    
  }
  abas.forEach(aba => aba.addEventListener('click', () => {
      const valor = aba.dataset.botao
      

      esconderConteudos()
      inativarAbas()
      ativarConteudo(valor)
      ativarAba(aba)
})) 

var abaTodas = document.querySelector(`[data-botao="todos"`)
console.log(abaTodas)
abaTodas.addEventListener('click',() => {

  const conteudoFechado = document.querySelectorAll(`[data-conteudo="fechado"]`)

  const conteudoAberto = document.querySelectorAll(`[data-conteudo="aberto"]`)
  console.log(conteudoAberto) 

  conteudoAberto.forEach(conteudo => conteudo.classList.remove('none'))
  conteudoFechado.forEach(conteudo => conteudo.classList.remove('none'))


  




})

//Pesquisar chamados


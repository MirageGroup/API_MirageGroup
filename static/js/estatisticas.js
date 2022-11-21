
   
   








      


     // ALTERNANDO VISIBILIDADE DE GRAFICOS


     const abas = document.querySelectorAll('[data-botao]'); 

     esconderConteudos = () => {
       const conteudos = document.querySelectorAll('[data-grafico]')
   
       conteudos.forEach(conteudo => conteudo.classList.add('none'))
     }
     inativarAbas = () => {
       abas.forEach(aba => aba.classList.remove('aba-ativa-estatisticas'))
     }
     ativarConteudo = (valor) => {
       const conteudo = document.querySelectorAll(`[data-grafico="${valor}"]`)
   
       conteudo.forEach(conteudo=> conteudo.classList.remove('none'))
     }
     ativarAba = (aba) => {
       aba.classList.add('aba-ativa-estatisticas')
       
     }
     abas.forEach(aba => aba.addEventListener('click', () => {
         const valor = aba.dataset.botao
         console.log(valor)
   
         esconderConteudos()
         inativarAbas()
         ativarConteudo(valor)
         ativarAba(aba)
   })) 
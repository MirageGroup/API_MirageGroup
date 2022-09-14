var form = document.getElementById('formid');
form.addEventListener("submit", function(e) {

  var numero = document.getElementById('input_numero_pc').value;
  var situacao = document.getElementById('modal_opções').value;
  var descricao = document.getElementById('exampleFormControlTextarea1').value;

  e.preventDefault();

  changeContainerClass(numero, situacao );
})


function changeContainerClass(number, situation, description) {
  let textContainer = document.getElementById(number).getElementsByClassName('container_texto')[0];

  if (situation == "Com Problemas"){
    textContainer.classList.remove('status_verde');
    textContainer.classList.remove('status_branco')
    textContainer.classList.add('status_vermelho');
  }else if (situation == "Faltando"){
    textContainer.classList.remove('status_verde');
    textContainer.classList.remove('status_vermelho');
    textContainer.classList.add('status_branco');
  }else if (situation == "Sem Problemas"){
    textContainer.classList.remove('status_branco');
    textContainer.classList.remove('status_vermelho');
    textContainer.classList.add('status_verde');
  }
}
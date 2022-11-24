// -*-*-*-*-*-*-*-*-*-*-*-*-*-*- DRAG & DROP -*-*-*-*-*-*-*-*-*-*-*-*-*-*-

/** app */
var cards = document.querySelectorAll('.card')
const dropzones = document.querySelectorAll('.dropzone')
const dropzonesSec = document.querySelectorAll('.dropzone_secundaria')
const dropzoneNone = document.querySelectorAll('#dropzone_none')
const addComputerIDForm = document.getElementById('new_pc_id_form');

/** our cards */
cards.forEach(card => {
    card.addEventListener('dragstart', dragstart)
    card.addEventListener('drag', drag)
    card.addEventListener('dragend', dragend)
})

function dragstart() {
    // log('CARD: Start dragging ')
    dropzones.forEach( dropzone => dropzone.classList.add('highlight'))
    dropzonesSec.forEach( dropzone => dropzone.classList.add('highlight_secundario'))
    dropzoneNone.forEach( dropzone => dropzone.classList.remove('highlight'))

    // this = card
    this.classList.add('is-dragging')
}

function drag() {
    // log('CARD: Is dragging ')
}

function dragend() {
    // log('CARD: Stop drag! ')
    dropzones.forEach( dropzone => dropzone.classList.remove('highlight'))
    dropzonesSec.forEach( dropzone => dropzone.classList.remove('highlight_secundario'))

    // this = card
    this.classList.remove('is-dragging')
    updateIdsInput()
}

/** place where we will drop cards */
dropzones.forEach( dropzone => {
    dropzone.addEventListener('dragenter', dragenter)
    dropzone.addEventListener('dragover', dragover)
    dropzone.addEventListener('dragleave', dragleave)
    dropzone.addEventListener('drop', drop)
})

function dragenter() {
    // log('DROPZONE: Enter in zone ')
}

function dragover() {
    // this = dropzone
    this.classList.add('over')

    // get dragging card
    const cardBeingDragged = document.querySelector('.is-dragging')

    // this = dropzone
    if(this.childElementCount == 0){
        this.appendChild(cardBeingDragged)
    }
        
  
}

function dragleave() {
    // log('DROPZONE: Leave ')
    // this = dropzone
    this.classList.remove('over')

}

function drop() {
    // log('DROPZONE: dropped ')
    this.classList.remove('over')
}

// -*-*-*-*-*-*-*-*-*-*-*-*-*-*- SALVAR LAYOUT EDITADO -*-*-*-*-*-*-*-*-*-*-*-*-*-*-

function updateIdsInput(){
    // fill hidden input
    const inputIds = document.getElementById('layout')
    inputIds.value = ''
    let dropzones_ = document.querySelectorAll('.dropzone')
    let ids = []
    for(i=0;i<dropzones_.length;i++){
        if(!dropzones_[i].firstElementChild){
            ids = ids + null + ','
        }else{
            pc_id = dropzones_[i].firstElementChild.getAttribute('data-pc-id')
            ids = ids + pc_id + ','
        }
    }
    ids = ids.slice(0, -1)
    inputIds.value = ids
}

// -*-*-*-*-*-*-*-*-*-*-*-*-*-*- ADICIONAR NOVO COMPUTADOR -*-*-*-*-*-*-*-*-*-*-*-*-*-*-

addComputerIDForm.addEventListener('submit', e => {

    e.preventDefault()

    dropzones.forEach(dropzone => {
        if (!dropzone.firstElementChild){ 
          dropzone.classList.add('adicionar') 
          dropzone.addEventListener('click', createNewComputerCard)
        }
    })
    cards.forEach(card => {
        card.removeEventListener('dragstart', dragstart)
        card.removeEventListener('drag', drag)
        card.removeEventListener('dragend', dragend)
    })
})

function createNewComputerCard(){
  // Função de criar o novo Card
  let newPcId = document.getElementById('new_pc_id').value

  // criando o card e adicionando os atributos de classe e data-id
  var newCard = document.createElement('card')
  newCard.className = "card_computador card"
  newCard.setAttribute("data-pc-id", newPcId)
  newCard.setAttribute("data-exists", "no")
  newCard.setAttribute("data-bs-toggle", "modal")
  newCard.setAttribute("dragabble", "true")
  newCard.setAttribute("data-bs-target", "#modal-teste")
  newCard.setAttribute("data-bs-whathever", newPcId)
  newCard.setAttribute("id", newPcId)

  var newCardContainerPopOver = document.createElement('div')
  newCardContainerPopOver.className = "container_popover"
  newCardContainerPopOver.setAttribute("data-bs-toggle", "popover")
  newCardContainerPopOver.setAttribute("data-bs-title", "Status do computador")
  newCardContainerPopOver.setAttribute("data-bs-content", "O computador está funcionando corretamente")
  newCardContainerPopOver.setAttribute("data-bs-trigger", "hover")

  // criando o elemento img dentro do card e atribuindo a imagem
  var newCardImg = document.createElement('img')
  newCardImg.setAttribute("src", "/static/img/img_monitor.png")
  newCardImg.className = "imagem_monitor"
  newCardContainerPopOver.appendChild(newCardImg)

  // criando a div container_texto embaixo
  var newCardText = document.createElement('div')
  newCardText.className = "container_texto status_verde"
  newCardText.innerHTML += '<p class="texto_computador">'+newPcId+'</p>'
  newCardContainerPopOver.appendChild(newCardText)

  newCard.appendChild(newCardContainerPopOver)

  this.appendChild(newCard)
  let newPos = this.getAttribute('data-pos')

  document.getElementById('new_pc_id').value = ''

  returnEventListeners()
  updateNewPcInput(newPcId, newPos)
}

function returnEventListeners(){
  dropzones.forEach(dropzone => {
    dropzone.classList.remove('adicionar')
    dropzone.removeEventListener('click', createNewComputerCard)
  })
  cards = document.querySelectorAll('.card')
  cards.forEach(card => {
      card.addEventListener('dragstart', dragstart)
      card.addEventListener('drag', drag)
      card.addEventListener('dragend', dragend)
  })
}

// Salvando o novo computador
// Colocar pc novo no input
var newPcIds = ''
var newPcPos = ''
    function updateNewPcInput(newPcId, newPos){
        newPcIDInput = document.getElementById('new_pcs')
        newPcIds = newPcIds + ',' + newPcId

        newPcPosInput = document.getElementById('new_pos')
        newPcPos = newPcPos + ',' + newPos

        let newPcIds_ = newPcIds.slice(1) 
        let newPcPos_ = newPcPos.slice(1)

        newPcIDInput.value = newPcIds_
        newPcPosInput.value = newPcPos_
    }

// -*-*-*-*-*-*-*-*-*-*-*-*-*-*- REMOVER COMPUTADOR -*-*-*-*-*-*-*-*-*-*-*-*-*-*-
const RemoveComputerBTN = document.getElementById('remove_computer_btn')

RemoveComputerBTN.addEventListener('click', removeComputerSelect)

function removeComputerSelect() {


  RemoveComputerBTN.removeEventListener('click', removeComputerSelect)
  RemoveComputerBTN.addEventListener('click', removeComputerCancel)

  cards.forEach(card => {
    card.removeEventListener('dragstart', dragstart)
    card.removeEventListener('drag', drag)
    card.removeEventListener('dragend', dragend)
    card.classList.remove('card_computador')
    card.classList.add('card_computador_remover')
    card.addEventListener('click', removeComputer)
  })
}

var removeComputerInput = ''
function removeComputer() {
  this.parentElement.innerHTML = ""

  var removePcInput = document.getElementById('remove_pcs')

  if(this.getAttribute('data-exists') == "yes" ){
    removeComputerInput = removeComputerInput + ',' + this.getAttribute('data-pc-id')
    let removeComputerInput_ = removeComputerInput.slice(1)
    removePcInput.value = removeComputerInput_
  }else if (this.getAttribute('data-exists') == "no"){
    cards = document.querySelectorAll('.card')
    var newPcIdInput = document.getElementById('new_pcs')
    var newPcPosInput = document.getElementById('new_pos')
    var newPcIdInput_ = ''
    var newPcPosInput_ = ''
    cards.forEach(card => {
      if (card.getAttribute('data-exists') == "no"){
        newPcIdInput_ = newPcIdInput_+ ',' + card.getAttribute('data-pc-id')
        newPcPosInput_ = newPcPosInput_ + ',' + card.parentElement.getAttribute('data-pos')
      }
    })
    newPcIdInput_ = newPcIdInput_.slice(1)
    newPcPosInput_ = newPcPosInput_.slice(1)
    newPcIdInput.value = newPcIdInput_
    newPcPosInput.value = newPcPosInput_
  }

}

function removeComputerCancel() {
  cards.forEach(card => {
    card.addEventListener('dragstart', dragstart)
    card.addEventListener('drag', drag)
    card.addEventListener('dragend', dragend)
    card.classList.remove('card_computador_remover')
    card.classList.add('card_computador')
  })
  RemoveComputerBTN.removeEventListener('click', removeComputerCancel)
  RemoveComputerBTN.addEventListener('click', removeComputerSelect)
}

// -*-*-*-*-*-*-*-*-*-*-*-*-*-*- ALTERAR ESPECIFICAÇÕES -*-*-*-*-*-*-*-*-*-*-*-*-*-*-
document.getElementById('cpu2').value = ""
document.getElementById('gpu2').value = ""
document.getElementById('ram2').value = ""
document.getElementById("os2").value = ""

document.getElementById('cpu1').addEventListener('input', () => {
  document.getElementById('cpu2').value = document.getElementById('cpu1').value
})

document.getElementById('gpu1').addEventListener('input', () => {
  document.getElementById('gpu2').value = document.getElementById('gpu1').value
})

document.getElementById('ram1').addEventListener('input', () => {
  document.getElementById('ram2').value = document.getElementById('ram1').value
})

document.getElementById('os1').addEventListener('input', () => {
  document.getElementById('os2').value = document.getElementById('os1').value
})
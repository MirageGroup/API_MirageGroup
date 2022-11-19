// -*-*-*-*-*-*-*-*-*-*-*-*-*-*- DRAG & DROP -*-*-*-*-*-*-*-*-*-*-*-*-*-*-

/** app */
var cards = document.querySelectorAll('.card')
const dropzones = document.querySelectorAll('.dropzone')
const dropzonesSec = document.querySelectorAll('.dropzone_secundaria')
const dropzoneNone = document.querySelectorAll('#dropzone_none')
const addComputerIDButton = document.getElementById('add_computer_id_btn');

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

// -*-*-*-*-*-*-*-*-*-*-*-*-*-*- SALVAR LAYOUT EDITADO - JavaScript -*-*-*-*-*-*-*-*-*-*-*-*-*-*-

function updateIdsInput(){
    // fill hidden input
    const inputIds = document.getElementById('ids')
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
    console.log(ids)
}

// -*-*-*-*-*-*-*-*-*-*-*-*-*-*- ADICIONAR NOVO COMPUTADOR - JavaScript -*-*-*-*-*-*-*-*-*-*-*-*-*-*-

addComputerIDButton.addEventListener('click', () => {
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
  newPcId = document.getElementById('new_pc_id').value

  // criando o card e adicionando os atributos de classe e data-id
  var newCard = document.createElement('card')
  newCard.className = "card_computador card"
  newCard.setAttribute("data-pc-id", newPcId)
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
  newCardText.innerHTML += '<p class="texto_computador">COMPUTADOR</p>'
  newCardText.innerHTML += '<p class="texto_computador">'+newPcId+'</p>'
  newCardContainerPopOver.appendChild(newCardText)

  newCard.appendChild(newCardContainerPopOver)

  this.appendChild(newCard)

  returnEventListeners()
  updateNewPcInput(newPcId)
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
    function updateNewPcInput(newPcId){
        newPcInput = document.getElementById('new_pcs')
        newPcIds = newPcIds + newPcId + ','
        newPcIds = newPcIds.slice(0, -1)
        newPcInput.value = newPcInput.value + newPcIds
        updateIdsInput()   
    }
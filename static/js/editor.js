/** help */
function log(message) {
    console.log('> ' + message)
}

/** app */
const cards = document.querySelectorAll('.card')
const dropzones = document.querySelectorAll('.dropzone')
const dropzonesSec = document.querySelectorAll('.dropzone_secundaria')
const dropzoneNone = document.querySelectorAll('#dropzone_none')

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

    // SAVE LAB EDIT

const dataPosicao = dropzones
const posicoes = []
for(let i = 0; i < dataPosicao.length; i++){
    console.log(dataPosicao[i].getAttribute('data-posicao');
    
    
    
    )
}

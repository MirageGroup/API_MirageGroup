const exampleModal = document.getElementById('modal-teste')
exampleModal.addEventListener('show.bs.modal', event => {
    // Button that triggered the modal
    const button = event.relatedTarget
    // Extract info from data-bs-* attributes
    const recipient = button.getAttribute('data-bs-whatever')
    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.
    
    const modalBodyInput = exampleModal.querySelector('#input_numero_pc')
    
    modalBodyInput.value = recipient
    })


const modalRed = document.getElementById('modal-red')
modalRed.addEventListener('show.bs.modal', event => {
    // Button that triggered the modal
    const button = event.relatedTarget
    // Extract info from data-bs-* attributes
    const recipient = button.getAttribute('data-bs-problema')
    const obj = JSON.parse(recipient);

    pc_problem = obj.pc_problema
    pc_description = obj.pc_descricao

    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.

    const modalInputProblem = modalRed.querySelector('#problema')
    const modalInputDescription = modalRed.querySelector('#descricao')
    

    modalInputProblem.value = pc_problem
    modalInputDescription.value = pc_description
    
})



















    const email = document.querySelector('#email');
    email.addEventListener('keypress' , function(event) {

        if (event.shiftKey && event.key === '@'){
            console.log('não pode ter @');
            event.preventDefault();
        }

    });
    email.onpaste = e => {
      console.log("NÂO PODE COLAR")
      e.preventDefault()
      return false;
    }
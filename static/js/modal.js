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

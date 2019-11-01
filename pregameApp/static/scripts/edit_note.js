

document.querySelector("#pregame_container").addEventListener("click", (evt) => {
    if (evt.target.id.startsWith("editBtn")) {
        evt.preventDefault()
        const id = evt.target.id.split("-")[1]
        const editField = document.querySelector(`#note-${id}`)
        const editInputField = document.querySelector(`#input-${id}`)
        const editButton = document.querySelector(`#editBtn-${id}`)
        const saveButton = document.querySelector(`#saveBtn-${id}`)
        // editField.setAttribute('contenteditable', true)
        // editField.classList.add('editable')
        editField.classList.add('hide')
        editInputField.classList.remove('hide')
        editButton.classList.add('hide')
        saveButton.classList.remove('hide')
    }
    else if (evt.target.id.startsWith("saveBtn")) {
        const id = evt.target.id.split("-")[1]
        const editField = document.querySelector(`#note-${id}`)
        const editButton = document.querySelector(`#editBtn-${id}`)
        const saveButton = document.querySelector(`#saveBtn-${id}`)
        const deleteInput = document.querySelector(`#deleteInput-${id}`)
        // editField.setAttribute('contenteditable', false)
        // editField.classList.remove('editable')
        editButton.classList.remove('hide')
        saveButton.classList.add('hide')
        deleteInput.value = 'EDIT'
    }
})
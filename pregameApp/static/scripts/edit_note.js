

document.querySelector("#pregame_container").addEventListener("click", (evt) => {
    if (evt.target.id.startsWith("editBtn")) {
        const id = evt.target.id.split("-")[1]
        const editField = document.querySelector(`#note-${id}`)
        const editButton = document.querySelector(`#editBtn-${id}`)
        const saveButton = document.querySelector(`#saveBtn-${id}`)
        editField.setAttribute('contenteditable', true)
        editField.classList.add('editable')
        editButton.classList.add('hide')
        saveButton.classList.remove('hide')
    }
    else if (evt.target.id.startsWith("saveBtn")) {
        const id = evt.target.id.split("-")[1]
        const editField = document.querySelector(`#note-${id}`)
        const editButton = document.querySelector(`#editBtn-${id}`)
        const saveButton = document.querySelector(`#saveBtn-${id}`)
        editField.setAttribute('contenteditable', false)
        editField.classList.remove('editable')
        editButton.classList.remove('hide')
        saveButton.classList.add('hide')
    }
})
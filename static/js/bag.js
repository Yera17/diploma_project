let deleteButtons = document.querySelectorAll(".delete-button");
let addButtons = document.querySelectorAll(".add-button");

deleteButtons.forEach(button => {
    button.addEventListener("click", (event) => {
        button.type = "submit";
    })
})

addButtons.forEach(button => {
    button.addEventListener("click", (event) => {
        button.type = "submit";
    })
})
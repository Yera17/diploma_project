const rangeInput = document.getElementById("id_rating")
const stars = document.getElementById("stars")
let value = rangeInput.value

for (let i = 0; i < value; i++) {
    stars.innerHTML += "<i class='text-yellow-600 mr-1 fa-solid fa-star'></i>"
}

for (let i = 0; i < 5 - value; i++) {
    stars.innerHTML += "<i class='text-yellow-600 mr-1 fa-regular fa-star'></i>"
}

let parsedValue;

rangeInput.addEventListener("input", (event) => {
    stars.innerHTML = ""
    value = rangeInput.value
    parsedValue = parseInt(rangeInput.value)
    for (let i = 0; i < parsedValue; i++) {
        stars.innerHTML += "<i class='text-yellow-600 mr-1 fa-solid fa-star'></i>"

    }
    if (value - parsedValue === 0.5) {
        stars.innerHTML += "<i class='text-yellow-600 mr-1 fa-solid fa-star-half-stroke'></i>"
        for (let i = 0; i < 4 - value; i++) {
            stars.innerHTML += "<i class='text-yellow-600 mr-1 fa-regular fa-star'></i>"
        }
    } else {
        for (let i = 0; i < 5 - value; i++) {
            stars.innerHTML += "<i class='text-yellow-600 mr-1 fa-regular fa-star'></i>"
        }
    }
})
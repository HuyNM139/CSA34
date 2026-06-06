// Gọi API để lấy ra dữ liệu
fetch("http://127.0.0.1:5000/")
.then(res => res.json())
.then(data => {
    console.log(data)
})
.catch(err => {
    console.log(err);
})

let name = document.getElementById("name")
let email = document.getElementById("email")
let phone = document.getElementById("phone")
let fav1 = document.getElementById("fav1")
let fav2 = document.getElementById("fav2")
let fav3 = document.getElementById("fav3")

// Gọi API để lấy ra dữ liệu
fetch("http://127.0.0.1:5000/get_person_information")
.then(res => res.json())
.then(data => {
    console.log(data)
    name.innerText = data.name
    email.innerText = data.email
    phone.innerText = data.phone
    fav1.innerText = data.favorites[0]
    fav2.innerText = data.favorites[1]
    fav3.innerText = data.favorites[2]
})
.catch(err => {
    console.log(err);
})

fetch("http://127.0.0.1:5000/")
.then(res => res.json())
.then(data => {
    console.log(data)
})
.catch(err => {
    console.log(err);
})

let params = new URLSearchParams(window.location.search);
let productId = params.get("id");
let id = document.getElementById("id")
let name = document.getElementById("name")
let category = document.getElementById("category")
let price = document.getElementById("price")
let stock = document.getElementById("stock")
let rating = document.getElementById("rating")
let is_available = document.getElementById("is_available")

fetch("http://127.0.0.1:5000/products/" + productId)
.then(res => res.json())
.then(data => {
    id.innerText = data.id
    name.innerText = data.name
    category.innerText = data.category
    price.innerText = data.price
    stock.innerText = data.stock
    rating.innerText = data.rating
    is_available.innerText = data.is_available
})
.catch(err => {
    console.log(err);
});
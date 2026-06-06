fetch("http://127.0.0.1:5000/")
.then(res => res.json())
.then(data => {
    console.log(data)
})
.catch(err => {
    console.log(err);
})

let products = document.getElementById("products");

fetch("http://127.0.0.1:5000/products")
.then(res => res.json())
.then(data => {

    for (let product of data) {
        products.innerHTML += `
            <h3>${product.name}</h3>
            <p>ID: ${product.id}</p>
            <p>Category: ${product.category}</p>
            <p>Price: ${product.price}</p>
            <p>Stock: ${product.stock}</p>
            <p>Rating: ${product.rating}</p>
            <p>Available: ${product.is_available}</p>
            <a href="idproduct.html?id=${product.id}">Xem chi tiết</a>
            <hr>
        `;
    }

})
.catch(err => {
    console.log(err);
})
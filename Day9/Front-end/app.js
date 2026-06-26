// Gọi API để lấy ra dữ liệu
fetch("http://127.0.0.1:5000/")
.then(res => res.json())
.then(data => {
    console.log(data)
})
.catch(err => {
    console.log(err);
})

// Gọi API để lấy ra dữ liệu
fetch("http://127.0.0.1:5000/get_person_information")
  .then(res => res.json())
  .then(data => {
    let user = data[0];
    document.getElementById("first_name").textContent = user[1];
    document.getElementById("last_name").textContent = user[2];
    document.getElementById("email").textContent = user[3];
    document.getElementById("phone").textContent = user[4];
    document.getElementById("city").textContent = user[5];
    document.getElementById("country").textContent = user[6];

  })
  .catch(err => {
      console.log(err);
  })


// POST
let getStartedBtn = document.getElementById("getStartedBtn");

getStartedBtn.addEventListener("click", () => {

    fetch("http://127.0.0.1:5000/create_person", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            first_name: document.getElementById("first_name").value,
            last_name: document.getElementById("last_name").value,
            email: document.getElementById("email").value,
            phone: document.getElementById("phone").value,
            city: document.getElementById("city").value,
            country: document.getElementById("country").value
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
    })
    .catch(err => {
        console.log(err);
    });

});
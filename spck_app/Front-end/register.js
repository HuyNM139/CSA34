let registerBtn = document.getElementById("registerBtn");

registerBtn.addEventListener("click", () => {

    let username = document.getElementById("username").value.trim();
    let password = document.getElementById("password").value.trim();

    if(username === "" || password === ""){
        alert("Please fill in all fields.");
        return;
    }

    fetch("http://127.0.0.1:5000/register",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            username:username,
            password:password
        })
    })
    .then(res=>res.json())
    .then(data=>{

        alert(data.message);

        if(data.success){
            window.location.href="login.html";
        }

    });

});
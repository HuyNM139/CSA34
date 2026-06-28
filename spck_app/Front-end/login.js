let loginBtn = document.getElementById("loginBtn");

loginBtn.addEventListener("click",()=>{

    let username = document.getElementById("username").value.trim();
    let password = document.getElementById("password").value.trim();

    if(username === "" || password === ""){
        alert("Please fill in all fields.");
        return;
    }

    fetch("http://127.0.0.1:5000/login",{

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

        if(data.success){

            localStorage.setItem("user_id",data.user_id);
            localStorage.setItem("username",data.username);

            window.location.href="index.html";

        }
        else{

            alert(data.message);

        }

    });

});
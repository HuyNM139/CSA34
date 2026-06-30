let loginBtn = document.getElementById("loginBtn");

loginBtn.addEventListener("click",()=>{
    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value;

    if(email==""){
        alert("Please enter your email.");
        return;
    }

    let emailPattern=/^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if(!emailPattern.test(email)){
        alert("Invalid email.");
        return;
    }

    if(password==""){
        alert("Please enter your password.");
        return;
    }

    fetch("http://127.0.0.1:5000/login",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            email:email,
            password:password
        })

    })

    .then(res=>res.json())
    .then(data=>{

        if(data.success){

            localStorage.setItem("user_id", data.user_id);
            localStorage.setItem(
                "full_name",
                data.first_name + " " + data.last_name
            );

            window.location.href="index.html";

        }
        else{

            alert(data.message);

        }

    });

});

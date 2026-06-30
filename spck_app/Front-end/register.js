let registerBtn = document.getElementById("registerBtn");

registerBtn.addEventListener("click", () => {
    let firstName=document.getElementById("firstName").value.trim();
    let lastName=document.getElementById("lastName").value.trim();
    let email=document.getElementById("email").value.trim();
    let password=document.getElementById("password").value;

    if(firstName === "" || lastName === "" || email === "" || password === ""){
        alert("Please fill in all fields.");
        return;
    }

    fetch("http://127.0.0.1:5000/register",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            email: email,
            password: password
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
let password=document.getElementById("password");
password.addEventListener("input", ()=>{
    let value=password.value;
    let strength=document.getElementById("strength");
    if(value.length<8){
        strength.innerHTML="Weak";
    }
    else if(value.length<12){
        strength.innerHTML="Medium";
    }
    else{
        strength.innerHTML="Strong";
    }
});
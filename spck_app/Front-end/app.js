let userID = localStorage.getItem("user_id");

if(userID == null){
    window.location.href = "login.html";
}
document.getElementById("username").textContent = localStorage.getItem("full_name");

let addGameBtn = document.getElementById("addGameBtn");

addGameBtn.addEventListener("click", () => {

    let name = document.getElementById("name").value.trim();
    let genre = document.getElementById("genre").value.trim();
    let hours = document.getElementById("hours").value.trim();
    let status = document.getElementById("status").value.trim();

    if(name === "" || genre === "" || hours === "" || status === ""){
        alert("Please fill in all fields.");
        return;
    }

    fetch("http://127.0.0.1:5000/games", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            user_id:localStorage.getItem("user_id"),
            name: name,
            genre: genre,
            hours_played: hours,
            status: status
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        loadGames();

        document.getElementById("name").value = "";
        document.getElementById("genre").value = "";
        document.getElementById("hours").value = "";
        document.getElementById("status").value = "";
    })
    .catch(err => {
        console.log(err);
    });

});


function loadGames() {
    fetch("http://127.0.0.1:5000/games/" + userID)
    .then(res => res.json())
    .then(data => {
        let html = "";
        data.forEach(game => {
            html += `
            <div class="game">
                <h3>${game[2]}</h3>
                <p>Genre: ${game[3]}</p>
                <p>Hours Played: ${game[4]}</p>
                <p>Status: ${game[5]}</p>
                <button onclick="deleteGame(${game[0]})">Delete🗑️</button>
                <button onclick="editGame(${game[0]})">Edit✏️</button>
            </div>
            `
        })
        document.getElementById("gameList").innerHTML = html
    })
    .catch(err => {
        console.log(err);
    })
}
loadGames();

function deleteGame(id) {
    fetch("http://127.0.0.1:5000/games/" + id, {
        method: "DELETE"
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message)
        loadGames()
    })
    .catch(err => {
        console.log(err)
    })
}

function editGame(id){

    let newHours = prompt("New Hours Played:");

    if(newHours === null){
        return;
    }

    newHours = newHours.trim();

    if(newHours === ""){
        alert("Hours Played cannot be empty.");
        return;
    }

    fetch("http://127.0.0.1:5000/games/" + id, {
        method:"PUT",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            hours_played:newHours
        })
    })
    .then(res=>res.json())
    .then(data=>{
        alert(data.message);
        loadGames();
    })
    .catch(err=>{
        console.log(err);
    });

}

function loadStats(){
    fetch("http://127.0.0.1:5000/stats")
    .then(res=>res.json())
    .then(data=>{
        document.getElementById("totalGames").textContent = data.total
        document.getElementById("playingGames").textContent = data.playing
        document.getElementById("completedGames").textContent =data.completed
        document.getElementById("wishlistGames").textContent = data.wishlist
    })
}
loadGames();
loadStats();

function searchGame(){
    let name = document.getElementById("search").value;
    fetch("http://127.0.0.1:5000/search/" + name)
    .then(res=>res.json())
    .then(data=>{
        let html = "";
        data.forEach(game=>{
            html += `
            <div class="game">
                <h3>${game[1]}</h3>
                <p>Genre: ${game[2]}</p>
                <p>Hours: ${game[3]}</p>
                <p>Status: ${game[4]}</p>
            </div>
            `;
        });
        document.getElementById("gameList").innerHTML = html;
    });
}

document.getElementById("logoutBtn")
.addEventListener("click",()=>{

    localStorage.removeItem("user_id");
    localStorage.removeItem("username");

    window.location.href="login.html";

});
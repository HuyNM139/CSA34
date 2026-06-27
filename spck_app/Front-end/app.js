let addGameBtn = document.getElementById("addGameBtn")
addGameBtn.addEventListener("click", () => {
    fetch("http://127.0.0.1:5000/games", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: document.getElementById("name").value,
            genre: document.getElementById("genre").value,
            hours_played: document.getElementById("hours").value,
            status: document.getElementById("status").value
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message)
    })
    .catch(err => {
        console.log(err)
    })
    loadGames()
})


function loadGames() {
    fetch("http://127.0.0.1:5000/games")
    .then(res => res.json())
    .then(data => {
        let html = "";
        data.forEach(game => {
            html += `
            <div class="game">
                <h3>${game[1]}</h3>
                <p>Genre: ${game[2]}</p>
                <p>Hours Played: ${game[3]}</p>
                <p>Status: ${game[4]}</p>
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
    let newHours = prompt("New Hours Played: ")
    fetch("http://127.0.0.1:5000/games/" + id, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            hours_played: newHours
        })
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

function loadStats(){
    fetch("http://127.0.0.1:5000/stats")
    .then(res=>res.json())
    .then(data=>{
        document.getElementById("totalGames").textContent = "Total Games: " + data.total
        document.getElementById("playingGames").textContent = "Playing: " + data.playing
        document.getElementById("completedGames").textContent ="Completed: " + data.completed
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
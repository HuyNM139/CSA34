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
                <button onclick="deleteGame"(${game[0]})>Delete</button>
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

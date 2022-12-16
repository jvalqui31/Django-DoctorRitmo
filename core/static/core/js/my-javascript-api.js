//Consumiento api randomuser.me
  const fetchUsers = () => {
    //console.log("ejecuting")
    const card = $('#profile-card');
    const xmlHttp = new XMLHttpRequest();
    //xmlHttp.addEventListener('load', showData);
    xmlHttp.open('GET', "https://randomuser.me/api/?results=8", true)
    xmlHttp.send();
    xmlHttp.onreadystatechange = () => {
        if (xmlHttp.readyState === 4 && xmlHttp.status === 200) {
            const response = JSON.parse(xmlHttp.responseText);
            response.results.forEach(currentUser => {
                console.log(currentUser)
                card.append(`<div class="card m-4 bg-dark text-white"> 
                                <img src="${currentUser.picture.large}" class="card-img-top" alt="..."> 
                                <div class="card-body">
                                <h5 class="card-title text-center style="font-size: 13px;">${currentUser.name.first} ${currentUser.name.last}</h5>
                                <p>Email: ${currentUser.email}</p>
                                <p>Teléfono: ${currentUser.phone}</p>
                                <p>Genero: ${currentUser.gender}</p>
                                <p>País: ${currentUser.location.country}</p>
                                </div>
                                </div>`);
            })
        }
    }
}
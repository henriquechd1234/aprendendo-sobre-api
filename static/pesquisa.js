document.getElementById("formbusca").addEventListener("click", function(evento){
    evento.preventDefault();

    const barra = document.getElementById('br').value;
    const url = `/buscar-artista?q=${encodeURIComponent(barra)}`;

    fetch(url)
        .then(Response => {
            if(!Response.ok){
                throw new Error("Erro na requisição");
            }
            return Response.json();
        })
        .then(data =>{
            const resultadoDiv = document.getElementById("resultado")
            if( data.data && data.data.length > 0){
                resultadoDiv.innerHTML = `
                    <h2>Resultados para "${termo}":</h2>
                    <ul>
                        ${data.data.map(artista => `
                            <li>
                                <strong>${artista.name}</strong><br>
                                <img src="${artista.picture_medium}" alt="${artista.name}"><br>
                                Fãs: ${artista.nb_fan}<br>
                                Álbuns: ${artista.nb_album}<br>
                                <a href="${artista.link}" target="_blank">Ver no Deezer</a>
                            </li>
                        `).join("")}
                    </ul>
                `;
            }
            else{
                resultadoDiv.innerHTML = `<p>Nenhum resultado encontrado para "${termo}".</p>`;
            }
            
             
        })
        .catch(error => {
            console.error("Erro:", error);
            document.getElementById("resultado").innerHTML = `<p>Erro ao buscar informações. Tente novamente.</p>`;
        });
})
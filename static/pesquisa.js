async function busca() {
    const info = document.getElementById("br").ariaValueMax
    const url = `http://127.0.0.1:5000/buscar-artista?q=${info}`;
    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log("Dados recebidos:", data);
    } catch (error) {
        console.error("Erro na requisição:", error);
    }
}
       
    
    

document.getElementById("botao").addEventListener('click',busca)
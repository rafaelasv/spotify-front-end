document.getElementById("gerarNome").addEventListener("click", function() {
    // Exibe a tela de carregamento
    document.getElementById("loadingScreen").style.display = "flex";

    // Frases aleatórias para a tela de carregamento
    const frases = [
        "Gerando o nome perfeito...",
        "Acalme-se, o nome está chegando!",
        "O nome da calopsita está sendo escolhido com carinho.",
        "Quase lá... só mais um segundo!",
        "O nome está tomando forma!",
        "Nada como um bom nome para uma calopsita fofinha!"
    ];

    let contador = 0;

    // Função para atualizar a frase a cada segundo
    const updateFrase = setInterval(function() {
        document.getElementById("loadingText").innerText = frases[contador];
        contador++;

        if (contador === frases.length) {
            contador = 0;
        }
    }, 1000); // Altera a frase a cada 1 segundo

    // Simula o tempo de carregamento (exemplo de 4 segundos)
    setTimeout(function() {
        // Limpa o intervalo de atualização da frase
        clearInterval(updateFrase);

        // Esconde a tela de carregamento
        document.getElementById("loadingScreen").style.display = "none";

        // Gera um nome aleatório de calopsita
        let nomes = ["Pipoca", "Pipoca Jr.", "Sol", "Estrela", "Luna", "Mel"];
        let nomeGerado = nomes[Math.floor(Math.random() * nomes.length)];

        // Exibe o nome gerado
        document.getElementById("resultado").innerText = "Nome Gerado: " + nomeGerado;
    }, 4000); // Tempo total de carregamento (4 segundos)
});
function checkContainer() {
    const containerRespostas = document.getElementsByClassName("respostas-container")[0];
    const showMoreButton = document.getElementById("showMoreBtn");

    if (!containerRespostas || !showMoreButton) return;

    const precisaExpandir = containerRespostas.scrollHeight > containerRespostas.clientHeight;

    showMoreButton.style.visibility = precisaExpandir ? "visible" : "hidden";

};

document.addEventListener("DOMContentLoaded", () => {
    const headers = document.querySelectorAll(".resposta-header");

    // Lógica das respostas
    headers.forEach(header => {
        header.addEventListener("click", () => {
            const indicator = header.getAttribute("indicator");

            const respostaHeader = header;
            const icone = header.getElementsByTagName("ion-icon")[0];
            const respostaBody = document.querySelector(
                `.resposta-body[indicator="${indicator}"]`
            );

            if (respostaBody.classList.contains("active")) {
                respostaBody.classList.remove('active');
                icone.classList.remove('rotate');
            } else {
                respostaBody.classList.add('active');
                icone.classList.add('rotate');
            }

            const respostasContainer = document.getElementsByClassName("respostas-container")[0];

            if (!respostasContainer.classList.contains("open")) {
                setTimeout(checkContainer, 350);
            };
        });
    });

    const botaoMostrarMais = document.getElementById("showMoreBtn");

    botaoMostrarMais.addEventListener("click", () => {
        const respostasContainer = document.getElementsByClassName("respostas-container")[0];
        const icone = botaoMostrarMais.getElementsByTagName("ion-icon")[0];

        if (respostasContainer.classList.contains("open")) {
            botaoMostrarMais.setAttribute("title", "Mostrar tudo")
            icone.classList.remove('rotate');

            respostasContainer.classList.remove('open');
        } else {
            botaoMostrarMais.setAttribute("title", "Mostrar menos")
            icone.classList.add('rotate');

            respostasContainer.classList.add('open');
        }
    });

    checkContainer();

});


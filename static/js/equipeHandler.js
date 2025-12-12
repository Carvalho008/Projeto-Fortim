const showNameElement = document.getElementById('memberShowName')
const showDescriptionElement = document.getElementById('memberShowDescription')
const showPhotoElement = document.getElementById('profileIcon')
const showButtonElement = document.getElementById('memberShowButton')

let idAtual = 0

const listaEquipe = [
    {
        nome: 'Márcia Vieira',
        descricao: 'Professora e Orientadora',
        imagem: '',
        linkCurriculo: '',
        id: 0,
    },
    {
        nome: 'Lian Carvalho',
        descricao: 'Integrado em Informática',
        imagem: '',
        linkCurriculo: '',
        id: 1,
    },
    {
        nome: 'Ana Luisa',
        descricao: 'Integrado em Aquicultura',
        imagem: '',
        linkCurriculo: '',
        id: 2,
    },
    {
        nome: 'Maria Clara',
        descricao: 'Integrado em Química - 1',
        imagem: '',
        linkCurriculo: '',
        id: 3,
    },
    {
        nome: 'Gabriele',
        descricao: 'Integrado em Química - 2',
        imagem: '',
        linkCurriculo: '',
        id: 4,
    },
]

const cardsEquipe = document.querySelectorAll('.equipe-card');

function changeDestaque(id) {
    const listaEquipeCopia = JSON.parse(JSON.stringify(listaEquipe));
    let membroDestaque = listaEquipeCopia[id]; // Membro que vai ser mostrado com destaque no membroShow

    listaEquipeCopia.splice(id, 1);

    // Informações de texto do ShowMember
    showNameElement.innerHTML = membroDestaque.nome;
    showDescriptionElement.innerHTML = membroDestaque.descricao;
    // Foto do ShowMember
    showPhotoElement.src = membroDestaque.imagem;
    showPhotoElement.title = `Foto de ${membroDestaque.nome}`;
    // Botão do ShowMember
    showButtonElement.href = membroDestaque.linkCurriculo;
    showButtonElement.title = `Currículo de ${membroDestaque.nome}`;

    cardsEquipe.forEach(card => {
        let index = card.getAttribute('index');

        let equipeMember = listaEquipeCopia[index];

        card.setAttribute("indicator", equipeMember.id)


        // pega o primeiro h6
        const nomeComponent = card.querySelector('h6:nth-of-type(1)');
        // pega o segundo h6
        const descricaoComponent = card.querySelector('h6:nth-of-type(2)');
        // pega o link/button <a>
        const buttonComponent = card.querySelector('a');
        // pega a imagem/img
        const imgComponent = card.querySelector('img');

        // Informações de texto do card
        nomeComponent.innerHTML = equipeMember.nome;
        descricaoComponent.innerHTML = equipeMember.descricao;
        // Imagem do card
        imgComponent.src = equipeMember.imagem;
        imgComponent.title = `Foto de ${equipeMember.nome}`;
        // Botão do card
        buttonComponent.href = equipeMember.linkCurriculo;
        buttonComponent.title = `Currículo de ${equipeMember.nome}`;
    });
};

changeDestaque(idAtual);

cardsEquipe.forEach(card => {
    card.addEventListener('click', () => {
        const id = card.getAttribute('indicator');

        changeDestaque(id);

        // aqui você coloca o que quiser fazer com esse valor
    });
});
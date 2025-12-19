const showNameElement = document.getElementById('memberShowName')
const showDescriptionElement = document.getElementById('memberShowDescription')
const showPhotoElement = document.getElementById('profileIcon')
const showButtonElement = document.getElementById('memberShowButton')

let idAtual = 0

const listaEquipe = [
    {
        nome: 'Márcia Vieira',
        descricao: 'Professora e Orientadora do projeto. Doutora em Educação pela Universidade Estadual Paulista Júlio de Mesquita Filho - UNESP (2017),Graduada em Administração pela UFC (1993), Mestra em Logística e Pesq. Operacional pela UFC,(2009),Especialista em Formação Pedagógica para Docência Profissional e Tecnológica pelo IFCE (2020) e Formação em Procedimentos Básicos para o atendimento Educacional Especializado (AEE) pelo IFTM (2018). ',
        imagem: 'marcia.gif',
        linkCurriculo: 'http://lattes.cnpq.br/4324545790655825',
        id: 0,
    },
    {
        nome: 'Lian Carvalho',
        descricao: 'Pesquisador FUNCAP PROGRAMA JOVEM CIENTISTA DA PESCA ARTESANAL, Técnico em Informática pelo IFCE Campus Aracati(2023-2025)',
        imagem: 'lian.gif',
        linkCurriculo: 'http://lattes.cnpq.br/6417304866666966',
        id: 1,
    },
    {
        nome: 'Ana Luisa',
        descricao: 'Cursando Ensino técnico integrado em aquicultura pelo Instituto Federal Do Ceará. Pesquisadora FUNCAP PROGRAMA JOVEM CIENTISTA DA PESCA ARTESANAL ',
        imagem: 'luisa.gif',
        linkCurriculo: 'http://lattes.cnpq.br/3521824364373872',
        id: 2,
    },
    {
        nome: 'Maria Clara',
        descricao: 'Sou Maria Clara de Souza Morais, estudante do Ensino Médio com Técnico Integrado em Química em tempo integral no IFCE - Campus Aracati. Atuo como bolsista da FUNCAP no Programa Jovem Cientista da Pesca Artesanal, onde busco oportunidades para aplicar e expandir meus conhecimentos na área.',
        imagem: 'clara.gif',
        linkCurriculo: 'http://lattes.cnpq.br/9241898983968558',
        id: 3,
    },
    {
        nome: 'Maria Gabrielle',
        descricao: 'Cursando Ensino técnico integrado em Química pelo Instituto Federal do Ceará. PESQUISADOR FUNCAP PROGRAMA JOVEM CIENTISTA DA PESCA ARTESANAL.',
        imagem: 'gabriele.gif',
        linkCurriculo: 'http://lattes.cnpq.br/6482692652552970',
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
    showPhotoElement.src = `/static/images/profiles/${membroDestaque.imagem}`;
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
        imgComponent.src = `/static/images/profiles/${equipeMember.imagem}`;
        imgComponent.title = `Foto de ${equipeMember.nome}`;
        // Botão do card
        buttonComponent.href = equipeMember.linkCurriculo;
        buttonComponent.title = `Currículo de ${equipeMember.nome}`;
    });
};

changeDestaque(idAtual);

cardsEquipe.forEach(card => {
    const botao = card.querySelector('.curriculo-btn');

    // Clique no botão: abre o link e PARA AQUI
    botao.addEventListener('click', (event) => {
        event.stopPropagation();
    });

    // Clique no card (fora do botão)
    card.addEventListener('click', () => {
        const id = card.getAttribute('indicator');
        changeDestaque(id);
    });
});

const dropButton = document.getElementById('drop-btn');
const dropContainer = document.getElementById('drop-container');
const icon = dropButton.querySelector('ion-icon');

dropButton.addEventListener('click', () => {
    if (icon.name === 'arrow-dropdown') {
        dropContainer.classList.add('active');
        icon.name = 'arrow-dropup';
    } else {
        dropContainer.classList.remove('active');
        icon.name = 'arrow-dropdown';
    }
});

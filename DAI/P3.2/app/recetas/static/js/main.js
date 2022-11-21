const btnSwitch = document.querySelector('#switch');
const barra = document.querySelector('#barra');
const botonBusqueda = document.querySelector('#boton-busqueda');

btnSwitch.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    barra.classList.toggle('dark');
    botonBusqueda.classList.toggle('dark');
});
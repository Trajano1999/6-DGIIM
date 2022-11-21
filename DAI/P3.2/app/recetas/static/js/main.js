const btnSwitch = document.querySelector('#switch');

btnSwitch.addEventListener('click', () => {
    let estado = document.body.classList.toggle('dark');
    localStorage.setItem('modo', estado);
});

if(localStorage.getItem('modo') == "true"){
    document.body.classList.add('dark');
}
else{
    document.body.classList.remove('dark');
}
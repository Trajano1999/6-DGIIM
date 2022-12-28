// ----------------------------------------------------------------------------
// Modo Nocturno
// ----------------------------------------------------------------------------

const btnSwitch = document.querySelector('#night-mode');

btnSwitch.addEventListener('click', () => {
    let estado = document.body.classList.toggle('dark');
    localStorage.setItem('modo', estado);
});

if(localStorage.getItem('modo') == "true")
    document.body.classList.add('dark');
else
    document.body.classList.remove('dark');

// ----------------------------------------------------------------------------
// Tamaño del Texto
// ----------------------------------------------------------------------------

const btnText = document.querySelector('#text-height');

btnText.addEventListener('click', () => {
    let estado = document.body.classList.toggle('tiny');
    localStorage.setItem('tamano', estado);
});

if(localStorage.getItem('tamano') == "true")
    document.body.classList.add('tiny');
else
    document.body.classList.remove('tiny');

// ----------------------------------------------------------------------------
// Main
// ----------------------------------------------------------------------------

const recetas = []              // declaraciones   
let html_str  = ''              // de variables
let i         = 0               //

// fetch devuelve una promise
fetch('/api/recipes')           // GET por defecto,
.then(res => res.json())        // respuesta en json, otra promise
.then(filas => {                // arrow function
    filas.forEach(fila => {     // bucle ES6, arrow function
        i++
        recetas.push(fila)      // se guardan para después sacar cada una             
        // ES6 templates
        html_str += `<tr>
                        <td>${i}</td>
                        <td>
                            <button onclick="detalle('${i-1}')" 
                                    type="button" class="btn btn-outline btn-sm"
                                    data-bs-toggle="modal" data-bs-target="#detailModal">
                            ${fila.name}
                            </button>
                        </td>
                        <td>
                            <button type="button" class="btn btn-warning btn-sm">Edit</button>
                            <button type="button" class="btn btn-danger btn-sm">Delete</button>
                        </td>
                    </tr>`         // ES6 templates
    });
    document.getElementById('tbody').innerHTML=html_str  // se pone el html en su sitio
})

function detalle(i) {  // saca un modal con la información de cada coctel
// saca un modal con receta[i]
}
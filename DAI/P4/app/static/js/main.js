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
                            <button onclick="detalle('${i-1}')" type="button" class="btn btn-outline btn-sm" data-bs-toggle="modal" data-bs-target="#detailModal">
                                ${fila.name}
                            </button>

                            <div class="modal fade" id="detailModal" tabindex="-1" aria-labelledby="labelModal" aria-hidden="true">
                                <div class="modal-dialog">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h1 class="modal-title fs-5" id="detailTitle"></h1>
                                        </div>
                                        <div class="modal-body" id="detailBody">
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </td>
                        <td>
                            <button onclick="editar('${i-1}')" type="button" class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#editModal">
                                Edit
                            </button>

                            <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="labelModal" aria-hidden="true">
                                <div class="modal-dialog">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h1 class="modal-title fs-5" id="editTitle">Edit Recipe</h1>
                                        </div>
                                        <div class="modal-body" id="editBody">
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                            <button onclick="aplicar_edicion('${i-1}')" type="button" class="btn btn-primary">Apply</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                                        
                            <button onclick="eliminar('${i-1}')" type="button" class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal">
                                Delete
                            </button>

                            <div class="modal fade" id="deleteModal" tabindex="-1" aria-labelledby="labelModal" aria-hidden="true">
                                <div class="modal-dialog">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h1 class="modal-title fs-5" id="deleteTitle">Delete Recipe</h1>
                                        </div>
                                        <div class="modal-body">
                                            Are you sure you want to remove it completely? There is no way back.
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                            <button onclick="aplicar_eliminacion('${i-1}')" type="button" class="btn btn-primary">Delete</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </td>
                    </tr>`         // ES6 templates
    });
    document.getElementById('tbody').innerHTML=html_str  // se pone el html en su sitio
})

function detalle(i) {  // saca un modal con la información de cada coctel
    let html_titulo = `<h1>${recetas[i].name}</h1>`
    let html_cuerpo = ''

    // rellenamos el modal
    html_cuerpo += `<h3>Ingredients</h3>
                    <ul>
                    `
    recetas[i].ingredients.forEach(ingrediente => {
        html_cuerpo += `<li>${ingrediente.name}</li>
                        `
    })
    html_cuerpo += `</ul>
                    <h3>Instructions</h3>
                    <ul>
                    `
    recetas[i].instructions.forEach(instruction => {
        html_cuerpo += `<li>${instruction}</li>
                        `
    })
    html_cuerpo += `</ul>`

    // aplicamos valores
    document.getElementById('detailTitle').innerHTML=html_titulo
    document.getElementById('detailBody').innerHTML=html_cuerpo
}

function editar(i) {
    let html_cuerpo = `<form enctype="multipart/form-data" action="/api/recipes/" method="put" id="edit-form">
                        <div class="form-group">
                        <label for="name">Nombre Receta</label>
                        <input type="text" class="form-control" id="name" name="name" value="${recetas[i].name}">
                        <div id="textHelp" class="form-text">Nombre de la receta</div>
                      </div>`

    html_cuerpo += `<div class="form-group">
                        <label for="ingredients">Ingredientes:</label>
                        <textarea class="form-control" id="ingredients" name="ingredients" rows="3">`

    recetas[i].ingredients.forEach(ingredient => {
        if(ingredient == recetas[i].ingredients[recetas[i].ingredients.length-1]) {
            html_cuerpo += `${ingredient.name}`
        }

        else{
            html_cuerpo += `${ingredient.name}\n`
        }
    })

    html_cuerpo += `</textarea>
                    <div id="textAreaHelp" class="form-text">Un ingrediente por línea</div>
                      </div>
                      <div class="form-group">
                        <label for="instructions">Instrucciones:</label>
                        <textarea class="form-control" id="instructions" name="instructions" rows="3">`

    recetas[i].instructions.forEach(instruction => {
        if(instruction === recetas[i].instructions[recetas[i].instructions.length-1]) {
            html_cuerpo += `${instruction}`
        }

        else{
            html_cuerpo += `${instruction}\n`
        }
    })

    html_cuerpo += `</textarea>
                    <div id="textAreaHelp" class="form-text">Una instruccion por línea</div>
                      </div>
                    </form>
                    `

    document.getElementById('edit').innerHTML=html_cuerpo
}

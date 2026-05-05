const contenero = document.querySelector('#container');

productos.forEach(producto => {
    console.log(producto);
});

const p = document.createElement('p');

p.textContent = 'Hola Mundo';

contenero.appendChild(p);
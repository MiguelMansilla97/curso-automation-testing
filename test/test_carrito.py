import pytest
from app.carrito_funciones import agregar_producto



def test_agregar_producto(carrito_vacio, producto_mouse):
    resultado = agregar_producto(carrito_vacio, producto_mouse)

    assert len(resultado) == 1
    # assert resultado[0].Nombre == "Mouse"

def test_validar_nombre_carrito (carrito_vacio, producto_mouse):
    resultado = agregar_producto(carrito_vacio, producto_mouse)

    assert resultado[0]["Nombre"] == "Mouse"
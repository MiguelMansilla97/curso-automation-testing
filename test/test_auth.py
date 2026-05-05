import pytest

from app.auth_funciones import register, login

@pytest.mark.register
@pytest.mark.login
@pytest.mark.parametrize("username,password, resultado",[
    ("Juan", "1234567", "registro exitoso"), #exito
    ("", "", "campos vacios"),
    ("Juan", "123", "contraseña muy corta")
])

def test_register(username, password, resultado):
    assert register(username, password) == resultado

@pytest.mark.parametrize("username,password, resultado",[
    ("Juan", "1234567", "login exitoso"), #exito
    ("Juan", "123333333", "credenciales invalidas"),
])

def test_login(username, password, resultado):
    register("Juan", "1234567") #registrar el usuario para el test
    assert login(username, password) == resultado
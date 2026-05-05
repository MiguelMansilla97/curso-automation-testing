import pytest

from calculadora.operaciones import sumar, dividir


def  test_sumar_positivo(numeros):
    a, b = numeros
    assert sumar(a, b) == 12
    
try:
    valor = int(input("Ingresa un número entero: "))
    resultado = 10 / valor
    print(f"10 / {valor} = {resultado}")
except ZeroDivisionError:
    print("Error: División por cero.")
except ValueError:
    print("Error: Entrada inválida, no es un número entero.")
finally:
    print("Operación finalizada.")

def test_sumar_positivo():
    assert sumar(5, 7) == 12

def test_sumar_negativo():
    assert sumar(-5, -7) == -12

def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(1,0)
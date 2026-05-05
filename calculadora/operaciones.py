# # Funciones

def suma(a,b):
    resultado = a + b
    return resultado

def saludo(nombre):
    return f"Hola {nombre}"

def dividir (a, b):
    try: # Hace esto mientras cumpla
        return a / b
    except ZeroDivisionError: # Cuando no ocurra
        print("No se puede dividir por cero")

def restar (a, b):
    return a - b

def multiplicar (a, b):
    return a * b
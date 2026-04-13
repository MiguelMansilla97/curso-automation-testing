# Funciones

def suma(a,b):
    resultado = a + b
    return resultado

def saludo(nombre):
    return f"Hola {nombre}"

print(suma(5,10))
print(saludo("Rey"))

def dividir (a, b):
    try: # Hace esto mientras cumpla
        return a / b
    except ZeroDivisionError: # Cuando no ocurra
        print("No se puede dividir por cero")
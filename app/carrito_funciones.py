carrito = []

def agregar_producto( carrito, producto):
    carrito.append(producto)
    return carrito

carrito = agregar_producto(carrito, {"Nombre": "Mouse", "precio": 20})
carrito = agregar_producto(carrito, {"Nombre": "manzana", "precio": 200})

print (carrito)
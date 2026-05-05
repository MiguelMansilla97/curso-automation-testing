usuarios = []

def register(username, password):
    # usuario no me ingrese campos vacíos
    if not username or not password:
        return "campos vacios"
    #contraseña corta
    if len(password) < 5:
        return "contraseña muy corta"
    
    #agregar al registro
    usuarios.append({
        "username": username, "password": password
    })

    return "registro exitoso"

def login( username, password):
    for usuario in usuarios:
        if usuario["username"] == username and usuario["password"] == password:
            return "login exitoso"
        
    return "credenciales invalidas"
    
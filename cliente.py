import requests
from requests.auth import HTTPBasicAuth

# URL del servidor
URL = 'http://localhost:5000/usuarios'

# Credenciales para la autenticación
nombre_usuario = 'admin'
contrasena = 'ca2004'

# Función para obtener usuarios
def obtener_usuarios():
    response = requests.get(URL)  
    if response.status_code == 200:  
        usuarios = response.json()  
        for usuario in usuarios: 
            print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}")
    else:
        print("Error al obtener usuarios")

# Función para agregar un usuario
def agregar_usuario(nuevo_usuario):
    response = requests.post(URL, json=nuevo_usuario, auth=HTTPBasicAuth(nombre_usuario, contrasena))  
    print(f"Respuesta del servidor: {response.status_code} - {response.text}")  
    if response.status_code == 201:
        print("Usuario agregado exitosamente")
    else:
        try:
            error_info = response.json()
            print(f"Error al agregar usuario: {response.status_code} - {error_info}")
        except ValueError:
            print(f"Error al agregar usuario: {response.status_code} - Respuesta no es JSON: {response.text}")

# Función para buscar un usuario por ID
def buscar_usuario_por_id(id_usuario):
    response = requests.get(f'{URL}/{id_usuario}', auth=HTTPBasicAuth(nombre_usuario, contrasena))  
    if response.status_code == 200:
        usuario = response.json()
        print(f"Usuario encontrado: ID: {usuario['id']}, Nombre: {usuario['nombre']}")
    else:
        print(f"Usuario con ID {id_usuario} no encontrado")

# Función para eliminar un usuario por ID
def eliminar_usuario(id_usuario):
    response = requests.delete(f'{URL}/{id_usuario}', auth=HTTPBasicAuth(nombre_usuario, contrasena))  
    if response.status_code == 200:
        print(f"Usuario con ID {id_usuario} eliminado exitosamente")
    else:
        print(f"Error al eliminar usuario con ID {id_usuario}: {response.status_code} - {response.text}")

# Función para agregar múltiples usuarios
def agregar_varios_usuarios(usuarios):
    for usuario in usuarios:
        agregar_usuario(usuario)

# Ejecución de funciones en el bloque principal
if __name__ == '__main__':
    # Obtener usuarios
    print("Lista de usuarios antes de agregar:")
    obtener_usuarios()

    # Crear una lista de nuevos usuarios
    nuevos_usuarios = [
        {"id": 3, "nombre": "Pedro"},
        {"id": 4, "nombre": "Armando"},  # Asegúrate de que los IDs sean únicos
    ]
    
    # Agregar nuevos usuarios
    agregar_varios_usuarios(nuevos_usuarios)

    # Buscar el usuario recién agregado por ID
    buscar_usuario_por_id(3)

    # Eliminar el usuario agregado por ID
    eliminar_usuario(3)

    # Mostrar usuarios después de eliminar
    print("Lista de usuarios después de eliminar:")
    obtener_usuarios()

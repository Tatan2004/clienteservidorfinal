from flask import Flask, jsonify, request  # Importa Flask para crear el servidor y jsonify para formatear las respuestas como JSON
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)  # Inicializa una aplicación Flask
auth = HTTPBasicAuth()  # Asegúrate de inicializarlo correctamente

# Base de datos simulada
base_datos = {
    "usuarios": [
        {"id": 1, "nombre": "Juan"},
        {"id": 2, "nombre": "María"}
    ]
}

# Ruta para obtener los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(base_datos["usuarios"])  # Devuelve la lista de usuarios en formato JSON

# Diccionario para almacenar usuarios y contraseñas
usuarios = {
    "admin": "ca2004",
}

# Función de verificación de usuarios
@auth.verify_password
def verify_password(usuario, contrasena):
    if usuario in usuarios and usuarios[usuario] == contrasena:
        return usuario
    return None  # Devuelve None si la verificación falla

# Ruta para agregar nuevos usuarios
# Ruta para agregar nuevos usuarios
@app.route('/usuarios', methods=['POST'])
@auth.login_required  # Protege la ruta con autenticación
def crear_usuario():
    nuevo_usuario = request.get_json()

    # Validar que el id y el nombre están presentes
    if "id" not in nuevo_usuario or "nombre" not in nuevo_usuario:
        return jsonify({"error": "Datos incompletos"}), 400  # Retorna código 400 (Bad Request)

    base_datos["usuarios"].append(nuevo_usuario)
    return jsonify({"mensaje": "Usuario creado exitosamente"}), 201

# Ruta para buscar usuarios por su ID
@app.route('/usuarios/<int:id_usuario>', methods=['GET'])
def obtener_usuario_por_id(id_usuario):
    for usuario in base_datos["usuarios"]:
        if usuario["id"] == id_usuario:
            return jsonify(usuario)
    return jsonify({"error": "Usuario no encontrado"}), 404  # Retorna código 404 (No encontrado)

# Ruta para eliminar un usuario
@app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    for usuario in base_datos["usuarios"]:
        if usuario["id"] == id_usuario:
            base_datos["usuarios"].remove(usuario)
            return jsonify({"mensaje": "Usuario eliminado exitosamente"}), 200  # Código 200 (OK)
    return jsonify({"error": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    app.run(port=5000)  # Ejecuta el servidor en el puerto 5000

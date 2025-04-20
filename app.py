
from flask import Flask, request, jsonify

app = Flask(__name__)

# Almacenamiento en memoria
usuarios = []

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "sistema": "Gestión de Usuarios y Productos",
        "version": "1.0",
        "autor": "Abdiel Rodríguez"
    })

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nombre = data.get('nombre')
    correo = data.get('correo')

    if not nombre or not correo:
        return jsonify({"error": "Faltan datos: nombre y correo son requeridos"}), 400

    usuario = {"nombre": nombre, "correo": correo}
    usuarios.append(usuario)
    return jsonify({"mensaje": "Usuario creado exitosamente", "usuario": usuario}), 201

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

if __name__ == '__main__':
    app.run(debug=True)

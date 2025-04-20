# Actividad: Módulo 1 - Lección 3

Este repositorio contiene una aplicación Flask desarrollada como parte de la actividad sobre manipulación de datos JSON y diseño de rutas RESTful. La aplicación permite crear, almacenar y recuperar información de usuarios en memoria, además de validar datos recibidos por medio de solicitudes POST.

## 📁 Estructura del proyecto

```
flask-json-leccion3/
├── app.py                     # Código principal del servidor Flask
├── requirements.txt           # Dependencias necesarias
├── estructura.json            # Estructura propuesta de productos y usuarios
├── test.http                  # Archivo de pruebas con REST Client
├── DOCUMENTACION_LECCION3.pdf # Documento con explicación y captura de pruebas
└── README.md                  # Información del proyecto
```

## 🚀 Cómo ejecutar el servidor

1. Clona este repositorio:

```bash
https://github.com/Zeurodite/flask-json.git
cd flask-json-leccion3
```

2. Crea un entorno virtual y actívalo:

```bash
python -m venv .venv
.\.venv\Scriptsctivate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecuta la aplicación:

```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## 🌐 Rutas disponibles

### `GET /info`
Retorna información básica del sistema en formato JSON.

### `POST /crear_usuario`
Recibe datos de un usuario (nombre y correo) y valida que ambos estén presentes. Devuelve un mensaje de confirmación o error.

### `GET /usuarios`
Retorna una lista de usuarios almacenados en memoria.

## 🧪 Archivo de Pruebas REST: `test.http`

El archivo `test.http` está diseñado para usarse con la extensión **REST Client** en Visual Studio Code.

Contiene pruebas para:

- `GET /info`
- `POST /crear_usuario` (válido e inválido)
- `GET /usuarios`

📸 Se incluye una captura de estas pruebas en el documento `DOCUMENTACION_LECCION3.pdf`.

## 📤 Entrega

Este repositorio debe subirse a GitHub como parte de la entrega del curso. Asegúrate de incluir:

- Código fuente y archivo de estructura JSON
- `requirements.txt`
- `test.http`
- `DOCUMENTACION_LECCION3.pdf`
- Este archivo `README.md`

✍️ _Autor: Abdiel Rodríguez_  
📅 _Fecha: Abril 2025_

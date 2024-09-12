import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Inicializamos la app
app = Flask(__name__)

# Carpeta donde se guardarán los archivos subidos
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Permitimos solo ciertos tipos de archivo (en este caso, imágenes)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Función para verificar si el archivo es de un tipo permitido
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Ruta para la página principal con el formulario de subida
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para manejar la subida de imágenes
@app.route('/upload', methods=['POST'])
def upload_file():
    # Verificamos si hay un archivo en la solicitud
    if 'file' not in request.files:
        return 'No se ha seleccionado ningún archivo'
    
    file = request.files['file']

    # Si no se seleccionó archivo o el nombre está vacío
    if file.filename == '':
        return 'No se ha seleccionado ningún archivo'

    # Verificamos si el archivo es permitido
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  # Aseguramos un nombre seguro para el archivo
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)  # Guardamos el archivo en la carpeta de uploads
        return render_template('upload_success.html', filename=filename)

    return 'Tipo de archivo no permitido'

# Ruta para mostrar la imagen subida
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename=f'uploads/{filename}'))

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.33') ## http://192.168.1.146:5000/


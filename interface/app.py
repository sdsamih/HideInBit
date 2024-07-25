import sys
import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import re

#volta uma pasta anterior para poder acessar os arq
sys.path.append('..')
from binaryoperations import *
from imageOperations import *

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(_name_)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            message = request.form['message']
            password = request.form['password']
            encrypted_image_path = insertBits(filepath, password, message)
            flash('Image encrypted successfully')
            return send_from_directory(directory=app.config['UPLOAD_FOLDER'], path=os.path.basename(encrypted_image_path), as_attachment=True)
    return render_template('encrypt.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            password = request.form['password']
            regexAscii = re.compile(r'[^\x00-\x7F]')
            extracted_message = extractBits(filepath, password)
            if regexAscii.search(extracted_message):
                extracted_message = 'senha incorreta'
            return render_template('decrypt.html', result=extracted_message)
    return render_template('decrypt.html')

if _name_ == '_main_':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
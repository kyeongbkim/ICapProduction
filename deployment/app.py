import pdb
import os
from unicodedata import category
from flask import Flask, request, flash, redirect, render_template, render_template_string, url_for, jsonify
from werkzeug.utils import secure_filename
import icap_service
import pathlib
import uuid

UPLOAD_FOLDER = str(pathlib.Path(__file__).parent.resolve()) + '/static'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif' }

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'Secret1234'

dataset = os.environ['ICAP_DATASET'] if 'ICAP_DATASET' in os.environ else 'Flickr30k'
model = os.environ['ICAP_MODEL'] if 'ICAP_MODEL' in os.environ else 'transformer'
epochs = int(os.environ['ICAP_EPOCHS']) if 'ICAP_EPOCHS' in os.environ else 30
icap_service.init(dataset=dataset, model=model, epochs=epochs)

@app.route('/')
def index():
    return redirect(url_for('upload'), code=302)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/html/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if not allowed_file(file.filename):
            flash('File not allowed')
            return redirect(request.url)

        file_ext = os.path.splitext(secure_filename(file.filename))[-1]
        file_name = '{}{}'.format(str(uuid.uuid4()), file_ext)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        file.save(file_path)
        caption = icap_service.predict(file_path)
        return render_template('result.html',
            dataset=dataset,
            model=model,
            epochs=epochs,
            file_name=file_name,
            caption=caption,
            home_url=url_for('upload'))

    else:
        return render_template('index.html',
            dataset=dataset,
            model=model,
            epochs=epochs)


@app.route('/rest/upload', methods=['POST'])
def upload_rest():
        if 'file' not in request.files:
            return jsonify(message="No file part", category="error", status=400)

        file = request.files['file']

        if file.filename == '':
            return jsonify(message="No selected file", category="error", status=400)

        if not allowed_file(file.filename):
            return jsonify(message="File not allowed", category="error", status=400)

        file_ext = os.path.splitext(secure_filename(file.filename))[-1]
        file_name = '{}{}'.format(str(uuid.uuid4()), file_ext)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        file.save(file_path)
        caption = icap_service.predict(file_path)
        return jsonify(category="success", data={ "caption": caption }, status=200)


if __name__ == "__main__":
    app.run(debug=True)

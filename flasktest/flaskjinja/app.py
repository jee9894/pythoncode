from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os

UPLOAD_DIRECTORY = os.path.dirname(__file__) + '/files'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        dirname = os.path.dirname(__file__) + '/files/' + f.filename
        print(dirname)
        f.save(dirname)
    return redirect('/files')

@app.route('/files')
def list_files():
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    # return jsonify(files)    
    return render_template('list.html', files=files)

@app.route('/files/<path:path>')
def get_file(path):
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment = True)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/resumeUpload', methods = ['POST'])
def upload_resume():
    resumes = request.form
    result = []
    result.append(resumes)
    f = request.files['file']
    dirname = os.path.dirname(__file__) + '/files/' + f.filename
    print(dirname)
    f.save(dirname)
    return render_template('list_resume.html', result = result)

if __name__ == '__main__':
    app.run(debug = True, port = 8089)
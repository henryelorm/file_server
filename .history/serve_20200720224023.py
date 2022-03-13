from flask import Flask, send_from_directory, render_template, request, redirect, url_for, safe_join
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# the directory files should be one level above the serve.py file
# rel_dir = BASE_DIR + '/Lesson_Folder'

# custom to access my files
rel_dir = 'e:/Programs'



hostip = '192.168.137.1'
port = '5000'


def list_files(directory):
    files = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            files.append(filename)
        elif os.path.isdir(path):
            files.append(filename)
    return files


@app.route('/')
def index():
    json_data = list_files(rel_dir)
    return render_template('index.html', len=len(json_data), files=json_data)


@app.route("/<path:path>")
def get_file_folder(path):
    location = safe_join(rel_dir, path)

    if os.path.isfile(location):
        return send_from_directory(rel_dir, path, as_attachment=True)

    json_data = list_files(location)
    return render_template('index.html', len=len(json_data), files=json_data)


if __name__ == '__main__':
    app.run(host=hostip, port=port, debug=True)

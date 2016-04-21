import os
import subprocess
import tempfile

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!\n'

@app.route('/upload', methods=['POST'])
def upload():
    photo = request.files['file']
    number = parse_number(photo).strip()
    return jsonify({'ticket number': str(number)})

def parse_number(photo):
    with tempfile.NamedTemporaryFile() as tmp:
        photo.save(tmp.name) # race condition, see how reading in process
        # can i just use STDIN and STDOUT ?
        tmp.flush()
        os.fsync(tmp.fileno()) 
        with tempfile.NamedTemporaryFile() as converted_file:
            args = ['convert', tmp.name, '-fuzz', '10%', '-fill', 'black',
                                       '-opaque', '#C1372C', '-threshold', '3%',
                                       converted_file.name]
            status = subprocess.call(args)
            
            if status:
                return 'OH NOSE!'
            converted_file.flush()
            os.fsync(converted_file.fileno()) 
            return subprocess.check_output(['tesseract', converted_file.name, 'stdout', 'digits'],
                                           universal_newlines=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

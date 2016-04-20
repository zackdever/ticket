import os
import subprocess
import tempfile

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!\n'

@app.route('/upload', methods=['POST'])
def upload():
    photo = request.files['file']
    number = parse_number(photo)
    return 'ticket number: %s\n' % number

def parse_number(photo):
    with tempfile.NamedTemporaryFile() as tmp:
        photo.save(tmp.name) # race condition, see how reading in process
        # can i just use STDIN and STDOUT ?
        tmp.flush()
        os.fsync(tmp.fileno()) 
        with tempfile.NamedTemporaryFile() as converted_file:
            args = ['convert', tmp.name, '-fuzz', '10%', '-fill', 'black',
                                       '-opaque', '#c5513b', '-threshold', '3%',
                                       converted_file.name]
            status = subprocess.call(args)
            
            if status:
                return 'OH NOSE!'
            converted_file.flush()
            os.fsync(converted_file.fileno()) 
            return subprocess.check_output(['tesseract', converted_file.name, 'stdout', 'digits'])

if __name__ == '__main__':
    app.run(debug=True)

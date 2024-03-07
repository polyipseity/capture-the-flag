import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute', methods=['GET'])
def execute_file():
    name = request.args.get('name')
    value = request.args.get('value')
    file = request.args.get('file')

    environ = {}
    environ[name] = value

    if os.path.exists(file) or os.path.isfile(file) or not os.path.isabs(file):
        return "NO"

    file = os.path.realpath(file)
    output = subprocess.check_output(file, shell=False, env=environ)

    return output

@app.route('/', methods=['GET'])
def index():
    return "No Flag for you!!!"

if __name__ == '__main__':
    app.run()

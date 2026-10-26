import os
from flask import Flask, send_from_directory, abort

app = Flask(__name__, static_folder='src')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'Load.html')

@app.route('/<path:filename>')
def serve_static(filename):
    safe_path = os.path.normpath(filename)
    if safe_path.startswith("..") or os.path.isabs(safe_path):
        abort(400)
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
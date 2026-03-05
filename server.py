# server.py
from flask import Flask, request
import base64
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file_data = request.form['file']
    filename = request.form['filename']

    # Decode Base64 and save file
    output_path = f"received_{os.path.basename(filename)}"
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(file_data))

    return f"File '{filename}' received securely as '{output_path}'!"

if __name__ == "__main__":
    # Use the generated cert.pem and key.pem
    # Make sure cert.pem and key.pem are in the same folder
    app.run(ssl_context=('cert.pem', 'key.pem'), port=5000)
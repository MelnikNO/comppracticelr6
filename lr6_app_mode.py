from flask import Flask, request, jsonify, abort, render_template
from PIL import Image
import os

app = Flask(__name__)

LOGIN = '1149288'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'png'

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/size2json", methods=["POST"])
def size2json():
    if 'image' not in request.files:
        abort(400, description="No image part")

    file = request.files['image']

    if file.filename == '':
        abort(400, description="No selected file")

    if file and allowed_file(file.filename):
        try:
            image = Image.open(file)
            width, height = image.size

            response = {"width": width, "height": height}
            return jsonify(response), 200, {'Content-Type': 'application/json'}

        except Exception as e:
            print(f"Error processing image: {e}")
            abort(500, description="Error processing image")

    else:
        return jsonify({"result": "invalid filetype"}), 400, {'Content-Type': 'application/json'}

@app.route("/login", methods=["GET"])
def login():
    return jsonify({"author": LOGIN}), 200, {'Content-Type': 'application/json'}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
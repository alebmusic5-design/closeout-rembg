from flask import Flask, request, Response
from rembg import remove
import requests

app = Flask(__name__)

@app.route("/remove-bg", methods=["POST"])
def remove_bg():

    data = request.get_json()

    image_url = data.get("image_url")

    if not image_url:
        return {"error": "missing image_url"}, 400

    response = requests.get(image_url)

    if response.status_code != 200:
        return {"error": "download failed"}, 400

    input_bytes = response.content

    output_bytes = remove(input_bytes)

    return Response(
        output_bytes,
        mimetype="image/png"
    )

@app.route("/")
def home():
    return "Rembg server online"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

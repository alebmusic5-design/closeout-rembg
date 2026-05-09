from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

@app.route("/remove-bg", methods=["POST"])
def remove_bg():

    image_url = request.json.get("image_url")

    if not image_url:
        return {"error": "missing image_url"}, 400

    response = requests.get(image_url)

    input_image = Image.open(BytesIO(response.content))

    output = remove(input_image)

    output_buffer = BytesIO()

    output.save(output_buffer, format="PNG")

    output_buffer.seek(0)

    return send_file(
        output_buffer,
        mimetype='image/png'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

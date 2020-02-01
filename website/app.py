from flask import Flask, render_template, request, send_file, make_response
import numpy as np
import cv2
import io

from cartoonizer import cartoonize as crtnz


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/cartoonize', methods=['POST'])
def cartoonize():
    file = request.files["image"]
    in_memory_file = io.BytesIO()
    file.save(in_memory_file)
    data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
    color_image_flag = 1
    img = cv2.imdecode(data, color_image_flag)
    output = crtnz(img)
    cv2.imwrite("output.jpg", output)
    return send_file("../output.jpg", as_attachment=True, mimetype='image/jpeg', attachment_filename="mypic.jpg")


if __name__ == '__main__':
    app.run()

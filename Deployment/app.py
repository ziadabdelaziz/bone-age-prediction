import os
import numpy as np

from keras.models import load_model
import tensorflow as tf
from keras.preprocessing import image

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

MODEL_PATH = 'models/model-best.h5'
model = load_model(MODEL_PATH, compile=False)


def generate_image(img_path, model):

    img = image.load_img(img_path, target_size=(256, 256))

    x = image.img_to_array(img)
    x = tf.image.rgb_to_grayscale(x)
    x = x / 255
    x = np.expand_dims(x, axis=0)

    preds = model(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def upload():

    f = request.files['file']

    basepath = os.path.dirname(__file__)
    file_path = os.path.join(
        basepath + '/test-data/', secure_filename(f.filename))
    f.save(file_path)

    print('File Path:', f)

    preds = generate_image(file_path, model)
    result = preds[0].numpy()[0]

    print('Resutl:', result)

    return str(result)


if __name__ == '__main__':
    app.run(debug=True)

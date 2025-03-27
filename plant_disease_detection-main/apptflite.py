import os
import tensorflow as tf
import numpy as np
# from tensorflow.keras.preprocessing import image
from keras._tf_keras.keras.preprocessing import image
from PIL import Image
import cv2
# from keras.models import load_model
from keras._tf_keras.keras.models import load_model
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras._tf_keras.keras.preprocessing.image import load_img, img_to_array
app = Flask(__name__)
import tensorflow as tf
# Load TensorFlow Lite Model
import tensorflow.lite as tflite

# interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter = tf.lite.Interpreter(model_path="model.tflite")
# interpreter.allocate_tensors()
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print('✅ TensorFlow Lite model loaded successfully!')

print('Model loaded. Check http://127.0.0.1:5000/')

labels = {0: 'Healthy', 1: 'Powdery', 2: 'Rust'}


def getResult(image_path):
    img = load_img(image_path, target_size=(225, 225))
    x = img_to_array(img)
    x = x.astype('float32') / 255.
    x = np.expand_dims(x, axis=0)

    # Reshape input to match TensorFlow Lite model input
    x = x.astype(np.float32)  # Ensure dtype matches TFLite model

    # Set input tensor
    interpreter.set_tensor(input_details[0]['index'], x)

    # Run inference
    interpreter.invoke()

    # Get output tensor
    predictions = interpreter.get_tensor(output_details[0]['index'])[0]

    return predictions



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        # basepath = os.path.dirname(__file__)
        # file_path = os.path.join(
        #     basepath, 'uploads', secure_filename(f.filename))
        # f.save(file_path)
        basepath = os.path.dirname(__file__)
        upload_folder = os.path.join(basepath, 'uploads')

        # ✅ Ensure the uploads folder exists
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        file_path = os.path.join(upload_folder, secure_filename(f.filename))
        f.save(file_path)

        predictions=getResult(file_path)
        predicted_label = labels[np.argmax(predictions)]
        return str(predicted_label)
    return None


if __name__ == '__main__':
    app.run(debug=True)
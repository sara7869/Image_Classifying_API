#!/usr/bin/env python
# encoding: utf-8
import pathlib
import os
from flask import Flask
import json
import numpy as np
# import tensorflow as tf
# from json import load
# from numpy import loadtxt
from keras.models import load_model
from keras.preprocessing import image
from flask import request
from werkzeug.utils import secure_filename

# Source: https://www.geeksforgeeks.org/how-to-convert-images-to-numpy-array/
# import PIL
# from PIL import Image
from numpy import asarray

# load model
model = load_model('./5 Classes 5 Epoch')

# summarize model.
model.summary()

app = Flask(__name__)

class_names = ['Acne and Rosacea Photos',
               'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions',
               'Atopic Dermatitis Photos',
               'Bullous Disease Photos',
               'Cellulitis Impetigo and other Bacterial Infections']


def classifyImage(loaded_image):
    loaded_image = np.expand_dims(loaded_image, axis=0)
    numpydata = asarray(loaded_image)

    predictions = model.predict(numpydata, batch_size=None, verbose=1, steps=None, callbacks=None,
                                max_queue_size=10, workers=1, use_multiprocessing=False)

    # print(predictions[0])

    predicted_class = class_names[np.argmax(predictions[0])]

    # predictions_array = predictions.ravel()

    print(predicted_class)
    return predictions[0]


@app.route('/', methods=['POST'])
def query_records():

    files = request.files
    image_file = files.getlist('file_contents')[0]
    filename = image_file.filename
    filename = secure_filename(filename)

    current_directory_path = pathlib.Path(__file__).parent.resolve()
    current_directory_path_string = current_directory_path.__str__()
    path_at_uploads = current_directory_path_string + '/uploads/'
    path = os.path.join(path_at_uploads, secure_filename(filename))
    image_file.save(path)

    loaded_image = image.load_img(path, target_size=(128, 128))

    print(request.files)
    predictions_nd_array = classifyImage(loaded_image)
    predictions_list = predictions_nd_array.tolist()

    os.remove(path)

    # range(5) => [0, 1, 2, 3, 4]
    records = []
    for x in range(predictions_list.__len__()):
        try:
            disease = class_names[x]
            confidence = predictions_list[x]
            record = {'disease': disease, 'confidence': confidence}
            records.append(record)
        except Exception as exc:
            print("Only " + str(x + 1) + " class names found")
            break

    # return json.dumps({'disease': predicted_class})

    response_body = json.dumps({
        'prediction_info': records
    })

    return response_body


app.run(debug=True)

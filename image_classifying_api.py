#!/usr/bin/env python
# encoding: utf-8
import pathlib
import os
from flask import Flask

# !/usr/bin/env python
# encoding: utf-8

import json
import numpy as np
from json import load
from numpy import loadtxt
from keras.models import load_model
from keras.preprocessing import image
from flask import request
from werkzeug.utils import secure_filename

# Source: https://www.geeksforgeeks.org/how-to-convert-images-to-numpy-array/
import PIL
from PIL import Image
from numpy import asarray

# load model
# model = load_model('./2 Classes 1 Epoch Model')
model = load_model('./5 Classes 5 Epoch')

# summarize model.
model.summary()
# load dataset
# dataset = loadtxt("pima-indians-diabetes.csv", delimiter=",")

# image = image.load_img('erythema-multiforme-88.jpg', target_size=(128, 128))
# image = image.load_img('03ichthyosis0213061.jpg', target_size=(128, 128))
# image = image.load_img('03ichthyosis0213061.jpg', target_size=(48, 48, 1))


# image = np.expand_dims(image, axis=3)
# image = np.expand_dims(image, axis=0)
# image = image.resize((128,128), Image.ANTIALIAS)

# image.show()
# image = Image.open('erythema-multiforme-88.jpg', target_s)


# split into input (X) and output (Y) variables
# X = dataset[:,0:8]
# Y = dataset[:,8]
# evaluate the model
# score = model.evaluate(X, Y, verbose=0)
# print("%s: %.2f%%" % (model.metrics_names[1], score[1]*100))

app = Flask(__name__)

# Assigns upload path to variable
folder = os.path.join(app.instance_path, 'uploads')

def classifyImage():
    numpydata = asarray(image)

    print(numpydata.shape)

    predictions = model.predict(numpydata, batch_size=None, verbose=1, steps=None, callbacks=None,
                                max_queue_size=10, workers=1, use_multiprocessing=False)

    class_names = ['Acne and Rosacea Photos',
                   'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions',
                   'Atopic Dermatitis Photos',
                   'Bullous Disease Photos',
                   'Cellulitis Impetigo and other Bacterial Infections']

    predicted_class = class_names[np.argmax(predictions[0])]

    print(predictions[0])
    print(predicted_class)


@app.route('/', methods=['POST'])
def query_records():
    # name = request.args.get('name')
    # print(name)
    # Read image and classify
    # scores = model.evaluate(testImage)
    # return ('Eczema')

    files = request.files
    file = files.getlist('file_contents')[0]
    filename = file.filename
    filename = secure_filename(filename)

    current_directory_path = pathlib.Path(__file__).parent.resolve()
    current_directory_path_string = current_directory_path.__str__()
    path_at_uploads = current_directory_path_string + '/uploads/'
    path = os.path.join(path_at_uploads, secure_filename(filename))
    file.save(path)

    print(request.files)
    classifyImage()
    return json.dumps(file)

    return json.dumps({'disease': predicted_class})

    # return jsonify({'disease': 'Eczema'})


app.run(debug=True)

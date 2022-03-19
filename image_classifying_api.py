# #!/usr/bin/env python
# # encoding: utf-8
# import json
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return json.dumps({'name': 'alice',
#                        'email': 'alice@outlook.com'})
# app.run()

#!/usr/bin/env python
# encoding: utf-8

import numpy as np
from json import load
from numpy import loadtxt
from keras.models import load_model
from keras.preprocessing import image

# Source: https://www.geeksforgeeks.org/how-to-convert-images-to-numpy-array/
import PIL
from PIL import Image
from numpy import asarray

# load model
model = load_model('./2 Classes 1 Epoch Model')

# summarize model.
model.summary()
# load dataset
# dataset = loadtxt("pima-indians-diabetes.csv", delimiter=",")

# image = image.load_img('erythema-multiforme-88.jpg', target_size=(128, 128))
image = image.load_img('crest-syndrome-44.jpg', target_size=(128, 128))

image = np.expand_dims(image, axis=0)
# image = image.resize((128,128), Image.ANTIALIAS)

# image.show()
# image = Image.open('erythema-multiforme-88.jpg', target_s)
numpydata = asarray(image)

print(numpydata.shape)

predictions = model.predict(numpydata, batch_size=None, verbose=1, steps=None, callbacks=None,
              max_queue_size=10, workers=1, use_multiprocessing=False)

class_names = ['Acne and Rosacea Photos',
 'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions',
 'Atopic Dermatitis Photos',
 'Bullous Disease Photos',
 'Cellulitis Impetigo and other Bacterial Infections',
 'Eczema Photos',
 'Exanthems and Drug Eruptions',
 'Hair Loss Photos Alopecia and other Hair Diseases',
 'Herpes HPV and other STDs Photos',
 'Light Diseases and Disorders of Pigmentation',
 'Lupus and other Connective Tissue diseases',
 'Melanoma Skin Cancer Nevi and Moles',
 'Nail Fungus and other Nail Disease',
 'Poison Ivy Photos and other Contact Dermatitis',
 'Psoriasis pictures Lichen Planus and related diseases',
 'Scabies Lyme Disease and other Infestations and Bites']

predicted_class = class_names[np.argmax(predictions[0])]

print (predicted_class)

# split into input (X) and output (Y) variables
# X = dataset[:,0:8]
# Y = dataset[:,8]
# evaluate the model
# score = model.evaluate(X, Y, verbose=0)
# print("%s: %.2f%%" % (model.metrics_names[1], score[1]*100))

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def query_records():
#     name = request.args.get('name')
#     print(name)
# Read image and classify
# scores = model.evaluate(testImage)
# return ('Eczema')

# return jsonify({'disease': 'Eczema'})


# @app.route('/', methods=['PUT'])
# def create_record():
#     record = json.loads(request.data)
#     with open('/tmp/data.txt', 'r') as f:
#         data = f.read()
#     if not data:
#         records = [record]
#     else:
#         records = json.loads(data)
#         records.append(record)
#     with open('/tmp/data.txt', 'w') as f:
#         f.write(json.dumps(records, indent=2))
#     return jsonify(record)


# @app.route('/', methods=['POST'])
# def update_record():
#     record = json.loads(request.data)
#     new_records = []
#     with open('/tmp/data.txt', 'r') as f:
#         data = f.read()
#         records = json.loads(data)
#     for r in records:
#         if r['name'] == record['name']:
#             r['email'] = record['email']
#         new_records.append(r)
#     with open('/tmp/data.txt', 'w') as f:
#         f.write(json.dumps(new_records, indent=2))
#     return jsonify(record)


# @app.route('/', methods=['DELETE'])
# def delete_record():
#     record = json.loads(request.data)
#     new_records = []
#     with open('/tmp/data.txt', 'r') as f:
#         data = f.read()
#         records = json.loads(data)
#         for r in records:
#             if r['name'] == record['name']:
#                 continue
#             new_records.append(r)
#     with open('/tmp/data.txt', 'w') as f:
#         f.write(json.dumps(new_records, indent=2))
#     return jsonify(record)


# app.run(debug=True)

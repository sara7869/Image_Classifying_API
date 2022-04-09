#!/usr/bin/env python
# encoding: utf-8
from operator import itemgetter
import pathlib
import os
from flask import Flask
import json
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from flask import request
from werkzeug.utils import secure_filename

# Source: https://www.geeksforgeeks.org/how-to-convert-images-to-numpy-array/
# import PIL
# from PIL import Image
from numpy import asarray

# load model
# model = load_model('./5 Classes 5 Epoch')
model = load_model('./downloaded model')

app = Flask(__name__)

class_names = ['Acne and Rosacea',
               'Actinic Keratosis Basal Cell Carcinoma or other Malignant Lesions',
               'Atopic Dermatitis',
               'Bullous Disease',
               'Cellulitis Impetigo or other Bacterial Infections',
               'Eczema',
               'Exanthems and Drug Eruptions',
               'Hair Loss, Alopecia or other Hair Diseases',
               'Herpes HPV and other STDs',
               'Light Diseases or Disorders of Pigmentation',
               'Lupus or other Connective Tissue diseases',
               'Melanoma, Skin Cancer, Nevi or Moles',
               'Nail Fungus or other Nail Disease',
               'Poison Ivy or other Contact Dermatitis',
               'Psoriasis, Lichen Planus or related diseases',
               'Scabies, Lyme Disease or other Infestations and Bites',
               'Seborrheic Keratoses or other Benign Tumors',
               'Systemic Disease',
               'Tinea, Ringworm, Candidiasis or other Fungal Infections',
               'Urticaria Hives',
               'Vascular Tumors',
               'Vasculitis',
               'Warts, Molluscum or other Viral Infections']

def classifyImage(loaded_image):
    loaded_image = np.expand_dims(loaded_image, axis=0)
    numpydata = asarray(loaded_image)

    predictions = model.predict(numpydata, batch_size=None, verbose=1, steps=None, callbacks=None,
                                max_queue_size=10, workers=1, use_multiprocessing=False)


    predicted_class = class_names[np.argmax(predictions[0])]

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
    
    sorted_records = sorted(records, key=itemgetter('confidence'), reverse=True)

    response_body = json.dumps({
        'prediction_info': sorted_records
    })

    return response_body


app.run(debug=True)

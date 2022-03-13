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


from json import load
from numpy import loadtxt
from keras.models import load_model
from keras.preprocessing import image

# load model
model = load_model('./2 Classes 1 Epoch Model')

# summarize model.
model.summary()
# load dataset
# dataset = loadtxt("pima-indians-diabetes.csv", delimiter=",")

image = image.load_img('erythema-multiforme-88.jpg', target_size=(350, 750))
image.show()

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

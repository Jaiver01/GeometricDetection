from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import base64
from classifier.classifier import classify
import os

app = Flask(__name__)
CORS(app)

file_name = 'image.jpg'
current_directory = os.getcwd()

@app.route('/classifier/geometric/predict', methods = ['POST'])
def predict():
    try:
        encoded_img = request.json['base64_img']
        encoded_img = encoded_img.replace('data:image/jpeg;base64,', '')
    except:
        return { 'done': False, 'message': 'Datos incorrectos para crear el cliente' }
    
    decoded_img = base64.b64decode((encoded_img))

    img_file = open(file_name, 'wb')
    img_file.write(decoded_img)
    img_file.close()

    prediction = classify(current_directory + '/' + file_name)

    return { 'done': True, 'prediction': prediction }

@app.errorhandler(404)
def not_found(error = None):
    response = jsonify({
        'done': False,
        'message': 'Resource Not Found',
        'status': 404
    })

    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug = True)
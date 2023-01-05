from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.xception import preprocess_input
import keras
import numpy as np

model = keras.models.load_model("C:/Users/Godwin/Downloads/xception_v3_08_0.954.h5")

def preprocess(path):
    img = load_img(path, target_size=(299,299))
    x = np.array(img)
    x = np.array([x])
    x = preprocess_input(x)
    return x

def predict(x, model, mapping):
    pred = model.predict(x)[0]
    max_val = np.where(pred == np.max(pred))[0][0]
    label = mapping[max_val]
    return label

dict = {0:'cup', 1:'fork', 2:'glass', 3:'knife', 4:'plate', 5:'spoon'}

app = Flask('kitchenware')
@app.route("/predict", methods = ['POST'])
def predict_endpoint():
    data = request.get_json()
    path = data['path']
    x = preprocess(path)
    pred = predict(x, model, dict)
    result = jsonify(pred)
    return result


if __name__ == '__main__':
    #path = "C:/Users/Godwin/Downloads/kitchenware-classification/images/train/cup/0082.jpg"
    #x = preprocess(path)
    #pred = predict(x, model, dict)
    #print(pred)
    app.run(debug=True, host = '0.0.0.0', port = 9696)
    #serve(app, port=5000)
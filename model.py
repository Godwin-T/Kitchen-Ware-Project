import tensorflow.lite as tflite
from PIL import Image
import numpy as np
import keras_image_helper

preprocess = keras_image_helper.create_preprocessor('xception', target_size=(299,299))

def preprocess_input(x):
    x = np.array(x, dtype = 'float32')
    x /= 127.5
    x -= 1.
    return x

def predict(url):

    classes =   ['cup',
                'fork',
                'glass', 
                'knife', 
                'plate', 
                'spoon']

    # with Image.open(path) as f:
    #     img = f.resize((299, 299), Image.NEAREST)

    # arr = np.array(img)
    # x = np.array([arr])
    # x = preprocess_input(x)

    x = preprocess.from_url(url)

    interpreter = tflite.Interpreter(model_path = 'C:/Users/Godwin/Downloads/kitchenware-classification1/lite_model.tflite')
    interpreter.allocate_tensors()

    input_index = interpreter.get_input_details()[0]['index']
    output_index = interpreter.get_output_details()[0]['index']

    interpreter.set_tensor(input_index, x)
    interpreter.invoke()

    preds = interpreter.get_tensor(output_index)
    flout_out = preds[0].tolist()
    out = dict(zip(classes, flout_out))
    return out

def lambda_handler(event, context =None):
    url = event['url']
    out = predict(url)
    return out

#path = 'C:/Users/Godwin/Downloads/kitchenware-classification/images/test/0001.jpg'
#print(predict(path))
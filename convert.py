import tensorflow as tf
import keras

model = keras.models.load_model('/content/xception_v5_09_0.944.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite = converter.convert()

with open('model.tflite', 'wb') as f:
    f.write(tflite)
print("Model has successfully been converted and saved as 'model.tflite'")
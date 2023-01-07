FROM tensorflow/serving:2.7.0

COPY utensils models/utensils/1
ENV MODEL_NAME='utensils'
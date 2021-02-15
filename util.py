import base64
from io import BytesIO

import numpy as np
import cv2
from tensorflow import keras
from keras.preprocessing import image
from tqdm import tqdm
from PIL import Image, ImageFile,ImageOps
import tensorflow as tf


__model = None



def get_cv2(b64str):
    encoded_data = b64str.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr,cv2.COLOR_BGR2RGB)
    cv2.imwrite("save.jpeg",img)
    return "save.jpeg"



def convert_image(file):
    train_image = []
    for i in tqdm(range(1)):
        img = image.load_img(file, grayscale=True)
        img = img.resize((256, 256), Image.ANTIALIAS)
        img = image.img_to_array(img)
        img = img / 255
        train_image.append(img)
    x = np.array(train_image)
    return x


def load_artifact():
    print("loading..")
    global __model
    __model=keras.models.load_model("artifacts/model.h5")

def get_b64_blight():
    with open("b64.txt") as f:
        return f.read()



def prediction_class(b64s):
    # re="None"
    prediction=__model.predict_classes(convert_image(get_cv2(b64s)))
    if (prediction[0] == 1):
        re='Leaf Smut'
    if (prediction[0] == 2):
        re='Bacterial Blight'
    if (prediction[0] == 3):
        re='Brown Spot'
    if (prediction[0] == 4):
        re="Sheath Blight"
    if (prediction[0] == 5):
        re = "Tungro"
    if (prediction[0] == 6):
        re = "Healthy"
    return re





if __name__=="__main__":
    load_artifact()
    print(prediction_class(get_b64_blight()))



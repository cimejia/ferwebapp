from flask import Flask, request
from flask_cors import CORS
import torch
import numpy as np
#from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

app = Flask(__name__)
CORS(app)

model = torch.jit.load('model.zip')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/predict", methods=['POST'])
def predict():

    # load image
 #   img = Image.open(request.files['file'].stream).convert('RGB').resize((224, 224))

    img=mpimg.imread(request.files['file'].stream)
    img=img.astype('float32')
    #img=img/255
    

    img = np.array(img)
    img = torch.FloatTensor(img.transpose((2, 0, 1)) / 255)

    # get predictions
    preds = model(img.unsqueeze(0)).squeeze()
    probas = torch.softmax(preds, axis=0)
    ix = torch.argmax(probas, axis=0)

    return {
        'label': model.labels[ix],
        'score': probas[ix].item()
    }

if __name__ == "__main__":
    app.run()
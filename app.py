from flask import Flask
from flask_cors import CORS
from PIL import Image

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/prediction')
def prediction():

    # load image
    #img = Image.open(request.files['file'].stream).convert('RGB').resize((224, 224))
    #img = np.array(img)
    return 'Hello, prediction!'

        
if __name__ == '__main__':
    app.run()
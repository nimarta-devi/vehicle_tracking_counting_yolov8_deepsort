import cv2
from flask import Flask, render_template, request, redirect, Response
from predict import predict
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/prediction', methods=['GET'])
def pred():
    predict()
    return 'Prediction initiated!'

if __name__ == '__main__':
    app.run()

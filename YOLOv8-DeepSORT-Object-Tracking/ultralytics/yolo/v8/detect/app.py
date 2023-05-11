import cv2
from flask import Flask, render_template, request, redirect, Response
from predict import predict, set_path, video_src
app = Flask(__name__)

import logging

import subprocess


# Set the logging level to DEBUG
app.logger.setLevel(logging.DEBUG)

# Configure a stream handler to output log messages to the console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
app.logger.addHandler(stream_handler)
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


# Route for processing video
@app.route('/process_video', methods=['POST'])
def process_video():
    video_file = request.files['video']
    video_path = 'my_video.mp4'  # Provide the path where you want to save the video

    # Save the uploaded video file
    video_file.save(video_path)

    # Open the video using OpenCV
    # cap = cv2.VideoCapture(video_path)
    #video_src = 'video.mp4'  # Set the video source path
    # file = set_path(video_file.filename)

    # video_src= 
    # app.logger.info(file)
    predict()
    # while True:
    #     ret, frame = cap.read()
    #     if not ret:
    #         break


        # Display the processed frame
        # cv2.imshow('Processed Frame', frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    # Release the video capture and destroy any OpenCV windows
    # cap.release()
    # cv2.destroyAllWindows()

    return 'Video processed successfully!'

# @app.route('/prediction', methods=['POST'])
# def process_video():
#     result = subprocess.run(['python', 'predict.py'], capture_output=True, text=True)
#
#     # my_predict =
#     video_file = request.files['video']
#
#     app.logger.debug('Video file path: %s', video_file)
#     app.logger.debug(video_file)
#     return 'No video file selected.'

    # if video_file:
    #     app.logger.debug("inside if condition")
    #
    #     video_file.save('/Users/soorajkumar/Downloads/test/YOLOv8-DeepSORT-Object-Tracking/save_video.mp4')  # Save the video file to disk
    #     # video_src = 'video.mp4'  # Set the video source path
    #     # set_path('video.mp4')
    #     predict()
    #     # predict(cfg)  # Call the predict function with the updated configuration
    #
    #     return 'Video processed successfully.'
    # else:
    #     return 'No video file selected.'




if __name__ == '__main__':
    app.run(debug=True)

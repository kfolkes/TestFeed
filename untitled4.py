from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/home')
def render_home():
    return render_template('home.html')


@app.route('/myclass')
def render_home():
    return render_template('home.html')


import picamera
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording('my_video.h264')
camera.wait_recording(60)
camera.stop_recording()


if __name__ == '__main__':
    app.run()

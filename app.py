import os
import random
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    # Get a list of all the PNG images in the static folder
    static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Static')
    images = os.listdir(static_path)
    png_images = [img for img in images if img.endswith('.png')]

    # Select a random PNG image from the list
    random_png = random.choice(png_images)

    return render_template('index.html',random_png=random_png)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static',path)
if __name__ == '__main__':
    app.run()
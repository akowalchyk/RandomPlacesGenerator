import flask
from flask import Flask, request, jsonify, render_template, flash
from main import get_random_place
from GoogleMapsAPIKey import get_my_key


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'aSldhasldkj'


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/generate',methods=['POST'])
def generate():
    address =  request.form.get('address')
    distance =  request.form.get('distance')
    address = str(address)
    distance = str(distance)
    google_url, photo_url, name, type = get_random_place(address, distance)
    return render_template('index.html', google_url = google_url, photo_url = photo_url, name = name, type = type)


if __name__ == "__main__":
    app.run(debug=True)




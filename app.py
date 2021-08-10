import flask
from flask import Flask, request, jsonify, render_template, flash
from main import get_random_place


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
    random_place = get_random_place(address, distance)
    return render_template('index.html', random_place = random_place)


if __name__ == "__main__":
    app.run(debug=True)




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
    address = str(address)
    type, name = get_random_place(address, '3000')
    return render_template('index.html', random_place= type + ':{}'.format(name))


if __name__ == "__main__":
    app.run(debug=True)




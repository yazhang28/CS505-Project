import jsonschema
from flask import Flask, jsonify, abort, make_response, request, render_template
from flask.ext.httpauth import HTTPBasicAuth
from regression import predictAmountCrimes

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/get_prediction/<district>/<type_crime>/<day>', methods=["GET"])
def get_prediction(district, type_crime, day):
	print(type_crime)
	predictions = predictAmountCrimes(district, type_crime, day)
	return jsonify({'results': predictions})

@app.route('/get_probability/<district>/<type_crime>/<day>', methods=["GET"])
def get_probability(district, type_crime, day):
	predictions = predictProbabilityOfCrime(district, type_crime, int(day))
	return jsonify({'results': predictions})

if __name__ == '__main__':
    app.run(debug=True)



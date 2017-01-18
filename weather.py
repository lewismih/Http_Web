from flask import Flask, render_template, request

# Have a way to Send request to URLs
import requests

app = Flask(__name__)

# opening temperature 
@app.route('/temperature', methods=['POST'])
def temperature():
	zip_code = request.form ['zip']
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zip_code+',us&appid=2299b7747a42a8b86b972374789ef4b6')
	json_object = r.text
	return zip_code

#opening main page i.e index page
@app.toute('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
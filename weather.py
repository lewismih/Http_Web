from flask import Flask, render_template, request
# Have a way to Send request to URLs
import requests


app = Flask(__name__)

# opening temperature 
@app.route('/temperature', methods=['POST'])
def temperature():
	zip_code = request.form['city_id']
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?id='+zip_code+',&appid=2299b7747a42a8b86b972374789ef4b6')
	json_object = r.json()

	#Checks the Temperature
	temp_k = str(json_object['main']['temp'])

	#Checks the Humidity
	temp_m = str(json_object['main']['humidity'])
	
	#return str(json_object)
	return render_template('temperature.html', temp=temp_k,  temp2=temp_m)

#opening main page i.e index page
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
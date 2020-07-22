from flask import Flask, send_from_directory, request, jsonify
from astral.sun import sun
from astral import LocationInfo, Observer
from countryinfo import CountryInfo
import datetime
import json

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/get_sunrise", methods = ['POST'])
def sunrise():
	req_data = json.loads(request.data)
	print(req_data)
	data = {"sunrise": "", "sunset": ""}
	if request.method == 'POST':
		date = datetime.datetime.strptime(req_data.get("time"), '%Y-%m-%d')

		country_info = CountryInfo(req_data.get('country'))

		s = sun(Observer(*country_info.capital_latlng()), date=date)
		print(s["sunrise"])
		data = {"sunrise":f'{s["sunrise"].hour}:{s["sunrise"].minute}', 
				"sunset":f'{s["sunset"].hour}:{s["sunset"].minute}'}
	
	return data


if __name__ == "__main__":
    app.run(debug=True)
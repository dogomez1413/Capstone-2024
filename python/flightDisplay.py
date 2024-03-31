from flask import Flask 
# from main import create_flight_table
from flask import render_template, request

from main import create_flight_table

# creates a Flask application 
app = Flask(__name__) 


@app.route("/", methods=["GET","POST"]) 
def hello(): 
	# print(request.form.get("airport"))
	# print(request.form.get("departure"))
	# print(request.form.get("return"))
	message = "Hello, World"
	if request.method == "POST":
		create_flight_table('MYR', request.form.get("airport"), request.form.get("departure"), request.form.get("return"))
	return render_template('index.html', message=message)

# run the application 
if __name__ == "__main__": 
	app.run(debug=True)

from flask import Flask 
from flask import render_template, request

# creates a Flask application 
app = Flask(__name__) 


@app.route("/", methods=["GET","POST"]) 
def hello(): 
	print(request.form.get("date"))
	message = "Hello, World"
	return render_template('index.html', message=message) 

# run the application 
if __name__ == "__main__": 
	app.run(debug=True)

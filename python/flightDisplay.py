from flask import Flask, flash, redirect
from flask import render_template, request
from main import create_flight_table

# creates a Flask application 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the-most-secret-key'


@app.route("/", methods=["GET", "POST"])
def hello():
    # Triggers when form is submitted.
    if request.method == "POST":
        # Updates table and sends user to other page
        try:
            create_flight_table('MYR', request.form.get("airport"), request.form.get("departure"),
                                request.form.get("return"))
            return render_template('table.html')
        except Exception as e:
            print("Caught error: ", e)
            flash("Error: Invalid input or no flights found. Please try again.")
            return render_template('index.html')
    return render_template('index.html')


# run the application
if __name__ == "__main__":
    app.run(debug=True)

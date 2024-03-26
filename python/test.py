from flask import Flask, request, render_template

app = Flask(__name__)


# Defining the home page of our site
@app.route("/", methods=["GET", "POST"])  # this sets the route to this page
def gfg():
    if request.method == "POST":
        date = request.form.get("date")
        return "the form date is: " + date
    return render_template("index.html")


if __name__ == "__main__":
    app.run()

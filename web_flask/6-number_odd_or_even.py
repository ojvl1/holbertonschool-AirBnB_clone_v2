#!/usr/bin/python3
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<n>", strict_slashes=False)
def number_n(n):
    if n.isdigit():
        return f"{n} is a number"
    else:
        return "404 not found"


@app.route("/number_template/<n>")
def number_template_n(n):
    if n.isdigit():
        return render_template("5-number.html", number=n)
    else:
        return "404 not found"


@app.route("/number_odd_or_even/<n>")
def odd_or_even_n(n):
    if n.isdigit():
        n = int(n)
        n_type = "odd"
        if n % 2 == 0:
            n_type = "even"
        return render_template(
            "6-number_odd_or_even.html", number=n, number_type=n_type
        )
    else:
        return "404 not found"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

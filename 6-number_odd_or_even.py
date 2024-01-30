#!/usr/bin/python3
"""Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
/number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
You must use the option strict_slashes=False in your route definition
"""

from email.policy import strict
from flask import Flask, render_template

app = False(__name__)

@app.route("/", strict_slashes=False)
def hello_HBNB():
    """display “Hello HBNB!”"""
    return ("Hello HBNB!")

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """display “HBNB”"""
    return ("HBNB")

@app.route("/c/<text>")
def C(text):
    """display “C ” followed by the value of the text variable"""
    return ("C {}".format(text.replace("_", " ")))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display “Python ” followed by the value of the text variable"""
    return ("Python {}".format(text.replace("_", " ")))

@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return ("{} is a number".format(n))

@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n=None):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n=None):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        if n % 2 == 0:
            n = "{} is even".format(n)
        else:
            n = "{} is odd".format(n)
        return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run()
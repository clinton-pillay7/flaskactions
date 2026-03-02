"""
app.py
This module contains the Flask application setup and routes.
"""

from flask import Flask

app = Flask(__name__)



@app.route("/")
def hello_world():
    """ Home Function """
    return "Hello earth!!!! - see what SSH did - with versioning this time"



@app.route('/contact')
def contact():
    """ Contact function """
    return "Contact us at email: support@example.com"

if __name__ == "__main__":
    # host="0.0.0.0" makes it accessible on the machine's IP
    # debug=True is optional, useful during development
    app.run(host="0.0.0.0", port=5000, debug=True)

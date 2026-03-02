from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello earth!!!! - see what SSH did - with versioning this time"

@app.route('/contact')
def contact():
    return "Contact us at support@example.com"

if __name__ == "__main__":
    # host="0.0.0.0" makes it accessible on the machine's IP
    # debug=True is optional, useful during development
    app.run(host="0.0.0.0", port=5000, debug=True)

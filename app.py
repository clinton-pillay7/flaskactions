from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, earth!!!!"

if __name__ == "__main__":
    # host="0.0.0.0" makes it accessible on the machine's IP
    # debug=True is optional, useful during development
    app.run(host="0.0.0.0", port=5000, debug=True)

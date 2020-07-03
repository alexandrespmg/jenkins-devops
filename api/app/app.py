from flask import Flask
app = Flask(__name__)

@app.route("/hi")
def hello():
    return "Hello World from Flask"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', port=80)

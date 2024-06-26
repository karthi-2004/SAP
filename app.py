from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
# Assuming get_response is defined somewhere
from chat import get_response  

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Assuming get_response function is defined
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)

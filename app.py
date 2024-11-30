from flask import Flask, render_template, request, jsonify
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load ML model
model = joblib.load("model/model.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.json["message"]
    prediction = model.predict([user_input])[0]
    return jsonify({"response": f"A suitable career for you could be in {prediction}."})

if __name__ == "__main__":
    app.run(debug=True)

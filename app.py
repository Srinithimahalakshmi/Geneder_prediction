# app.py
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/decision_tree_model.pkl")
features = joblib.load("model/features.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    input_data = dict.fromkeys(features, "")

    if request.method == "POST":
        input_data = {feature: request.form[feature] for feature in features}
        values = [float(input_data[feature]) for feature in features]
        result = model.predict([values])[0]
        prediction = "Female" if result == 1 else "Male"

    return render_template("index.html", features=features, input_data=input_data, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

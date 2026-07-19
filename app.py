from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("flood_model.joblib")
scaler = joblib.load("scaler.joblib")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [
            float(request.form["Temp"]),
            float(request.form["Humidity"]),
            float(request.form["Cloud Cover"]),
            float(request.form["ANNUAL"]),
            float(request.form["Jan-Feb"]),
            float(request.form["Mar-May"]),
            float(request.form["Jun-Sep"]),
            float(request.form["Oct-Dec"]),
            float(request.form["avgjune"]),
            float(request.form["sub"])
        ]

        features = np.array(features).reshape(1, -1)
        features = scaler.transform(features)

        prediction = model.predict(features)

        if prediction[0] == 1:
            result = "Flood Risk"
        else:
            result = "No Flood Risk"

        return render_template("index.html", prediction=result)

    except Exception as e:
        return render_template("index.html", prediction=f"Error: {e}")


if __name__ == "__main__":
    app.run(debug=True)

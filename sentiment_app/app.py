from flask import Flask, render_template, request
import pickle

# Load model + vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    review_text = ""

    if request.method == "POST":
        review_text = request.form["review"]
        if review_text.strip():
            transformed = vectorizer.transform([review_text])
            prediction = model.predict(transformed)[0]

    return render_template("index.html", prediction=prediction, review=review_text)

if __name__ == "__main__":
    app.run(debug=True)

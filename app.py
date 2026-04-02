from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Analyze sentiment
@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form["text"]
    
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        result = "Positive 😊"
    elif polarity < 0:
        result = "Negative 😞"
    else:
        result = "Neutral 😐"

    return render_template("index.html", result=result, text=text)


# IMPORTANT (this was missing)
if __name__ == "__main__":
    app.run(debug=True)
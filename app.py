from flask import Flask, render_template, request
import google.generativeai as palm  # Ensure this is a valid import
import os
from textblob import TextBlob

app = Flask(__name__)

# Fetching the API key from environment variables
api = os.getenv("MAKERSUITE_API_TOKEN")
if not api:
    raise ValueError("MAKERSUITE_API_TOKEN is not set in environment variables.")

# Configure the API key for Google Generative AI
palm.configure(api_key=api)
model = {"model": "models/chat-bison-001"}

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/financial_FAQ", methods=["GET", "POST"])
def financial_FAQ():
    return render_template("financial_FAQ.html")

@app.route("/makersuite", methods=["GET", "POST"])
def makersuite():
    q = request.form.get("q")
    r = palm.chat(messages=q, **model)
    return render_template("makersuite.html", r=r.last)

@app.route("/sentiment_analysis", methods=["GET", "POST"])
def sentiment_analysis():
    return render_template("sentiment_analysis.html")

@app.route("/transfer_money", methods=["GET", "POST"])
def transfer_money():
    return render_template("transfer_money.html")

@app.route("/sentiment_analysis_result", methods=["GET", "POST"])
def sentiment_analysis_result():
    text = request.form.get("q")
    sentiment_result = TextBlob(text).sentiment
    return render_template("sentiment_analysis_result.html", sentiment=sentiment_result)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

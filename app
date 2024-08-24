from flask import Flask, render_template, request
import google.generativeai as palm
import os

# Fetching the API key from environment variables
api = os.getenv("MAKERSUITE_API_TOKEN")
if not api:
    print("Error: MAKERSUITE_API_TOKEN is not set.")
    exit(1)

# Configure the API key for Google Generative AI
palm.configure(api_key=api)
model = {"model": "models/chat-bison-001"}

app = Flask(__name__)

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

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

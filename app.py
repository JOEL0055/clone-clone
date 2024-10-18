from flask import Flask, render_template, request
import requests
from textblob import TextBlob

api = os.getenv("MAKERSUITE")
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

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
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": q}
                ]
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        generated_response = response.json()['candidates'][0]['content']['parts'][0]['text']
        sentiment = TextBlob(q).sentiment
    except Exception as e:
        generated_response = f"An error occurred: {str(e)}"
        sentiment = None
    
    return render_template("makersuite.html", response=generated_response, sentiment=sentiment)

@app.route("/transfer_money", methods=["GET", "POST"])
def transfer_money():
    if request.method == "POST":
        # You would handle the money transfer logic here
        amount = request.form.get("amount")
        to_account = request.form.get("to_account")
        # Fake transfer success for the example
        transfer_status = f"Successfully transferred ${amount} to account {to_account}."
        return render_template("transfer_result.html", status=transfer_status)
    return render_template("transfer_money.html")

if __name__ == "__main__":
    app.run()

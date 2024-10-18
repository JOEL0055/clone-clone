from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder="/Users/joelaiweithai/Downloads/BC3411/templates")

api_key = "AIzaSyD8ocNijPFuNfaae5VDChD9jG2cXd12G50"
model_id = "gemini-1.5-flash-latest"
url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_id}:generateContent?key={api_key}"

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
        result = response.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        result = f"An error occurred: {str(e)}"
    
    return render_template("makersuite.html", r=result)

if __name__ == "__main__":
    app.run()

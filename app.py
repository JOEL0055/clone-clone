from flask import Flask, render_template, request
import google.generativeai as genai
import textblob
import os

# Load the API key from environment variables
api = os.getenv("MAKERSUITE")
if not api:
    raise ValueError("The API key is not set. Make sure the 'MAKERSUITE' environment variable is loaded.")

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

    if not q:
        return render_template("makersuite.html", r="Please provide a query.")

    try:
        # Attempt to generate content using the AI model
        response = model.generate_content(q)
        r = response.text if hasattr(response, 'text') else "No content found in response."
    except Exception as e:
        # Catch any exception and display an error message
        r = f"An error occurred: {str(e)}"
    
    return render_template("makersuite.html", r=r)

@app.route("/sentiment_analysis", methods=["GET", "POST"])
def sentiment_analysis():
    return render_template("sentiment_analysis.html")

@app.route("/transfer_money", methods=["GET", "POST"])
def transfer_money():
    return render_template("transfer_money.html")

@app.route("/sentiment_analysis_result", methods=["GET", "POST"])
def sentiment_analysis_result():
    q = request.form.get("q")

    if not q:
        return render_template("sentiment_analysis_result.html", r="Please provide text for analysis.")
    
    try:
        # Perform sentiment analysis using TextBlob
        analysis = textblob.TextBlob(q).sentiment
        r = {
            'polarity': analysis.polarity,
            'subjectivity': analysis.subjectivity
        }
    except Exception as e:
        r = f"An error occurred during sentiment analysis: {str(e)}"
    
    return render_template("sentiment_analysis_result.html", r=r)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import google.generativeai as genai
import textblob
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Get the API key from the environment variable
api = os.getenv("MAKERSUITE")
if not api:
    raise ValueError("API key for Makersuite is not set")
genai.configure(api_key=api)

# Initialize the model
try:
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    logging.error(f"Error initializing model: {e}")
    raise

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/financial_FAQ", methods=["GET", "POST"])
def financial_FAQ():
    return render_template("financial_FAQ.html")

@app.route("/makersuite", methods=["GET", "POST"])
def makersuite():
    try:
        # Extract user input from the form
        q = request.form.get("q")
        if not q:
            raise ValueError("No query provided")

        # Generate content using the model
        r = model.generate_content(q)
        
        # Ensure the response has the correct structure
        if hasattr(r, 'text'):
            return render_template("makersuite.html", r=r.text)
        else:
            logging.error("Model response does not have a 'text' attribute")
            return render_template("makersuite.html", r="Invalid response from the model")
    
    except Exception as e:
        # Log the error and return a user-friendly message
        logging.error(f"Error in /makersuite: {e}")
        return render_template("makersuite.html", r="An error occurred")

@app.route("/sentiment_analysis", methods=["GET", "POST"])
def sentiment_analysis():
    return render_template("sentiment_analysis.html")

@app.route("/transfer_money", methods=["GET", "POST"])
def transfer_money():
    return render_template("transfer_money.html")

@app.route("/sentiment_analysis_result", methods=["GET", "POST"])
def sentiment_analysis_result():
    try:
        # Extract user input from the form
        q = request.form.get("q")
        if not q:
            raise ValueError("No text provided for sentiment analysis")

        # Perform sentiment analysis using TextBlob
        r = textblob.TextBlob(q).sentiment
        return render_template("sentiment_analysis_result.html", r=r)
    
    except Exception as e:
        # Log the error and return a user-friendly message
        logging.error(f"Error in /sentiment_analysis_result: {e}")
        return render_template("sentiment_analysis_result.html", r="An error occurred during sentiment analysis")

if __name__ == "__main__":
    app.run(debug=True)

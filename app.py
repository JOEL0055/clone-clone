from flask import Flask,render_template,request
import google.generativeai as genai
import textblob
import os

api = os.getenv("MAKERSUITE")
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/financial_FAQ",methods=["GET","POST"])
def financial_FAQ():
    return(render_template("financial_FAQ.html"))

@app.route("/makersuite",methods=["GET","POST"])
def makersuite():
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("makersuite.html",r=r.text))

@app.route("/sentiment_analysis",methods=["GET","POST"])
def sentiment_analysis():
    return(render_template("sentiment_analysis.html"))

@app.route("/transfer_money",methods=["GET","POST"])
def transfer_money():
    return(render_template("transfer_money.html"))

@app.route("/sentiment_analysis_result",methods=["GET","POST"])
def sentiment_analysis_result():
    q = request.form.get("q")
    r=textblob.TextBlob(q).sentiment
    return(render_template("sentiment_analysis_result.html",r=r))

if __name__ == "__main__":
    app.run()

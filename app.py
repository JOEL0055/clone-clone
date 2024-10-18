from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/sentiment_analysis", methods=["POST"])
def sentiment_analysis():
    # Assuming you process and redirect or you can use AJAX to stay on the page
    text = request.form['text']
    sentiment_result = analyze_sentiment(text)
    return render_template("index.html", r=sentiment_result)

@app.route("/transfer_money", methods=["POST"])
def transfer_money():
    # Process and show results
    return render_template("index.html")

@app.route("/financial_FAQ", methods=["POST"])
def financial_faq():
    # Show FAQs or redirect
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


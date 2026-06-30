from flask import Flask, render_template
app= Flask(__name__)
# print(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/learnmore")
def learnmore():
    return render_template("learnmore.html")

@app.route("/webscraping")
def webscraping():
    return render_template("webscraping.html")

@app.route("/static-web-scraping")
def static_web_scraping():
    return render_template("static-web-scraping.html")

if(__name__ == "__main__"):
     app.run(debug= True)
    
"""Main."""
from flask import Flask, render_template
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("test.log")
logger.addHandler(file_handler)

app = Flask(__name__)


@app.route("/")
def index():
    title = "Home Page"
    return render_template('index.html', title=title)

@app.route("/about")
def about():
    title = "About us"
    return render_template('about.html', title=title)

@app.route("/contact")
def contact():
    title = "Contact Us"
    return render_template('contact.html', title=title)

if __name__ == "__main__":
    app.run()

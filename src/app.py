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
    programming_languages = [
        "Python",
        "Java",
        "Javascript"
    ]
    return render_template('index.html', title=title, programming_languages=programming_languages)


if __name__ == "__main__":
    app.run()

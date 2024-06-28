from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

@app.route('/')
def index():
    return render_template("main_page.html")


@app.route('/skills')
def about():
    return render_template("skills.html")


@app.route('/contact')
def a():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)

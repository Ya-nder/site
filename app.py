from flask import Flask, render_template

app = Flask(__name__)

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

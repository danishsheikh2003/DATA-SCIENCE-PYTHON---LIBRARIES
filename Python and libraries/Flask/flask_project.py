from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('test.html')

@app.route("/about")
def hello_home():
    return render_template('raza.html')

@app.route("/<name>")
def user(name):
    return f"Ha Bol be Jhatu {name}"

@app.route("/about/test")
def about():
    return redirect(url_for("home"))

@app.route("/simple")
def game():
    return render_template('Backhodi.html')


@app.route("/games")
def games():
    return render_template('Game.html')

if __name__ == "__main__":
    app.run(debug=True)


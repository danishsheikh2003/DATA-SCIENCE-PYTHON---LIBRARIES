from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/home")
def hello_home():
    return "Ky Re Bosdike aa gya apni gand marane"

@app.route("/<name>")
def user(name):
    return f"Ha Bol be Jhatu {name}"

if __name__ == "__main__":
    app.run(debug=True)
ve    
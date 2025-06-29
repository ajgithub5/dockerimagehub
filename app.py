from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Everyone!! This is used to create my app for understanding the gtihub actions."


if __name__=="__main__":
    app.run(host="0.0.0.0",port = 8000)
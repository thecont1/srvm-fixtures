from flask import Flask

app = Flask(__name__)


@app.get("/")
def hello():
    return "<h1>04 - flask</h1><p>Served by srvm's flask fixture.</p>"


if __name__ == "__main__":
    app.run(debug=True)

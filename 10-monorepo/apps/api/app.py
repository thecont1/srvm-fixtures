from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(service="api", fixture="10-monorepo", status="ok")


if __name__ == "__main__":
    app.run(debug=True)

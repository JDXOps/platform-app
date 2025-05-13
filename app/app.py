import logging
from flask import Flask

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route("/")
def index():
    message = "JDXOps demo app running on Kubernetes =)!"
    return f"<h1>{message}</h1>"


@app.route("/livez")
def liveness_check():
    return "OK", 200


@app.route("/readyz")
def readiness_check():
    return "READY", 200


if __name__ == "__main__":
    # Start Flask App
    app.logger.info("Starting Flask application")
    app.run(host="0.0.0.0", port=5000)

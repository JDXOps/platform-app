import logging
from flask import Flask

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route("/")
def index():

    message = "Flask app running on Kubernetes =)!"
    return f"<h1>{message}</h1>"


if __name__ == "__main__":
    # Start Flask App
    app.logger.info("Starting Flask application")
    app.run(host="0.0.0.0", port=5000)

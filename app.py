import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 CI/CD TEST SUCCESS</h1>
    <p>This update proves Cloud Build auto-deployment is working.</p>
    <p>If you see this, GitHub → Cloud Build → Cloud Run is active.</p>
    """

@app.route("/about")
def about():
    return """
    <h2>About</h2>
    <p>I am learning Flask, Docker, and Google Cloud Run.</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
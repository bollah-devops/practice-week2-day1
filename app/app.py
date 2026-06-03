import os
from flask import Flask, jsonify

app = Flask(__name__)

ENV_NAME = os.getenv("ENV_NAME", "staging")
VERSION = os.getenv("VERSION", "1.0.0")

@app.route("/")
def home():
    return f"""
      <html>
        <body style="font-family: Arial; background-color: #f4f4f4; text-align: center;">
            <h1 style="color: navy;">Welcome to Blog Platform</h1>
            <p style="font-size: 18px; color: #555;">
                This is my Flask application.
            </p>
        </body>
    </html>
"""

@app.route("/about")
def about():
    return """
    <body style="font-family: Arial, sans-serif; background:#eef2f7; text-align:center; padding:50px;">
        <div style="background:white; padding:30px; border-radius:10px; width:60%; margin:auto;">
            <h1 style="color:#34495e;">About Us</h1>
            <p style="font-size:18px;">
                Blog Platform is a simple Flask application built to share
                articles about DevOps, Cloud Computing, Linux, and Automation.
            </p>

            <a href="/">Home</a>
        </div>
    </body>
    """
    
    
@app.route("/blog")
def blog():
    return """
    <body style="font-family: Arial, sans-serif; background:#fafafa; padding:50px;">
        <div style="background:white; padding:30px; border-radius:10px; width:70%; margin:auto;">
            <h1 style="text-align:center; color:#2c3e50;">Latest Blog Posts</h1>

            <div style="border-bottom:1px solid #ddd; padding:15px;">
                <h2>Getting Started with Terraform</h2>
                <p>Learn how Infrastructure as Code simplifies cloud deployments.</p>
            </div>

            <div style="border-bottom:1px solid #ddd; padding:15px;">
                <h2>Docker Essentials</h2>
                <p>Containerize your applications for consistent deployments.</p>
            </div>

            <div style="padding:15px;">
                <h2>Monitoring with Bash Scripts</h2>
                <p>Build lightweight monitoring solutions using shell scripting.</p>
            </div>

            <p style="text-align:center;">
                <a href="/">Home</a>
            </p>
        </div>
    </body>
    """

    
@app.route("/health")
def health():
    return {
        "healthy": True
    }, 200
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)    
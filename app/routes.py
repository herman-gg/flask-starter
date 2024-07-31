from flask import render_template
from app import app


@app.route("/health")
def health():
    return render_template("status.html", status="ok")
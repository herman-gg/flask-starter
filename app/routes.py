from app import app


@app.route("/health")
def health():
    return "OK"
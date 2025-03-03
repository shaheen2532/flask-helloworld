from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.getenv("NAME")
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
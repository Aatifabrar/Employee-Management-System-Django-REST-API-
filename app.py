from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hello, World! Your Flask API is working 🚀"}

if __name__ == "__main__":
    app.run(debug=True)

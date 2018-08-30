from flask import Flask
app = Flask(__name__)

@app.route("/")
# CODE GOES HERE

if __name__ == "__main__":
    app.run(port=5000,debug=False)

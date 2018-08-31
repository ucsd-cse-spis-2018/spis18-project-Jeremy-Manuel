from flask import flask
app = Flask(__name__)

@app.route("/")
def Hello():
    return "Hello World!"

<input type="submit" name="0" value="0">
<input type="submit" name="1" value="1">
<input type="submit" name="2" value="2">
<input type="submit" name="3" value="3">
<input type="submit" name="4" value="4">
<input type="submit" name="5" value="5">
<input type="submit" name="6" value="6">
<input type="submit" name="7" value="7">
<input type="submit" name="8" value="8">
<input type="submit" name="9" value="9">
<input type="submit" name="=" value="=">
<input type="submit" name="+" value="+">
<input type="submit" name="-" value="-">
<input type="submit" name="x" value="*"> # shud i just change x to *
<input type="submit" name="/" value="/">
<input type="submit" name="/" value="/">

if __name__ == "__main__":
    app.run(port=5000,debuf =False)

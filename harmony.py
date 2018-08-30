import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')
# CODE GOES HERE

@app.route("/colorpick")
def render_colorpick():
    return render_template('colorpick.html')

@app.route("/colorresult")
def render_colorResults():
    try:
        color_result = float(request.args['inColor'])
        # PROCESS COLOR
        return render_template('colorResult.html', inColor=color_result, compColor=comp_result)
    except ValueError:
        return "Sorry: something went wrong."

if __name__ == "__main__":
    app.run(port=5000,debug=False)

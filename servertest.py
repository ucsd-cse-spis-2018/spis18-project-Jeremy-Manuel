import os
from jinja2 import Environment, FileSystemLoader
from flask import Flask, send_from_directory, jsonify, request, render_template, url_for
import flask
from flask import Flask
from flask import request

app = Flask(__name__)
# app.config.from_object(__name__)
#
# @app.route('/')
# def index():
#     return send_from_directory("templates", "index.html")
#
# @app.route('/<string:name>')
# def static_files(name):
#     return send_from_directory("templates", name)
#
# @app.route('/hello')
# def hello():
#     result="Hey, I saw that! You clicked at {}".format(datetime.datetime.now())
#     return jsonify(result=result)
num0 = ""
num1 = ""
@app.route('/')
def gotoCalculator():
    return render_template ("testHome.html")

@app.route('/json')
def json():
    return render_template('json2.html')
@app.route ('/background_process_test')
def background_process_test():
    #tempResult = 0
    if request.method == "POST":
        tempResult = request.form.get("TEST")
        print("hhhhh")
    #print(tempResult)
    print ("Hello")
    return "nothing"


@app.route('/test', methods=['GET', 'POST'])
def testcalc():
    #if request.method == 'POST':

    return render_template("test.html")
@app.route("/forward/", methods = ['POST'])
def afunction():
    print("FUCK")
    forward_message = "FUCK"
    return render_template ('test.html', message=forward_message)



if __name__ == "__main__":
    app.run(port=5000,debug =False)

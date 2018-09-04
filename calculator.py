import os
#from tkinter import Button
from jinja2 import Environment, FileSystemLoader
from flask import Flask, url_for, render_template, request
app = Flask(__name__)

result = 0
value1= ""
value2 = ""

def clever_function():
    print("WOOOOOOOOO")
    #return u'HELLO'

app.jinja_env.globals.update(clever_function=clever_function)

@app.route("/fuck")
def tester():

    return render_template("test.html")


@app.route("/")
def Hello():
    return "Hello World!"
#@app.route("/calculation")
"""def grabValue():
    global value1
    global value2
    try:
        value1 = int(request.args['zero'])"""
@app.route("/my-link/")
def tester():
    value = 0
    print(value)

@app.route("/buttons", methods=['GET','POST'])
def buttons():
    global value1
    global value2

    runTime = 0
    if request.method == 'POST':
        if request.form.get(pleaseWork) == '':
            pass
        else:
            value1 = request.form.get(pleaseWork)

    #return render_template("buttons.html")
    """if request.method == 'POST':
        if request.form.get ('zero') == '0':
            print(0)
            value0 =
        elif request.form['submit'] == '':
            #pass
            print(1)
        else:
            print(2)
    elif request.method =='GET':
        print(3)"""

    if request.method == 'post':
        print('post')
        #print(request.form.get)
    #if request.form.get(*arg) !=
        if value1 == "":

            value1 = request.form.get ('value0')
            print("value1")
            print(value1)
            #return (value1)


        elif value2 == "":
            value2 = request.form.get('value0')
            print("value2")
            print(value2)
            #return (value2)
        # else:
        #     value1 = ""
        #     value2 = ""


        #return render_tempate ('buttons.html', form=form)

    return render_template("buttons.html")

def hello():
    print("hello")
def multiplication (x,y):
    global result
    result = x * y



def addition (x,y):
    global result
    result = x + y

def subtraction (x,y):
    global result
    result = x - y

def division (x,y):
    global result
    result = x / y

def remainder(x,y):
    global result
    result = x%y

def result ():
    global value1
    global value2





if __name__ == "__main__":
    app.run(port=5000,debug =False)

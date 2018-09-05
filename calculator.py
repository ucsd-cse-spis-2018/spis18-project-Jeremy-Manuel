import os
from jinja2 import Environment, FileSystemLoader
from flask import Flask, url_for, render_template, request
app = Flask(__name__)

result = ""
value1= "0"
value2 = ""
first = 1
operation = 0
more = 0


@app.route("/")
def Hello():
    return "Hello World!"

@app.route("/buttons", methods=['GET','POST'])
def buttons():
    global value1
    global value2
    global first
    global result
    global operation
    global more

    # clears everything to start over
    if 'clear' in request.args:
        value1 = str("0")
        value2 = ""
        result =""
        operation = 0
        first = 1
        print("clear works")

    # allows users to continue doing computations
    if result != "":
        if more == 0:
            if 'value00' in request.args:
                value1 = result
                more = 1
                value2 = ""
                value2 +="0"
                print(value2)
            elif 'value01' in request.args:
                value1 = result
                more = 1
                value2 = ""
                value2 +="1"
                print(value2)
            elif 'value02' in request.args:
                value1 = result
                more = 1
                value2 = ""
                value2 +="2"
                print(value2)
            elif 'value03' in request.args:
                value1 = result
                more = 1
                value2 = ""
                value2 +="3"
                print(value2)
            elif 'value04' in request.args:
                value1 = result
                more = 1
                value2 = ""
                value2 +="4"
                print(value2)
            elif 'value05' in request.args:
                value1 = result
                more = 1
                value2 = ""
                value2 +='5'
                print(value2)
            elif 'value06' in request.args:
                value1 = result
                more = 1
                value2 = ""
                value2 +='6'
                print(value2)
            elif 'value07' in request.args:
                value1 = result
                more = 1
                value2 = ""
                value2 +='7'
                print(value2)
            elif 'value08' in request.args:
                value1 = result
                more = 1
                value2 = ""
                value2 +='8'
                print(value2)
            elif 'value09' in request.args:
                value1 = result
                more = 1
                value2 = ""
                value2 +='9'
                print(value2)
            elif 'decimal' in request.args:
                value1 = result
                more = 1
                value2 += '.'
                print(value2)
        elif more == 1:
            if 'value00' in request.args:
                value1 = result
                value2 +="0"
                print(value2)
            elif 'value01' in request.args:
                value1 = result
                value2 +="1"
                print(value2)
            elif 'value02' in request.args:
                value1 = result
                value2 +="2"
                print(value2)
            elif 'value03' in request.args:
                value1 = result
                value2 +="3"
                print(value2)
            elif 'value04' in request.args:
                value1 = result
                value2 +="4"
                print(value2)
            elif 'value05' in request.args:
                value1 = result
                value2 +='5'
                print(value2)
            elif 'value06' in request.args:
                value1 = result
                value2 +='6'
                print(value2)
            elif 'value07' in request.args:
                value1 = result
                value2 +='7'
                print(value2)
            elif 'value08' in request.args:
                value1 = result
                value2 +='8'
                print(value2)
            elif 'value09' in request.args:
                value1 = result
                value2 +='9'
                print(value2)
            elif 'decimal' in request.args:
                value1 = result
                value2 += '.'
                print(value2)



    #If you click equals, does the math
    if 'equals' in request.args:
        print("equals")
        if value1 != "" and value2 != "":
            print("has both values")
            more = 0
            if operation == "+":
                result = float(value1) + float(value2)
                print (result)
                operation = 0
            elif operation == "*":
                result = float(value1) * float(value2)
                print (result)
                operation = 0
            elif operation == "-":
                result = float(value1) - float(value2)
                print (result)
                operation = 0
            elif operation == "/":
                result = float(value1) / float(value2)
                print (result)
                operation = 0

    #chooses operand
    if 'addition' in request.args:
        operation = "+"
        first = 0
        print(operation)
    if 'subtraction' in request.args:
        operation = "-"
        first = 0
        print(operation)
    if 'multiplication' in request.args:
        operation = "*"
        first = 0
        print(operation)
    if 'division' in request.args:
        operation = "/"
        first = 0
        print(operation)

    #Checks if a number needs to replace 0
    if value1 == "0":
        if first == 1:
            if 'value00' in request.args:
                print("first click")
                value1 = ""
                value1 +="0"
                print(value1)
            elif 'value01' in request.args:
                value1 = ""
                value1 +="1"
                print(value1)
            elif 'value02' in request.args:
                value1 = ""
                value1 +="2"
                print(value1)
            elif 'value03' in request.args:
                value1 = ""
                value1 +="3"
                print(value1)
            elif 'value04' in request.args:
                value1 = ""
                value1 +="4"
                print(value1)
            elif 'value05' in request.args:
                value1 = ""
                value1 +='5'
                print(value1)
            elif 'value06' in request.args:
                value1 = ""
                value1 +='6'
                print(value1)
            elif 'value07' in request.args:
                value1 = ""
                value1 +='7'
                print(value1)
            elif 'value08' in request.args:
                value1 = ""
                value1 +='8'
                print(value1)
            elif 'value09' in request.args:
                value1 = ""
                value1 +='9'
                print(value1)
            elif 'decimal' in request.args:
                value1 = ""
                value1 += '.'
                print(value1)

    #checks if second number 0 needs to be replaced
    elif value2 == "0":
        if first == 0:
            if 'value00' in request.args:
                value2 = ""
                value2 +="0"
                print(value2)
            elif 'value01' in request.args:
                value2 = ""
                value2 +="1"
                print(value2)
            elif 'value02' in request.args:
                value2 = ""
                value2 +="2"
                print(value2)
            elif 'value03' in request.args:
                value2 = ""
                value2 +="3"
                print(value2)
            elif 'value04' in request.args:
                value2 = ""
                value2 +="4"
                print(value2)
            elif 'value05' in request.args:
                value2 = ""
                value2 +='5'
                print(value2)
            elif 'value06' in request.args:
                value2 = ""
                value2 +='6'
                print(value2)
            elif 'value07' in request.args:
                value2 = ""
                value2 +='7'
                print(value2)
            elif 'value08' in request.args:
                value2 = ""
                value2 +='8'
                print(value2)
            elif 'value09' in request.args:
                value2 = ""
                value2 +='9'
                print(value2)
            elif 'decimal' in request.args:
                value2 = ""
                value2 += '.'
                print(value2)

    # if no numbers need to be replaced, place value
    else:
        if first == 1:
            if 'value00' in request.args:
                value1 +='0'
                print(value1)
            elif 'value01' in request.args:
                value1 +='1'
                print(value1)
            elif 'value02' in request.args:
                value1 +='2'
                print(value1)
            elif 'value03' in request.args:
                value1 +='3'
                print(value1)
            elif 'value04' in request.args:
                value1 +='4'
                print(value1)
            elif 'value05' in request.args:
                value1 +='5'
                print(value1)
            elif 'value06' in request.args:
                value1 +='6'
                print(value1)
            elif 'value07' in request.args:
                value1 +='7'
                print(value1)
            elif 'value08' in request.args:
                value1 +='8'
                print(value1)
            elif 'value09' in request.args:
                value1 +='9'
                print(value1)
            elif 'decimal' in request.args:
                value1 += '.'
                print(value1)
        elif first == 0 and result == "":
            if 'value00' in request.args:
                value2 +='0'
                print(value2)
            elif 'value01' in request.args:
                value2 +='1'
                print(value2)
            elif 'value02' in request.args:
                value2 +='2'
                print(value2)
            elif 'value03' in request.args:
                value2 +='3'
                print(value2)
            elif 'value04' in request.args:
                value2 +='4'
                print(value2)
            elif 'value05' in request.args:
                value2 +='5'
                print(value2)
            elif 'value06' in request.args:
                value2 +='6'
                print(value2)
            elif 'value07' in request.args:
                value2 +='7'
                print(value2)
            elif 'value08' in request.args:
                value2 +='8'
                print(value2)
            elif 'value09' in request.args:
                value2 +='9'
                print(value2)
            elif 'decimal' in request.args:
                value2 += '.'
                print(value2)

    return render_template("buttons.html")



if __name__ == "__main__":
    app.run(port=5000,debug =False)

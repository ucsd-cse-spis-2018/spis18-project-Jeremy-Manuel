import os
from flask import Flask, url_for, render_template, request
app = Flask(__name__)

value=""
temp = ""
operation = ""

@app.route("/")
def calculate():
    global value
    global temp
    global operation
    # htmlresult = str(request.args['telnum'])
    htmlreturn = temp
    print('htmlreturn')


    if 'value00' in request.args:
        if temp != "" and operation == "":
            temp = ""
            value += '0'
        else:
            if value == "":
                value += '0'
                print(value)
            elif value == "0":
                value = ""
                value += '0'
                print(value)
            elif value != "":
                value += '0'
                print(value)
    elif 'value01' in request.args:
        if temp != "" and operation == "":
            temp = ""
            value += '1'
        else:
            if value == "":
                value += '1'
                print(value)
            elif value == "0":
                value = ""
                value += '1'
                print(value)
            elif value != "":
                value += '1'
                print(value)
    elif 'value02' in request.args:
        if temp != "" and operation == "":
            temp = ""
            value += '2'
        else:
            if value == "":
                value += '2'
                print(value)
            elif value == "0":
                value = ""
                value += '2'
                print(value)
            elif value != "":
                value += '2'
                print(value)
    elif 'value03' in request.args:
        if temp != "" and operation == "":
            temp = ""
            value += '3'
        else:
            if value == "":
                value += '3'
                print(value)
            elif value == "0":
                value = ""
                value += '3'
                print(value)
            elif value != "":
                value += '3'
                print(value)
    elif 'value04' in request.args:
        if temp != "" and operation == "":
            temp = ""
            value += '4'
        else:
            if value == "":
                value += '4'
                print(value)
            elif value == "0":
                value = ""
                value += '4'
                print(value)
            elif value != "":
                value += '4'
                print(value)
    elif 'value05' in request.args:
        if temp != "" and operation == "":
            temp = ""
            value += '5'
        else:
            if value == "":
                value += '5'
                print(value)
            elif value == "0":
                value = ""
                value += '5'
                print(value)
            elif value != "":
                value += '5'
                print(value)
    elif 'value06' in request.args:
        if temp != "" and operation == "":
            temp = ""
            value += '6'
        else:
            if value == "":
                value += '6'
                print(value)
            elif value == "0":
                value = ""
                value += '6'
                print(value)
            elif value != "":
                value += '6'
                print(value)
    elif 'value07' in request.args:
        if temp != "" and operation == "":
            temp = ""
            value += '7'
        else:
            if value == "":
                value += '7'
                print(value)
            elif value == "0":
                value = ""
                value += '7'
                print(value)
            elif value != "":
                value += '7'
                print(value)
    elif 'value08' in request.args:
        if temp != "" and operation == "":
            temp = ""
            value += ''
        else:
            if value == "":
                value += '8'
                print(value)
            elif value == "0":
                value = ""
                value += '8'
                print(value)
            elif value != "":
                value += '8'
            print(value)
    elif 'value09' in request.args:
        if temp != "" and operation == "":
            temp = ""
            value += '9'
        else:
            if value == "":
                value += '9'
                print(value)
            elif value == "0":
                value = ""
                value += '9'
                print(value)
            elif value != "":
                value += '9'
                print(value)
    elif 'decimal' in request.args:
        if temp != "" and operation == "":
            temp = ""
            value += '.'
        else:
            if value == "":
                value += '.'
                print(value)
            elif value == "0":
                value = ""
                value += '.'
                print(value)
            elif value != "":
                value += '.'
                print(value)
    elif 'clear' in request.args:
        value = ""
        temp = ""
        operation = ""
    elif 'negative' in request.args:
        if temp != "" and operation == "":
            temp = ""
            value += '-'
        else:
            if value == "":
                value += '-'
                print(value)
            elif value == "0":
                value = ""
                value += '-'
                print(value)
            elif value != "" and value[0] != "-":
                v= value
                n = "-"
                value = n + v
                print(value)
            elif value != "" and value[0] == '-':
                value = value[1:]
                print (value)
    elif 'equals' in request.args:
        if value != "" and temp != "":
            if operation == "+":
                temp = float(value) + float (temp)
                value = ''
                # operation = '+'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "-":
                temp = float(temp) - float (value)
                value = ''
                # operation = '+'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "*":
                temp = float(value) * float (temp)
                value = ''
                # operation = '+'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "/":
                temp = float(temp) / float (value)
                value = ''
                # operation = '+'
                print(operation)
                print('previous')
                print (temp)
        elif value == "" and temp != "":
            temp = temp
            value = ''
            operation = ''
        elif value != "" and temp == "":
            temp = value
            value = ''
            operation = ''
    elif 'addition' in request.args:
        if temp == "":
            temp = value
            value = ""
            operation = "+"
            print(operation)
            print('previous')
            print (temp)
        elif value != "" and temp != "":
            if operation == "+":
                temp = float(value) + float (temp)
                value = ''
                operation = '+'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "-":
                temp = float(temp) - float (value)
                value = ''
                operation = '+'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "*":
                temp = float(value) * float (temp)
                value = ''
                operation = '+'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "/":
                temp = float(temp) / float (value)
                value = ''
                operation = '+'
                print(operation)
                print('previous')
                print (temp)
        elif value == "" and temp != "":
            operation = '+'
    elif 'subtraction' in request.args:
        if temp == "":
            temp = value
            value = ""
            operation = "-"
            print(operation)
            print('previous')
            print (temp)
        elif value != "" and temp != "":
            if operation == "+":
                temp = float(temp) + float (value)
                value = ''
                operation = '-'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "-":
                temp = float(temp) - float (value)
                value = ''
                operation = '-'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "*":
                temp = float(value) * float (temp)
                value = ''
                operation = '-'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "/":
                temp = float(temp) / float (value)
                value = ''
                operation = '-'
                print(operation)
                print('previous')
                print (temp)
        elif value == "" and temp != "":
            operation = '-'
    elif 'multiplication' in request.args:
        if temp == "":
            temp = value
            value = ""
            operation = "*"
            print(operation)
            print('previous')
            print (temp)
        elif value != "" and temp != "":
            if operation == "+":
                temp = float(value) + float (temp)
                value = ''
                operation = '*'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "-":
                temp = float(temp) - float (value)
                value = ''
                operation = '*'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "*":
                temp = float(value) * float (temp)
                value = ''
                operation = '*'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "/":
                temp = float(temp) / float (value)
                value = ''
                operation = '*'
                print(operation)
                print('previous')
                print (temp)
        elif value == "" and temp != "":
            operation = '*'
    elif 'division' in request.args:
        if temp == "":
            temp = value
            value = ""
            operation = "/"
            print(operation)
            print('previous')
            print (temp)
        elif value != "" and temp != "":
            if operation == "+":
                temp = float(value) + float (temp)
                value = ''
                operation = '/'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "-":
                temp = float(temp) - float (value)
                value = ''
                operation = '/'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "*":
                temp = float(value) * float (temp)
                value = ''
                operation = '/'
                print(operation)
                print('previous')
                print (temp)
            elif operation == "/":
                temp = float(temp) / float (value)
                value = ''
                operation = '/'
                print(operation)
                print('previous')
                print (temp)
        elif value == "" and temp != "":
            operation = '/'

    return render_template("buttons.html", temp=temp, operation = operation, result = value)


if __name__ == "__main__":
    app.run(port=5000,debug =False)

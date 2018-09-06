import os
from flask import Flask, url_for, render_template, request
from colorsys import rgb_to_hls, hls_to_rgb
from PIL import Image

app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

value=""
temp = ""
operation = ""

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/calcHome")
def render_calc():
    return render_template('calcpage.html')


@app.route("/colorpick")
def render_colorpick():
    return render_template('colorpick.html')


@app.route("/colorresult")
def render_colorResults():
    try:
        # Turns HTML hex value into python hex value
        color_result = request.args['inColor']
        # Turns python hex value into three separate RGB values
        (redIn, greenIn, blueIn) = hex_to_rgb(color_result)

        comp_result = convertRGB(redIn, greenIn, blueIn, 180)

        analog1 = convertRGB(redIn, greenIn, blueIn, 330)
        analog2 = convertRGB(redIn, greenIn, blueIn, 30)

        splitComp1 = convertRGB(redIn, greenIn, blueIn, 150)
        splitComp2 = convertRGB(redIn, greenIn, blueIn, 210)

        triadic1 = convertRGB(redIn, greenIn, blueIn, 120)
        triadic2 = convertRGB(redIn, greenIn, blueIn, -120)

        imageRGB(redIn, greenIn, blueIn, "original.jpg")

        imageRGB(comp_result[0], comp_result[1], comp_result[2], "complementary.jpg")

        imageRGB(analog1[0], analog1[1], analog1[2], "an1.jpg")
        imageRGB(analog2[0], analog2[1], analog2[2], "an2.jpg")

        imageRGB(splitComp1[0], splitComp1[1], splitComp1[2], "splitComp1.jpg")
        imageRGB(splitComp2[0], splitComp2[1], splitComp2[2], "splitComp2.jpg")

        imageRGB(triadic1[0], triadic1[1], triadic1[2], "triadic1.jpg")
        imageRGB(triadic2[0], triadic2[1], triadic2[2], "triadic2.jpg")

        # PROCESS COLOR
        return render_template('colorresult.html', inColor=(redIn, greenIn, blueIn),
                                compColor=comp_result, an1Color=analog1, an2Color=analog2,
                                split1Color=splitComp1, split2Color=splitComp2,
                                triadic1Color=triadic1, triadic2Color=triadic2)
    except ValueError:
        return request.args['inColor'] + "Sorry: something went wrong."

@app.route("/calcpage")
def calculate():
    global value
    global temp
    global operation
    # htmlresult = str(request.args['telnum'])
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

    return render_template("calcpage.html", temp=temp, operation = operation,result = value)

def convertRGB(red, green, blue, shiftValue):
    # Turns RGB and shiftValue into percentages between zero and one
    (red, green, blue) =  (red/255, green/255, blue/255)
    shiftValue = shiftValue/360

    #Turn RGB into an HLS value
    (hue, lightness, saturation) = rgb_to_hls(red, green , blue)

    # "Shifts" the hue by the shiftValue, altering its position on the color wheel
    hue = hue - shiftValue
    # Fixes negative results for hues
    if hue <= 0:
        hue = 1.0 + hue

    # Moves color back into RGB output
    (redOut, greenOut, blueOut) = hls_to_rgb(hue, lightness, saturation)
    (redOut, greenOut, blueOut) =  (round(redOut*255), round(greenOut*255), round(blueOut*255))
    return (redOut, greenOut, blueOut)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def hexToggle(inputString):
    print(type(inputString))
    if type(inputString) == str:
        outputHex = inputString.replace("#", "0x")
        outputHex = int(outputHex, 16)
        return hex(outputHex)
    elif type(inputString) == int:
        outputHex = str(hex(inputString))
        print(outputHex)
        outputHex = outputHex.replace("0x", "#")
        return outputHex
    else:
        print("No result")
        return


def imageRGB (r,g,b, fileName):
    new = Image.new ("RGB", (100, 100), color = (r,g,b))
    new.save("static/" + fileName)


if __name__ == "__main__":
    app.run(port=5000,debug=True)

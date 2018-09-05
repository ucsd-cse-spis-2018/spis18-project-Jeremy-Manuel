from flask import Flask, url_for, render_template, request
from colorsys import rgb_to_hls, hls_to_rgb
from PIL import Image

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

result = ""
value1= str("0")
value2 = ""
first = 1
operation = 0

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

@app.route("/calcpage", methods=['GET','POST'])
def buttons():
    global value1
    global value2
    global first
    global result
    global operation

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
        if 'value00' in request.args:
            value1 = result
            value2 = ""
            value2 +="0"
            print(value2)
        elif 'value01' in request.args:
            value1 = result
            value2 = ""
            value2 +="1"
            print(value2)
        elif 'value02' in request.args:
            value1 = result
            value2 = ""
            value2 +="2"
            print(value2)
        elif 'value03' in request.args:
            value1 = result
            value2 = ""
            value2 +="3"
            print(value2)
        elif 'value04' in request.args:
            value1 = result
            value2 = ""
            value2 +="4"
            print(value2)
        elif 'value05' in request.args:
            value1 = result
            value2 = ""
            value2 +='5'
            print(value2)
        elif 'value06' in request.args:
            value1 = result
            value2 = ""
            value2 +='6'
            print(value2)
        elif 'value07' in request.args:
            value1 = result
            value2 = ""
            value2 +='7'
            print(value2)
        elif 'value08' in request.args:
            value1 = result
            value2 = ""
            value2 +='8'
            print(value2)
        elif 'value09' in request.args:
            value1 = result
            value2 = ""
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

    return render_template("calcpage.html", result=result)

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

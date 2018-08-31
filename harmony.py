from flask import Flask, url_for, render_template, request 
from colorsys import rgb_to_hls
from colorsys import hls_to_rgb
#from math import round
from PIL import Image

app = Flask(__name__)


@app.route("/")
def render_main():
    return render_template('home.html')


@app.route("/colorpick")
def render_colorpick():
    return render_template('colorpick.html')


@app.route("/colorresult")
def render_colorResults():
    try:
        # Turns HTML hex value into python hex value
        color_result = hexToggle(request.args['inColor'])
        # Turns python hex value into three separate RGB values
        (redIn, greenIn, blueIn) = tuple(int(color_result[i:i+2], 16) for i in (2, 4 ,4))

        comp_result = convertRGB(redIn, greenIn, blueIn, 180)

        imageRGB(redIn, greenIn, blueIn, "original.jpg")
        imageRGB(comp_result[0], comp_result[1], comp_result[2], "complementary.jpg")

        # PROCESS COLOR
        return render_template('colorresult.html', inColor=(redIn, greenIn, blueIn), compColor=comp_result)
    except ValueError:
        return request.args['inColor'] + "Sorry: something went wrong."


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
        hue = 1.0 - hue

    # Moves color back into RGB output
    (redOut, greenOut, blueOut) = hls_to_rgb(hue, lightness, saturation)
    (redOut, greenOut, blueOut) =  (round(redOut*255), round(greenOut*255), round(blueOut*255))
    return (redOut, greenOut, blueOut)


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
    #new.show("static/" + fileName)
    #Image.open()


if __name__ == "__main__":
    app.run(port=5000,debug=False)

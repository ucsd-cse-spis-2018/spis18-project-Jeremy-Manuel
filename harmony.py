from flask import Flask, url_for, render_template, request 
from colorsys import rgb_to_hls
from colorsys import hls_to_rgb
from math import floor

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
        color_result = float(request.args['inColor'])
        comp_result = 0
        # PROCESS COLOR
        return render_template('colorResult.html', inColor=color_result, compColor=comp_result)
    except ValueError:
        return "Sorry: something went wrong."

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
    (redOut, greenOut, blueOut) =  (floor(redOut*255), floor(greenOut*255), floor(blueOut*255))
    return (redOut, greenOut, blueOut)

if __name__ == "__main__":
    app.run(port=5000,debug=False)

from flask import Flask, url_for, render_template, request 
from colorsys import rgb_to_hls
from colorsys import hls_to_rgb

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
        # PROCESS COLOR
        return render_template('colorResult.html', inColor=color_result, compColor=comp_result)
    except ValueError:
        return "Sorry: something went wrong."

def convertRGB(red, green , blue):
    difference = 0
    (hue, lightness, saturation) = colorsys.rgb_to_hls(red, green , blue)

    if hue >= 180:
        difference = hue - 180
        hue = difference
    else:
        (hue, lightness, saturation) = (hue + 180, lightness, saturation)

    print (colorValue)

if __name__ == "__main__":
    app.run(port=5000,debug=False)

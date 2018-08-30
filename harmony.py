
from colorsys import rgb_to_hls
from colorsys import hls_to_rgb

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')
# CODE GOES HERE

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

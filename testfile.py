from colorsys import rgb_to_hsv
from colorsys import hls_to_rgb
from PIL import Image


def convertRGB(red, green , blue):
    red = red / 255 # converts the rgb values to floats between 0 to 1 to use the rgb_to_hsv function
    green = green / 255
    blue = blue / 255
    difference = 0

    (hue, saturation, value) = rgb_to_hsv(red, green , blue)  # converts to float between 0 to 1
    print ((hue, saturation, value))

    if hue >= .5: # if the value is .5 or higher, we want the difference to be used as the hue value
        difference = hue - .5
        print(difference)
        (hue, saturation, value) = (difference, saturation, value)

    else:

        (hue, saturation, value) = (hue + .5, saturation, value)

    (hue, saturation, value) =  (hue * 360, saturation * 100, value * 100)  # converts the values to normal hsl values
    print ((hue, saturation, value))

def imageRGB (r,g,b, fileName):
    new = Image.new ("RGB", (100, 100), color = (r,g,b))
    new.save(fileName)
    new.show(fileName)
    #Image.open()

imageRGB(120,245,53, "test.jpg")

convertRGB(35, 212, 154)

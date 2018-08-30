from colorsys import rgb_to_hsv
from colorsys import hls_to_rgb

def convertRGB(red, green , blue):
    red = red / 255
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

    (hue, saturation, value) =  (hue * 360, saturation * 100, value * 100)
    print ((hue, saturation, value))


convertRGB(35, 212, 154)

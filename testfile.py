from PIL import Image

def imageRGB (r,g,b, fileName):
    new = Image.new ("RGB", (100, 100), color = (r,g,b))
    new.save(fileName)
    new.show(fileName)
    #Image.open()

imageRGB(120,245,53, "test.jpg")
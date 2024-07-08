from PIL import Image
import matplotlib.pyplot as plt

image = Image.open(
    "/Users/jules/Documents/GitHub/pythonIA/img/premier.jpg")
largeur, hauteur = image.size
nouvelle_image = Image.new("RGB", (largeur, hauteur))


for y in range(hauteur):
    for x in range(largeur):
        pixel = image.getpixel((x, y))
        if pixel[0] > 65 and pixel[1] > 65 and pixel[2] > 65:
            nouvelle_image.putpixel((x, y), (255, 255, 255))

nouvelle_image.save(
    "/Users/jules/Documents/GitHub/pythonIA/img.jpg")

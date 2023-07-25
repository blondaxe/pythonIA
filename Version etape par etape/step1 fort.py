from PIL import Image
import matplotlib.pyplot as plt

image = Image.open(
    "/Users/julesquartier/Desktop/PROJETS PERSO/Python/numeriseAI/IMG/step1.jpg")
largeur, hauteur = image.size
nouvelle_image = Image.new("RGB", (largeur, hauteur))


for y in range(hauteur):
    for x in range(largeur):
        pixel = image.getpixel((x, y))
        if pixel[0] > 65 and pixel[1] > 65 and pixel[2] > 65:
            nouvelle_image.putpixel((x, y), (255, 255, 255))

nouvelle_image.save(
    "/Users/julesquartier/Desktop/PROJETS PERSO/Python/numeriseAI/IMG/step2.jpeg")

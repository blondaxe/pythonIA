from PIL import Image

image = Image.open(
    "/Users/jules/Documents/GitHub/pythonIA/img/step1.jpg")
largeur, hauteur = image.size
nouvelle_image = Image.new("RGB", (largeur, hauteur))


for y in range(hauteur):
    for x in range(largeur):
        pixel = image.getpixel((x, y))
        if pixel[0] > 90 and pixel[1] > 90 and pixel[2] > 90:
            nouvelle_image.putpixel((x, y), (255, 255, 255))

nouvelle_image.save(
    "/Users/jules/Documents/GitHub/pythonIA/img/step2.jpg")

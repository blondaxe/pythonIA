from PIL import Image

# Inclure un bout de code (peut être celui dessous OU celui du step1 doux) qui permet de passer de step1 à
# step2 içi car on doit utiliser l'image simplifiée dans toute la suite du programme
'''
for y in range(hauteur):
    for x in range(largeur):
        pixel = image.getpixel((x, y))
        if pixel[0] > 65 and pixel[1] > 65 and pixel[2] > 65:
            nouvelle_image.putpixel((x, y), (255, 255, 255))

nouvelle_image.save(
    "/Users/julesquartier/Desktop/PROJETS PERSO/Python/numeriseAI/IMG/step2.jpeg")
'''

image = Image.open(
    "/Users/jules/Documents/GitHub/pythonIA/img/step2.jpg")
largeur, hauteur = image.size
nouvelle_image = Image.new("RGB", (largeur, hauteur))

compt = 0  # Compte le nombre de pixels presque noir pour 1 ligne
ecrit = []
non_ecrit = []

puissance_ligne = []  # Donne le nombre de pixels presque noir par ligne


def verifier_ligne(num):
    global ecrit, non_ecrit

    if num in non_ecrit: # Si la ligne n'est pas écrite, on ne fait rien
        return

    if num == hauteur or num == hauteur - 1 or num == hauteur - 2 or num == hauteur - 3:  # Pour les 4 dernières lignes
        if num - 1 in non_ecrit or num - 2 in non_ecrit or num - 3 in non_ecrit or num - 4 in non_ecrit:
            ecrit.remove(num)
            non_ecrit.append(num)
            verifier_ligne(hauteur - 6)
            verifier_ligne(hauteur - 5)
            verifier_ligne(hauteur - 4)
            verifier_ligne(hauteur - 3)

    elif num == 0 or num == 1 or num == 2 or num == 3:  # Pour les 4 1eres lignes
        if num + 1 in non_ecrit or num + 2 in non_ecrit or num + 3 in non_ecrit or num + 4 in non_ecrit:
            ecrit.remove(num)
            non_ecrit.append(num)
            verifier_ligne(3)
            verifier_ligne(4)
            verifier_ligne(5)
            verifier_ligne(6)

    else:  # Pour les cas en général
        if num - 1 in non_ecrit or num - 2 in non_ecrit or num - 3 in non_ecrit or num - 4 in non_ecrit:
            if num + 1 in non_ecrit or num + 2 in non_ecrit or num + 3 in non_ecrit or num + 4 in non_ecrit:
                ecrit.remove(num)
                non_ecrit.append(num)
                verifier_ligne(num-4)
                verifier_ligne(num-3)
                verifier_ligne(num-2)
                verifier_ligne(num-1)
                verifier_ligne(num+1)
                verifier_ligne(num+2)
                verifier_ligne(num+3)
                verifier_ligne(num+4)


for y in range(hauteur):
    for x in range(largeur):
        pixel = image.getpixel((x, y))

        # Permet de compter le nombre de pixels presque noir
        if pixel[0] < 30 and pixel[1] < 30 and pixel[2] < 30:
            compt = compt + 1

    puissance_ligne.append(compt)

    if compt > 10:  # Si le nombre de pixels presque noir par ligne > 10 : ligne écrite
        ecrit.append(y)
    else:
        non_ecrit.append(y)
    compt = 0


for i in ecrit:  # Pour enlever les imperfections des lignes
    verifier_ligne(i)

bandes = []  # Pour savoir de quelle ligne à quelle ligne part une bande
bande_actuelle = []

for i in ecrit:  # Pour lister les bandes 1 par 1
    if bande_actuelle == []:
        bande_actuelle.append(i)
    elif i == bande_actuelle[-1] + 1:
        bande_actuelle.append(i)
    else:
        bandes.append(bande_actuelle)
        bande_actuelle = []

if bande_actuelle != []:
    bandes.append(bande_actuelle)
    bande_actuelle = []

for i in bandes:  # Pour ajustre une marge de 4 aux bandes
    mini = min(i)
    if mini-4 >= 0:
        i.append(mini-4)
    if mini-3 >= 0:
        i.append(mini-3)
    if mini-2 >= 0:
        i.append(mini-2)
    if mini-1 >= 0:
        i.append(mini-1)

    maxi = max(i)
    if maxi+4 <= hauteur:
        i.append(maxi+4)
    if maxi+3 <= hauteur:
        i.append(maxi+3)
    if maxi+2 <= hauteur:
        i.append(maxi+2)
    if maxi+1 <= hauteur:
        i.append(maxi+1)

    i = sorted(i)
# bandes contient maintenant tous les bandes avec des écritures
from PIL import Image
import matplotlib.pyplot as plt


image = Image.open(
    "/Users/julesquartier/Desktop/PROJETS PERSO/Python/numeriseAI/IMG/step2.jpeg")
largeur, hauteur = image.size
nouvelle_image = Image.new("RGB", (largeur, hauteur))

# A REMPLIR
bandes = [[344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 340, 341, 342, 343, 384, 383, 382, 381], [387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446,
                                                                                                                                                                                                                                              447, 448, 449, 450, 451, 452, 453, 454, 383, 384, 385, 386, 458, 457, 456, 455], [486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 482, 483, 484, 485, 561, 560, 559, 558], [1820, 1816, 1817, 1818, 1819, 1824, 1823, 1822, 1821]]

mots = []  # Contient les colonnes où il y a un bout de mot pour chaques bandes
trait_noir = []  # Contient les colonnes où il y a un trait noir pour chaques bandes

mot_ecrit = []
mot_non_ecrit = []
puissance_colonne = []
compt = 0

for bande in bandes:
    for x in range(largeur):
        for ligne in bande:
            pixel = image.getpixel((x, ligne))

            if pixel[0] < 30 and pixel[1] < 30 and pixel[2] < 30:
                compt = compt + 1

        puissance_colonne.append(compt)

        if compt > 0:  # Si le nombre de pixels presque noir = 0 mot_non_ecrite
            mot_ecrit.append(x)

            pixel = image.getpixel((x, ligne))
            for ligne in bande:
                nouvelle_image.putpixel((x, ligne), pixel)
        else:
            mot_non_ecrit.append(x)
            for ligne in bande:
                nouvelle_image.putpixel((x, ligne), (0, 0, 0))
        compt = 0

    mots.append(mot_ecrit)
    trait_noir.append(mot_non_ecrit)
    mot_ecrit = []
    mot_non_ecrit = []


# plt.plot(axe_x, puissance_colonne)
# plt.show()
nouvelle_image.save(
    "/Users/julesquartier/Desktop/PROJETS PERSO/Python/numeriseAI/IMG/step5.jpeg")


trait_actuel = []
tmp = []
compt = -1
# Faire pareil avec les mots = []
for bande in trait_noir:  # Pour faire la correction des petites lignes noires
    compt = compt + 1
    for trait in bande:
        if trait_actuel == []:
            trait_actuel.append(trait)
        elif trait == trait_actuel[-1] + 1:
            trait_actuel.append(trait)
        else:
            if len(trait_actuel) < 11:
                for trait in trait_actuel:  # Pour changer dans les listes
                    tmp.append(trait_noir[compt])
                    tmp = tmp[0]
                    tmp.remove(trait)
                    trait_noir.pop(compt)
                    trait_noir.insert(compt, tmp)
                    tmp = []

                    tmp.append(mots[compt])
                    tmp = tmp[0]
                    tmp.append(trait)
                    tmp = sorted(tmp)
                    mots.pop(compt)
                    mots.insert(compt, tmp)
                    tmp = []
                    # mots[bande].append(trait) LE METTRE SUR CETTE LISTE

                    # for y in _________:
                    #   nouvelle_image.putpixel((trait, y), (255, 255, 255))

            trait_actuel = []

# On peut aussi essayer de faire avec la fonction verifier pour enlever les petits traits noirs


compt = - 1
for bande in bandes:  # POur visualiser les petites modifications
    compt = compt + 1
    for x in range(largeur):
        if x in mots[compt]:
            for ligne in bande:
                nouvelle_image.putpixel((x, ligne), (255, 255, 255))


nouvelle_image.save(
    "/Users/julesquartier/Desktop/PROJETS PERSO/Python/numeriseAI/IMG/step6.jpeg")

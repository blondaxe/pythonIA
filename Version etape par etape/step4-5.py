from PIL import Image
import matplotlib.pyplot as plt
# Faire en sorte que les largeurs de 5 ou 10 pixels ne soient pas pris en compte

image = Image.open(
    "/Users/jules/Documents/GitHub/pythonIA/img/step2.jpg")
largeur, hauteur = image.size
nouvelle_image = Image.new("RGB", (largeur, hauteur))

# A REMPLIR
bandes = [[466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748]]
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
    "/Users/jules/Documents/GitHub/pythonIA/img/step5.jpg")


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
    "/Users/jules/Documents/GitHub/pythonIA/img/step6.jpg")

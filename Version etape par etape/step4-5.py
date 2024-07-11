from PIL import Image
import matplotlib.pyplot as plt
# Faire en sorte que les largeurs de 5 ou 10 pixels ne soient pas pris en compte

image = Image.open(
    "/Users/jules/Documents/GitHub/pythonIA/img/step2.jpg")
largeur, hauteur = image.size
nouvelle_image = Image.new("RGB", (largeur, hauteur))

# A REMPLIR
bandes = [[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 18, 19, 20, 21, 58, 57, 56, 55], [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 83, 84, 85, 86, 125, 124, 123, 122], [157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 153, 154, 155, 156, 190, 189, 188, 187], [218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 214, 215, 216, 217, 259, 258, 257, 256], [284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 280, 281, 282, 283, 325, 324, 323, 322], [356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 352, 353, 354, 355, 392, 391, 390, 389], [420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 416, 417, 418, 419, 458, 457, 456, 455], [490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 486, 487, 488, 489, 524, 523, 522, 521], [555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 551, 552, 553, 554, 590, 589, 588, 587], [616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 612, 613, 614, 615, 657, 656, 655, 654], [685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 681, 682, 683, 684, 723, 722, 721, 720], [756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 752, 753, 754, 755, 790, 789, 788, 787], [823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 819, 820, 821, 822, 855, 854, 853, 852], [888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 884, 885, 886, 887, 922, 921, 920, 919], [950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 946, 947, 948, 949, 989, 988, 987, 986], [1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1014, 1015, 1016, 1017, 1058, 1057, 1056, 1055], [1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1083, 1084, 1085, 1086, 1121, 1120, 1119, 1118], [1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1152, 1153, 1154, 1155, 1193, 1192, 1191, 1190], [1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1217, 1218, 1219, 1220, 1257, 1256, 1255, 1254], [1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318, 1319, 1320, 1285, 1286, 1287, 1288, 1324, 1323, 1322, 1321]]
# ^ numéros des lignes qui contienent des écritures
mots = []  # Contient les colonnes où il y a un bout de mot pour chaques bandes
trait_noir = []  # Contient les colonnes où il y a un trait noir pour chaques bandes

mot_ecrit = []
mot_non_ecrit = []
puissance_colonne = []
compt = 0

for bande in bandes: # Compte le nombre de pixels presque noir de chaque colonnes pour toutes les lignes écrites qu'on a
    for x in range(largeur):
        for ligne in bande:
            pixel = image.getpixel((x, ligne))
            # Permet de compter le nombre de pixels presque noir
            if pixel[0] < 30 and pixel[1] < 30 and pixel[2] < 30:
                compt = compt + 1

        puissance_colonne.append(compt)

        if compt > 0:  # Si le nombre de pixels presque noir = 0 mot_non_ecrite
    # Peut être changer et mettre >5 ou 10
            mot_ecrit.append(x)

            for ligne in bande:
                pixel = image.getpixel((x, ligne))
                nouvelle_image.putpixel((x, ligne), pixel)
        else:
            mot_non_ecrit.append(x)
            for ligne in bande:
                nouvelle_image.putpixel((x, ligne), (0, 0, 0)) # On met en noir s'il n'y a rien
        compt = 0

    mots.append(mot_ecrit) # mots[0]
    trait_noir.append(mot_non_ecrit)
    mot_ecrit = []
    mot_non_ecrit = []


# plt.plot(axe_x, puissance_colonne)
# plt.show()
nouvelle_image.save(
    "/Users/jules/Documents/GitHub/pythonIA/img/step5.jpg")

'''
### Partie pour enlever les petits traits et avoir une marge (faire avec vérifier ??)
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
            if len(trait_actuel) < 11: # S'il y a un petit trait noir
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
'''

nouvelle_image.save(
    "/Users/jules/Documents/GitHub/pythonIA/img/step6.jpg")

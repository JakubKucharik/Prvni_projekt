"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jakub Kuchařík
email: jakub.kucharik@gmail.com
discord: Jakub Kuchařík#8660
"""
import collections
from task_template import TEXTS
uzivatel = input("Enter username: ")
heslo = input("Enter password: ")
users = {1: {"name": "bob", "password": "123"},
         2: {"name": "ann", "password": "pass123"},
         3: {"name": "mike", "password": "password123"},
         4: {"name": "liz", "password": "pass123"}}

if users[1]["name"] == uzivatel and users[1]["password"] == heslo:
    print(f'''
$ python projekt1.py
username:{uzivatel}
password:{heslo}
----------------------------------------
Welcome to the app, {uzivatel}
We have 3 texts to be analyzed.
----------------------------------------
    ''')
elif users[2]["name"] == uzivatel and users[2]["password"] == heslo:
    print(f'''
$ python projekt1.py
username:{uzivatel}
password:{heslo}
----------------------------------------
Welcome to the app, {uzivatel}
We have 3 texts to be analyzed.
----------------------------------------
    ''')
elif users[3]["name"] == uzivatel and users[3]["password"] == heslo:
    print(f'''
$ python projekt1.py
username:{uzivatel}
password:{heslo}
----------------------------------------
Welcome to the app, {uzivatel}
We have 3 texts to be analyzed.
----------------------------------------
    ''')
elif users[4]["name"] == uzivatel and users[4]["password"] == heslo:
    print(f'''
$ python projekt1.py
username:{uzivatel}
password:{heslo}
----------------------------------------
Welcome to the app, {uzivatel}
We have 3 texts to be analyzed.
----------------------------------------''')
else:
    print(f'''
$ python projekt1.py
username:{uzivatel}
password:{heslo}
unregistered user, terminating the program..''')
    exit()
vyber_textu = input("Enter a number btw. 1 and 3 to select: ")
if vyber_textu == "1":
    text1 = TEXTS[0]
    rozdeleni1 = text1.split(sep=None)
    # počet slov
    pocet_slov1 = len(rozdeleni1)
    list_slova1 = list(text1.split(sep=None))
    print(f'''----------------------------------------
There are {str(pocet_slov1)} words in the selected text.''')
    # počet slov s prvním písmenem velkým
    slova_prvni_pismeno_velke1 = 0
    for i in range(len(list_slova1)):
        if list_slova1[i].istitle():
            slova_prvni_pismeno_velke1 += 1
    print(f"There are {str(slova_prvni_pismeno_velke1)} titlecase words.")
    # počet slov psaných velkými písmeny
    slova_velka_pismena1 = 0
    for z in range(len(list_slova1)):
        if list_slova1[z].isupper() and list_slova1[z].isalpha():
            slova_velka_pismena1 += 1
    print(f"There are {str(slova_velka_pismena1)} uppercase words.")
    # počet slov psaných malými písmeny
    slova_mala_pismena1 = 0
    for i in range(len(list_slova1)):
        if list_slova1[i].islower():
            slova_mala_pismena1 += 1
    print(f"There are {str(slova_mala_pismena1)} lowercase words.")
    # počet čísel
    list1_cisla = []
    pocet_cisel1 = 0
    for y in range(len(list_slova1)):
        if list_slova1[y].isdigit():
            pocet_cisel1 += 1
            list1_cisla.append(list_slova1[y])
    print(f"There are {str(pocet_cisel1)} numeric strings.")
    # součet čísel
    list1_soucet_cisel = sum([int(x) for x in list1_cisla])
    print(f"The sum of all the numbers {str(list1_soucet_cisel)}")
    # četnosti slov
    list_slova1_vycisteno = []
    for y in range(len(list_slova1)):
        list_slova1[y] = list_slova1[y].strip(".")
        list_slova1[y] = list_slova1[y].strip(",")
        list_slova1_vycisteno.append(list_slova1[y])
    list_delky_slov1 = []
    for z in range(len(list_slova1_vycisteno)):
        list_delky_slov1.append(len(list_slova1_vycisteno[z]))
    cetnosti1 = collections.Counter(list_delky_slov1)
    max_v_keys1 = max(cetnosti1.keys())
    print('''----------------------------------------
LEN|  OCCURENCES   |NR.
----------------------------------------''')
    for x in range(1, max_v_keys1 + 1):
        if cetnosti1[x] == 0:
            continue
        elif 0 < x < 10:
            print("  " + str(x) + "|" +
                  (cetnosti1[x] * "*") + ((14 - cetnosti1[x]) * " ") + " |" +
                  str(cetnosti1[x]))
        elif 10 <= x < 99:
            print(" " + str(x) + "|" +
                  (cetnosti1[x] * "*") + ((14 - cetnosti1[x]) * " ") + " |" +
                  str(cetnosti1[x]))
# ---------------------------------------------------
elif vyber_textu == "2":
    text2 = TEXTS[1]
    rozdeleni2 = text2.split(sep=None)
    pocet_slov2 = len(rozdeleni2)
    list_slova2 = list(text2.split(sep=None))
    print(f'''----------------------------------------
There are {str(pocet_slov2)} words in the selected text.''')
    slova_prvni_pismeno_velke2 = 0
    for i in range(len(list_slova2)):
        if list_slova2[i].istitle():
            slova_prvni_pismeno_velke2 += 1
    print(f"There are {str(slova_prvni_pismeno_velke2)} titlecase words.")
    # počet slov psaných velkými písmeny
    slova_velka_pismena2 = 0
    for z in range(len(list_slova2)):
        if list_slova2[z].isupper() and list_slova2[z].isalpha():
            slova_velka_pismena2 += 1
    print(f"There are {str(slova_velka_pismena2)} uppercase words.")
    # počet slov psaných malými písmeny
    slova_mala_pismena2 = 0
    for i in range(len(list_slova2)):
        if list_slova2[i].islower():
            slova_mala_pismena2 += 1
    print(f"There are {str(slova_mala_pismena2)} lowercase words.")
    # počet čísel
    list2_cisla = []
    pocet_cisel2 = 0
    for y in range(len(list_slova2)):
        if list_slova2[y].isdigit():
            pocet_cisel2 += 1
            list2_cisla.append(list_slova2[y])
    print(f"There are {str(pocet_cisel2)} numeric strings.")
    # součet čísel
    list2_soucet_cisel = sum([int(x) for x in list2_cisla])
    print(f"The sum of all the numbers {str(list2_soucet_cisel)}")
    # četnosti slov
    list_slova2_vycisteno = []
    for y in range(len(list_slova2)):
        list_slova2[y] = list_slova2[y].strip(".")
        list_slova2[y] = list_slova2[y].strip(",")
        list_slova2_vycisteno.append(list_slova2[y])
    list_delky_slov2 = []
    for z in range(len(list_slova2_vycisteno)):
        list_delky_slov2.append(len(list_slova2_vycisteno[z]))
    cetnosti2 = collections.Counter(list_delky_slov2)
    max_v_keys2 = max(cetnosti2.keys())
    print('''----------------------------------------
LEN|   OCCURENCES     |NR.
----------------------------------------''')
    for x in range(1, max_v_keys2 + 1):
        if cetnosti2[x] == 0:
            continue
        elif 0 < x < 10:
            print("  " + str(x) + "|" +
                  (cetnosti2[x] * "*") + ((17 - cetnosti2[x]) * " ") + " |" +
                  str(cetnosti2[x]))
        elif 10 <= x < 99:
            print(" " + str(x) + "|" +
                  (cetnosti2[x] * "*") + ((17 - cetnosti2[x]) * " ") + " |" +
                  str(cetnosti2[x]))
#------------------------------------------------
elif vyber_textu == "3":
    text3 = TEXTS[2]
    rozdeleni3 = text3.split(sep=None)
    pocet_slov3 = len(rozdeleni3)
    list_slova3 = list(text3.split(sep=None))
    print(f'''----------------------------------------
There are {str(pocet_slov3)} words in the selected text.''')
    slova_prvni_pismeno_velke3 = 0
    for i in range(len(list_slova3)):
        if list_slova3[i].istitle():
            slova_prvni_pismeno_velke3 += 1
    print(f"There are {str(slova_prvni_pismeno_velke3)} titlecase words.")

    # počet slov psaných velkými písmeny
    slova_velka_pismena3 = 0
    for z in range(len(list_slova3)):
        if list_slova3[z].isupper() and list_slova3[z].isalpha():
            slova_velka_pismena3 += 1
    print(f"There are {str(slova_velka_pismena3)} uppercase words.")
    # počet slov psaných malými písmeny
    slova_mala_pismena3 = 0
    for i in range(len(list_slova3)):
        if list_slova3[i].islower():
            slova_mala_pismena3 += 1
    print(f"There are {str(slova_mala_pismena3)} lowercase words.")
    # počet čísel
    list3_pocet_cisel = []
    pocet_cisel3 = 0
    for y in range(len(list_slova3)):
        if list_slova3[y].isdigit():
            pocet_cisel3 += 1
            list3_pocet_cisel.append(list_slova3[y])
    print(f"There are {str(pocet_cisel3)} numeric strings.")
    # součet čísel
    list3_soucet_cisel = sum([int(x) for x in list3_pocet_cisel])
    print(f"The sum of all the numbers {str(list3_soucet_cisel)}")
    # četnosti slov
    list_slova3_vycisteno = []
    for y in range(len(list_slova3)):
        list_slova3[y] = list_slova3[y].strip(".")
        list_slova3[y] = list_slova3[y].strip(",")
        list_slova3_vycisteno.append(list_slova3[y])
    list_delky_slov3 = []
    for z in range(len(list_slova3_vycisteno)):
        list_delky_slov3.append(len(list_slova3_vycisteno[z]))
    cetnosti3 = collections.Counter(list_delky_slov3)
    max_v_keys3 = max(cetnosti3.keys())
    print('''----------------------------------------
LEN|   OCCURENCES   |NR.
----------------------------------------''')
    for x in range(1, max_v_keys3 + 1):
        if cetnosti3[x] == 0:
            continue
        elif 0 < x < 10:
            print("  " + str(x) + "|" +
                  (cetnosti3[x] * "*") + ((15 - cetnosti3[x]) * " ") + " |" +
                  str(cetnosti3[x]))
        elif 10 <= x < 99:
            print(" " + str(x) + "|" +
                  (cetnosti3[x] * "*") + ((15 - cetnosti3[x]) * " ") + " |" +
                  str(cetnosti3[x]))
else:
    if vyber_textu.isdigit() and vyber_textu not in range(1, 4):
        print("musíte zadat číslo od 1 do 3")
        exit()
    else:
        print("musíte zadat číslo od 1 do 3")
        exit()

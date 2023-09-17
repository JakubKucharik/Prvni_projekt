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

if users[1]["name"] == uzivatel and users[1]["password"] == heslo\
        or users[2]["name"] == uzivatel and users[2]["password"] == heslo\
        or users[3]["name"] == uzivatel and users[3]["password"] == heslo\
        or users[4]["name"] == uzivatel and users[4]["password"] == heslo:
    print(f'''
$ python projekt1.py
username:{uzivatel}
password:{heslo}
----------------------------------------
Welcome to the app, {uzivatel}
We have 3 texts to be analyzed.
----------------------------------------
    ''')
else:
    print(f'''
$ python projekt1.py
username:{uzivatel}
password:{heslo}
unregistered user, terminating the program..''')
    exit()
    
while True:
    vyber_textu = input("Enter a number btw. 1 and 3 to select: ")
    if vyber_textu.isdigit() and int(vyber_textu) not in range(1, 4):
        print("Číslo musí být od 1 do 3")
        continue
    elif not vyber_textu.isdigit():
        print("Číslo textu musí být číslo")
        continue
    else:
        break

text = TEXTS[int(vyber_textu)-1]
rozdeleni = text.split(sep=None)
# počet slov
pocet_slov = len(rozdeleni)
list_slova = list(text.split(sep=None))
print(f'''----------------------------------------
There are {str(pocet_slov)} words in the selected text.''')
# počet slov s prvním písmenem velkým
slova_prvni_pismeno_velke = 0
for i in range(len(list_slova)):
    if list_slova[i].istitle():
            slova_prvni_pismeno_velke += 1
print(f"There are {str(slova_prvni_pismeno_velke)} titlecase words.")

# počet slov psaných velkými písmeny
slova_velka_pismena = 0
for z in range(len(list_slova)):
    if list_slova[z].isupper() and list_slova[z].isalpha():
            slova_velka_pismena += 1
print(f"There are {str(slova_velka_pismena)} uppercase words.")
#počet slov psaných malými písmeny
slova_mala_pismena = 0
for i in range(len(list_slova)):
    if list_slova[i].islower():
            slova_mala_pismena += 1
print(f"There are {str(slova_mala_pismena)} lowercase words.")
#počet čísel
list_cisla = []
pocet_cisel = 0
for y in range(len(list_slova)):
    if list_slova[y].isdigit():
        pocet_cisel += 1
        list_cisla.append(list_slova[y])
print(f"There are {str(pocet_cisel)} numeric strings.")

#součet čísel
list_soucet_cisel = sum([int(x) for x in list_cisla])
print(f"The sum of all the numbers {str(list_soucet_cisel)}")

#četnosti slov
list_slova_vycisteno = []
for y in range(len(list_slova)):
    list_slova[y] = list_slova[y].strip(".")
    list_slova[y] = list_slova[y].strip(",")
    list_slova_vycisteno.append(list_slova[y])
list_delky_slov = []
for z in range(len(list_slova_vycisteno)):
    list_delky_slov.append(len(list_slova_vycisteno[z]))
    cetnosti = collections.Counter(list_delky_slov)
    max_v_keys = max(cetnosti.keys())
print('''----------------------------------------
LEN|    OCCURENCES    |NR.
----------------------------------------''')
for x in range(1, max_v_keys + 1):
    if cetnosti[x] == 0:
        continue
    elif 0 < x < 10:
            print("  " + str(x) + "|" +
                  (cetnosti[x] * "*") + ((17 - cetnosti[x]) * " ") + " |" +
                  str(cetnosti[x]))
    elif 10 <= x < 99:
                print(" " + str(x) + "|" +
                  (cetnosti[x] * "*") + ((17 - cetnosti[x]) * " ") + " |" +
                  str(cetnosti[x]))
# ---------------------------------------------------




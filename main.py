import random

for i in range(5):  # [0,1,2,3,4] #ciklas
    print("labas")
    print("rytas")
    print(i)

print("zemiau ciklo")

num = 24

nums = [1, 2, 15, 8, 10] #masyvas (list)
print(nums)
print(nums[0])
print(nums[2])

nums.append(14) #prideti nauja nari
print(nums)
nums[1] = 16 #pakeisti viena skaiciu kitu
print(nums)
nums.remove(16) #pasalinti nurodyta reiksme
print(nums)

#         0           1               2
games = ["zelda", "final fantasy", "nfs"]
print(games)
print(games[2])

for number in nums:
    print(number)
print("----------------")
print(len(games)) #pasako kiek yra elementu masyve
for zaidimas in games:
    print("My favorite game is " + zaidimas)

# i % 10 == 0 ar porinis ar ne

count = 0
for i in range(50):
    print(i)
    count+= 1

print("prasisuko", count)

for i in range(10):
    if i % 2 == 0:
        continue #jeigu (True) skaičius porinis, tai print nesuveiks. sustabdo ciklą
        #break - sustoja, kai patenkinama sąlyga
        print(i)

#loop loop
#while - suksis tol, kol bus patenkinta sąlyga. Jį naudojam tada, kai nežinom kiek kartų reikės prasukt ciklą


counter = 0
while True:
    counter += 1
    if counter >= 5:
        break
    print(counter)

while True:
    rnd_num = random.randint(1,6)
    print(rnd_num)
    if rnd_num == 1:
        break

print("---------------------------------")

is_even = False

while not is_even:
    rnd_num = random.randint(1,10)
    if rnd_num % 2 == 0:
        is_even = True
    print(rnd_num)

is_not_even = True
while is_not_even:
    rnd_num = random.randint(1,10)
    if rnd_num % 2 == 0:
        is_not_even = False
    print(rnd_num)

print("---------------------------------")

#vidinis ciklas atidirba ir tada pasileidžia išorinis ciklas (toliau)

for y in range(1,11): #1
     for x in range(1,11):
         print(y * x, end=" ") #po tokio reikia padaryt tuscia printa, nes kitu atveju naujas printas bus atvaizduotas pries tai buvusios eilutes gale
print()

print()
print(" ---------------------------- 1 užduotis -----------------------------")

#Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.

for i in range(10):
    print("labas")

print()

print(" ---------------------------- 2 užduotis -----------------------------")

#Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.

for i in range(0,10):
    print(i)

print()

print(" ---------------------------- 3 užduotis -----------------------------")

#Sukurkite masyvą iš dešimties augalų pavadinimų.

plants = ["agrastas", "pienė", "levanda", "dilgėlė", "rožė", "salota", "dobilas", "hortenzija", "magnolija", "lubinas"]
print(plants)

print()

print(" ---------------------------- 4 užduotis -----------------------------")

#Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje

for plant in plants:
    print(plant)

print()

print(" ---------------------------- 5 užduotis -----------------------------")

#Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).

text = plants [::-1]
print(text)

print()

print(" ---------------------------- 6 užduotis -----------------------------")

#Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);

for i in range(10,51):
    if i % 2 == 0:
        print(i)

print()

print(" ---------------------------- 7 užduotis -----------------------------")

#Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite.
# ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)


for num in range(10,51,2):
    if num % 10 == 0:
       continue
    print(num, end=" ")
print()

print()

print(" ---------------------------- 8 užduotis -----------------------------")

#Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę

count = 0
for i in range(0,21,2):
    count += 1
print("Kintamasis 'i' porinę reikšmę tutėjo " + str(count) + " kart.")


print()

print(" ---------------------------- 9 užduotis -----------------------------")

#Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai, ir kiek ilgesnių nei 7 simboliai.
# (du skaičiavimai)

plants = ["agrastas", "pienė", "levanda", "dilgėlė", "rožė", "salota", "dobilas", "hortenzija", "magnolija", "lubinas"]
print(plants)

count_tr = 0
for plant in plants:
    if len(plant) < 5:
        count_tr += 1
        print("trumpesnių nei 5 simboliai yra ", count_tr)

count_il = 0
for plant in plants:
    if len(plant) < 7:
        count_il += 1

print("ilgesnių nei 7 simboliai yra ", count_il)

print()

print(" ---------------------------- 10 užduotis -----------------------------")

#Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai.
# (tarp 5 ir 10 simbolių ilgio)

count = 0
for plant in plants:
    if 5 < len(plant) < 10:
        count += 1

print("žodžių, kurie ilgesni nei 5 simboliai, bet trumpesni nei 10 simbolių yra ", count)

print()

print(" ---------------------------- sunkesni 1 užduotis -----------------------------")

#Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais ir suskaičiuokite kiek tarp jų yra didesnių už 150.
# Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “

nums = [random.randint(0,300) for num in range(300)]
print(nums, end=" ")
print()


print()

print(" ---------------------------- sunkesni 2 užduotis -----------------------------")

#Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos.
# Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti


for num in range(1,3001):
    if num % 77 == 0:
       print(num, end = ", ")
text = "77, 154, 231, 308, 385, 462, 539, 616, 693, 770, 847, 924, 1001, 1078, 1155, 1232, 1309, 1386, 1463, 1540, 1617, 1694, 1771, 1848, 1925, 2002, 2079, 2156, 2233, 2310, 2387, 2464, 2541, 2618, 2695, 2772, 2849, 2926,"
print(text[:-1])

print()

print(" ---------------------------- sunkesni 3 užduotis -----------------------------")

#Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.


for y in range(25):
    for x in range(25):
        print("*", end=" ")
    print()

print()

print(" ---------------------------- sunkesni 4 užduotis -----------------------------")

#Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu.

for y in range(25):
    for x in range(25):
        if x == y or x == (25 -1 - y):
            print("-", end = " ")
        else:
              print("*", end = " ")
    print()

print(" ---------------------------- sunkesni 5 užduotis -----------------------------")

#Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius.
# Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas.
# Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# a) Iškritus herbui;
# b) Tris kartus iškritus herbui;
# c) Tris kartus iš eilės iškritus herbui;

herbas = 0
skaičius = 1

print("a)----------")
while True:
    rezultatas = random.randint(0, 1)
    if rezultatas == 0:
        print("H")
        break
else:
    print("S")

print("b)-----------")

herbu_kiekis = 0
while herbu_kiekis < 3:
    rezultatas = random.randint(0, 1)
    if rezultatas == 0:
        print("H")
        herbu_kiekis += 1
        if herbu_kiekis == 3:
            break
    else:
        print("S")

print("c)---------------")

herbai_is_eiles = 0
while herbai_is_eiles < 3:
    rezultatas = random.randint(0, 1)
    if rezultatas == 0:
        print("H")
        herbai_is_eiles += 1
        if herbai_is_eiles == 3:
            break
    else:
        print("S")

print()

print(" ---------------------------- sunkesni 6 užduotis -----------------------------")

#Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20, Kazys surenka taškų kiekį nuo 5 iki 25.
# Vienoje eilutėje išvesti žaidėjų vardus su taškų kiekiu ir “Partiją laimėjo: ​laimėtojo vardas​”.
# Taškų kiekį generuokite funkcija ​random.randint(x,x)​.
# Žaidimą laimi tas, kas greičiau surenka 222 taškus. Partijas kartoti tol,
# kol kažkuris žaidėjas pirmas surenka 222 arba daugiau taškų

Kazys = random.randint(10, 20)
Petras = random.randint(5, 25)
print("Kazys " + str(Kazys))
print("Petras " + str(Petras))
if Kazys > Petras:
    print("Partiją laimėjo Kazys")
elif Kazys < Petras:
    print("Partiją laimėjo Petras")
else   :
    print("Lygiosios")

print()

petras_viso = 0
kazys_viso = 0
partijos_nr = 1

while True:
    petras_taskai = random.randint(10, 20)
    kazys_taskai = random.randint(5, 25)

    petras_viso += petras_taskai
    kazys_viso += kazys_taskai

    print(str(partijos_nr) + " partija – Petras: " + str(petras_taskai) + " (viso: " + str(petras_viso) + "), Kazys: " + str(kazys_taskai) + " (viso: " + str(kazys_viso) + ")")

    if petras_viso >= 222 and kazys_viso >= 222:
        if petras_viso > kazys_viso:
            laimetojas = "Petras"
            break
        elif kazys_viso > petras_viso:
            laimetojas = "Kazys"
            break
        else:
            laimetojas = "Niekas – lygiosios"
            break
    elif petras_viso >= 222:
        laimetojas = "Petras"
        break
    elif kazys_viso >= 222:
        laimetojas = "Kazys"
        break

    partijos_nr += 1

print("Žaidimą laimėjo: " + str(laimetojas))

print()

print(" ---------------------------- sunkesni 7 užduotis -----------------------------")

#Reikia nupaišyti pilnavidurį rombą, taip pat, kaip ir pilnavidurį kvadratą
# (https://lt.wikipedia.org/wiki/Rombas), kurio aukštis 21 eilutė

aukstis = 21
vidurys = aukstis // 2
print(vidurys)

for y in range(aukstis):
    if y <= vidurys:
        simbolis = 1 + y * 2
        tarpas = (aukstis - simbolis) // 2
    else:
        simbolis = 1 +(aukstis - y - 1) * 2
        tarpas = (aukstis - simbolis) // 2
    print(" " * tarpas + "*" * simbolis)

print()

print(" ---------------------------- sunkesni 8 užduotis -----------------------------")

#Sumodeliuokite vinies kalimą. Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija.
# Vinies ilgis 8.5cm (pilnai sulenda į lentą)
# a) “Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm. Suskaičiuokite kiek reikia smūgių.
# b) “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė
# (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį.
# Suskaičiuokite kiek reikia smūgių








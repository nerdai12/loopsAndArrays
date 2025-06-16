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

for i in range(10,50):
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









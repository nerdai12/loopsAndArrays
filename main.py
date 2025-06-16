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

for i in range(5): #ciklas
    print("labas")
    print("rytas")

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
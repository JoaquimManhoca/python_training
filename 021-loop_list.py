#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

print("_________________________________________")
#Loop Through the Index Numbers
for x in range(len(thislist)):
    print(x)

print("_________________________________________")
#Using a While Loop
x = 0
while x <= len(thislist):
    print(x)
    x += 1

print("_________________________________________")
#Looping Using List Comprehension
[print(x) for x in thislist]
#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    newlist.append(x)
print(newlist)

#With list comprehension you can do all that with only one line of code:
newlist2 = [x for x in fruits if "a" in x]

print(newlist2)

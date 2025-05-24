#Change Tuple Values

#Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y.append('Mango')
x = tuple(y)
print(x)

#Add tuple to a tuple
w = ('orange',)
x += w
print(x)

#Remove Items
x = list(x)
x.remove('banana')
x = tuple(x)
print(x)

#delete the tuple
del x
print("list deleted", x)
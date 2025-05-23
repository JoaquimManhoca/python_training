#Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative Indexing
print(thistuple[-1])

#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:4])

#By leaving out the start value, the range will start at the first item
print(thistuple[:5])

#By leaving out the end value, the range will go on to the end of the tuple
print(thistuple[2:])

#Range of Negative Indexes
print(thistuple[-4:-1])

#Check if Item Exists
if 'banana' in thistuple:
    print('yes exist')
else:
    print('It don\'t exist')
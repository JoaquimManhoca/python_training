#Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append('Mango')
print(thislist)

#Insert Items
thislist.insert(1, "watermenol")
print(thislist)

#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable
thislist = ["apple", "banana", "cherry"]
tropical = ("mango", "pineapple", "papaya")
thislist.extend(tropical)
print(thislist)
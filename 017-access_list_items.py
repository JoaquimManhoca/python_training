#Access List Items
thislist = ["apple", "banana", "cherry","apple", "banana", "cherry"]
print(thislist[1])

#Negative Indexing
print(thislist[-1])

#Range of Indexes
print(thislist[2:4])

#Range of Negative Indexes
print(thislist[-4:-1])

#Check if Item Exists
if "Mango" in thislist:
    print("mango exist in the list")
else:
    print("Mango are not in the list")
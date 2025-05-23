#Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

num_list = [100, 50, 65, 82, 23]
num_list.sort()
print(num_list)

#Sort Descending
thislist.sort(reverse=True)
print(thislist)

print('_________________________________________')
#Customize Sort Function
def myfunc(n):
  return abs(n - 50)

list = [100, 50, 65, 82, 23]
list.sort(key = myfunc)
print(list)


print('_________________________________________')
#Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
L = []
for x in thislist:
  y = x.lower()
  L.append(y)

L.sort()
print(L)

print('_________________________________________')

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

print('_________________________________________')
thislist.reverse()
print(thislist)
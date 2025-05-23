#Copy a List
list1 = ['banana', 'cherry', 'Kiwi', 'Orange']
list2 = list1
print(list2)

#Use the copy() method
copyList = list1.copy()
print(copyList)

#Use the list() method
listmethod = list(list1)
print(listmethod)

#Use the slice Operator
sliceList = list1[:]
print(sliceList)
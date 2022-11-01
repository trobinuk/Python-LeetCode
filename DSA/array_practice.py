#Create an Array
from array import *

array_ex = array('i',[1,2,3,4,5])

#Traverse through an Array
for i in array_ex:
    print(i)

#Access element from an Array
print(array_ex[2])

#Append values into an Array
array_ex.append(6)

print(array_ex)

#Insert values into an Array

array_ex.insert(0,0)

print(array_ex)

array_ex.insert(3,22)

print(array_ex)

#Extend method for an array
array_ex1 = array('i',[7,8,9,10])

array_ex.extend(array_ex1)

print(array_ex)

#Remove element from an array
array_ex.remove(22)

print(array_ex)

#Remove last element of an array using POP method
print(array_ex.pop())

print(array_ex)

#Add elements using fromlist() method

list_ex = [10,11,12,13]

array_ex.fromlist(list_ex)

#Reverse method for arrays
array_ex.reverse()
print(array_ex)



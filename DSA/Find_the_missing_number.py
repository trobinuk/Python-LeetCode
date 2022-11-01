#How to find the missing number in an integer array of 1 to 100
#n(n+1)/2
from array import *

array_ex = array('i',[1,2,4,9,99])

array_missing_val = array('i',[])

for i in range(1,101):
    if i not in array_ex:
        array_missing_val.append(i)

print(array_missing_val)

#O(N) for the above query 
#Can I reduce this ?100*101/2
from array import *

missing_val = ''
s1 = ''
s = (100*101)/2
print(s)

array_val = array('i',[])
for i in range(1,101):
    array_val.append(i)

array_val.remove(89)

print(array_val)

s1 = sum(array_val)

missing_val = s-s1

print(missing_val)

def findMissing(list,n)


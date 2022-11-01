# Question 3 How to check if an array contains a number in Python
import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

#print(myArray)

def check_array_for_num (num_list,target_number):
    for i in num_list:
        if i == target_number:
            return True
    return False

check_array_for_num(myArray,22)



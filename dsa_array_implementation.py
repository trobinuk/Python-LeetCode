# implement 2 dimensional array
'''
import numpy as np

class Array_2D:
    def __init__(self):
        self.array_val = np()


array_val = np((1,'Robin'),(2,'Rakesh'),(3,'Ricky'))
print(array_val)
'''
from array import *

arr_val = array('i',(1,3,5,6,9,10))
arr_dec_val = array('d',(1.2,2.3,3.6,4.5))
arr_str_val = array('u',"robin,rakesh")

print(arr_val)
print(arr_dec_val)
print(arr_str_val)
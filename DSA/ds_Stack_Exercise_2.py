'''
Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
'''
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def insert_values(self,data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def reverse_using_stack(self):
        result = ''
        for i in range(len(self.container)):
            result = str(result)+str(self.pop())
        return result

    def is_balance(self):
        return None

stac_ex1 = Stack()
str_ex = '({a+b})'
for i in str_ex:
    if i in ('(',')','{','}','[',']'):
        stac_ex1.insert_values(i)

print(stac_ex1.container)

def opp_paran(in_data):
    if in_data == ')':
        return '('
    elif in_data == '}':
        return '{'
    elif in_data == ']': 
        return '['
    else:
        return None

str1 = ['(','{','}',')',']']
for i in str1:
    last_val = str1.pop()
    equivalent_val = opp_paran(last_val)
    for i in str1:
        if i == equivalent_val:
            str1.remove(equivalent_val)
            break
        if i == len(str1):
            print('False 1')

if len(str1) == 0:
    print('True')
else:
    print('False')

print(str1)
    

last_val = stac_ex1.pop()
#if last_val_1 in 
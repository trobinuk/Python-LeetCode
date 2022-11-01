#reverse_string("We will conquere COVID-19") should return "91-DOVOC ereuqnoc lliw eW"

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def insert_values(self,data):
        self.container.append(data)

    def last_out_values(self):
        return self.container.pop()

    def reverse_using_stack(self):
        result = ''
        for i in range(len(self.container)):
            result = str(result)+str(self.last_out_values())
        return result

stac_ex = Stack()
str_ex = "We will conquere COVID-19"

print(stac_ex.container)
for i in str_ex:
    #print(i)
    stac_ex.insert_values(i)

print(stac_ex.container)

print(stac_ex.reverse_using_stack())



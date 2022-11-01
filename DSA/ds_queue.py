from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()
    
    def insert_value(self,data):
        self.container.append(data)

    def last_out_value(self):
        if self.container:
            return self.container.popleft()
        else:
            return 'No values in the conatiner'

queue = Queue()
queue.insert_value('2')
queue.insert_value('89')
queue.insert_value('45')

print(queue.container)
queue.last_out_value()

print(queue.container)

#from collections import deque
#dir(deque)
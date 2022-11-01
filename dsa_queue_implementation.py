from collections import deque

class Queue:
    def __init__(self):
        self.queue_val = deque()

    def insert_val(self,val):
        self.queue_val.append(val)

    def get_val(self):
        out_val = self.queue_val.popleft()
        return out_val

queue = Queue()
queue.insert_val(21)
queue.insert_val(32)
queue.insert_val(48)
queue.insert_val(52)

print(queue.queue_val)

print(queue.get_val())

print(queue.queue_val)




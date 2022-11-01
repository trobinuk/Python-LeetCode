orders = ['pizza','samosa','pasta','biryani','burger']
#Place Order
#Serve Order
from collections import deque
from time import sleep

class Queue:
    def __init__(self):
        self.orders = deque()

    def place_order(self,in_data):
        self.orders.append(in_data)
        print('Order Placed')
        
    def order_queue(self,in_data_list=[]):
        for i in in_data_list:
            sleep(0.5)
            self.place_order(i)

    def serve_order(self):
        sleep(2)
        for i in range(len(self.orders)):
            if i == len(self.orders):
                print(self.orders.pop())
            else:
                print(self.orders.popleft())

queue = Queue()

orders = ['pizza','samosa','pasta','biryani','burger']
queue.order_queue(orders)
print(queue.serve_order())



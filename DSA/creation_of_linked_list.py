class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class Slinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertSLL(self,value,location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head 
                self.head = new_node
            elif location == -1:
                new_node.next = None
                self.tail = new_node
                self.tail.next = new_node
            else:
                i = 0
                while i < location-1:
                    temp_node = temp_node.next
                    i += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node



'''
singly_linked_list = Slinkedlist()
node1 = Node(1)
node2 = Node(2)

singly_linked_list.head = node1
node1.next = node2
singly_linked_list.tail = node2
'''




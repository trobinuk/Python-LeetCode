class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+'--> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def chk_ll_empty(self):
        if self.head is None:
            print("Linked list is empty")
            return

    def insert_at_end(self,data):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            print('Index out of range')

        if index == 0:
            self.insert_at_beginning(data)
            return
        elif index == self.get_length()-1:
            self.insert_at_end(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                #temp_node = itr
                node = Node(data,itr.next)
                itr.next = node

            itr = itr.next
            count += 1
            

ll = Linkedlist()
ll.insert_at_beginning('9856')
ll.insert_at_beginning('45')
ll.print()
ll.insert_at_end('200')
ll.print()
ll.insert_at(1,356)
ll.print()


        
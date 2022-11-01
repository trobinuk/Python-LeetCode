class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        lv_print  = ''
        while itr:
            lv_print += str(itr.val)+'---> ' if itr.next else str(itr.val)
            itr = itr.next
        print(lv_print)
        return

    def insert_val_at_beginning(self,val):
        node = Node(val,self.head)
        self.head = node

    def insert_val_at_end(self,val):
        if self.head is None:
            self.insert_val_at_beginning(val)
            return
            #print("Linked List is empty")
        cnt = 0
        itr = self.head
        while itr.next:   
            itr = itr.next
            cnt += 1
        #itr.next = val
        node = Node(val,None)
        itr.next = node

    def find_len(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1

        return count

    def insert_at(self,index,val):
        if index < 0 or index > self.find_len():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_val_at_beginning(val)

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(val,itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_val_at_beginning(24)
    ll.insert_val_at_beginning(49)
    ll.insert_val_at_end(89)
    ll.print()
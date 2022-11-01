class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert_val_at_begin(self,val):
        node = ListNode(val,self.head)
        self.head = node
    '''
     def insert_val_at_beginning(self,val):
        node = Node(val,self.head)
        self.head = node'''

    def print_val(self):
        itr = self.head
        print_val = ''
        while itr:
            print_val += str(itr.val)+'-->' if itr.next else str(itr.val)
            itr = itr.next
        print(print_val)

        '''itr = self.head
        lv_print  = ''
        while itr:
            lv_print += str(itr.val)+'---> ' if itr.next else str(itr.val)
            itr = itr.next
        print(lv_print)
        return'''

l1 = LinkedList()
l1.insert_val_at_begin(3)
l1.insert_val_at_begin(4)
l1.insert_val_at_begin(2)
l1.print_val()

l2 = LinkedList()
l2.insert_val_at_begin(4)
l2.insert_val_at_begin(6)
l2.insert_val_at_begin(5)
l2.print_val()

l1 = ListNode(3,4)

from typing import Optional

class Solution:
    def addTwoNos(self,l1: Optional[ListNode],l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            currentSum = l1Val+l2Val+carry
            newNode = ListNode(currentSum%10)
            curr.next = newNode
            curr = newNode
            carry = currentSum//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

solution = Solution()
l3 = LinkedList()
l3 = solution.addTwoNos(l1,l2)

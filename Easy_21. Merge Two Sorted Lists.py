# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_values_at_beginning(self,val):
        node = ListNode(val,self.head)
        self.head = node
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #if list1.val is None and list2.val is None:
            #return list1.val
        print('list1 ',list1.val)
        print('list2 ',list2.val)
        listnode = ListNode()
        if list1.val <= list2.val:
            listnode.val = list1.val
            listnode.next = list2.val
            print(listnode.val) 
        else:
            listnode.val = list2.val
            listnode.next = list1.val
            print(listnode.val) 
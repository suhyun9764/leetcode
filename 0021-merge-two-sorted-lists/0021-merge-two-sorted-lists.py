# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        current = prev
        
        while list1 and list2:
            if list1.val < list2.val:
                node = list1
                current.next = node
                current = current.next
                list1 = list1.next
            else :
                node = list2
                current.next = node
                current = current.next
                list2 = list2.next
                
        if list1:
            current.next = list1
            
        if list2:
            current.next = list2 
            
        return prev.next
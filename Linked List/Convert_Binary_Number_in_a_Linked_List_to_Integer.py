# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        curr = head

        inte = 0
        count = 0

        while curr.next:
            curr = curr.next
            count += 1
        
        while head:
            
            b = head.val
            inte += b*(2**count)
            head = head.next
            count -= 1
            
        return inte
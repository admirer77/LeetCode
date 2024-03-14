# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        front = ListNode(0)
        back = ListNode(0)

        small = front
        large = back

        while head != None:
            if head.val < x:
                small.next = head
                small = small.next
            
            else:
                large.next = head
                large = large.next

            head = head.next
        
        large.next = None
        small.next = back.next

        return front.next

        
        

            


            
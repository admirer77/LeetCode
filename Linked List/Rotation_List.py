# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head

        length = 1

        curr = head

        while curr.next:
            length += 1
            curr = curr.next

        k = k % length
        if k == 0:
            return head
        
        curr.next = head


        rotate = length - k

        while rotate:
            head = head.next
            curr = curr.next
            rotate -= 1


        curr.next = None
        
        return head
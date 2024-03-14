# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        lst = []

        if head is None:
            return 0

        slow = head
        fast = head

        while fast:

            fast = fast.next.next
            slow = slow.next

        
        prev = None
        curr = slow

        while curr:

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            

        first = head
        second = prev

        while second:
            a = first.val + second.val
            lst.append(a)
            first = first.next
            second = second.next
            
        return max(lst)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        left = right = head

        c1 = c2 = 0
        n = 0

        while c1<k-1:
            left = left.next
            c1+=1

        temp = head

        while temp:
            temp = temp.next
            n+=1


        while c2<n-k:
            right = right.next
            c2+=1

        t = left.val
        left.val = right.val
        right.val = t

        return head

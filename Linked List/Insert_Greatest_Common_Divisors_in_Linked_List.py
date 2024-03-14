# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)

        curr = dummy

        ele = head
        cur = head

        while ele.next:

            d = gcd(ele.val, ele.next.val)

            curr.next = ListNode(d)
            curr = curr.next
            ele = ele.next

        dummy = dummy.next

        while cur and dummy:
            temp = cur.next
            dum = dummy.next
            cur.next = dummy
            cur = cur.next
            cur.next = temp
            cur = cur.next
            dummy = dum

        return head

    def gcd(x,y):

        while y:
            x, y = y, x % y
        return x


        
    
    
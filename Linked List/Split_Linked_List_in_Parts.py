# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        lst = []

        curr = head
        cur = head

        length = 0

        while  curr:
            length += 1
            curr = curr.next
        
        b = length % k
        a = length // k

        while cur:
            l = ListNode(0)
            c = l
            if b != 0 :
                b -= 1
                for i in range(a+1):
                    c.next = ListNode(cur.val)
                    c = c.next
                    cur = cur.next
                lst.append(l.next)
                k -= 1
            else:
                for i in range(a):
                    c.next = ListNode(cur.val)
                    c = c.next
                    cur = cur.next
                lst.append(l.next)
                k -= 1


        while k:
            l = ListNode(0)
            lst.append(l.next)
            k -= 1
                
        return (lst)

        

                

                
        

        


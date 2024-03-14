# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        head1 = list1

        curr1 = head1
        curr2 = head1

        head2 = list2

        for i in range(a-1):
            curr1 = curr1.next

        for i in range(b):
            curr2 = curr2.next
        
        curr1.next = head2

        while head2.next:
            head2 = head2.next

        head2.next = curr2.next

        return head1
        

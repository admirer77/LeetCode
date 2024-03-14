# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        dummy = ListNode(0)
        curr = dummy

        ele = head

        while ele:
            if len(stack) == 0 or stack[-1] >= ele.val:
                stack.append(ele.val)
                ele = ele.next
            else:
                stack.pop()
        
        for i in range(len(stack)):
            curr.next = ListNode(stack[i])
            curr = curr.next
        

        return dummy.next

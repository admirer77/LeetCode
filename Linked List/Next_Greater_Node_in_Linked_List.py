# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        stack = []
        result = []

        while head:
            stack.append(head.val)
            head = head.next
        
        a = 0
        i = 0

        while len(stack) > 1:
            if stack[-1] >= stack[-2] and stack[-1] >= a:
                result.append(0)
                a = stack[-1]
                stack.pop()
            elif stack[-1] > stack[-2] and stack[-1] < a:
                result.append(a)
                a = stack[-1]
                stack.pop()
            elif stack[-1] < stack[-2] and stack[-1] == a:
                result.append(0)
                a = stack[-1]
                stack.pop()
            elif stack[-1] < stack[-2] and stack[-1] > a:
                result.append(a)
                a = stack[-1]
                stack.pop()
            else:
                result.append(a)
                stack.pop()
                
        if stack[-1] < a:
            result.append(a)
        else:
            result.append(0)
        
        return result[::-1]
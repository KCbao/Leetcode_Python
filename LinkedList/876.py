# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        seen = []
        pos = 0
        while head != None:
            seen.append(head)
            pos += 1
            head = head.next
        
        return seen[pos//2]
     
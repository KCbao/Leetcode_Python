# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# idea: use a list to record listnode seen
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        seen = []
        while head not in seen:
            seen.append(head)
            head = head.next
            if head == None:
                return False
        return True
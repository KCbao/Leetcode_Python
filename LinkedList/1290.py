# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        seenint = ""

        while head != None:
            seenint += str(head.val)
            head = head.next
        return int(seenint, 2)
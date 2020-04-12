# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        ans = ListNode(head.val)
        tmp = ans
        head = head.next
        while head != None:
            if tmp.val == head.val:
                head = head.next
            else:
                tmp.next = ListNode(head.val)
                tmp = tmp.next
        return ans
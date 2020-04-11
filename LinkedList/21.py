# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# idea: recursion
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            if l1.val <= l2.val:
                ans = ListNode(l1.val)
                l1 = l1.next
            else:
                ans = ListNode(l2.val)
                l2 = l2.next
            ans.next = self.mergeTwoLists(l1,l2)
            return ans
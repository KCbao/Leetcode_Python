# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        tmp = head
        if tmp == None:
            return head
        while tmp.val == val:
            if head != None:
                head = head.next
                tmp = head
            else:
                return head
            if tmp == None:
                return head
        while tmp.next != None:
            while tmp.next.val == val:
                tmp.next = tmp.next.next            
                if tmp.next == None:
                    return head
            tmp = tmp.next
        return head
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
       if root is None:
           return True
        return self.isSymmetricRecur(root.left, root.right)
        
    def isSymmetricRecur(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRecur(left.right, right.left) and self.isSymmetricRecur(left.left, right.right)
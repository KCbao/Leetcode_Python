# 看两个tree 是不是the same
# Idea: 
# Use recursion
# E.g., 
#     1
#   /   \
#  2     3
# TreeNode(1, left:2, right:3)
# TreeNode(2, left: None, right: None)
# None: 2.left
# None: 2.right
# TreeNode(3, left: None, right: None)
# None: 3.left
# None: 3.right


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Case 1: p,q are None nodes
        if p is None and q is None:
            return True
        # Case 2: p,q are not None nodes, they compare their node value, and recursion to left/right nodes
        if p is not None and q is not None: 
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

p = [1,2,3]
q = [1,2,3]
sol = Solution()
print(sol.isSameTree(p,q))
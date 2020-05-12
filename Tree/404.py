# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.sumOfLeft(root, 1)
    
    def sumOfLeft(self, root, label):
        # label 0: left, label 1: right
        left = root.left
        right = root.right
        total = 0
        if right != None or left != None:
            if left != None:
                total += self.sumOfLeft(left, 0)
            if right != None:
                total += self.sumOfLeft(right,1)
        else:
            if label == 0:
                total += root.val
        return total
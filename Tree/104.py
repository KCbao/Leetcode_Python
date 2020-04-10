# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}
# idea: use recursion

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        leftroot = root.left
        rightroot = root.right
      
        if leftroot != None or rightroot != None:      
            leftdepth, rightdepth = 0,0
            if leftroot != None:
                leftdepth = self.maxDepth(leftroot)
            if rightroot != None:
                rightdepth = self.maxDepth(rightroot)
            depth= 1+max(leftdepth, rightdepth)
        else:
            depth= 1
        return depth
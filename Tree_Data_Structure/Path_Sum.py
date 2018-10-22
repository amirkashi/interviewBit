# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Pay attention when you need to return 
"""


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def findSum(self, node, Sum, B):
        if not node:
            return
        if not node.left and not node.right:
            if Sum == B:
                return True
        if node.left:
            if self.find_sum(node.left, Sum + node.left.val, B):
                return True
        if node.right:
            if self.find_sum(node.right, Sum + node.right.val, B):
                return True

    def hasPathSum(self, A, B):
        Sum = A.val
        k = self.find_sum(A, Sum, B)
        if k:
            return 1
        else:
            return 0

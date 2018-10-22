# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def find_path(self, node, node_val, sums, target, result):
        if not node:
            return
        node_val.append(node.val)
        if not node.left and not node.right and sums == target:
            result.append(node_val[:])
        if node.left:
            self.find_path(node.left, node_val, sums + node.left.val, target, result)
        if node.right:
            self.find_path(node.right, node_val, sums + node.right.val, target, result)
        node_val.pop()

    def pathSum(self, A, B):
        if not A:
            return []
        result = []
        node_val = []
        sums = A.val
        self.find_path(A, node_val, sums, B, result)
        return result

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorder(self, node, tree_vals):
        if node == None:
            return 
        tree_vals.append(node.val)
        self.preorder(node.left, tree_vals)
        self.preorder(node.right, tree_vals)
    def preorderTraversal(self, A):
        if A == None:
            return []
        tree_vals = []
        self.preorder(A, tree_vals)
        return tree_vals


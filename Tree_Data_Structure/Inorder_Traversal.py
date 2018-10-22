# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorder(self, node, tree_vals):
        if not node:
            return
        self.inorder(node.left, tree_vals)
        tree_vals.append(node.val)
        self.inorder(node.right, tree_vals)

    def inorderTraversal(self, A):
        if not A:
            return []
        tree_vals = []
        self.inorder(A, tree_vals)
        return tree_vals
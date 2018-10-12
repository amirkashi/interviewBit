# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorder(self, node, tree_vals):
        if node == None:
            return 
        self.postorder(node.left, tree_vals)
        self.postorder(node.right, tree_vals)
        tree_vals.append(node.val)
        
    def postorderTraversal(self, A):
        if A == None:
            return []
        tree_vals = []
        self.postorder(A, tree_vals)
        return tree_vals


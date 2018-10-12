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
    def find_sum(self, node, Sum, B):
        if node == None:
            return 
        #print (Sum)
        if node.left == None and node.right == None:
            if Sum == B:
                return True
        #print (123)
        if node.left:
            if self.find_sum(node.left,  Sum + node.left.val, B):
                return True # key point
        if node.right:
            if self.find_sum(node.right, Sum + node.right.val, B):
                return True ## key point
                
    
    def hasPathSum(self, A, B):
        Sum = A.val
        #print (self.find_sum(A, Sum, B)) 
        #print (A.left.left.right)
        k = self.find_sum(A, Sum, B)
        if k:
            return 1
        else:
            return 0
        


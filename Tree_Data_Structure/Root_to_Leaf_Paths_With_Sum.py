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
    
    def find_path(self, node, node_val, Sum, target, result):
        if node == None:
            return 
        node_val.append(node.val)
        #print (node_val, Sum)
        if node.left == None and node.right == None and Sum == target:
            #print (node_val)
            result.append(node_val[:])

        if node.left:
            self.find_path(node.left, node_val, Sum + node.left.val, target, result)
        if node.right:
            self.find_path(node.right, node_val, Sum + node.right.val, target, result)
        node_val.pop()
        #return result 
    
    def pathSum(self, A, B):
        if not A:
            return []
        result = []
        node_val = []
        Sum = A.val
        #node_val.append(Sum)
        self.find_path(A, node_val, Sum, B, result)
        #print (self.result)
        return result

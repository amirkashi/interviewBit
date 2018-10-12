# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import OrderedDict
class Node:
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zig_zag(self, node, layers, level):
        if node == None:
            return 
        if len(layers) < level:
            #print (123)
            temp = []
            temp.append(node.val)
            layers.append(temp)
        else:
            if level%2 == 0:
                layers[level-1].insert(0, node.val)
            if level%2 == 1:
                layers[level-1].append(node.val)
        
        self.zig_zag(node.left, layers, level+1)
        self.zig_zag(node.right, layers, level+1)
    
    def zigzagLevelOrder(self, A):
        if A == None:
            return []
        layers = []
        level = 1
        self.zig_zag(A, layers, level)
        return layers

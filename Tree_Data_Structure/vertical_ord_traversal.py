# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
        
    def verticalOrderTraversal(self, A):
        if A == None:
            return []
        levels = {}
        q_node = []
        q_level = []
        
        q_node.append(A)
        q_level.append(0)
        while q_node:
            curr_node = q_node.pop(0)
            curr_level = q_level.pop(0)
            if curr_level not in levels:
                levels[curr_level] = [curr_node.val]
            else:
                levels[curr_level].append(curr_node.val)
            if curr_node.left != None:
                q_node.append(curr_node.left)
                q_level.append(curr_level-1)
            if curr_node.right != None:
                q_node.append(curr_node.right)
                q_level.append(curr_level+1)
        verticals = []
        for i in sorted(levels):
            verticals.append(levels[i])
        
        return verticals

"""
Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def level_order_helper(self, node, levels, level):
        if not node:
            return 
        if len(levels) < level:
            temp = []
            temp.append(node.val)
            levels.append(temp)
        else:
            levels[level-1].append(node.val)
        self.level_order_helper(node.left, levels, level + 1)
        self.level_order_helper(node.right, levels, level + 1)
    def levelOrder(self, A):
        if not A:
            return []
        levels = []
        level = 1
        temp = A
        self.level_order_helper(A, levels, level)
        return levels

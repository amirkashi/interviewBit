# solev using stack
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        result = 0
        if A == None:
            return result
        else:
            stack = []
            temp = A
            while temp != None:
                stack.append(temp.val)
                temp = temp.next
            temp = A
            pal = True
            while temp != None:
                if stack[-1] != temp.val:
                    pal = False
                else:
                    stack.pop()
                temp =temp.next
        if pal:
            result = 1
        return result 

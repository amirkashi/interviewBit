# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if A.next != None:
            first = A
            second = first.next
            # while first != None and second != None :
            while  second != None :
                if first.val == second.val:
                    first.next = second.next
                    second.next = None
                    second = first.next
                #elif first.val == second.val and second.next == None:
                #    first.next = None
                #    break
                else:
                    first = first.next
                    second = first.next
            
        return A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    
    def mergeTwoLists(self, A, B):
        if A == None and B == None:
            return None
        if A == None:
            return B
        if B == None :
            return A
    
        if A.next == None and B.next == None:
            if A.val <= B.val:
                A.next = B
                return A
            else:
                B.next = A
                return B
        if A.next == None:
            A, B = B, A
        head_A = A
        first_A = A
        second_A = A.next
        first_B = B
        
        while second_A != None and B != None:
            if first_B.val <= first_A.val and  first_A == A:
                B = first_B.next
                first_B.next = A
                A = first_B
                first_A = A
                second_A = A.next
                first_B = B
            
            #if first_A.val <= first_B.val and first_B.val <= second_A.val:
            elif  first_B.val <= second_A.val:
                #print (first_B.val)
                B = first_B.next
                #print (B.val)
                first_B.next = second_A
                first_A.next = first_B
                second_A = first_A.next
                first_B = B
                #print (B.val)
            else:
                first_A = first_A.next
                second_A = second_A.next
            
        #print (last_node.val)
        if B != None:
            first_A.next = B
        
        return A
        
            


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        if A == None:
            return None
        if A.next == None:
            return A
        if B <= 0:
            return A
        head = A
        # find number of node in list
        node_number = 0
        temp = A 
        while temp != None:
            #print (temp.val)
            node_number+=1
            temp = temp.next
        B = B%node_number
        if B == 0:
            return A
        #print (node_number)
        ### move temp where we  want to rotate
        rotate_index = node_number - B 
        
        #print (rotate_index)
        temp = A
        #print (rotate_index)
        rotate_index-=1
        while rotate_index !=0:
            rotate_index-=1
            temp = temp.next 
        #print (temp.val)
        rotate = temp.next
        temp.next = None
        #print (rotate.val)
        A = rotate # make rotation location head 
        #print (head.val, rotate.val)
        while rotate.next != None:
            rotate = rotate.next
        #print (A.val, rotate.val, head.val)
        rotate.next = head
        return A

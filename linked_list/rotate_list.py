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
        node_number = 0
        temp = A 
        while temp != None:
            node_number+=1
            temp = temp.next
        B = B%node_number
        if B == 0:
            return A
        rotate_index = node_number - B 
        temp = A
        rotate_index-=1
        while rotate_index !=0:
            rotate_index-=1
            temp = temp.next 
        rotate = temp.next
        temp.next = None
        A = rotate
        while rotate.next != None:
            rotate = rotate.next
        rotate.next = head
        return A
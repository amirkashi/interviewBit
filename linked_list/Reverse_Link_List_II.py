# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def search(self, node ,n):
        counter = 1
        curser = node
        while counter < n:
            curser = curser.next
            counter+=1
        return curser 
        
    def reverse(self, node):
        if node == None:
            return None
        if node.next == None:
            return node
        curser = node
        rev = None
        while curser != None:
            if rev == None:
                rev = curser
                curser = curser.next
                rev.next = None
            else:
                temp = curser.next
                curser.next = rev
                rev = curser
                curser = temp 
                
    def reverseBetween(self, A, B, C):
        if not A:
            return A
        if A.next == None:
            return A
        if B == C:
            return A
        head = A
        prv_B = None
        if B == 1:
            node_B = A
            head = self.search(A, C)
            tail = node_B.next
            last_head = head.next
            head.next = None
            node_B.next = None
            self.reverse(tail)
            tail.next = node_B
            node_B.next = last_head
            
            return head 
        else:
            prv_B = self.search(A, B-1)
            prv_C = self.search(A, C)
            mid_head = prv_B.next
            prv_B.next = None
            last_head =  prv_C.next
            prv_C.next = None
            self.reverse(mid_head)
            prv_B.next = prv_C
            mid_head.next = last_head
            return head 

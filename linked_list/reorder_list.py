# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def find_middle(self, node):
        slow = node
        fast = node.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse(self, node):
        curr = node
        rev = None
        while curr != None:
            if rev == None:
                rev = curr
                curr = curr.next
                rev.next = None
            else:
                temp = curr.next
                curr.next = rev
                rev = curr
                curr = temp
        return rev        
            
        
    def reorderList(self, A):
        if A == None or A.next == None or A.next.next == None:
            return A
        head = A
        middle = self.find_middle(head)
        right = middle.next
        middle.next = None
        
        #print(right.val)
        right = self.reverse(right)
        #print(right.val)
        curr = head
        #temp_l = head
        
        while curr != None and right != None:
            #print (curr.val)
            temp_l = curr.next
            temp_r = right.next
            #print (curr.val, right.val)
            curr.next = right
            right.next = temp_l
            
            right = temp_r
            curr = temp_l
             
        return head 

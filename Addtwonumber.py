# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode()
        curr_node = dummy_head
        carry = 0
        p = l1
        q = l2

        while p!=None or q!=None:
            x = 0 if p is None else p.val
            y = 0 if q is None else q.val               
            
            sum_ = x + y + carry
            carry = sum_//10

            curr_node.next = ListNode(sum_ % 10)
            curr_node = curr_node.next
            p = p.next if p is not None else p
            q = q.next if q is not None else q
        
        if carry > 0:
            curr_node.next = ListNode(carry)
                
        return dummy_head.next 
                

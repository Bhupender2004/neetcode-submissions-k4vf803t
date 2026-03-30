# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            # Save the next node
            next_temp = curr.next
            # Reverse the link
            curr.next = prev
            # Move pointers one step forward
            prev = curr
            curr = next_temp
        
        return prev

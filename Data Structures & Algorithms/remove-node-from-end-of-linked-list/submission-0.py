# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # take two pointer, left, right,
        # first took the right ponter ahead of n numbers
        # then start to moving left and right
        # so , we can ensure that, left is always be behind of n numbers 

        dummy = ListNode(0,head)
        left,right = dummy, head
        
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next
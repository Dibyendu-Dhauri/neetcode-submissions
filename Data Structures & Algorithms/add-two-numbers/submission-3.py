# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        rem = carry = 0
        dummy = ListNode(-1)
        curr = dummy

        while l1 or l2 or carry:
            total_sum = 0
            total_sum += carry
            total_sum += l1.val if l1 else 0
            total_sum += l2.val if l2 else 0
        
            rem = total_sum % 10
            carry = total_sum  // 10
            curr.next = ListNode(rem)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next


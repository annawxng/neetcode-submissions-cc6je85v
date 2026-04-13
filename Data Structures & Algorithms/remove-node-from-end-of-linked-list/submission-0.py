# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # left / right pointer
        # gap is n
        # intialize L to dummy, R is initalized to n nodes after

        dummy = ListNode(0)
        dummy.next = head

        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        # left.next is the node we want to remove
        left.next = left.next.next
        return dummy.next
        

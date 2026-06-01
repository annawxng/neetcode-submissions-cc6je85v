# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        

        # 3 phases:
        # find the middle - fast / slow pointers
        # reverse the second half
        # create the list, alternating between first and second half

        # [2,4,6s,8,10f]
        # once fast pointer reaches end, we know s is the middle
            # fast moves by 2, s moves by 1
        # [2,4,6s,8sec,10f] reverse [s, f] ==> [2,4,6,10,8], since we want to reverse second = slow.next
        # set slow.next = None as well to cut the two lists
        # 2, 10, 4, 8, 6 -- alternate between first half and second half
        
        # [2,4f,6,8f,10,]  

        #  8  ->  10f, we want #  10 ->  8  
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None
        
        # reverse second list
        # e.g., curr = 4 in 4 -> 5 -> 6, becomes 6-> 5 -> 4, and 

        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # prev is now at start of second list

        # alternate

        first = head
        second = prev
      
        # 2f -> 4p1 -> 6,     10s -> 8p2s

        # 2 -> 10 -> 4

        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
    
        return
        


        





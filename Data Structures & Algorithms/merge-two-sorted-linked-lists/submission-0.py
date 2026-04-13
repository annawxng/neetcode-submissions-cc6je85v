# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # loop through each linkedlist - compare the nodes
        # if list1 node < list2 node, add list1 node first: else, add list2 node first


        # list1 = [1,2,4]
        # list2 = [1,3,5]
        # dummy -> 1 - 1 - 2 - 3 - 4 - 5
        # return dummy -> next (head of the output linkedlist)
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # dont forget the case where one list still has stuff
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
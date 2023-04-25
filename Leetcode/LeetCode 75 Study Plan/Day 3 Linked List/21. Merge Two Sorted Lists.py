# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # If one of the linked lists is empty, return the other
        if not l1:
            return l2
        if not l2:
            return l1
        
        # If the value of the first node in l1 is less than or equal to the value of the first node in l2,
        # set the next node of l1 to the result of recursively merging the rest of l1 with l2,
        # and return l1 as the merged list
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        # If the value of the first node in l2 is less than the value of the first node in l1,
        # set the next node of l2 to the result of recursively merging l1 with the rest of l2,
        # and return l2 as the merged list
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
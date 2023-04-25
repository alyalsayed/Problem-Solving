# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            # save the next node
            next_node = curr.next
            
            # reverse the current node's pointer
            curr.next = prev
            
            # update the prev and curr pointers
            prev = curr
            curr = next_node
        
        # return the new head of the reversed list
        return prev
        
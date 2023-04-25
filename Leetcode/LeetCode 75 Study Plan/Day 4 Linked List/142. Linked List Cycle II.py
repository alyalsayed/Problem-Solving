# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Step 1: Find the intersection point of the two pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not fast or not fast.next:
            # No cycle
            return None

        # Step 2: Move one pointer to the head of the list
        slow = head

        # Step 3: Move both pointers at the same pace until they meet
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # The meeting point is the node where the cycle begins
        return slow
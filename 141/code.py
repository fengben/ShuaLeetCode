# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        # ListNode
        fast = head
        slow = head
        while fast.next:
            fast=fast.next
            if fast.next is None:
                return False
            fast=fast.next
            slow=slow.next
            if (fast == slow):
                return True
        return False
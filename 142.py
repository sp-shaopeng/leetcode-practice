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
        s = set()
        h = head
        while((h not in s) and (h != None)) :
            s.add(h)
            h = h.next
        return h
        
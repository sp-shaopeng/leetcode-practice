# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r = head
        resetHead = True
        prev = None
        while(r != None and r.next != None) :
            if(resetHead) :
                head = r.next
                resetHead = False

            a = r.next.next
            if(prev != None) :
                prev.next = r.next
            r.next.next = r
            r.next = a
            prev = r
            r = a
            
        return head

        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr = head
        toRemove = head
        p = None
        for i in range(1,n):
            ptr =ptr.next
        
        while(ptr.next != None) :
            p = toRemove
            toRemove = toRemove.next
            ptr= ptr.next
            
        
        if(toRemove.val == head.val and p == None) :
            return head.next
        
        
        p.next = toRemove.next
        return head
        
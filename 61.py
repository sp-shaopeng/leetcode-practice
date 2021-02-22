# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        p = head
        i = 0
        while(p != None):
            i += 1
            p = p.next
        if(i == 0):
            return head
        k = k % i
        k = i - k
        
        r = head
        before = head
        newR = head
        
        for i in range(k):
            if(newR.next == None):
                return r
            
            before = newR
            newR = newR.next
            
        tail = newR
        while(tail.next != None):
            tail = tail.next
            
        tail.next = r
        before.next = None
        return newR
        
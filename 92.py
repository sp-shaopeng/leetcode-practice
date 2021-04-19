# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        
        ptr = head
        count = 1
        p = None
        while(ptr != None and count < left):
            p = ptr
            ptr = ptr.next
            count += 1
        
        if( ptr == None) :
            return head
        
        ll = ptr
        l = ptr
        r = ptr.next
        count += 1
        while(l != None and r != None and count <= right) :
            holder = r.next
            r.next = l
            l = r
            r = holder
            count += 1
        
        ptr.next = r
        
        if(p == None):
            return l
        p.next = l

    
        return head
        
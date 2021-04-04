# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = None
        ans = None
        
        if(l1 == None and l2 == None) :
            return None
        if(l1 == None) :
            return l2
        if(l2 == None) :
            return l1
        if(l1.val < l2.val) :
            head = l1
            ans = l1
            l1 = l1.next
        else:
            ans = l2
            head = l2
            l2 = l2.next
        
        while(True) :
            if(l1 == None):
                head.next = l2
                return ans
            if(l2 == None):
                head.next = l1
                return ans
            if(l1.val < l2.val):
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next
            
            
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = []
        extra = 0
        
        strl1, strl2 = "", ""
        while(l1 != None):
            strl1 += str(l1.val)
            l1 = l1.next
        
        while(l2 != None):
            strl2 += str(l2.val)
            l2 = l2.next
        
        strl1 = strl1[::-1]
        strl2 = strl2[::-1]
        intl1 = int(strl1)
        intl2 = int(strl2)
        ans = intl1 + intl2
        out = ListNode(0)
        p = out
        while(ans>0) :
            p.val = ans%10
            ans = ans /10
            if(ans > 0) :
                p.next = ListNode(0)
                p = p.next
        return out           
        
        
        
        
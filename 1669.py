# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        head = list1
        tail = list1
        hc = 1
        tc = 1
        
        
        while(True):
             
            if(hc <= a - 1):
                head = head.next
            
            if(tc <= b + 1) :
                tail = tail.next
            else:
                break
                
            hc += 1
            tc += 1  
        
        head.next = list2
        while(True) :
            if(list2.next == None):
                list2.next = tail
                break
            list2 = list2.next
        
        return list1
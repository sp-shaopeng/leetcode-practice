# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less = None
        lessPointer = None
        more = None
        morePointer = None
        
        while(head != None) :
            if(head.val < x) :
                if(less == None):
                    less = head
                    lessPointer = head
                else:
                    lessPointer.next = head
                    lessPointer = lessPointer.next
            else:
                if(more == None):
                    more = head
                    morePointer = head
                else:
                    morePointer.next = head
                    morePointer = morePointer.next
            head = head.next
        if(lessPointer != None) :
            lessPointer.next = more
        
        if(morePointer != None) :
            morePointer.next = None
        
        if(less == None) :
            return more
        else:
            return less
        
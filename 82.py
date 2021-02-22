# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = None
        c = -99
        track = []
        ptr1 = None
        while(head is not None):
            if(head.next is not None):
                if(head.val != head.next.val and c != head.val):
                    if(ptr is None) :
                        ptr = head
                        ptr1 = ptr
                    else :
                        ptr1.next = head
                        ptr1 = ptr1.next
                else :
                    c = head.val
            
            else:
                if(head.val != c) :
                    if(ptr is None) :
                        ptr = head
                        ptr1 = ptr
                    else :
                        ptr1.next = head
                        ptr1 = ptr1.next
            head = head.next
            
        print(c)
        if(ptr1 is not None):
            ptr1.next = None
        return ptr
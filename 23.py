from Queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        
        pq = PriorityQueue()
        
        
        for nodes in lists :
            if(nodes != None) :
                pq.put((nodes.val, nodes))
       
        if(pq.qsize() == 0) :
            return None
        
        head = None
        v, node = pq.get()
        head = node
        ptr = head
        if(node.next != None) :
            pq.put((ptr.next.val, node.next))
        
        while(pq.qsize() > 0) :
            v, node = pq.get()
            ptr.next = node
            ptr = ptr.next
            if(node.next != None) :
                pq.put((ptr.next.val, node.next))
        return head
        
        
        
        
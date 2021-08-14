"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        def flat(node) :
            start, end = node, node
            n = node.next
            if(node.child != None) :
                s, e = flat(node.child)
                s.prev = node
                node.next = s
                end = e
                node.child = None
            
            if(n) :
                ns, ne = flat(n)
                end.next = ns
                ns.prev = end
                end = ne           
            return start, end
        
        if(head) :
            return flat(head)[0]
        return None
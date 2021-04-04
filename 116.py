"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if(root == None) :
            return None
        
        Q = [root]
        while(Q) :
            newQ = []
            curr = Q.pop(0)
            while(True) :
                n = None
                if(Q):
                    n = Q.pop(0)
                curr.next = n
                if(curr.left != None) :
                    newQ.append(curr.left)
                if(curr.right != None) :
                    newQ.append(curr.right)
                curr = n
                if(curr == None) :
                    break
            Q = newQ
        return root
        
        
        
        
        
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        
        def link(node) :
            start, end = node, node
            if(node.left != None) :
                ls, le = link(node.left)
                start = ls
                le.right = node
                node.left = le
            if(node.right != None) :
                rs, re = link(node.right)
                end = re
                node.right = rs
                rs.left = node
  
            return start, end
        
        if(root) :
            s, e = link(root)
            s.left = e
            e.right = s
            return s
        return root
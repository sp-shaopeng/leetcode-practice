"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def find(node) :
            if(not node) :
                return 0
            m = 0
            for i in node.children :
                m = max(m, find(i))
            return 1 + m
        return find(root)
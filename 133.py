"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        e = {}

        return self.find(node, e)
        
        
        
    def find(self, node, e):
        if(node == None) :
            return None
        if(node in e):
            return e[node]
        
        newN = Node(node.val)
        e[node] = newN
        
        for i in node.neighbors :
            newN.neighbors.append(self.find(i, e))
        
        return newN
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def find(node) :
            if(node == None):
                return False
            
            r1 = find(node.left)
            if( not r1):
                node.left = None
            
            r2 = find(node.right)
            
            if(not r2):
                node.right = None
            
            return node.val == 1 or r1 or r2
        
        r = find(root)
        if(not r):
            root = None
        return root
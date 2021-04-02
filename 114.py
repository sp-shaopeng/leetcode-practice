# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        def find(node):
            l = None
            if(node.left != None):
                l = find(node.left)
            
            r = None
            if(node.right != None):
                r = find(node.right)
            if(l!=None):
                node.right = l
                while(l.right != None):
                    l = l.right
                l.right = r
            else:
                node.right = r
            node.left = None
            return node
        
        if(root == None) :
            return []
        
        return find(root)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(node):
            if(node == None):
                return 
            
            a = invert(node.right)
            b = invert(node.left)
            node.left = a
            node.right = b
            return node
        
        root = invert(root)
        return root
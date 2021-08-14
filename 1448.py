# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if(not root) :
            return 0
        
        res = [0]
        
        def find(node, curr) :
            if(node.val >= curr) :
                res[0] += 1
                curr = node.val
            
            if(node.left != None) :
                find(node.left, curr)
                  
            if(node.right != None) :
                find(node.right, curr)
            
        find(root, root.val)
        return res[0]
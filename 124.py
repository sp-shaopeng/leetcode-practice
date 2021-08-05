# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        m = [root.val]
        
        def find(node) :
            if(not node) :
                return 0, False
            res = node.val
            l, cl = find(node.left)
            r, cr = find(node.right)
            if(cl) :
                m[0] = max(m[0], l, l + node.val)
                res = max(res, l + node.val)
            if(cr) :
                m[0] = max(m[0], r, r + node.val)
                res = max(res, r + node.val)
            
            if(cl and cr) :
                m[0] = max(m[0], l + r + node.val)
            return res, True
    
        find(root)
        return m[0]
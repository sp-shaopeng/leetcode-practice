# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        paV = root.val
        pv = p.val
        qv = q.val
        
        if(pv > paV and qv > paV) :
            return self.lowestCommonAncestor(root.right, p, q)
        
        if(pv < paV and qv < paV) :
            return self.lowestCommonAncestor(root.left, p, q)
        
        return root
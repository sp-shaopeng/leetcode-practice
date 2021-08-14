# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if( not root ) :
            return 0
        
        Q = [root]
        res = 0
        while(Q) :
            newQ = []
            res = 0
            while(Q) :
                n = Q.pop()
                res += n.val
                if(n.left != None) :
                    newQ.append(n.left)
                if(n.right != None) :
                    newQ.append(n.right)
            
            if(not newQ) :
                return res
            Q = newQ
                
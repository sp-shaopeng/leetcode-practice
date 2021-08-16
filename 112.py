# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        if(not root) :
            return False
        Q = [[root, targetSum]]
        
        while(Q) :
            newQ = []
            while(Q) :
                n, v = Q.pop()
                v = v - n.val
                if(n.left == None and n.right == None and v == 0) :
                    return True
                if(n.left != None) :
                    newQ.append([n.left, v])
                if(n.right != None) :
                    newQ.append([n.right, v])
            
            Q = newQ
            
        return False
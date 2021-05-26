# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
    
        def equal(t1,t2) :
            
            if(t1 == None or t2 == None) :
                return t1 == t2
            
            if(t1.val == t2.val) :
                return equal(t1.left, t2.left) and equal(t1.right, t2.right)
            
            return False
        
        def subT(t1, t2) :
            
            if(t1 == None or t2 == None) :
                return t1 == t2
            
            if(equal(t1, t2)) :
                return True
            return subT(t1.left, t2) or subT(t1.right, t2)
        
        return subT(s, t)
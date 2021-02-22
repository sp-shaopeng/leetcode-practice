# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        b = [True]
        def find(node) :
            l = 0
            r = 0
            if(node.left != None):
                l = find(node.left) 
            if(node.right != None):    
                r = find(node.right)
            if(l > r + 1 or r > l + 1):
                b[0] = False
                return -9999
            else:
                return max(l,r) + 1
        if(root == None):
            return True
        
        a = find(root)
        return b[0]
        
        
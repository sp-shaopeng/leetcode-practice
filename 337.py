# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def find(node):
            a = [0,0]
            b = [0,0]
            
            if(node.left == None and node.right == None) :
                return [node.val, 0]
            
            if(node.left != None) :
                a = find(node.left)
            
            if(node.right != None) :
                b = find(node.right)
            
            s = a[0] + b[0]
            k = a[1] + b[1]
            
            
            return (max(node.val + k, s), max(s,k))
        
        return max(find(root))
                
            
            
            
            
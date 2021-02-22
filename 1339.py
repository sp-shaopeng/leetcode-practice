# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def total(node):
            if(node == None):
                return 0
            else:
                return node.val + total(node.left) + total(node.right)
        
        t = total(root)
        val = [-999]
        

        def find(node):
            if(node == None):
                return 0
            
            else:
                v = node.val + find(node.left) + find(node.right)
                if(v* (t - v) > val[0]):
                    val[0] = v * (t-v)
                return v
        find(root)            
        return val[0]%(1000000007)
    
    
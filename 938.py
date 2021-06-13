# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        ans = [0]
        
        def find(node) :
            
            if(node == None) :
                return
            
            if(node.val >= low and node.val <= high) :
                ans[0] += node.val
                find(node.left)
                find(node.right)
                return
            
            if(node.val < low) :
                find(node.right)
            else:
                find(node.left)
        
        find(root)
        return ans[0]
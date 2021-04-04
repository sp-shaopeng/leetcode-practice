# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        ans = []
        def find(node) :
            
            if(node.left != None) :
                find(node.left)
            
            ans.append(node.val)
            
                
            if(node.right != None) :
                find(node.right)
                
        if(root == None) :
            return ans
        
        find(root)
        return ans
            
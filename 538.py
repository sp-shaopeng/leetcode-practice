# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
#         we need DFS       
        
        def dfs(node, v):            
            if(node.right != None):
                node.val += dfs(node.right, v)
            else:
                 node.val += v
            
            v = node.val
            if(node.left != None):
                return dfs(node.left, v) 
                
            return v
        if(root == None):
            return None
        
        dfs(root, 0)
        return root
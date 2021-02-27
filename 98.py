# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def find(node, lower, upper):
            # print(node.val, lower, upper)
            if(node == None):
                return True
            if(node.val <= lower or node.val >= upper):
                print(node.val, lower, upper)
                return False
            
            if(node.left != None and node.right != None):
                return find(node.left, lower, node.val) and find(node.right, node.val, upper)
            if(node.left != None):
                return find(node.left, lower, node.val)
            if(node.right != None):
                return find(node.right, node.val, upper)
            
            return True
            
            
        return find(root.left, -99999999999999, root.val) and find(root.right, root.val, 99999999999999)
            
            
        
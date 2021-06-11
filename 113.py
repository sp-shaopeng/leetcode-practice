# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        path = []
        def find(node, v, leftOver) :
            
            if(node == None) :
                return 
            
            a = v[:]
            a.append(node.val)
            leftOver -= node.val
            
            
            if(node.left == None and node.right == None) :
                if(leftOver == 0) :
                    path.append(a)
                return
            
            if(node.left != None) :
                find(node.left, a, leftOver)
            
            if(node.right != None) :
                find(node.right, a, leftOver)
            
        
        find(root, [], targetSum)
        return path
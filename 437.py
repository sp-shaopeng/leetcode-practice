# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        
        if(not root) :
            return 0
        
        res = [0]
        
        def find(node) :
            
            s = []
            
            if(node.left != None) :
                s += find(node.left)
                            
            if(node.right != None) :
                s += find(node.right)
            
            newS = [node.val]
            if(node.val == sum):
                res[0] += 1
            for i in s :
                k = node.val + i
                if(k == sum) :
                    res[0] += 1
                newS.append(k)
            return newS
            
            
            
        a = find(root)
        return res[0]
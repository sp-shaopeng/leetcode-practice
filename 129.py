# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = []
        
        q = [[0,root]]
        
        while(q) :
            newQ = []
            while(q):
                val, node = q.pop()
                v = val* 10 + node.val
                if(node.left == None and node.right == None) :
                    nums.append(v)
                
                if(node.left != None) :
                    newQ.append([v, node.left])
                
                if(node.right != None) :
                    newQ.append([v, node.right])
            q = newQ    
        
        return sum(nums)
        
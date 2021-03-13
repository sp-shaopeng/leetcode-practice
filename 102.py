# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        ans = []
        if(root == None):
            return ans
        queue = [root]
        
        while(queue) :
            
            level = []
            newQ = []
            while(queue):
                v = queue.pop(0)
                level.append(v.val)
                if(v.left != None):
                    newQ.append(v.left)
                if(v.right != None):
                    newQ.append(v.right)
            # level.sort()
            ans.append(level)
            queue = newQ
        return ans
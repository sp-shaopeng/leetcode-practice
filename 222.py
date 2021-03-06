# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        
#         can do dfs or bfs
        queue = []
        
        if(root == None):
            return 0
        queue.append(root)
        
        while queue:
            v = queue.pop()
            ans += 1
            if(v.left != None):
                queue.append(v.left)
            if(v.right != None):
                queue.append(v.right)
        
        return ans
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        if(root == None) :
            return ans
        
        queue = [root]
        
        while(queue) :
            newQ = []
            toAppend = True
            while(queue) :
                n = queue.pop()
                
                if(toAppend) :
                    ans.append(n.val)
                    toAppend = False
                 
                if(n.right != None) :
                    newQ.insert(0, n.right)
                
                if(n.left != None) :
                    newQ.insert(0, n.left)
            
            queue = newQ
        
        return ans
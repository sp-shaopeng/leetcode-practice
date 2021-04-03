# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        Q = [root]
        if(root == None) :
            return []
        while(Q) :
            newQ = []
            val = 0 
            count = 0.0
            while(Q) :
                n = Q.pop()
                val += n.val
                count += 1.0
                if(n.left != None) :
                    newQ.append(n.left)
                if(n.right != None) :
                    newQ.append(n.right)


            ans.append(val/count)
            Q = newQ
        return ans
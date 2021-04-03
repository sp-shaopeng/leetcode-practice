# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        Q = [root]
        if(root == None) :
            return []
        while(Q) :
            newQ = []
            val = []

            while(Q) :
                n = Q.pop(0)
                val.append(n.val)
                if(n.left != None) :
                    newQ.append(n.left)
                if(n.right != None) :
                    newQ.append(n.right)


            ans.insert(0, val)
            Q = newQ
        return ans
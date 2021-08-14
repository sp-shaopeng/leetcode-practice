# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def sums(node) :
            ans = 0
            if(node.left != None) :
                ans += node.left.val
            if(node.right != None) :
                ans += node.right.val
            
            return ans
        
        Q = [root]
        res = 0
        while(Q) :
            newQ = []
            while(Q) :
                n = Q.pop()
                
                if(n.left != None) :
                    if(n.val % 2 == 0) :
                        res += sums(n.left)
                    newQ.append(n.left)
                
                if(n.right != None) :
                    if(n.val % 2 == 0) :
                        res += sums(n.right)
                    newQ.append(n.right)
            Q = newQ
        
        return res
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        ans = []
        def find(node):
            if(node.left == None and node.right == None):
                ans.append(node.val)
                return [node.val,True, node.val, node.val]
            
            left, leftC, lmin, lmax = 0, True, node.val, node.val
            right, rightC, rmin, rmax  = 0, True, node.val, node.val
            
            if(node.left != None):
                if(node.val <= node.left.val) :
                    leftC = False
                    find(node.left)
                else:
                    left, leftC, lmin, lmax = find(node.left)
            
            if(node.right != None):
                if(node.val >= node.right.val) :
                    rightC = False
                    find(node.right)
                else:
                    right, rightC, rmin, rmax = find(node.right)
            if(leftC and rightC and node.val >= lmax and node.val <= rmin):
                ans.append(left + right + node.val)
                lm = min(node.val, lmin)
                rm = max(node.val, rmax)
                return [left + right + node.val, True, lm, rm]
            else:
                return [0, False, node.val, node.val]
        
        find(root)
        return max(max(ans), 0)
            
            
            
            
            
        
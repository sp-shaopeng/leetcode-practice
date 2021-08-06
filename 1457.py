# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = [0]
        def find(node, d) :
            if(node.val in d) :
                d.pop(node.val)
            else :
                d[node.val] = 1
                
            dd = d.copy()
            if(node.left != None) :
                find(node.left, d)
            if(node.right != None) :
                find(node.right,dd)
            
            if(node.left == None and node.right == None) :
                if(len(d) <= 1) :
                    count[0] += 1
        
        find(root, {})
        return count[0]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        m = [0]
        
        def find(node, expected, count) :
            # print(expected, count)
            m[0] = max(m[0], count)
            if(expected == "L") :
                if(node.left != None):
                    find(node.left, "R", count + 1)
                    find(node.left, "L", 0)
            
            if(expected == "R") :
                if(node.right != None):
                    find(node.right, "L", count + 1)
                    find(node.right, "R", 0)
        find(root, "L", 0)
        find(root, "R", 0)
        return m[0]
            
            
            
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        
        def find(node, level):
            if(level == d - 1):
                lhs = TreeNode()
                lhs.val = v
                lhs.left = node.left
                node.left = lhs
                
                rhs = TreeNode()
                rhs.val = v
                rhs.right = node.right
                node.right = rhs
            else:
                if(node.left != None):
                    find(node.left, level + 1)
                if(node.right != None):
                    find(node.right, level + 1)
              
        if(d == 1) :
            lhs = TreeNode()
            lhs.val = v
            lhs.left = root
            return lhs
        else:
            find(root,1)
        return root
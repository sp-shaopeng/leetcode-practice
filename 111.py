# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find(node) :
            if(node.left == None and node.right == None) :
                return 1           
            elif(node.left != None and node.right != None) :
                return 1 + min(find(node.left), find(node.right))
            elif(node.left != None) :
                return 1 + find(node.left)
            elif(node.right != None) :
                return 1 + find(node.right)
       
        if(root == None) :
            return 0
        return find(root)
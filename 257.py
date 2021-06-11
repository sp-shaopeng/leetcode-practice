# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        
        path = []
        
        def find(node, val) :
            if(node == None) :
                return
            if(val == "") :
                val = str(node.val)
            else:
                val = val + "->" + str(node.val)
            
            if(node.left == None and node.right == None) :
                path.append(val)
            
            if(node.left != None) :
                find(node.left, val)
            
            if(node.right != None) :
                find(node.right, val)
                
        
        find(root, "")
            
        return path
            
        
        
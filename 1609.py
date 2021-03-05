# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        v = []
        nextLevel = []
        v.append(root)
        even = True;
        while(True):
            val = -1
            for node in v:
                
                if(even and node.val % 2 != 1) :
                    return False
                
                if(not even and node.val % 2 != 0 ):
                    return False
                
                if(val == -1):
                    val = node.val
                else:
                    if(even):
                        if(val >= node.val):
                            return False
                    
                    else:
                        if(val <= node.val):
                            return False
                    
                    val = node.val
                if(node.left != None):
                    nextLevel.append(node.left)
                if(node.right != None):
                    nextLevel.append(node.right)
            
            even = not even
            v = nextLevel
            nextLevel = []
            if(len(v) == 0):
                break
        
        return True
                        
            
        
            
            
        
        
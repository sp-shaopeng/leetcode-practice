# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        
        visited = []
        dup = set()
        dupV = []
        
        
        def find(node) :
            if(node.left == None and node.right == None) :
                if([node.val] in visited) :
                    if([node.val] not in dupV) :
                        dup.add(node)
                        dupV.append([node.val])
                else :
                    visited.append([node.val])
                return [node.val]
            
            s = [node.val]
            
            if(node.left != None) :
                s = find(node.left) + ["-"] + s
            
            if(node.right != None) :
                s += ["--"] + find(node.right) 
            
            if(s in visited) :
                if(s not in dupV) :
                    dupV.append(s)
                    dup.add(node)
            else :
                visited.append(s)
                
            return s
        
        
        find(root)
        return list(dup)
                
                
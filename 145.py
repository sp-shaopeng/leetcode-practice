# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
#         ans = []
#         def find(node) :
            
#             if(node.left != None) :
#                 find(node.left)
                
#             if(node.right != None) :
#                 find(node.right)
                
#             ans.append(node.val)
                
                
#         if(root == None) :
#             return ans
        
#         find(root)
#         return ans
        //iterative
        ans = []
        stack = []
        n = root
        while(len(stack) != 0 or n != None ) :
            if(n != None) :
                stack.append(n)
                ans.insert(0,n.val)
                n = n.right
            else :
                n = stack.pop().left
        return ans
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        
        if(root.val < val) :
            a = TreeNode()
            a.val = val
            a.left = root
            return a
        
   
        def insert(node):
            print(node.val)
            if(node.val > val and node.right == None):
                print("12")
                T = TreeNode()
                T.val = val
                node.right = T
                return ;
            elif(node.val > val and node.right.val < val):
                T = TreeNode()
                T.val = val
                T.left = node.right
                node.right = T
                return ;
            else:
                insert(node.right)

            
        insert(root)
        return root
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        mapping = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
              'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']
        
        ls = []
        
        def find(node, v) :
            v = mapping[node.val] + v
            if(node.left == None and node.right == None) :
                ls.append(v)
            
            if(node.left) :
                find(node.left, v)
            if(node.right) :
                find(node.right, v)
        if(root):
            find(root, '')
            ls.sort()
            return ls[0]
        else :
            return ''
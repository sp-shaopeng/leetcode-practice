# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ans = [0]
        counter = [0]
        def find(node):
            if(node.left != None):
                a = find(node.left)
            counter[0] += 1
            v = node.val
            if(counter[0] == k):
                ans[0] = v
                return;
            if(node.right != None):
                find(node.right)
            return;
        find(root)
        return ans[0]
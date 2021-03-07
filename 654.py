# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def find(x,y):
            m = -1
            p = -1
            
            for i in range(x,y + 1):
                if(nums[i] > m):
                    m = nums[i]
                    p = i
            return m,p
        
        def create(start, end):
            m,p = find(start,end)
            if(p >= 0):
                a = TreeNode()
                a.val = m
                if(p - 1 >= start) :
                    a.left = create(start, p - 1)

                if(p + 1 <= end) :
                    a.right = create(p + 1, end)

                return a

        return create(0,len(nums) - 1)
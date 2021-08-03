# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """         

        def compose(tree) :
            if(tree == None) :
                return []
            res = []
            res += compose(tree.left)
            res.append(tree.val)
            res += compose(tree.right)
            return res
        
        ls1 = compose(root1)
        ls2 = compose(root2)
        
        pt1 = 0
        pt2 = 0
        
        res = []
        while(pt1 < len(ls1) and pt2 < len(ls2)) :
            if(ls1[pt1] < ls2[pt2]) :
                res.append(ls1[pt1])
                pt1 += 1
            else :
                res.append(ls2[pt2])
                pt2 += 1
        
        while(pt1 < len(ls1)) :
            res.append(ls1[pt1])
            pt1 += 1
        
        while(pt2 < len(ls2)) :
            res.append(ls2[pt2])
            pt2 += 1
        
        return res
        
        
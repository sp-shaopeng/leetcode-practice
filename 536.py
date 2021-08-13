# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        
        
        def recur(string) :
            string = string.strip()
            l = len(string)
            if(l == 0) :
                return None
            p = string.find("(")
       
            if(p == -1) :
                return TreeNode(int(string))
            node = TreeNode(int(string[:p]))

            c = 1
            e = l
            for i in range(p + 1, l) :
                if(string[i] == "(") :
                    c += 1
                if(string[i] == ")") :
                    c -= 1
                if(c == 0) :
                    e = i
                    break
            if(e == l - 1) :
                node.left = recur(string[p+1 : e])
            else :
                node.left = recur(string[p+1 : e])
                node.right = recur(string[e+2: -1])
            
            return node
        
        return recur(s)
        
            
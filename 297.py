# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if(not root) :
            return "X"
        else :
            return ",".join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
        
        
#         Q = [root]
#         res = []
#         while(Q) :
#             newQ = []
#             noChange = True
#             while(Q) :
#                 v = Q.pop(0)
#                 if(v == None) :
#                     res.append(' ')
#                     newQ.append(None)
#                     newQ.append(None)
#                 else :
#                     res.append(str(v.val))
                            
#                     if(v.left == None) :
#                         newQ.append(None)
#                     else :
#                         noChange = False
#                         newQ.append(v.left)  
                    
#                     if(v.right == None) :
#                         newQ.append(None)
#                     else :
#                         noChange = False
#                         newQ.append(v.right)

                        
#             if(noChange) :
#                 break
#             Q = newQ
#         return ','.join(res)
                
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.data = data
        
        if(data[0] == "X") :
            return None
        else :
            t = TreeNode(int(self.data[: self.data.find(",")]))
            t.left = self.deserialize(self.data[self.data.find(",") + 1 :])
            t.right = self.deserialize(self.data[self.data.find(",") + 1 :])
            return t
            
        
        
#         arr = data.split(",")
        
#         l = len(arr)
        
#         if(l == 0 or arr[0] == " ") :
#             return None
        
#         t = TreeNode(int(arr[0]))
        
#         Q = [t]
        
#         half = (l + 1) / 2 - 1
        
#         i = 0
        
        
#         while(i < half) :
#             v = Q.pop(0)
#             if(v == None) :
#                 i += 1
#                 Q.append(None)
#                 Q.append(None)
#                 continue
                
#             if(arr[2 * i + 1] == ' ') :
#                 v.left = None
#                 Q.append(None)
#             else :
#                 l = TreeNode(int(arr[2 * i + 1]))
#                 v.left = l
#                 Q.append(l)
#             if(arr[2 * i + 2] == ' ') :
#                 v.right = None
#                 Q.append(None)
#             else :
#                 r = TreeNode(int(arr[2 * i + 2]))
#                 v.right = r
#                 Q.append(r)
#             i += 1
#         return t
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
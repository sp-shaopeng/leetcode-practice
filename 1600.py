class ThroneInheritance(object):
    
    
    #[parent, [children], death]
    
    root = ''
    ls = {}
    
    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.ls[kingName] = [None, [],  False]
        self.root = kingName
        

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        self.ls[parentName][1].append(childName)
        self.ls[childName] = [parentName, [], False]
        

    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        self.ls[name][2] = True
        

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        res = []
        
        
        def dfs(node) :
            p, c, d = self.ls[node]
            if(not d) :
                res.append(node)
            for i in c :
                dfs(i)
        
        dfs(self.root)
        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
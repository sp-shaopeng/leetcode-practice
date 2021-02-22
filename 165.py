class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = version1.split(".")
        ver2 = version2.split(".")  
        
        l1 = len(ver1)
        l2 = len(ver2)
        
        l = min(l1, l2)
        
        for i in range(l):
            if(int(ver1[i]) < int(ver2[i]) ) :
                return -1;
            elif(int(ver1[i]) > int(ver2[i]) ) :
                return 1;
            
        if(l1 < l2):
            for j in range(l1,l2):
                if(int(ver2[j])!= 0):
                    return -1
        elif(l1 > l2) :
            for j in range(l2,l1):
                if(int(ver1[j])!= 0):
                    return 1
        return 0
            
        
        
        
        
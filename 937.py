class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        letter = []
        dig = []
        
        for i in logs :
            checker = True
            j = i.split(" ")
            if(j[1].isdigit()) :
                dig.append(i)
            else: 
                letter.append(i)
                
        letter = sorted(letter, key = lambda x : x.split(" ")[0])
        letter = sorted(letter, key = lambda x : x.split(" ")[1:])
        
        return letter + dig
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = list(secret)
        b = list(guess)
        
        da = {}
        db = {}
        countA = 0
        
        for i in range(len(a)) :
            if(a[i] == b[i]) :
                countA += 1
            else:
                if a[i] in da :
                    da[a[i]] = da[a[i]] + 1
                else :
                    da[a[i]] = 1
                if b[i] in db :
                    db[b[i]] = db[b[i]] + 1
                else :
                    db[b[i]] = 1
        
        countB = 0
        
        for key in da :
            if key in db:
                if (da[key] <= db[key]) :
                    countB += da[key]
                else:
                    countB += db[key]
        
        res = ""

        res += str(countA) + "A"

        res += str(countB) + "B"
        
        return res
        
        
        
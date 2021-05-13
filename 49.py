class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        dic = {}
        
        for j in range(len(strs)) :
            s = list(strs[j])
            key = {}
            for i in range(len(s)) :
                if(s[i] in key) :
                    key[s[i]] += 1
                else:
                    key[s[i]] = 1
            key = frozenset(key.items())
            if(key in dic) :
                ans[dic[key]].append(strs[j])
            else:
                dic[key] = len(ans)
                ans.append([strs[j]])
                
        return ans            
            
            
            
# class Solution {
#     public int lengthOfLongestSubstring(String s) {
#         HashSet<String> val = new HashSet<>();
#         int l = s.length();
#         String ans ="";
#         String temp = "";
#         for(int i = 0; i < l; i++ ) {
#             String t = s.substring(i, i+1);
#             if(!val.contains(t)) {
#                 val.add(t);
#                 temp += t;
#             } else {
#                 if(temp.length() > ans.length()) {
#                     ans = temp;
#                 }
#                 temp = temp.substring(temp.lastIndexOf(t) + 1);
#                 temp += t;
#                 val.clear();
#                 int ll = temp.length();
#                 for(int k = 0; k < ll; k++) {
#                     val.add(temp.substring(k, k+1));
#                 }
#             }
#         }
        
#         if(temp.length() > ans.length()) {
#                 ans = temp;
                
#             }
        
#         return ans.length();
        
#     }
# }

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if(not n) :
            return 0
        
        head = 0
        tail = 1
        maxCount = 1
        count = 1
        tracker = {}
        tracker[s[0]] = 0
    
        while(head < n and tail < n) :
            l = s[tail]
            if(l in tracker) :
                pos = tracker[l]
                for i in range(head, pos + 1) :
                    tracker.pop(s[i])
                head = pos + 1
                tracker[l] = tail
                count = tail - pos
            else:
                count += 1
                tracker[l] = tail
                maxCount = max(count, maxCount)            
            tail += 1
        
        return maxCount
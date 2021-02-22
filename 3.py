class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<String> val = new HashSet<>();
        int l = s.length();
        String ans ="";
        String temp = "";
        for(int i = 0; i < l; i++ ) {
            String t = s.substring(i, i+1);
            if(!val.contains(t)) {
                val.add(t);
                temp += t;
            } else {
                if(temp.length() > ans.length()) {
                    ans = temp;
                }
                temp = temp.substring(temp.lastIndexOf(t) + 1);
                temp += t;
                val.clear();
                int ll = temp.length();
                for(int k = 0; k < ll; k++) {
                    val.add(temp.substring(k, k+1));
                }
            }
        }
        
        if(temp.length() > ans.length()) {
                ans = temp;
                
            }
        
        return ans.length();
        
    }
}
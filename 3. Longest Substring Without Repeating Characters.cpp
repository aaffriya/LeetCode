
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        unordered_map<char, bool> dct;
        
        int i = 0, j = 0, r = 0, l = 0 ;
        
        while (true){
            
            dct.insert({s[j], true});
            
            if ( dct[s[j]] ) {
                dct[s[j]] = false;
                if (j == s.size()) {
                    l = j - i;
                    return max(l, r);
                }
                j++;
            } else {
                dct[s[i]] = true;
                l = j - i;
                i++;
                if (l > r) {r = l;}
            }
        }
    }
};

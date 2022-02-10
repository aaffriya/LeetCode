// https://leetcode.com/problems/largest-number/
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        
        unsigned int sum = 0; string res; vector<string> str;
        
        for (auto &i : nums) {
            str.push_back(to_string(i));
            
            if (!sum) sum += i;
        }
        if (!sum) return "0";
        
        sort(str.begin(), str.end(), [](string x, string y){return x+y > y+x;});
        
        for (auto &s : str) res += s;
        
        return res;
    }
};

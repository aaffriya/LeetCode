// https://leetcode.com/contest/weekly-contest-278/problems/keep-multiplying-found-values-by-two/
class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        
        set<int> s;
        
        for (const auto &i : nums){
            s.insert(i);
        }
        while (true){
            auto it = s.find(original);
            if (it != s.end()){
                original *= 2;
            } else {
                return original;
            }
        }
    }
};

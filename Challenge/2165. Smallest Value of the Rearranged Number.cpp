// https://leetcode.com/problems/smallest-value-of-the-rearranged-number/
class Solution {
public:
    long long smallestNumber(long long num) {
        
        bool sign = (num > 0) ? false: true;
        string num_str = to_string(num);
        short len = num_str.size();
        
        if (!sign){
            sort(num_str.begin(), num_str.end());
            for (short i = 0; i < num_str.size(); i++){
                if (num_str[i] != '0'){
                    num_str.insert(0, 1, num_str[i]);
                    num_str.erase(i+1, 1);
                    break;
                }
            }
        } else {
            sort(num_str.begin(), num_str.end(), greater());
            num_str.pop_back();
        }
        
        long long int res = 0;
        for (char &i : num_str){
            res *= 10; res += i - 48;
        }
        if (sign) res *= -1;
        return res;
    }
};

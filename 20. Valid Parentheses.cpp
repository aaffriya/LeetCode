// https://leetcode.com/problems/valid-parentheses/submissions/
  class Solution {
public:
    bool isValid(string s) {
        
        stack<char> st;
        
        unordered_map<char, char> dct;
        dct['('] = ')';
        dct['['] = ']';
        dct['{'] = '}';
        
        for (auto &item : s){
            auto it = dct.find(item);
            if (it != dct.end()) {
                st.push(item);
            } else {
                if (st.size()) {
                    auto it = dct.find(st.top());
                    if (item == (*it).second) {
                        cout<<(*it).second;
                        st.pop();
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        return st.empty();
    }
};

# https://leetcode.com/problems/watering-plants-ii/
class Solution {
public:
    int minimumRefill(vector<int>& plants, int capacityA, int capacityB) {
        
        int Alice = capacityA, Bob = capacityB;
        
        int res = 0, i = 0, j = plants.size()-1;
        
        while (i < j){
            if (Alice >= plants[i]) {
                Alice -= plants[i];
            } else {
                res++;
                Alice = capacityA - plants[i];
            }
            if (Bob >= plants[j]) {
                Bob -= plants[j];
            } else {
                res++;
                Bob = capacityB - plants[j];
            }
            i++;
            j--;
            }
        if (i == j and Alice < plants[i] and Bob < plants[i]) {
            return res + 1;
        }
        return res;
    }
};

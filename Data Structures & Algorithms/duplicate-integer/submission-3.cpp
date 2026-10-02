#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> mySet;
        for (int i = 0; i < nums.size(); i++) {
            mySet.insert(nums[i]);
        }
        if (mySet.size() == nums.size())
            return false;
        return true;
    }
};
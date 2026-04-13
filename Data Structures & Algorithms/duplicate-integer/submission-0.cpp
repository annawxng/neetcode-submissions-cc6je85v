class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> mySet;
        for (int i = 0; i < nums.size(); i++) {
            auto it = mySet.find(nums[i]);
            if (it != mySet.end()){
                return true;
            }
            mySet.insert(nums[i]);
        }
        return false;
    }
};
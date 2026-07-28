class Solution {
public:
    int findDuplicate(vector<int>& nums) {
      set<int> numSet;

      for (int num : nums) {
        if (numSet.contains(num)) {
            return num;
        }
        numSet.insert(num);
      }
    }
};

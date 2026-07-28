class Solution {
public:
    vector<vector<int>> combinations;

    void backtrack(vector<int> current_combination, vector<int> remaining_set) {
        // base case
        if(remaining_set.size() == 0) {
            combinations.push_back(current_combination);
            return;
        }
        else {
            combinations.push_back(current_combination);
            while (remaining_set.size() > 0) {
                int additional_num = remaining_set.back();
                // recursive calls
                current_combination.push_back(additional_num);
                remaining_set.pop_back();
                backtrack(current_combination, remaining_set);
                current_combination.pop_back();
            }
        }
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        backtrack({}, nums);
        return combinations;
    }
};
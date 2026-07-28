class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // Kadane's Greedy Approach
        // - maintain current and max sums
        // - if current sum becomes negative, reset it to zero
        // - if max sum is greater than current sum, update

        int currentSum = 0;
        int maxSum = -1*pow(10, 4);
        for (auto num : nums) {
            currentSum += num;
            if (currentSum > maxSum) {
                maxSum = currentSum;
            }
            if (currentSum < 0) {
                currentSum = 0;
            }
        }

        return maxSum;
    }
};
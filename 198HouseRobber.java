// Uses dynamic programming, the key is to figure out the dynamic
// function values[i] = Math.max(values[i - 2] + nums[i - 2], values[i - 1])
// If values[i - 2] + nums[i - 2] is greater, it means I should rob this
// house. Otherwise should skip this house because robbing the one house
// before yields more money
// values[i - 2] stores the current max value robbed when the robber is at
// house i
class Solution {
    public int rob(int[] nums) {
        int[] values = new int[nums.length + 2];
        values[0] = 0;
        values[1] = 0;
        for (int i = 2; i < nums.length + 2; i++) {
            values[i] = Math.max(values[i - 2] + nums[i - 2], values[i - 1]);
        }
        return values[nums.length + 1];
    }
}
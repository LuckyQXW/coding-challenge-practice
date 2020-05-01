// Brute force, O(n^2)
// Assume nums is non-empty since it has solution
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            result[0] = i;
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    result[1] = j;
                    return result;
                }
            }
        }
        return result;
    }
}

// Double for loop is inefficient, want to save the work of revisiting
// the same values
// Overall is O(n) runtime with O(n) space
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        // Key: value of the num, Value: index of the num. Use a map to keep track of values
        // we have already seen and their indicies
        Map<Integer, Integer> m = new HashMap<>();  // HashMap for fast access O(1)
        result[0] = 0;
        m.put(nums[0], 0);
        // The first iteration, compare (0, [1-n]) and populate the map
        for (int j = 1; j < nums.length; j++) {
            if (nums[0] + nums[j] == target) {
                result[1] = j;
                return result;
            } else {
                m.put(nums[j], j);
            }
        }
        // The second iteration, check if the difference between target and curr exist in the
        // map and store the index right away
        for (int k = 1; k < nums.length; k++) {
            result[0] = k;
            // Need to make sure that the two indicies are not the same
            if (m.containsKey(target - nums[k]) && m.get(target - nums[k]) != k) {
                result[1] = m.get(target - nums[k]);
                return result;
            }
        }
        return result;
    }
}

// Optimized one pass hash table
// Realization that when we get to later values we can start utilizing the previous elements stored
// in the map
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Key: value of the num, Value: index of the num
        Map<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (m.containsKey(complement)) {
                return new int[] {m.get(complement), i};  // maintain ordering of smaller index comes first
            }
            m.put(nums[i], i);
        }
        throw new IllegalArgumentException("No solution");
    }
}
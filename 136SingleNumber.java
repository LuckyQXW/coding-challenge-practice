// Use a map as extra memory to store the count, O(n) solution
class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!counts.containsKey(nums[i])) {
                counts.put(nums[i], 0);
            }
            counts.put(nums[i], counts.get(nums[i]) + 1);
        }
        for (int key : counts.keySet()) {
            if (counts.get(key) == 1) {
                return key;
            }
        }
        throw new IllegalArgumentException("Can't find the single number");
    }
}

// Solution without using extra space, O(nlogn) for using the built-in sort
class Solution {
    public int singleNumber(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        Arrays.sort(nums);
        for (int i = 1; i < nums.length - 1; i++) {
            if (nums[i] != nums[i+1] && nums[i] != nums[i-1]) {
                return nums[i];
            }
        }
        if (nums[0] != nums[1]) {
            return nums[0];
        } else {
            return nums[nums.length - 1];
        }
    }
}

// Super neat solution with XOR, since the repeated elements
// will get canceled out. O(n) runtime.
class Solution {
    public int singleNumber(int[] nums) {
        int val =  0;
        for (int i = 0; i < nums.length; i++) {
            val = val ^ nums[i];
        }
        return val;
    }
}

// Test cases:
// [1]
// [1,2,2,4,4] - at the beginning
// [2,4,1,4,2] - at the middle
// [4,2,2,4,1] - at the end
// [5,3,3,2,1,9,2,1,5] - longer example
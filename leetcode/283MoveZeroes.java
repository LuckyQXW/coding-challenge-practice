// Two pointer approach, fast pointer finds the nonzero values
// and overwrites the value slow is pointing to, and in the
// end fill in the zeroes from the back
// O(n) solution, O(1) space
class Solution {
    public void moveZeroes(int[] nums) {
        int zeroCounts = 0;
        int slow = 0;
        int fast = 0;
        while (fast != nums.length) {
            if (nums[fast] != 0) {
                nums[slow] = nums[fast];
                slow++;
                fast++;
            } else {
                fast++;
                zeroCounts++;
            }
        }
        for (int j = nums.length - 1; j >= nums.length - zeroCounts; j--) {
            nums[j] = 0;
        }
    }
}

// Optimal less than O(n) solution, key observation is that if fast
// pointer is nonzero, we can swap it with slow which points to the
// next element that could be 0.
// The invariant is everything before slow is non-zero, and everything
// between slow and fast are zeros, so we can swap as we wish without
// messing up the order of non-zero elements.
class Solution {
    public void moveZeroes(int[] nums) {
        int slow = 0;
        int fast = 0;
        while (fast < nums.length) {
            if (nums[fast] != 0) {
                int temp = nums[slow];
                nums[slow] = nums[fast];
                nums[fast] = temp;
                slow++;
                fast++;
            } else {
                fast++;
            }
        }
    }
}

// Test cases
// [0]
// [1]
// [1,0]
// [0,1]
// [0,0,1]
// [1,2,0,3,0,4,0]
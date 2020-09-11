class Solution {
    public static void main(String[] args) {
      int[] arr = {-1, 0, 0, 0, 0, 0, 3, 3};
      int len = removeDuplicates(arr);
      System.out.println(len);
      
      // Test cases
      // []
      // [1]
      // [1,2,3,4] - all unique
      // [1,1,1] - all duplicates
      // [1,1,2] - duplicate at front
      // [1,1,1,1,1,1,2] - more duplicates at front
      // [1,1,2,2,3,3,3,3,4,5] - multiple duplicates
      // [-2,-2,-1,0] - negative input
    }
    
    // Kind of brute force
    // Iterate through each element in array
    // If curr equals curr + 1
    //   Find the next unique item, copy over the rest of the list
    //   Increment length
    public static int removeDuplicates(int[] nums) {
        int length = 0;
        // Sorted, check nums[i] with nums[i + 1], if equal, swap
        for (int i = 0; i < nums.length - 1; i++) {
            length++;
            // Check if reach the end of the unique sorted list
            if (nums[i] > nums[i + 1]) {
                return length;
            }
            if (nums[i] == nums[i + 1]) {
                int next = i + 1;
                // Find the next unique item
                while (next < nums.length && nums[next] == nums[i]) {
                    next++;
                }
                // Next will either at the nums.length
                // or the end of the unique sorted list
                // or the next unique element
                if (next == nums.length || nums[next] < nums[i])  {
                    return length;
                } else {
                    // copy the rest of the list over starting from next
                    int j = i + 1;
                    while (next < nums.length) {
                        nums[j] = nums[next];
                        j++;
                        next++;
                    }
                }
            }
        }
        // Add 1 because it only iterates up to length - 1
        return length + 1;
    }
}

// Two pointers approach, keep one fast and one slow
class Solution {
    public int removeDuplicates(int[] nums) {
        int length = 0;
        // Handle empty and 1 element case
        if (nums.length <= 1) {
            return nums.length;
        }
        // Create two pointers
        int slow = 0;  // End of unique sorted
        int fast = 1;  // Search for next unique
        while (fast < nums.length) {
            if (nums[slow] == nums[fast]) {
                fast++;
            } else {
                slow++;
                nums[slow] = nums[fast];
                fast++;
            }
        }
        return slow + 1;
    }
}
// O(n) solution, use a map to store count, need extra space
class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!m.containsKey(nums[i])) {
                m.put(nums[i], 0);
            }
            m.put(nums[i], m.get(nums[i]) + 1);
            if (m.get(nums[i]) > nums.length / 2) {
                return nums[i];
            }
        }
        throw new IllegalArgumentException("No majority element in array");
    }
}

// O(nlogn) solution, sort first then calculate the length of 
// consecutive number subarrays, O(1) space
class Solution {
    public int majorityElement(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        Arrays.sort(nums);
        int length = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1])  {
                length++;
            } else {
                length++;
                if (length > nums.length / 2) {
                    return nums[i];
                } else {
                    length = 0;
                }
            }
        }
        // Need to handle the edge case where the last value is the 
        // majority
        length++;
        if (length > nums.length / 2) {
            return nums[nums.length - 1];
        }
        throw new IllegalArgumentException("No majority element in array");
    }
}

// Cleaner solution with sorting, since majority will show up
// Math.floor(length / 2) times, the element at nums[nums.length / 2]
// after sort will be the majority :o
class Solution {
    public int majorityElement(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }
}

// Boyer-Moore Voting Algorithm, basically increment the vote if
// the current element is the majority, decrement it otherwise, 
// and switch majority if the count is 0 (disgarded the prefix where
// there are the same number of majority and minority). Works
// because there majority is guaranteed to have Math.floor(nums.length / 2)
// instances
// O(n) runtime and O(1) space
class Solution {
    public int majorityElement(int[] nums) {
        int majority = nums[0];
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            // Order of if check matters
            if (count == 0) {
                majority = nums[i];
            }
            if (nums[i] == majority) {
                count++;
            }  else {
                count--;
            }
        }
        return majority;
    }
}
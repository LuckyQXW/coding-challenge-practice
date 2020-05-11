// Use a set to keep track of values seen, O(n) runtime
// and O(n) space
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (s.contains(nums[i])) {
                return true;
            }
            s.add(nums[i]);
        }
        return false;
    }
}

// In place solution, sort nums first, O(nlogn) runtime
// and O(1) space
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                return true;
            }
        }
        return false;
    }
}

// Second version of containsDuplicate, returns true if differences
// between indices of two duplicates less than or equal to k. Use
// a hash map to keep track of last seen indices as we go.
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (m.containsKey(nums[i]) && i - m.get(nums[i]) <= k) {
                return true;
            }
            m.put(nums[i], i);
        }
        return false;
    }
}
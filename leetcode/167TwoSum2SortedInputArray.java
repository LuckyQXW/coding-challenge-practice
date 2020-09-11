// Anything from Two Sum still works
// O(n) solution with two pointers, one starting from the left
// and other starting from right. If the sum is greater than
// current target, move right to the left for smaller sum, otherwise
// move left to the right for bigger sum, until we find the target.
// O(1) space
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        while (numbers[right] + numbers[left] != target) {
            if (numbers[right] + numbers[left] > target) {
                right--;
            } else {
                left++;
            }
        }
        return new int[] {left + 1, right + 1};
    }
}
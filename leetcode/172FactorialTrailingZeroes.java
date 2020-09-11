// The key observation here is that to determine how many
// trailing zeroes there are in the final result, we only
// need to count how many factors of 5's from 6 to n. 
// Total number of 5's = n/5 + n/5^2 + n/5^3...
// O(logn) runtime since it is dividing by 5 each iteration
class Solution {
    public int trailingZeroes(int n) {
        int count = 0;
        while (n >= 5) {
            count += n / 5;
            n = n / 5;
        }
        return count;
    }
}

// Test cases:
// 0
// 3
// 5 - 0
// 6 - 1
// 10 - 2
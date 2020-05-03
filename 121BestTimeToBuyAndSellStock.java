// Brute force, try every combination of sell - buy
class Solution {
    public int maxProfit(int[] prices) {
        int maxProf = 0;
        for (int i = 0; i < prices.length; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                maxProf = Math.max(maxProf, prices[j] - prices[i]);
            }
        }
        return maxProf;
    }
}

// O(n) solution, keep the current min and update the max prof as
// we find peaks in the price
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) {
            return 0;
        }
        int maxProf = 0;
        int min = prices[0];
        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i+1] > prices[i]) {
                maxProf = Math.max(maxProf, prices[i+1] - min);
            } else {
                min = Math.min(min, prices[i+1]);
            }
        }
        return maxProf;
    }
}

// Test cases
// []
// [1]
// [7,1,5,3,6,4] - 5, regular, not 7-1 but 6-1
// [4,3,2,1] - 0, only decreasing price, not buy in the first place
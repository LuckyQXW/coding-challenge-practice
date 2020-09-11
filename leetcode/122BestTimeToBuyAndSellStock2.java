// Examine the trend graph, only sell with current observed min/max 
// when see descending trend
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) {
            return 0;
        }
        int total = 0;
        int currMax = prices[0];
        int currMin = prices[0];
        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i + 1] > prices[i]) { // ascending trend
                currMax = prices[i + 1];
                currMin = Math.min(prices[i], currMin);
                if (i == prices.length - 2) {  // last ascending trend
                    total += currMax - currMin;
                }
            } else {  // descending trend, sell current share
                total += currMax - currMin;
                currMin = currMax;
            }
        }
        return total;
    }
}

// Easier solution, just sell whenever the next day
// has higher prices... No need to worry if there are two consecutive
// days of increasing trend or not, because the profits always add up
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) {
            return 0;
        }
        int total = 0;
        for (int i = 0; i < prices.length - 1; i++)  {
            if (prices[i + 1] >= prices[i]) {
                total += prices[i + 1] - prices[i];
            }
        }
        return total;
    }
}

// Test cases:
// []
// [1]
// [7,6,4,1]- 0, never buy or sell
// [2,7,1,5]- 9, add up two sells
// [2,3,5,1]- 3, two consecutive days of ascending trend
// [1,0,3]- 3, sell on last day
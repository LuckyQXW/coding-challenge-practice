// Brute force solution, just keep dividing 2, 3, 5 while they
// are still a factor of the current number
class Solution {
    public boolean isUgly(int num) {
        // need to explicitly handle 0 case, else stuck in
        // infinite loops
        if (num <= 0) {
            return false;
        }
        while (num % 5 == 0) {
            num /= 5;
        }
        while (num % 2 == 0) {
            num /= 2;
        }
        while (num % 3 == 0) {
            num /= 3;
        }
        return num == 1;
    }
}

// Recursive solution
class Solution {
    public boolean isUgly(int num) {
        if (num <= 0) {
            return false;
        } else if (num == 1) {
            return true;
        } else {
            if (num % 2 == 0) {
                return isUgly(num / 2);
            } else if (num % 3 == 0) {
                return isUgly(num / 3);
            } else if (num % 5 == 0) {
                return isUgly(num / 5);
            } else {
                // Need to handle this case explicitly as well
                return false;
            }
        }
    }
}

// Test cases:
// -1 - negative case
// 0 - should be false
// 1
// 6
// 14 - has other factors
// 60 - has multiple 2, 3, 5 factors
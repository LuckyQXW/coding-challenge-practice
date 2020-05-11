// Bit maniputation, power of 4s have even number of trailing
// zeros with a 1 in front
class Solution {
    public boolean isPowerOfFour(int n) {
        while (n > 1) {
            if ((n & 1) != 0 || ((n >> 1) & 1) != 0) {
                return false;
            }
            n = n >>> 1;
            n = n >>> 1;
        }
        return n == 1;
    }
}

// Observation that if n is a power of 4, then it must be
// a power of 2, which can be determined by n & (n - 1) == 0
// There should also be a 1 in odd positions, thus the
// 0x55555555 mask
class Solution {
    public boolean isPowerOfFour(int n) {
        if (n == 1) return true;
        if (n < 4) return false;
        if ((n & (n - 1)) != 0) return false;
        return (n & 0x55555555) == n;
    }
}

// Even shorter solution, key observation is that num must be a power
// of 2, and num - 1 must be divisible by 3
class Solution {
    public boolean isPowerOfFour(int num) {
       return num > 0 && (num & (num - 1)) == 0 && (num - 1) % 3 == 0;
    }
}

// Test cases:
// -4
// 0
// 1
// 256
// 255
// 20
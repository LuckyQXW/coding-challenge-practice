// Brute force, starting from beginning of nums1, if nums2
// should be inserted before curr nums1, shift everything
// left in nums1 later, insert nums2, then repeat.
// potentially O(m + n^2) solution
class Solution {
    // Test cases
    // [1,2,3,0,0,0],3,[2,5,6],3 - [1,2,2,3,5,6]
    // [2,2,0,0],2,[0,1],2 - [0,1,2,2] start insertion from first
    // [1,2],2,[],0 - empty nums2
    // [0,0],0,[1,2],2 - empty nums1
    // [1,2,3,0,0],3,[4,5],2 - run off nums1 and append the rest of nums2
    // [-2,-1,0,0],2,[-5,-3],2 - [-5,-3,-2,-1] negative cases
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = 0;  // Pointer to nums1
        int j = 0;  // Pointer to nums2
        
        while (i < m && j < n) {
            // Need extra check here in case run out of bounds
            while (i < m && j < n && nums1[i] > nums2[j]) {
                for (int k = m - 1; k >= i; k--) {
                    nums1[k+1] = nums1[k];
                }
                nums1[i] = nums2[j];
                i++;
                j++;
                m++;
            }
            i++;
        }
        if (i == m && m < nums1.length) {
            for (int k = 0; k < nums2.length - j; k++) {
                nums1[m + k] = nums2[j + k];
            }
        }
    }
}

// O(m + n) solution that keeps track of two pointers starting from
// the end of each list, and then pick the larger one to overwrite
// nums1 starting from last spot
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (m == 0) {
            for (int i = 0; i < n; i++) {
                nums1[i] = nums2[i];
            }
        } else {
            int i = m - 1;  // Pointer to nums1
            int j = n - 1;  // Pointer to nums2
            int curr = nums1.length - 1;
            while(i >= 0 && j >= 0) {
                if (nums1[i] > nums2[j]) {
                    nums1[curr] = nums1[i];
                    i--;
                } else {
                    nums1[curr] = nums2[j];
                    j--;
                }
                curr--;
            }
            if (j >= 0) {
                for (int k = 0; k <= j; k++) {
                    nums1[k] = nums2[k];
                }
            }
        }
    }
}

// Kinda trivial solution, adding all nums2 at the end of nums1
// then sort. Probably use O((m + n)log(m + n)) runtime
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int i = 0; i < nums2.length; i++) {
            nums1[m + i] = nums2[i];
        }
        Arrays.sort(nums1);
    }
}

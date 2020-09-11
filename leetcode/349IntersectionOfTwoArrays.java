// Kinda brute force, use Sets to find duplicates between the two
// O(n + m) space + O(n + m) runtime
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> s = new HashSet<>();
        Set<Integer> intersection = new HashSet<>();
        for (int i = 0; i < nums1.length; i++) {
            s.add(nums1[i]);
        }
        for (int j = 0; j < nums2.length; j++) {
            if (s.contains(nums2[j])) {
                intersection.add(nums2[j]);
            }
        }
        int[] result = new int[intersection.size()];
        int k = 0;
        for (int num : intersection) {
            result[k] = num;
            k++;
        }
        return result;
    }
}

// Inplace solution, have to use an extra loop since Java array is
// fixed size. Sort two arrays first, so O(nlogn + mlogm + m + n).
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        List<Integer> l = new ArrayList<>();
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int i = 0;  // Pointer to nums1
        int j = 0;  // Pointer to nums2
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] == nums2[j]) {
                l.add(nums1[i]);
                while (i < nums1.length && nums1[i] == l.get(l.size() - 1)) {
                    i++;
                }
                while (j < nums2.length && nums2[j] == l.get(l.size() - 1)) {
                    j++;
                }
                continue;
            } else if (nums1[i] < nums2[j]) {
                i++;
            } else {
                j++;
            }
        }
        int[] result = new int[l.size()];
        for (int k = 0; k < result.length; k++) {
            result[k] = l.get(k);
        }
        return result;
    }
}

// Test cases:
// [], [] - empty arrays
// [1], [1] - arrays with one element
// [1,2,3], [2,3] - multiple element in intersection
// [1,2,3], [4,5,6] - no intersection
// [-1,-5], [-1,4,2] - negative vals
// [0,-1,0], [1,2,4,-1,0] - duplicates
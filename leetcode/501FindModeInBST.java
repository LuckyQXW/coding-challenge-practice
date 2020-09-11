/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// Brute force, use a hashtable to count the occurrences and find
// the mode later. O(n) solution and O(n) space, need extra because
// Java has fixed size arrays
class Solution {
    public int[] findMode(TreeNode root) {
        Map<Integer, Integer> counts = new HashMap<>();
        int max = searchMode(root, counts);
        List<Integer> l = new ArrayList<>();
        for (int key : counts.keySet()) {
            if (counts.get(key) == max) {
                l.add(key);
            }
        }
        int[] result = new int[l.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = l.get(i);
        }
        return result;
    }
    
    // Returns the frequency of the mode
    private int searchMode(TreeNode root, Map<Integer, Integer> counts) {
        if (root == null) {
            return 0;
        } else {
            if (!counts.containsKey(root.val)) {
                counts.put(root.val, 0);
            }
            counts.put(root.val, counts.get(root.val) + 1);
            int lmax = searchMode(root.left, counts);
            int rmax = searchMode(root.right, counts);
            return Math.max(Math.max(counts.get(root.val), lmax), 
                Math.max(counts.get(root.val), rmax));
        }
    }
}

// Utilizes the property of BST since only right subtree can
// have equal values
class Solution {
    TreeNode preNode = null;
    int max = 0;
    int count = 0;
    
    public int[] findMode(TreeNode root) {
        List<Integer> l = new ArrayList<>();
        searchMode(root, l);
        int[] result = new int[l.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = l.get(i);
        }
        return result;
    }
    
    private void searchMode(TreeNode root, List<Integer> l) {
        if (root != null) {
            searchMode(root.left, l);
            // Only need to compare with previous node
            if (preNode != null && preNode.val == root.val) {
                count++;
            } else {
                count = 1;
            }
            
            if (count == max) {
                l.add(root.val);
            } else if (count > max) {  // Found a new max, so reset the list
                l.clear();
                l.add(root.val);
                max = count;
            }
            // Replace preNode with root since we have done processing root
            preNode = root; 
            searchMode(root.right, l);
        }
    }
}
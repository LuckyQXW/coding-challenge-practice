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
// Nice and elegant recursive solution
class Solution {
    public int maxDepth(TreeNode root) {
        return getDepth(root);
    }
    
    private int getDepth(TreeNode root) {
        if (root == null) {
            return 0;
        } else {
            return 1 + Math.max(getDepth(root.left), getDepth(root.right));
        }
    }
}

// Iterative solution with BFS, keeping track of a distTo map
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Queue<TreeNode> toVisit = new LinkedList<>();
        Map<TreeNode, Integer> distTo = new HashMap<>();
        toVisit.add(root);
        distTo.put(root, 0);
        while (!toVisit.isEmpty()) {
            TreeNode curr = toVisit.remove();
            if (curr.left != null) {
                toVisit.add(curr.left);
                distTo.put(curr.left, distTo.get(curr) + 1);
            }
            if (curr.right != null) {
                toVisit.add(curr.right);
                distTo.put(curr.right, distTo.get(curr) + 1);
            }
        }
        
        int max = 0;
        for (TreeNode n : distTo.keySet()) {
            max = Math.max(max, distTo.get(n));
        }
        return max + 1;
    }
}


// Iterative solution with BFS without distTo map, use null to
// mark the end of each level
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Queue<TreeNode> toVisit = new LinkedList<>();
        toVisit.add(root);
        toVisit.add(null);
        int depth = 0;
        while (!toVisit.isEmpty()) {
            TreeNode curr = toVisit.remove();
            if (curr == null) {
                // The check below is necessary otherwise will stuck
                // in infinite loop at the end
                if (!toVisit.isEmpty()) {
                    toVisit.add(null);  // Mark the end of adding nodes in a level
                }
                depth++;
            } else {
                if (curr.left != null) {
                    toVisit.add(curr.left);
                }
                if (curr.right != null) {
                    toVisit.add(curr.right);
                }
            }
        }
        return depth;
    }
}
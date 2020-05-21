// Use choose/explore/unchoose pattern, recursive solution
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> acc = new ArrayList<>();
        getCombo(result, acc, 1, n, k);
        return result;
    }
    
    private void getCombo(List<List<Integer>> result, List<Integer> acc, int curr, int n, int k) {
        if (acc.size() == k) {
            result.add(new ArrayList<Integer>(acc));
        } else if (curr <= n) {
            // Choose & explore
            // Not include curr in the list
            getCombo(result, acc, curr + 1, n, k);
            
            // Include curr in the list
            acc.add(curr);
            getCombo(result, acc, curr + 1, n, k);
            
            // Unchoose
            acc.remove(acc.size() - 1);
        }
    }
}

// Use a loop inside recursion, speedup to only explore the options left
// instead of going through all possible results that might exceed k
// or won't reach k
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> acc = new ArrayList<>();
        getCombo(result, acc, 1, n, k);
        return result;
    }
    
    private void getCombo(List<List<Integer>> result, List<Integer> acc, int curr, int n, int k) {
        if (acc.size() == k) {
            result.add(new ArrayList<Integer>(acc));
        } else{
            // The loop bound here is key
            for (int i = curr; i <= n - (k - acc.size()) + 1; i++) {
                acc.add(i);
                getCombo(result, acc, i + 1, n, k);
                acc.remove(acc.size() - 1);
            }
        }
    }
}
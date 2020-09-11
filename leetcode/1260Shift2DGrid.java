// Brute force solution, just translate the problem, find the
// new starting point and fill it in from there
class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        List<List<Integer>> result = new ArrayList<>();
        // Initial position
        int i = 0;
        int j = 0;
        
        // Find the new [0][0], need to traverse backwards
        while (k > 0) {
            if (i > 0) {
                i--;
            } else {
                i = grid[0].length - 1;
                // Can't do j - 1 since Java returns negative
                // with mod
                j = (j + 1) % grid.length;
            }
            k--;
        }
        j = (grid.length - j) % grid.length;
        // grid[i][j] will be the new [0][0]
        for (int m = 0; m < grid.length; m++) {
            result.add(new ArrayList<Integer>());
            for (int n = 0; n < grid[0].length; n++) {
                result.get(m).add(grid[j][i]);
                // Loop through in the original direction
                if (i < grid[0].length - 1) {
                    i++;
                } else {
                    i = 0;
                    j = (j + 1) % grid.length;
                }
            }
        }
        return result;
    }
}

// Transform 2D grid to 1D, then use 3 reverses to do the shifting,
// finally change it back to 2D grid
// Overall O(n)
class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        List<Integer> oneDList = new ArrayList<>();
        // O(n): 2D to 1D
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                oneDList.add(grid[i][j]);
            }
        }
        int size = grid.length * grid[0].length;
        k = k % size;
        // Should be O(n) overall here
        reverse(oneDList, 0, size - k);
        reverse(oneDList, size - k, size);
        reverse(oneDList, 0, size);
        // O(n): 1D to 2D
        List<List<Integer>> result = new ArrayList<>();
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            result.add(new ArrayList<>());
            for (int j = 0; j < grid[0].length; j++) {
                result.get(i).add(oneDList.get(count));
                count++;
            }
        }
        return result;
    }
    
    private void reverse(List<Integer> l, int start, int end) {
        while (start < end) {
            int temp = l.get(start);
            l.set(start, l.get(end - 1));
            l.set(end - 1, temp);
            start++;
            end--;
        }
    }
}
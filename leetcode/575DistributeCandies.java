// Observe that we want the sister to get as many unique
// candies as possible, so use a set to keep track of
// unique values, and the max the sister can get is half
// of the total candies since the other half goes to her
// brother
class Solution {
    public int distributeCandies(int[] candies) {
        Set<Integer> s = new HashSet<>();
        for (int i = 0; i < candies.length; i++) {
            s.add(candies[i]);
        }
        if (s.size() > candies.length / 2) {
            return candies.length / 2;
        } else {
            return s.size();
        }
    }
}
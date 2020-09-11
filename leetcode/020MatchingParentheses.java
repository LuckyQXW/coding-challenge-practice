// Relatively brute force, make use of a Stack, O(n)
class Solution {
    public boolean isValid(String s) {
        Stack<Character> chars = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{') {
                chars.push(s.charAt(i));
            } else if (s.charAt(i) == ')') {
                if (chars.isEmpty() || chars.pop() != '(') {
                    return false;
                }
            } else if (s.charAt(i) == ']') {
                if (chars.isEmpty() || chars.pop() != '[') {
                    return false;
                }
            } else if (s.charAt(i) == '}') {
                if (chars.isEmpty() || chars.pop() != '{') {
                    return false;
                }
            }
        }
        return chars.isEmpty();
    }
}

// Use a map to make the code a bit more elegant, use a bit extra storage but compared
// to a length n input it is relatively O(1) space for the hash table, but O(n) for
// the stack and still O(n) runtime
class Solution {
    public boolean isValid(String s) {
        Stack<Character> chars = new Stack<>();
        Map<Character, Character> matches = new HashMap<>();
        matches.put('(', ')');
        matches.put('[', ']');
        matches.put('{', '}');
        for (int i = 0; i < s.length(); i++) {
            if (matches.containsKey(s.charAt(i))) {
                chars.push(s.charAt(i));
            } else if (chars.isEmpty() || s.charAt(i) != matches.get(chars.pop())) {  // need to be a bit more careful in the comparison
                return false;
            }
        }
        return chars.isEmpty();
    }
}
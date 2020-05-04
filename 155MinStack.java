// Idea is to store the difference with the last min
// instead of the real value. Have trouble passing the
// integer overflow tests due to Java integer type
// constraints. Works if implemented in Python.
class MinStack {

    private Stack<Integer> s;
    private int min;
    
    /** initialize your data structure here. */
    public MinStack() {
        s = new Stack<>();
        min = 0;
    }
    
    public void push(int x) {
        // Doesn't work with integer overflow...
        int val = x - min;
        s.push(val);
        if (s.size() == 1) {
            min = x;
        } else {
            min = Math.min(x, min);
        }
    }
    
    public void pop() {
        int val = s.pop();
        if (val < 0) {
            min -= val;
        }
    }
    
    public int top() {
        if (s.peek() < 0 || s.size() == 1) {
            return s.peek();
        }
        return s.peek() + min;
    }
    
    public int getMin() {
        return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
 
// Two stack solution, only push to min stack if the given value
// is smaller or equal than the top
// O(1) runtime and O(n) space
class MinStack {

    Stack<Integer> s;
    Stack<Integer> minS;
    /** initialize your data structure here. */
    public MinStack() {
        s = new Stack<>();
        minS = new Stack<>();
    }
    
    public void push(int x) {
        s.push(x);
        if (minS.isEmpty() || x <= minS.peek()) {
            minS.push(x);
        }
    }
    
    public void pop() {
        // For some reason only works if explicitly store the val
        int val = s.pop();
        if (val == minS.peek()) {
            minS.pop();
        }
    }
    
    public int top() {
        return s.peek();
    }
    
    public int getMin() {
        return minS.peek();
    }
}

// Uses a two stack approach, all push goes to sBack while
// all pop/peek from sFront. Add all element from sBack to
// sFront whenever sFront is empty.
class MyQueue {
    
    private Stack<Integer> sFront;
    private Stack<Integer> sBack;
    /** Initialize your data structure here. */
    public MyQueue() {
        sFront = new Stack<>();
        sBack  = new Stack<>();
    }
    
    /** Push element x to the back of queue. */ 
    // O(1)
    public void push(int x) {
        sBack.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    // O(n)
    public int pop() {
        if (sFront.isEmpty()) {
            while (!sBack.isEmpty()) {
                sFront.push(sBack.pop());
            }
        }
        return sFront.pop();
    }
    
    /** Get the front element. */
    // O(n)
    public int peek() {
        if (sFront.isEmpty()) {
            while (!sBack.isEmpty()) {
                sFront.push(sBack.pop());
            }
        }
        return sFront.peek();
    }
    
    /** Returns whether the queue is empty. */
    // O(1)
    public boolean empty() {
        return sFront.isEmpty() && sBack.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
 
 // If we want O(n) push and O(1) peek/pop instead, just add all stack
 // element to helper stack push new elements on top then add everything
 // back. The end runtime result is kinda similar, depends on how
 // frequent each operation is. If we have long queues and push very often
 // it will be expensive, but if we have short queues and pop/peek often
 // the original solution will be expensive. I still think that my solution
 // behaves better though- kinda like amortized O(1) under certain
 // circumstances.
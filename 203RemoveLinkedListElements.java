/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
// Iterative solution
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if (head == null) {
            return head;
        } else {
            while (head != null && head.val == val) {
                head = head.next;
            }
            ListNode curr = head;
            while (curr != null && curr.next != null) {
                if (curr.next.val == val) {
                    curr.next = curr.next.next;
                } else {
                    curr = curr.next;
                }
            }
        }
        return head;
    }
}

// Recursive solution, less overhead compared to iterative solution
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if (head != null) {
            if (head.val == val) {
                // Skip to next element
                head = removeElements(head.next, val);
            } else {
                // Preserve current element
                head.next = removeElements(head.next, val);
            }
        }
        return head;
    }
}

// Test cases
// []
// [1], 1
// [1,1,2,3], 1 - consecutive head removal
// [2,3,1,1,1,2], 1 - consecutive middle removal
// [2,3,1,1], 1 - end case
// [1,2,3,1,1,2,3,1], 1 - mix multiple subsections to remove
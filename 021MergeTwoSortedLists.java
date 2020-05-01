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

// Super standard solution, O(n + m) where n is length of l1 and m is length of l2
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // Build a new list instead of worrying about splicing with one of the lists
        ListNode result;

        // Front case
        if (l1 == null) {
            return l2;
        } else if (l2 == null) {
            return l1;
        } else if (l1.val <= l2.val) {
            result = l1;
            l1 = l1.next;
        } else {
            result = l2;
            l2 = l2.next;
        }

        // Middle case
        ListNode curr = result;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }

        // End case
        if (l1 != null) {
            curr.next = l1;
        } else {
            curr.next = l2;
        }

        return result;
    }
}
"""
Remove Dups
Remove duplicates from an unsorted linked list
Follow up: solve the problem without extra space
U:
1->2->3->1 -> 1->2->3
1->1->2->3 -> 1->2->3
1->1 -> 1
1->2->2->2->3 -> 1->2->3
1->2->1->2->3 -> 1->2->3
M:
1. Use hash set to keep track of unique values
2. Pointer bookkeeping
P:
1. Use a set to keep track of values seen, then remove nodes if the value
is already seen
(1) Create an empty set
(2) Create curr to point to head
(3) while curr.next is not None, check if its value is contained in the set
    if contained:
        curr.next = curr.next.next
    else:
        add current val into the set
        move curr to point to next node
Runtime: O(N)
Space: O(N) worst case all unique values
2. For each node, iterate through the rest of the list to remove nodes with
the same value
Runtime: O(N^2), worst case all unique values
Space: O(1)
"""


def remove_dups(head):
    #  Handles empty list or list with one node
    if head and head.next:
        vals = set()
        vals.add(head.data)
        curr = head
        while curr.next:
            if curr.next.data in vals:
                curr.next = curr.next.next
            else:
                curr = curr.next
                vals.add(curr.data)


def remove_dups2(head):
    if head and head.next:
        p1 = head
        while p1.next:
            p2 = p1
            while p2.next:
                if p2.next.data == p1.data:
                    p2.next = p2.next.next
                else:
                    p2 = p2.next
            p1 = p1.next


"""
R:
1.
1->2->3
head [1]
head.next [2]
vals = {1, 2, 3}
curr = [3]
1
head [1]
head.next [1]
vals = {1}
curr = [1]
2.
1->2->3
head [1]
head.next [2]
p1 [3]
p2 [3]
"""

"""
Return Kth to Last
Find the kth to last element of a singly linked list
U:
Assume k is valid, from 1 to n?
1->2->3, 1 -> 3
1->2->3, 2 -> 2
1->2->3, 3 -> 1
M:
Need to use one iteration to find the size of the linked list first
P:
1. First find the length then iterate to n - k element
(1) Find the length of the linked list
(2) Set up a curr pointer to point to head
(3) K to last means n - k moves forward for the curr pointer
(4) Return the data at the curr pointer
Runtime: O(N)
Space: O(1)
2. Recursive approach
Return (node, n-1), and if n is zero, return the value
Runtime: O(N)
Space: O(N)
3. Two pointers, have one fast that is k ahead of the slow one but move at the
same speed, then when the fast reaches the end, the slow should point at kth
to last element
Runtime: O(N) worst case
Space: O(1)
"""


def get_kth_to_last(head, k):
    length = get_length(head)
    curr = head
    for i in range(0, length - k):
        curr = curr.next
    return curr.data


def get_length(head):
    # Returns the length of the linked list
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next
    return length


def get_kth_to_last_recursive(head, k):
    return helper(head, k)[0]


def helper(node, k):
    if not node.next:
        return (node.data, 1)
    result = helper(node.next, k)
    if result[1] == k:
        return result
    else:
        return (node.data, result[1] + 1)


def get_kth_to_last_two_p(head, k):
    fast = head
    slow = head
    for i in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow.data


"""
R:
Approach 3:
1->2->3, 3
fast = None
slow = [1]
i = 3

1->2->3, 1
fast = None
slow = [3]
i = 1

1->2->3, 2
fast = None
slow = [2]
i = 3

Approach 2:
1->2->3, 1
node [1]
result = helper([2], 1) = (3, 1) -> (3, 1)
    node [2]
    result = helper([3], 1) = (3, 1) -> (3, 1)
        node [3]
        -> (3, 1)

1->2->3, 3
node [1]
result = helper([2], 3) -> (1, 3)
    node [2]
    result = helper([3], 3) = (3, 1) -> (2, 2)
        node [3]
        -> (3, 1)

Approach 1:
1->2->3, 1
length = 3
length - k = 2
curr = [3]
i = 2

1->2->3, 3
length = 3
length - k = 0
curr = [1]
i = 0
"""

"""
Partition
Write code to partition a linked list around a value x, such that all nodes
less than x comes before all nodes greater than or equal to x. If x is in the
list, it goes after all nodes less than x.
U:
3->2->19->2->28->5, 18 -> 3->2->2->5->19->28
1->3->20->13->27->23, 20 -> 1->3->13->20->27->23
x can be in or not in the list, can be greater than all or less than all,
can be negative
If list is empty or has one element, just return
Might not need to maintain original order
M:
Make separate lists and append them in the end
P:
1. Make separate lists, smaller and greater/equal, then append greater/equal
at the end of smaller (stable)
2. Iterate through the list, if next element is smaller, put in front
(not stable but easy)
Can also start a new list and grow at head or tail
if curr.next < val:
    temp = curr.next
    curr.next = curr.next.next
    temp.next = head
    head = temp
Runtime: O(N)
Space: O(1)
"""


def partition(head, val):
    curr = head
    while curr and curr.next:
        if curr.next.data < val:
            temp = curr.next
            curr.next = curr.next.next
            temp.next = head
            head = temp
        else:
            curr = curr.next


"""
R:
2->2->3->19->28->5
val = 5
head = [2]
curr = [5]
temp = [2]
1->3->5
val = -1
head = [1]
curr = [5]
5->3->1
val = 7
head = [5]
curr = [1]
temp = [5]
2->20->10
val = 5
head = [2]
curr = [10]
temp = [2]
"""

"""
Palindrome
Implement a function to find out whether a linked list is a palindrome
U:
1->2->3->2->1 True
1->2->2->1 True
1->1->3 False
1 True
None True
M:
Use stacks and queues as extra storage to check whether the values match from
either direction (O(N) space)
Two pointers
P:
1. Use stack and queue
(1) Iterate through the list, add each value into a stack and a queue
(2) while the stack or queue is not empty, pop from stack and remove from
queue and compare the values, if anything is unequal then it is not a
palindrome
Runtime: O(N)
Space: O(N)
2. Use two pointers
for each i in 0 to n // 2, find list[0] and list[n - i - 1] and compare.
If anything doesn't match, return False
Runtime: O(N^2) need to traverse linked list for each i
Space: O(1)
3. Recursive approach (still O(N^2))
base case: middle
recursive case: check first node and last node value
Runtime: O(N^2)
space: O(N)
4. Recursive approach (O(N))
base case: middle of the list, pass back node and is palindrome result
"""


def is_palindrome(head):
    length = get_length(head)
    return check(head, length)


def check(node, length):
    if length < 2:
        # Empty or single node in the middle
        return True
    curr = node
    for i in range(length - 1):
        curr = curr.next
    if curr.data != node.data:
        return False
    return check(node.next, length - 2)


def is_palindrome2(head):
    length = get_length(head)
    return check2(head, length)[1]


def check2(node, length):
    if not node or length <= 0:
        # Even length
        return (node, True)
    elif length == 1:
        # Odd length
        return (node.next, True)
    result = check2(node.next, length - 2)
    if not result[1]:
        return (node, False)
    if result[0].data == node.data:
        return (result[0].next, True)
    return (node, False)


"""
R:
Recursive 2:
1a->2a->2b->1b
length = 4
check([1a], 4) -> (None, True)
    node = [1a]
    result = check([2a], 2) -> ([1b], True)
        node = [2a]
        result = check([2b], 0) -> ([2b], True)

1a->2->3->4->1b
length = 5
check([1a], 5) -> ([1a], False)
    node = [1a]
    result = check([2], 3) -> ([2], False)
        node = [2]
        result = check([3], 1) -> ([4], True)

Recursive 1:
1->2->2->1
length = 4
check([1], 4) -> True
    node = [1]
    curr = [1]
    check([2], 2) -> True
        node = [2]
        curr = [2]
        check([2], 0) -> True
1->3->1
length = 3
check([1], 3) -> True
    node = [1]
    curr = [1]
    check([3], 1) -> True

1->3->2
length = 3
check([1], 3) -> False
    node = [1]
    curr = [2] -> False
"""

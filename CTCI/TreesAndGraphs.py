"""
Route Between Nodes
Given a directed graph, find out whether there is a route between two nodes
U:
1 -> 2 -> 3
|    |
v    v
4 -> 5    6
has_route(g, 1, 5) -> True
has_route(g, 1, 6) -> False
Is the graph in adjacency list form or adjacency matrix form?
Assume adjacency list
Will the given nodes guaranteed to be in the graph?
No, so handle that case.
Assume path can go either way. Assume no duplicates in the graph

M: BFS
P:
(1) Check if the given nodes are both in the graph
(2) Perform a BFS from both given nodes. If find the other, return True
class Graph:
    def __init__(self):
        self.nodes = {}
    key: node (assume int value)
    value: list of destination nodes for outgoing edges
Runtime: O(V) worst case, need to visit every node
Space: O(V) worst case, visited and queue both store all nodes
"""

from collections import deque


def has_route(g, a, b):
    if a not in g.nodes or b not in g.nodes:
        return False
    return bfs(g, a, b) or bfs(g, b, a)


def bfs(g, start, end):
    queue = deque()
    queue.append(start)
    visited = set()
    while queue:
        curr = queue.popleft()
        visited.add(curr)
        if curr == end:
            return True
        for node in g.nodes[curr]:
            if node not in visited:
                queue.append(node)
    return False


def has_route_bidirectional(g, a, b):
    if a not in g.nodes or b not in g.nodes:
        return False
    a_queue = deque()
    b_queue = deque()
    a_queue.append(a)
    b_queue.append(b)
    a_visited = set()
    b_visited = set()
    while a_queue and b_queue:
        a_curr = a_queue.popleft()
        b_curr = b_queue.popleft()
        if b_curr in a_visited or a_curr in b_visited:
            return True
        a_visited.add(a_curr)
        b_visited.add(b_curr)
        for node in g.nodes[a_curr]:
            if node not in a_visited:
                a_queue.append(node)
        for node in g.nodes[b_curr]:
            if node not in b_visited:
                b_queue.append(node)
    return False


"""
Minimal Tree
Given a sorted array with unique integer elements, write an algorithm to
create a BST with minimal height.
U:
[1, 2, 3, 4, 5]
  2    or    4
1   4      2   5
   3 5    1 3
M:
Make a complete tree from sorted array
P:
Root will be the middle element, children will be middle of first and second
half, etc.
mid = (start + stop) // 2

"""


class BinaryTree:
    def __init__(self):
        self.overall_root = None


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def make_bst(arr):
    tree = BinaryTree()
    tree.overall_root = helper(arr, 0, len(arr))


def helper(arr, start, stop):
    if start == stop:
        return None
    mid = (start + stop) // 2
    val = arr[mid]
    root = TreeNode(val, helper(start, mid), helper(mid+1, stop))
    return root


"""
R:
arr = [1, 2, 3, 4, 5], len = 5
helper(0, 5)
mid = 2
val = 3
root = [3, helper(0, 2), helper(3, 5)]
helper(0, 2)
mid = 1
val = 2
root = [2, helper(0, 1), helper(2, 2)]
helper(0, 1)
mid = 0
val = 1
root = [1, helper(0, 0), helper(1, 1)]
helper(3, 5)
mid = 4
root = [5, helper(3, 4), helper(5, 5)]
helper(3, 4)
mid = 3
root = [4, helper(3, 3), helper(4, 4)]
    3
  2   5
 1   4
arr = [0, 1], len = 2
helper(0, 2)
mid = 1
root = [1, helper(0, 1), helper(2, 2)]
helper(0, 1)
mid = 0
root = [0]
    1
  0
arr = [0, 1, 2], len = 3
helper(0, 3)
mid = 1
root = [1, helper(0, 1), helper(2, 3)]
helper(0, 1) -> [0]
helper(2, 3) -> [2]
    1
  2   3
"""

"""
List of Depths
Given a binary tree, design an algorithm which creates a linked list of all
the nodes at each depth.
U:
    1
  2    3
 4 5  6 7
-> [[1], [2, 3], [4, 5, 6, 7]]
M: BFS or level order traversal
Assume maintain the original order
P:
(1) Use BFS to add each node into a queue along with its depth
(2) Construct linked lists based on the depth and return
Runtime: O(N)
Space: O(N)
"""


def list_of_depths(tree):
    queue = deque()
    queue.add((tree.overall_root, 0))
    list_of_lists = []
    while queue:
        curr_node, curr_depth = queue.popleft()
        if curr_depth >= len(list_of_lists):
            list_of_lists.append([])
        list_of_lists[curr_depth].append(curr_node.data)
        # No need to check visited since trees don't have cycles
        if curr_node.left:
            queue.add((curr_node.left, curr_depth + 1))
        if curr_node.right:
            queue.add((curr_node.right, curr_depth + 1))
    return list_of_lists


"""
R:
   1
 2    3
4 5  6 7
queue = []
list_of_lists = [[1], [2, 3], [4, 5, 6, 7]]
curr_node = [7]
curr_depth = 2
"""

"""
Check Balanced
Implement a function to check if a binary tree is balanced. A balanced tree
is defined to be a tree such that the  heights of the two subtrees never
differ by more than one.
U:
  1
2   3
True

  2
1   3
      4
True

  3
1   2
   1  5
     6
False, height of right subtree of [3] is 3 while the left is 1
M:
Recursion, get height of subtrees
P:
Base case: leaf node height is 1, return True
Recursive case: get height of left and right subtree, return False if differs
more than one
return both the curr height and T/F
Runtime: O(N), need to go to every node, or short circuit if left is not
balanced
Space: O(log N) recursive calls
"""


def check_balanced(tree):
    return check(tree.overall_root)[1]


def check(root):
    if root is None:
        return (0, True)
    left_height, left_balanced = check(root.left)
    right_height, right_balanced = check(root.right)
    # necessary to maintain left_balanced or right_balanced state
    # The overall height could differ by no more than one but some subtrees
    # differ by more than one
    if abs(left_height - right_height) > 1 or not left_balanced \
       or not right_balanced:
        return (max(left_height, right_height) + 1, False)
    else:
        return (max(left_height, right_height) + 1, True)


"""
Validate BST
Implement a function to check if a binary tree is a BST
U:
BST definition: for all nodes, left child < node < right child
An empty tree or a tree with one node is a BST
Assume the BST stores integers, no duplicates, but input might have duplicates
M:
Use recursion to check BST
P:
Base case: empty tree or tree with one node, return True
Recursive case: if have left or right, check left < root and right > root, if
not return False, otherwise check left and right subtree
* Need to make sure the subtree values fall within the right ranges as well!!
       6
    3      10
 1    5  7    30
0  2

at [3]: max is 6, min can be anything
at [1]: max is 3, min can be anything
at [0]: max is 1, min can be anything
at [2]: max is 3, min is 1
at [5]: max is 6, min is 3
at [10]: max can be anything, min is 6
at [7]: max is 10, min is 6
Runtime: O(N) worst case, need to look through every node
Space: O(log N) worst case, need to maintain call stack for one path
"""


def validate_bst(tree):
    return validate(tree.overall_root, None, None)


def validate(root, curr_min, curr_max):
    if root is None:
        return True
    valid = True
    if root.left:
        if root.left.data >= root.data or \
           (curr_min is not None and root.left.data <= curr_min):
            return False
        valid = validate(root.left, curr_min, root.data)
    if root.right:
        if root.right.data <= root.data or \
           (curr_max is not None and root.right.data >= curr_max):
            return False
        valid = valid and validate(root.right, root.data, curr_max)
    return valid


"""
    5
  2    7
1  3  6  8
root = [5]
valid = validate([2]) -> T
root = [2]
valid = validate([1]) -> T
root = [1]
valid = True and validate([3]) -> T
root = [3]
valid = True and validate([7]) -> T
root = [7]
valid = validate([6]) -> T
valid = True and validate([8]) -> T

    3
  2
1
root = [3]
valid = validate([2]) -> T
root = [2]
valid = validate([1]) -> T

    4
  3   2
1
root = [4]
valid = T return False
root = [3]
valid = validate([1]) -> T

       6
    3      10
 1    5  4    30
root = [6]
curr_min = None
curr_max = None
valid = validate([3], None, 6) -> T
    root = [3]
    curr_min = None
    curr_max = 6
    valid = validate([1], None, 3) -> T
    valid = T and validate([5], 3, 6) -> T
valid = validate([10], 6, None) -> F
    root = [10]
    curr_min = 6
    curr_max = None
    root.left.data < curr_min -> F
"""

"""
Successor
Write an algorithm to find the next node or a given node in a BST, assume
each node has a link to its parent
U:
       6
    3      10
 1    5  7    30
Successor of 1: 3
Successor of 5: 6
Successor of 6: 7
Successor of 10: 30
Successor of 30: None
       6
    2      10
      4  7    30
     3 5
Successor of 2: 3
    3
  2   5
1   4

M:
Recursively find the next larger node?
P:
If node has right child: successor is right then all the way left
If node doesn't have right child and parent is greater than node: successor
is the parent (given node is a left child of parent)
If node doesn't have right child parent is less than node: keep finding
parent until find one greater than node (given node is a right child of
parent). If cannot find any, then it is the right most leaf node.
"""


def successor(node):
    if node is None:
        return None
    if node.right:
        return find_leftmost_node(node.right)
    else:
        if node.parent and node.parent.data > node.data:
            return node.parent.data
        else:
            return find_larger_parent(node, node.parent)


def find_leftmost_node(node):
    if node.left is None and node.right is None:
        return node.data
    return find_leftmost_node(node.left)


def find_larger_parent(node, parent):
    while parent is not None and parent.data < node.data:
        parent = parent.parent
    if not parent:
        return None
    return parent.data


"""
Build Order
Given a list of projects and a list of dependencies, all project's dependencies
must be built before the project is. Find a build order that will allow the
projects to be build. Return None if no valid order.
U:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
second is dependent on the first
output: e, f, a, b, d, c
M:
Topological sort, post order graph traversal
Graph modification
P:
Reverse post order:
(1) Find all nodes with no incoming edges
(2) Start postorder DFS from those nodes and record the order
(3) Reverse the order from each postorder DFS
(3) Check if the orders covers all nodes. If so, combine the orders somehow.
Otherwise there are no proper order so return None.
Problem: no way to properly combine the orders
Graph modification:
(1) Find all nodes with no incoming edges and add them in build order
(2) Remove all outgoing edges from those nodes
(3) Repeat, find all nodes with no incoming edges and add.
(4) When there are no longer nodes with no incoming edges, compare built nodes
with all projects. If the number match, the build order is valid. Otherwise
there are circular dependencies, return None.
(reverse the dependencies and change to outgoing edges instead for easier
check)
Runtime: O(P + D) where P is number of projects and D is number of dependencies
P: generate the graph
D: add the edges, and process every edge while figuring out the order
"""


def build_order(projects, dependencies):
    g = {p: [] for p in projects}
    for d in dependencies:
        g[d[1]].append(d[0])
    order = []
    to_build = deque()
    built = set()
    for p in g:
        if not g[p]:
            to_build.append(p)
            built.add(p)
    while to_build:
        curr = to_build.popleft()
        order.append(curr)
        remove_edges_to(g, curr)
        for p in g:
            if p not in built and not g[p]:
                to_build.append(p)
                built.add(p)
    if len(order) != len(projects):
        return None
    else:
        return order


def remove_edges_to(g, to):
    for p in g:
        if g[p]:
            new_edge = [i for i in g[p] if i != to]
            g[p] = new_edge


"""
First Common Ancestor
Design an algorithm to find the first common ancestor of two nodes in a
binary tree. Not necessarily a BST.
U:
   2
1     3
find_common_ancestor(1, 3) -> 2
find_common_ancestor(1, 2) -> 2?

    3
 1      2
5  4   8  10
  6
find_common_ancestor(6, 8) -> 3
find_common_ancestor(6, 5) -> 1
Assume no duplicates?
M:
Recursion
P:
If a and b are descendents of different subtrees, then current node is the
common ancestor. If they are both descendents of the same subtree, then the
subtree holds the common ancestor.
Brute force:
Do DFS on every single node and figure out which one satisfies the condition
above.
for each node x:
    check if a, b are both in left subtree of x
        if yes, recurse for x.left
    check if a, b are both in right subtree of x
        if yes, recurse for x.right
    else
        x is common first ancester, return x
    return (1, 1) -> in each, (2, 0) -> both in left, (0, 2) -> both in right?
    or return (None, T) if found, (None, F) if not found. And if left = T and
    right = T, returns the common ancestor to be (node, T)?
    Or just return a if found a, b if found b, and common ancestor if found
    each in left and right (But this won't handle the case where one of the
    nodes are not in the tree vs. a is a child of b)
    So return (node, F), where node is a or b or common ancestor, and T/F
    indicating if the common ancestor is actually found.

"""


def find_common_ancestor(tree, a, b):
    return find_common(tree.overall_root, a, b)[0]


def find_common(root, a, b):
    if root is None:
        return (None, False)
    if root is a and root is b:
        # a and b somehow are the same node, it is its common ancestor
        return (root, True)
    left_result = find_common(root.left, a, b)
    if left_result[1]:
        # Found the common ancestor, just bubble it up
        return left_result
    right_result = find_common(root.right, a, b)
    if right_result[1]:
        # Found the common ancestor, just bubble it up
        return right_result
    if left_result[0] and right_result[0]:
        # Found a and b in both subtrees, current root is the common ancestor
        return (root, True)
    elif (root is a or root is b) and (left_result[0] or right_result[0]):
        # Found a or b as the current root and the other in one of the
        # subtrees
        return (root, True)
    elif root is a or root is b:
        # Found a or b as the current root, but haven't found the other
        return (root, False)
    else:
        # Haven't found both in the subtrees, bubble up discovery if there
        # is any
        return left_result if left_result[0] else right_result


"""
R:
    3
 1      2
5  4   8  10
  6
find_common([3], [5], [6]) -> ([1], True)
root = [3]
left_result = find_common([1], [5], [6]) -> ([1], True)
    root = [1]
    left_result = find_common([5], [5], [6]) -> ([5], False)
        root = [5]
        left_result = (None, False)
        right_result = (None, False)
    right_result = find_common([4], [5], [6]) -> ([6], False)
        root = [4]
        left_result = find_common([6], [5], [6]) -> ([6], False)
            root = [6]
            left_result = (None, False)
            right_result = (None, False)
        right_result = (None, False)
"""

"""
BST Sequence
Given a BST with distinct elements, print all possible arrays that could have
led to the tree.
U:
  2
1   3
-> [2, 1, 3], [2, 3, 1]
   2
0     3
  1
-> [2, 0, 3, 1], [2, 3, 0, 1], [2, 0, 1, 3]
M:
Recursive backtracking that maintains parent-child relationship?
Preorder is necessary
Level-order traversal?
P:
Maintain a list of to process nodes
Base case:
toProcess is empty: print toProcess
Recursive case:
Choose: for each option in toProcess
Explore: add the child node of the option in toProcess, continue exploring
Unchoose: pop the option from toProcess
Alternative: generate the sequence from left and right then weave them together
"""


def bst_sequences(tree):
    if not tree.overall_root:
        print([])
    to_process = [tree.overall_root]
    acc = []
    print_sequences(tree.overall_root, to_process, acc)


def print_sequences(root, to_process, acc):
    # Choose
    acc.append(root.data)
    # Make sure the root is inserted back to the original place
    index = to_process.index(root)
    to_process.remove(root)
    if root.left:
        to_process.append(root.left)
    if root.right:
        to_process.append(root.right)
    if not to_process:
        print(acc)
    # Explore
    for option in to_process:
        print_sequences(option, to_process, acc)
    # Unchoose
    acc.pop()
    to_process.insert(index, root)
    # Important to remove the child nodes since once we back track those
    # are no longer valid to be processed next
    if root.left:
        to_process.remove(root.left)
    if root.right:
        to_process.remove(root.right)


"""
Check Subtree
T1 and T2 are two very large binary trees with T1 much bigger than T2. Create
an algorithm to determine if T2 is a subtree of T1
U:
T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n
is identical to T2. Has to be identical if we cut off the tree in node n.
M:
Recursively check if trees are identical
P:
Recursion:
Go through all nodes in T1 and check if T2 match exactly starting from that
root.
Runtime: O(N * M), each being the number of nodes in T1 or T2, but the reality
will be less since we won't check through all N nodes or all M nodes when
checking identical.
Space: O(log(N) + log(M)) note this is significantly less than alternative
Alternative with substrings:
Do a pre-order traversal and decide whether the T2 is a substring for T1
also need to insert None nodes just to indicate the empty trees we skipped over
while traversing elements.
Runtime: O(N + M)
Space: O(N + M)
"""


def check_subtree(t1, t2):
    t1_order = get_preorder(t1.overall_root)
    t2_order = get_preorder(t2.overall_root)
    return t2_order in t1_order


def get_preorder(root):
    if root is None:
        return 'n'
    else:
        return str(root.data) + get_preorder(root.left)
        + get_preorder(root.right)


def check_subtree2(t1, t2):
    return check_sub(t1.overall_root, t2.overall_root)


def check_sub(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return check_identical(root1, root2) \
        or check_sub(root1.left, root2) \
        or check_sub(root1.right, root2)


def check_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None or root1.data != root2.data:
        return False
    else:
        return check_identical(root1.left, root2.left) or \
            check_identical(root1.right, root2.right)


"""
Paths with Sum
Given a binary tree in which each node contains an int value, design an
algorithm to count the number of paths that sum to a given value. The paths
does not need to start or end at the root or a leaf but must go downwards.
U:
   2
 1    3
2  4   0
      1  2
     -1
sum = 5 -> 4, [2, 1, 2], [1, 4], [2, 3], [2, 3, 0], [2, 3, 0, 1, -1], [3, 0, 2]
M:
Recursively explore the tree for every subpaths
P:
1. Brute force:
Base case:
root is None and curr_sum != target, return 0
Recursive case:
path_sum = 0
(1) include curr node
    path_sum += (count(left, target - curr.data)
                + count(right, target - curr.data))
(2) not include curr node
    path_sum += (count(left, target) + count(right, target))
return path_sum
Runtime: O(N^2) worst case
Space: O(N) worst case
2. Optimize
Use a hash table to keep track of the times we need a target sum, thus saving
repeated calculation
[running_sum, count]
Base case:
root is None, return 0
Recursive case:
Choose:
running_sum += root.data
path_sum = 0
path_sum += memo[running_sum - target_sum] # find the matching running sum seen
if target_sum == running_sum:
    # Add extra path from root
    path_sum += 1
recurse on left
recurse on right
decrement counts in memo
Runtime: O(N)
Space: O(N)
"""


def count_path_sum(tree, target):
    memo = {}
    return count(tree.overall_root, target, 0, memo)


def count(root, target, running_sum, memo):
    if root is None:
        return 0
    else:
        running_sum += root.data
        path_sum = memo.get(running_sum - target, 0)
        if running_sum == target:
            path_sum += 1
        memo[running_sum] = memo.get(running_sum, 0) + 1
        path_sum += count(root.left, target, running_sum, memo)
        path_sum += count(root.right, target, running_sum, memo)
        memo[running_sum] -= 1
        return path_sum

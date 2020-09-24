"""
Triple Step
A child is running up a staircase with n steps and can hop either 1, 2, or 3
steps at a time. Count how many possible ways the child can run up the stairs.
U:
1 steps: 1 way
2 steps: 2 ways, 1-1 or 2
3 steps: 4 ways, 1-1-1, 1-2, 2-1, 3
4 steps: 7 ways, 1-1-1-1, 1-1-2, 1-2-1, 1-3, 2-1-1, 2-2, 3-1
Choose 1 -> 3 remaining, 4 combos
Choose 2 -> 2 remaining, 2 combos
Choose 3 -> 1 remaining, 1 combo
Add up to 7
Assume n >= 0
M:
Recursive backtracking + memoization
P:
Base case: 1 step (1), 2 steps (2), and 3 steps (4)
Recursive case:
If target not in memo:
    memo[target] = count_step(target - 1) + count_step(target - 2)
                   + count_step(target - 3)
else:
    return memo[target]
Runtime:
Before optimization: O(3^N), 3 options every time
After optimization: O(N), have calculated combo for every N and O(1) look up
in memo
Space: O(N)
"""


def count_step(n):
    memo = {0: 0, 1: 1, 2: 2, 3: 4}
    return count(n, memo)


def count(n, memo):
    if n not in memo:
        memo[n] = count(n - 1, memo) + count(n - 2, memo) + count(n - 3, memo)
    return memo[n]


"""
R:
n = 0: 0
n = 4:
memo[4] = count(3, memo) + count(2, memo) + count(1, memo)
        = 4 + 2 + 1
        = 7
n = 7
memo = {0:0, 1:1, 2:2, 3:4, 4:7, 5:13, 6:24, 7:}
memo[7] = count(6, memo) + count(5, memo) + count(4, memo) -> 44
        = 24 + 13 + 7
    n = 6
    memo[6] = count(5, memo) + count(4, memo) + count(3, memo) -> 24
            = 13 + 7 + 4
        n = 5
        memo[5] = count(4, memo) + count(3, memo) + count(2, memo) -> 13
                = 7 + 4 + 2
            n = 4
            memo[4] = count(3, memo) + count(2, memo) + count(1, memo) -> 7
"""

"""
Robot in a Grid
A robot starts at the upper left corner of a grid with r rows and c columns.
The robot can only move right and down, but certain cells are "off limits".
Design an algorithm to find a path from the top left to the bottom right.
U:
3x3, (2, 1) is off-limits
O O O
O O O
O X O
Take in an r x c grid, and a list of off-limits cells
Assume there will always be a valid path
Returns a list of coordinates in the path
M:
Recursive backtracking, try both right and down until find a path, if neither
is valid, backtrack until find a valid path. Possibly memoization to save
some time since currently it is exponential.
P:
Pass in an accumulator for storing the valid paths, curr_row and curr_col,
start at (0, 0), and return a flag showing whether a path is found.
If so add the current point into the path.
Base case:
Current cell is not in the grid or contains obstacle, return False
Recursive case:
If any of the below condition is true:
(1) the current cell is bottom right
(2) exploring the right cell leads to a valid path
(3) exploring the bottom cell leads to a valid path
add current point to the accumulator
return True
Otherwise return false
Runtime: O(2^(r + c))
Optimize: Keep track of a set of points we know has failed and return early
Runtime: O(r * c), since only visit each point once
"""


def find_path(r, c, obstacles):
    acc = []
    obstacles = set(obstacles)
    failed = set()
    find(r, c, 0, 0, obstacles, acc, failed)
    return acc.reverse()  # If start from the end can save this reverse


def find(r, c, curr_row, curr_col, obstacles, acc, failed):
    if (curr_row, curr_col) in failed:
        return False
    if not is_valid_cell(r, c, curr_row, curr_col, obstacles):
        return False
    found = curr_row == r - 1 and curr_col == c - 1
    if found or \
        find(r, c, curr_row + 1, curr_col, obstacles, acc, failed) \
            or find(r, c, curr_row, curr_col + 1, obstacles, acc, failed):
        acc.append((curr_row, curr_col))
        return True
    failed.add((curr_row, curr_col))
    return False


def is_valid_cell(r, c, curr_row, curr_col, obstacles):
    return curr_row >= 0 and curr_col >= 0 and \
        curr_row < r and curr_col < c and \
        (curr_row, curr_col) not in obstacles


"""
Magic Index
A magic index in an array A[0...n-1] is defined to be an index such that
A[i] = i. Given a sorted array of distinct integers, write a method to find a
magic index, if one exists, in A.
U:
A[-1, 1, 3] -> 1, A[1] = 1
A[-3, -1, 0, 3, 10] -> 3
A[3, 4, 5] -> None
M:
Binary search
P:
mid = middle index between start and end
if mid > A[mid]:  # [-3, -1, 0, 3, 10], 2 > A[2] = 0
    search the right half
else if mid < A[mid]:  # [-1, 1, 4, 8, 10], 2 < A[2] = 4
    search the left half
else:
    return mid
Runtime: O(log N)
Space: O(log N) if use recursion, O(1) if in place
"""


def magic_index(arr):
    if not arr:
        return None
    start = 0
    stop = len(arr)
    while stop > start:
        mid = (start + stop) // 2
        if mid == arr[mid]:
            return mid
        elif mid > arr[mid]:
            start = mid + 1
        elif mid < arr[mid]:
            stop = mid
    return None


"""
R:
[-3, -1, 0, 3, 10]
start = 3
stop = 4
mid = 3
arr[mid] = 3

[0, 2, 3, 4]
start = 0
stop = 1
mid = 0
arr[mid] = 0

[3, 8, 10]
start = 0
stop = 0
mid = 0
arr[mid] = 3
"""

"""
Power Set
Write a method to return all subsets of a set
U:
{1, 2, 3} -> {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}
{1} -> {}, {1}
{} -> {}
M:
Recursive backtracking, choose or not choose each element when constructing
the set
P:
result {} containing all subsets
accumulator {} containing current subset
to_choose containing all remaining options or can use original set
Base case:
to_choose is empty, add accumulator into result as a new set
Recursive case:
to_choose is not empty, two options:
(1) not choose the first element and pass it on as it-is
(2) choose the first element and add it to accumulator
Runtime: O(N * 2^N), generate each subset then copy them to result
Space: O(N * 2^N), 2^N subsets of max size N
"""


def power_set(s):
    result = []
    acc = set()
    get_power_set(s, result, acc)
    return result


def get_power_set(to_choose, result, acc):
    if not to_choose:
        result.append(set(acc))
    else:
        # Choose
        val = to_choose.pop()
        # Explore
        get_power_set(to_choose, result, acc)
        acc.add(val)
        get_power_set(to_choose, result, acc)
        # Unchoose
        acc.remove(val)
        to_choose.add(val)


"""
Permutation without Dups
Write a method to compute all permutations of a string of unique characters.
U:
a -> a
ab -> ab, ba
abc -> abc, acb, bac, bca, cab, cba
M:
Recursive backtracking to combine characters at different order
P:
Start off to_choose being the original string
acc be empty list
result be empty list
If to_choose is empty:
    add acc as a string into result
else:
    for each character in to_choose:
        append that character to acc
        recurse on remaining options
        pop that character from acc
Runtime: O(N * N!) convert acc to list + N! permutations
Space: O(N * N!) N! permutations of length N
"""


def permutations(s):
    acc = []
    result = []
    to_choose = list(s)
    get_permutations(to_choose, acc, result)
    return result


def get_permutations(to_choose, acc, result):
    if not to_choose:
        result.append(''.join(acc))
    else:
        for c in to_choose:
            # Choose
            index = to_choose.index(c)
            to_choose.remove(c)
            acc.append(c)
            # Explore
            get_permutations(to_choose, acc, result)
            # Unchoose
            to_choose.insert(index, c)
            acc.pop()


"""
Permutations with Dups
Write a method to compute all permutations of a string whose characters are
not necessarily unique. The list of permutations shouldn't have duplicates.
U:
abb -> [abb, bab, bba]
M:
Still backtracking, but maybe use a set at the end
P:
1. Naive approach
Use backtracking from above but instead of using list for result, use a set
instead so the result doesn't contain duplicates
2. First count the characters with a hash table
When recursing, only proceed with unique characters as options
"""


def permutations_with_dup(s):
    acc = []
    result = []
    to_choose = count_letters(s)
    get_permutations(to_choose, acc, result)
    return result


def get_permutations_with_dup(to_choose, acc, result):
    if no_letters(to_choose):
        result.append(''.join(acc))
    else:
        for c in to_choose:
            if to_choose[c] > 0:
                # Choose
                acc.append(c)
                to_choose[c] -= 1
                # Explore
                get_permutations_with_dup(to_choose, acc, result)
                # Unchoose
                to_choose[c] += 1
                acc.pop()


def count_letters(s):
    result = {}
    for c in s:
        result[c] = result.get(c, 0) + 1
    return result


def no_letters(to_choose):
    for c in to_choose:
        if to_choose[c] > 0:
            return False
    return True


"""
Parens
Implement an algorithm to print all valid combos of n pairs of parentheses
U:
n = 1 -> ()
n = 2 -> ()() or (())
n = 3 -> ()()(), ()(()), (())(), ((())), (()())
M:
Recursive backtracking
P:
The combo is valid if only every opening paren has a closing paren after
Keep track of n, opening count, closing count, acc
Base case:
opening count = closing count = n, print(acc)
if opening count < n:
    can add opening paren to acc, opening count += 1
if closing count < opening count:
    can add closing paren to acc, closing count += 1
"""


def parens(n):
    print_parens(n, 0, 0, '')


def print_parens(n, opening, closing, acc):
    if n == opening and n == closing:
        print(acc)
    else:
        if opening < n:
            print_parens(n, opening + 1, closing, acc + '(')
        if closing < opening:
            print_parens(n, opening, closing + 1, acc + ')')

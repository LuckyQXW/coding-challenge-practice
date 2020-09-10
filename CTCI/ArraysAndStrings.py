"""
Is Unique
Implement an algorithm to determine if a string has all unique characters
Follow up: not use additional DS

U: abc -> True, aab -> False, '' -> True, case-sensitive
M: use hash table or two pointers
P:
1. Use hash table:
(1) Create a set
(2) For each character in string:
    if character is already in the set
        return False (has duplicates)
    add current character in the set
(3) Return True at the end
Runtime: O(N) for going through n chars in string
Space: O(N) for storing n chars in hash set worst case

2. Use two pointers and no extra space
(1) For each character i in string
      for each remaining character j in string
        if i == j
          return False
(2) Return True at the end
Runtime: O(N^2)
Space: O(1)
"""


def is_unique(s):
    chars = set()
    for c in s:
        if c in chars:
            return False
        chars.add(c)
    return True


def is_unique_2(s):
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


"""
R:
s = aab, len(s) = 3
i = 0
j = 1
s[i] = a
s[j] = a -> False

s = abb, len(s) = 3
i = 1
j = 2
s[i] = b
s[j] = b -> False

s = abc -> True
s = '', len(s) = 0 -> True
"""

"""
URLify
Write a method to replace all spaces in a string with %20, also given the true
length of the string
U:
"Hi there you", 12 -> "Hi%20there%20you"
"   ", 3 -> "%20%20%20"
"abc", 3 -> "abc"
Assume valid input
M:
Iterate from the back
P:
1. Brute force:
for each character in string at i:
  if the character is a space:
    repalce current character with %
    shift the remaining string two characters over
    insert 2 and 0 at i + 1 and i + 2
Runtime: O(N^2) for shifting characters over
Space: O(1)
2. Improve:
Keep track of two pointers. i starts at the end of the original
string (given true length - 1), j starts at the end of the array
buffer (length of list - 1)
while j > i: (if j == i, we have replaced all spaces)
  if i is not a space:
    set s[j] = s[i]
  else:
    set s[j] = 0
    j -= 1
    s[j] = 2
    j -= 1
    s[j] = %
  j -= 1
  i -= 1
Runtime: O(N) for only iterating over the array buffer once
Space: O(1) in place
"""


def urlify(s, l):
    """
    Assume s comes in as [a, ' ', c, None, None] -> [a, %, 2, 0, c]
    """
    j = len(s) - 1
    i = l - 1
    while j > i:
        if s[i] == ' ':
            s[j] = '0'
            j -= 1
            s[j] = '2'
            j -= 1
            s[j] = '%'
        else:
            s[j] = s[i]
        i -= 1
        j -= 1


"""
R:
s = [a, %, 2, 0, c], l = 3
j = 0
i = 0
s[i] = ' '
s[j] = None
s = [%, 2, 0, %, 2, 0, %, 2, 0], l = 3
j = -1
i = -1
s[i] = ' '
s[j] = ' '
s = [], l = 0
j = -1
i = -1
"""

"""
Palindrome Permumation
Given a string, check if it is a permutation of a palindrome
U:
abcbc -> True, can be bcabc
ab b -> True, can be bab (space seems to be ignored, only consider letters)
ab -> False, both ab and ba are not palindromes
'' -> True (assume empty strings are palindromes)
Assume case sensitive
M: Use hash tables to count characters
P:
1. Hash table counts
(1) Create a hash table
(2) Go through the string once and count each character (ignore nonletters)
(3) Go through the hash table and check if at most one of the characters have
an odd number count (can be placed at the center), if so return True,
otherwise False
Runtime: O(N) to count letters, O(52) = O(1) to go through the hash table
2. Slight improvement to eliminate separate hash table iteration
Keep track of an odd count and increment it every time we see an odd count. If
we get an even count for a specific character we will always get an even odd
count overall.
3. Use bit masks
Instead of storing actual count, just create a bit vector from the counts with
only 0 and 1
Even case: all 0s, so compare to 0
Have one 1 case: subtract 1 (which generates a vector with no overlaps with
the original) then AND 0
Runtime: O(N)
Space: O(1)? O(26)
"""


def is_palindrome_permutation(s):
    counts = count_letters(s)
    has_odd_count = False
    for c in counts:
        if counts[c] % 2 == 1:
            if has_odd_count:
                return False
            else:
                has_odd_count = True
    return True


def count_letters(s):
    counts = {}
    for c in s:
        if c.isAlpha():
            counts[c] = counts.get(c, 0) + 1
    return counts


"""
R:
s = abbac (bacab)
counts = {a: 2, b: 2, c: 1}
has_odd_count = True
c = 'c'
counts[c] = 1

s = abdbac
counts = {a: 2, b: 2, c: 1, d: 1}
has_odd_count = True
c = 'd'
counts[d] = 1

s = ''
counts = {}
"""

"""
One Away
Given two strings, check if they are one edit (insert, remove, or replace) or
zero edits away
U:
pale, ple -> True, remove 'a'
pale, pales -> True, insert 's'
pale, bale -> True, replace 'p' with 'b'
pale, bake -> False
pale, pale -> True, zero edits
M:
Two pointers
P:
if equal string, True
if difference in length of string is greater than two, False
set up a flag has_edit = False
check each character and compare
(1) Same character, continue
(2) Different character, check if has_edit, if so return False, else
    increment the index in longer string (essentially remove the character),
    or increment both index if length is the same (replace),
    and flip has_edit flag
(3) Return True at the end
Runtime: O(N)
Space: O(1)
"""


def one_away(s1, s2):
    if s1 == s2:
        return True
    if abs(len(s1) - len(s2)) > 1:
        return False
    i = 0  # point at s1
    j = 0  # point at s2
    has_edit = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if has_edit:
                return False
            else:
                if len(s1) > len(s2):
                    i += 1
                elif len(s1) < len(s2):
                    j += 1
                else:
                    i += 1
                    j += 1
                has_edit = True
        else:
            i += 1
            j += 1
    return True


"""
R:
s1 = pale
s2 = pale

s1 = pale
s2 = palely

s1 = pale (len = 4)
s2 = kale (len = 4)
i = 4
j = 4
has_edit = True
s1[i] = e
s2[j] = e

s1 = abc (len = 3)
s2 = ab (len = 2)
i = 2
j = 2
has_edit = False
s1[i] = b
s2[j] = b

s1 = abc (len = 3)
s2 = ad (len = 2)
i = 2
j = 1
has_edit = True
s1[i] = c
s2[j] = d
"""

"""
Rotate Matrix
Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes (4 channels), write a method to rotate the image by 90 degrees.
Assume clockwise
In place?
U:
3x3x4
one channel:
1, 2, 3    7, 4, 1
4, 5, 6 -> 8, 5, 2
7, 8, 9    9, 6, 3

1, 2, 3    7, 4, 1
4, 5, 6 -> 8, 5, 2
7, 8, 9    9, 6, 3

4x4x4
1, 2, 3, 4    1, 0, 5, 1    1, 0, 5, 1
5, 6, 7, 8 -> 3, 6, 7, 2 -> 3, 2, 6, 2
0, 2, 4, 8    5, 2, 4, 3    5, 4, 7, 3
1, 3, 5, 7    7, 8, 8, 4    7, 8, 8, 4

M: matrix rotation
P:
Rotate from outer edge to inner
starting point: (0, 0), (1, 1)... (N // 2, N // 2)

for each row:
    temp = bottom left
    bottom left = bottom right
    bottom right = top right
    top right = top left
    top left = temp

Iteration 1:
bottom left = (N - 1, 0)
bottom right = (N - 1, N - 1)
top right = (0, N - 1)
top left = (0, 0)

Iteration 2:
bottom left = (N - 1 - 1, 0)
bottom right = (N - 1, N - 1 - 1)
top right = (0 + 1, N - 1)
top left = (0, 1)

Iteration 3:
bottom left = (N - 1 - 2, 0)
bottom right = (N - 1, N - 1 - 2)
top right = (0 + 2, N - 1)
top left = (0, 0 + 2)

Iteration 4
bottom left = (N - 1 - 1, 1)
bottom right = (N - 1 - 1, N - 1 - 1)
top right = (1, N - 1 - 1)
top left = (1, 1)
"""


def rotate_matrix(m):
    n = len(m)
    for i in range(0, n // 2):
        for j in range(0, n - 1 - 2*i):
            temp = m[n-1-i-j][i]
            m[n-1-i-j][i] = m[n-1-i][n-1-i-j]
            m[n-1-i][n-1-i-j] = m[i+j][n-1-i]
            m[i+j][n-1-i] = m[i][i+j]
            m[i][i+j] = temp


"""
R:
2x2
3, 1
4, 2
n = 2
i = 1
j = 1
n - 1 - i = 1
temp = 3
m[n-1-i][i] = m[1][0] = 3
m[n-1-i][n-1-i] = m[1][1] = 4
m[i][n-1-i] = m[0][1] = 2
m[i][i] = m[0][0] = 1


5x5
51, 41, 31, 21, 11
52, 42, 32, 22, 12
53, 43, 33, 23, 13
54, 44, 34, 24, 14
55, 45, 35, 25, 15
n = 5
i = 1
j = 2
n - 1 - i = 3
n - 1 - i - j = 1
i + j = 3
temp = m[n-1-i-j][i] = m[1][1] = 32
m[n-1-i-j][i] = m[2][1] = 32
m[n-1-i][n-1-i-j] = m[3][2] = 43
m[i+j][n-1-i] = m[2][3] = 34
m[i][i+j] = m[1][2] = 23

(0, 4)
(0, 2)

8x8
n = 8
n - 1 - 2*i = 7 i = 0: (0, 7)
n - 1 - 2*i = 5 i = 1: (1, 6) -> (0, 5)
n - 1 - 2*i = 3 i = 2: (2, 5) -> (0, 3)
n - 1 - 2*i = 0 i = 3: (3, 3) -> (0, 1)
"""

"""
Zero Matrix
Write an algorithm such that if an element in MxN matrix is 0, its entire
row and column are set to 0.
U:
1, 2, 3    1, 0, 3
2, 0, 1 -> 0, 0, 0
2, 3, 4    2, 0, 4

0, 2, 3, 4    0, 0, 0, 0
1, 3, 4, 0 -> 0, 0, 0, 0
1, 2, 3, 1    0, 2, 3, 0

M: 2D matrix
P:
1. Use extra storage
(1) Go through the matrix and find all the zeros, store its row and column into
separate sets
(2) Go through the matrix again and set all spots whose row or column is
contained in either set to 0
Runtime: O(M * N)
Space: O(M + N)
2. Use first row as marker
(1) Go through first row and first column and check if there are 0s needed to
nullify
(2) Go through the rest of the matrix and set 0 in first row or column
(3) Nullify the rows and columns based on the 0 flags
(4) Nullify the first row and column as needed
Runtime: O(M * N)
Space: O(1)
"""


def zero_matrix(m):
    height = len(m)
    width = len(m[0])
    zero_rows = set()
    zero_columns = set()
    for i in height:
        for j in width:
            if m[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)
    for i in height:
        for j in width:
            if i in zero_rows or j in zero_columns:
                m[i][j] = 0


def zero_matrix2(m):
    first_row_zero = False
    first_column_zero = False
    # Checking first row and column for zeros
    for i in range(len(m)):
        if m[i][0] == 0:
            first_column_zero = True
            break
    for j in range(len(m[0])):
        if m[0][j] == 0:
            first_row_zero = True
            break
    # Find 0s from the rest of the matrix and set the flags
    for i in range(1, len(m)):
        for j in range(1, len(m[0])):
            if m[i][j] == 0:
                m[i][0] = 0
                m[0][j] = 0
    # Set the 0s based on flags in first row and column
    for i in range(1, len(m)):
        if m[i][0] == 0:
            nullify_row(m, i)
    for j in range(1, len(m[0])):
        if m[0][j] == 0:
            nullify_column(m, j)
    # Set the first row and column to 0 if needed
    if first_row_zero:
        nullify_row(m, 0)
    if first_column_zero:
        nullify_column(m, 0)


def nullify_row(m, i):
    for j in range(len(m[0])):
        m[i][j] = 0


def nullify_column(m, j):
    for i in range(len(m)):
        m[i][j] = 0


"""
R:
1, 0, 3    1, 0, 3
0, 0, 0 -> 0, 0, 0
2, 0, 4    2, 0, 4
height = 3
width = 3
zero_rows = {1}
zero_columns = {1}
i = 1
j = 0
"""

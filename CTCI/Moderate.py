import heapq


"""
Number Swapper
Write a function to swap a number in place
i = 4 -> 0100 -> 1101 -> 1001
j = 9 -> 1001 -> 0100
arr[i] ^ arr[j] = 1001
"""


def swap(arr, i, j):
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]


"""
Word Frequency
Design a method to find frequency of occurrence of any given word in a book.
What if we are running it multiple times?
U:
Single vs multiple queries?
Will more words be added to the book?
How is a word defined? Case-sensitivity & remove punctuation?
Invalid input?
"""


class WordLookup:
    def __init__(self, book):
        self.frequencies = {}
        num_words = len(book)
        for w in book:
            self.frequencies[w] = self.frequencies.get(w, 0) + 1
        for w in self.frequencies:
            self.frequencies[w] /= num_words

    def look_up(self, word):
        if word not in self.frequencies:
            return 0
        else:
            return self.frequencies[word]


"""
Factorial Zero
Write an algorithm which computes the number of trailing zeros in n factorial
U:
0!: 0
1!: 0
1*2*3*4*5 = 5! = 120: 1
10!: 2
P:
1. count factors of 5 (since more 2 than 5s must have been seen already)
2. count number of multiples of 5, 25, 125, etc.
    5 * a < target
    25 * b < target (already counted 1 5s)
    125 * c < target (already counted 2 5s)
    a + b + c + ... = total num of 5 factors
"""


def factorial_zero(n):
    if n < 0:
        return None
    count = 0
    for i in range(2, n):
        while i % 5 == 0:
            count += 1
            i = i // 5
    return count


def factorial_zero_2(n):
    if n < 0:
        return None
    count = 0
    i = 5
    while n // i > 0:  # 25
        count += n // i  # count = 6
        i *= 5  # i = 25
    return n


"""
25! -> 19?
5, 10, 15, 20, 25
1, 1,  1,  1,  2
"""

"""
Smallest Difference
Given two arrays of integers, compute pair of values with the smallest abs
difference. Return the difference.
U:
[1, 3, 15, 11, 2]
[23, 127, 235, 19, 8]
Output: 3 -> (11, 8)
Not sorted
Abs difference
Assume no empty array?
Duplicates doesn't matter
Not necessarily same length

P:
Brute force:
Try every pair
Runtime: O(M*N)

Optimize:
(1) Sort both arrays, keep track of min (abs diff)
(2) Two pointers start at beginning, figure out which pointer has smaller value
let's say p1
(3) while arr1[p1] < arr2[p2], increment p1, update min diff
(4) once arr1[p1] > arr2[p2], increment p2, update min diff
(5) repeat until p1 or p2 reach the end
Runtime: O(MlogM + NlogN)
"""


def get_min_diff(arr1, arr2):
    arr1.sort()
    arr2.sort()
    p1 = 0
    p2 = 0
    min_val = None
    while p1 < len(arr1) and p2 < len(arr2):
        val1 = arr1[p1]
        val2 = arr2[p2]
        diff = abs(val1 - val2)
        min_val = min(min_val, diff) if min_val is not None else diff
        if val1 < val2:
            p1 += 1
        else:
            p2 += 1
    return min_val


"""
arr1 = [1, 3, 15, 11, 2] -> [1,2,3,11,15]
arr2 = [23, 127, 235, 19, 8] -> [8,19,23,127,235]
p1 = 5
p2 = 1
min_val = 3
val1 = 15
val2 = 19
"""


"""
Living People
Given a list of people with birth and death years, implement a method to find
the year with the most number of people alive. Assume all people were born
between 1900 and 2000 (inclusive). Both the birth and death years should be
considered inclusive.
U:
[(1900, 1970), (1910, 1950), (2000, 2078), (1960, 2000)] -> 1910
[(1900, 1970), (1910, 1950), (1930, 2000), (1940, 1960)] -> 1940

P:
Brute force:
(1) Initialize an array from 1900 to 2000 (101 slots)
(2) For each person's alive years, increment the corresponding year count
(3) Find the max count value
Optimize:
1. (1) Sort (birth, death) by birth
(2) Keep track of a heap of death years seen
(3) Keep track of count of people alive at that birth year
(4) Keep track of max count
(5) For each birth year curr:
    count += 1
    add to_exclude to the heap of death years
    while to_exclude is not empty and top of to_exclude < birth year
        count -= 1
        to_exclude.pop()
    update max count
(6) Return max count
Runtime: O(NlogN)
2. (1) Sort birth, death separately
(2) Use two pointers to walk through the two lists and keep track of count
Runtime: O(NlogN)
3. (1) Make an array of all birth years + 1
(2) Walk through the birth and death years and set the deltas
    birth: year[birth] += 1
    death: year[death + 1] -= 1 (Note that it is important to offset the year)
(3) Walk through the whole array and find max population
Runtime: O(N + P), P is the range of years, so technically O(N)
"""


def living_people(records):
    # sort first by death year then by birth year
    records.sort(key=lambda item: item[1])
    records.sort()
    to_exclude = 0
    count = 0
    max_count = 0
    max_year = None
    for record in records:
        birth, death = record
        heapq.heappush(to_exclude, death)
        # count current person
        count += 1
        while to_exclude and to_exclude[0] < birth:
            heapq.heappop(to_exclude)
            count -= 1
        if count > max_count:
            max_count = max(max_count, count)
            max_year = birth
    return max_year


"""
[(1930, 1955), (1900, 1970), (1960, 2000), (1910, 1950)]
birth: [1900, 1910, 1930, 1960]
death: [1950, 1955, 1970, 2000]
b = 0
d = 0
if b <= d:
    count += 1
    b += 1
else:
    count -= 1
    d -= 1
"""


def living_people_2(records):
    births = [r[0] for r in records]
    deaths = [r[1] for r in records]
    births.sort()
    deaths.sort()
    b = 0
    d = 0
    count = 0
    max_count = 0
    max_year = None
    while b < len(births):
        if births[b] <= deaths[d]:
            count += 1
            if count > max_count:
                max_count = count
                max_year = births[b]
            b += 1
        else:
            d += 1
            count -= 1
    return max_year


def living_people_3(records):
    years = [0] * 102
    for record in records:
        birth, death = record
        years[birth - 1900] += 1
        years[death - 1900 + 1] -= 1
    max_count = 0
    max_year = None
    count = 0
    for i in range(len(years)):
        y = years[i]
        count += y
        if count > max_count:
            max_year = y + 1900
    return max_year

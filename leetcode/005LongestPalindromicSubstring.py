class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        U:
        "abcba" -> "abcba", happy case with whole string being a palindrome
        "babad" -> "bab" or "aba", a substring being a palindrome
        "abc" -> "a", "b" or "c"
        "" -> ""
        M:
        Recursion
        Two pointers
        Stack for checking palindromes?
        P:
        Brute force: Generate all substrings, find the longest palindrome
        Runtime: O(N^3)
        Optimize:
        For each character at index i in s, expand it on both sides
        max_p = 0
        max_l = 0
        max_r = 0
        Odd case
            babad
            l = i
            r = i
            # still a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            length = r - l + 1
            if length > max_p:
                max_l = l
                max_r = r
                max_p = length
        Even case
            l = i
            r = i + 1
            same check after
        return s[max_l:max_r + 1]
        Runtime: O(N^2)
        """
        if s == "":
            return s

        max_l = 0
        max_p = 0
        for i in range(len(s)):
            # odd case
            l, length = self.find_bounds(s, i, i)
            if length > max_p:
                max_l = l
                max_p = length
            # even case
            l, length = self.find_bounds(s, i, i+1)
            if length > max_p:
                max_l = l
                max_p = length
        return s[max_l:max_l + max_p]

    def find_bounds(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        l += 1
        r -= 1
        length = r - l + 1
        return (l, length)
    
    """
    R:
    babad, len = 5
    max_l = 0
    max_r = 2
    max_p = 3
    i = 4
        l = 5
        r = 4
        length = 0
    s[0:3] = bab
    
    cbbd len = 4
    max_l = 1
    max_r = 2
    max_p = 2
    i = 3
        l = 3
        r = 2
        length = 0
    """
    
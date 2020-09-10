# Hash map + recursion solution
class Solution:
    def get_combo(self, combos, digits, acc, result):
        if (len(digits) == 0):
            result.append(acc)
        else:
            for c in combos[digits[0]]:
                self.get_combo(combos, digits[1:], acc + c, result)

    def letterCombinations(self, digits: str) -> List[str]:
        combos = {'1': [],
                  '2': ['a', 'b', 'c'],
                  '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'],
                  '5': ['j', 'k', 'l'],
                  '6': ['m', 'n', 'o'],
                  '7': ['p', 'q', 'r', 's'],
                  '8': ['t', 'u', 'v'],
                  '9': ['w', 'x', 'y', 'z']}
        # Need to handle empty input case!
        if (len(digits) == 0):
            return []
        acc = ''
        result = []
        self.get_combo(combos, digits, acc, result)
        return result

# Test cases: '23', '13', '', etc
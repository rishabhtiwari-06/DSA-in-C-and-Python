from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        pattern_list = [pattern.index(char) for char in pattern]
        words_list = [words.index(char) for char in words]
        if pattern_list == words_list:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    strs = "abba"
    s = "dog cat cat dog"
    result = sol.wordPattern(strs, s)
    print(result)

from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        pattern_indices = [pattern.index(char) for char in pattern]
        word_indices = [words.index(word) for word in words]
        return pattern_indices == word_indices


if __name__ == "__main__":
    sol = Solution()
    strs = "abba"
    s = "dog cat cat dog"
    result = sol.wordPattern(strs, s)
    print(result)

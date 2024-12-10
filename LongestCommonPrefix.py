#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        x=strs[0]
        for i in strs[1:]:
            while i[:len(x)] != x and x:
                x = x[:len(x)-1]
        if not x :
            return ""
        else:
            return x

if __name__ == "__main__":
    sol = Solution()
    strs = ["flower","flow","flight"]
    result = sol.longestCommonPrefix(strs)
    print(result)

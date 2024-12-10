class Solution:
    def longestPalindrome(self, s: str) -> str:

        if s==s[::-1]: 
            return s
        left = self.longestPalindrome(s[1:])
        right = self.longestPalindrome(s[:-1])

        if len(left)>len(right):
            return left
        else:
            return right

if __name__ == "__main__":
    s = "babad"
    sol = Solution()
    res = sol.longestPalindrome(s)
    print(res)

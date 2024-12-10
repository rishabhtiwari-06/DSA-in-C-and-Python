class Solution:
    def multiply(self, s: str) -> int:
        chars = set()
        left = 0
        max_count = 0
        for right in range (len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left+=1
            chars.add(s[right])
            max_count = max(max_count, right-left+1)
        return max_count

if __name__ == "__main__":
    s = "pwwkew"
    sol = Solution()
    res = sol.multiply(s)
    print(res)
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        
        return ' '.join(l[::-1])

if __name__ == "__main__":
    s = "the sky is blue"
    sol = Solution()
    print(sol.reverseWords(s))
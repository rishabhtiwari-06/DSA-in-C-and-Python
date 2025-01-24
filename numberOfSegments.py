class Solution:
    def countSegments(self, s: str) -> int:
        l = s.split()
        return len(l)


if __name__ == "__main__":
    s = "Hello, my name is John"
    sol = Solution()
    print(sol.countSegments(s))
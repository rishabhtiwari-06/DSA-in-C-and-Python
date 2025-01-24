class Solution:
    def new_String(self, s: str) -> str:
        prefix = "do not"
        return prefix +" "+ s

if __name__ == "__main__":
    s = "like tea"
    sol = Solution()
    print(sol.new_String(s))
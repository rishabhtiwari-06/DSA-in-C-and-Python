class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        res = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        for i in range(len(s)-1):
            if res[s[i]] < res[s[i+1]]:
                sum -= res[s[i]]
            else:
                sum+= res[s[i]]
        return sum + res[s[-1]]

# s = "III"
s = "MCMXCIV"
sol = Solution()
print(sol.romanToInt(s))
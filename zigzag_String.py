class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows>= len(s):
            return s
        idx,d = 0,1
        rows = [[] for _ in range(numRows)]
        for char in s:
           rows[idx].append(char)
           if idx ==0:
               d = 1
           elif idx == n-1:
               d = -1
           idx += d
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)
    
if __name__ == "__main__":
    s = "PAYPALISHIRING"
    n=3
    sol = Solution()
    print(sol.convert(s,n))
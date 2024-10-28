class Solution:
    def reverseVowels(self, s: str) -> str:
        x =[]
        for i in s:
            if(i == 'a' or i =='e' or i=='i' or i =='o' or i =='u' or i == 'A' or i =='E' or i=='I' or i =='O' or i =='U'):
                x.append(i)
        count = len(x)-1
        print(x)
        print(s)
        for i in range(len(s)):
            if(s[i] == 'a' or s[i] =='e' or s[i]=='i' or s[i] =='o' or s[i] =='u' or s[i] == 'A' or s[i] =='E' or s[i]=='I' or s[i] =='O' or s[i] =='U'):
                s = s[:i]+x[count]+s[i+1:]
                count-=1
        return s

if __name__ == "__main__":
    sol = Solution()
    s = "IceCreAm"
    sol.reverseVowels(s)

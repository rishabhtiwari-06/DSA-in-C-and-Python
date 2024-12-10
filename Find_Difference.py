#You are given two strings s and t.
#String t is generated by random shuffling string s and then add one more letter at a random position.
#Return the letter that was added to t.

class Solution:
    def findDiff(self, s: str, t:str)-> str:
        char_count = {}
        for char in t:
            char_count[char] = char_count.get(char,0)+1
        for char in s:
            char_count[char] -=1
        for char, count in char_count.items():
            if count>0:
                return char
        

if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    sol = Solution()
    res = sol.findDiff(s,t)
    print(res)
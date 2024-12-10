#Get fuunction can be used in dictonary to retrive the value assocated with they key, get function ek character/number 
#leta h or uski default value leta hai hmare case me 0 hai

# Enumerate function aapko index or value dono deta hai isliye we using it here


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count ={}    #Creating Empty Dictionary to store each character nd its frequency in it
        for char in s:
            char_count[char] = char_count.get(char,0)+1   #if char doesnt exist in dictionary to default value uski 0 le lega ye or hai to +1 ke dega
        
        for i, char in enumerate(s):
            if char_count[char]==1:
                return i
        return -1
            

if __name__ == "__main__":
    s = "loveleetcode"
    sol=Solution()
    res = sol.firstUniqChar(s)
    print(res)
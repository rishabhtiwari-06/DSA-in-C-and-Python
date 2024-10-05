from typing import List

class Solution(object):
    def printString(self, s, t):
        """
        :type s: str
        :rtype: None
        """
    
        if (len(s) != len(t)):
            return False
        if(sorted(s) == sorted(t)):
            print("Found Anagram")
            return True
        else:
            return False


def getInputAndPrint():
    s = "anagram"
    t = "nagaram"

    sol = Solution()
    sol.printString(s, t)

getInputAndPrint()

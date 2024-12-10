#25
class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_string = "".join(filter(lambda x: x.isalnum(), s.lower()))

        return formatted_string == formatted_string[::-1]

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    sol= Solution()
    res = sol.isPalindrome(s)
    print(res)

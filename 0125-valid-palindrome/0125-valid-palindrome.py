class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ans = ""
        a = "abcdefghijklmnopqrstuvwxyz1234567890"
        for i in s:
            if i in a:
                ans+=i
        temp = ans[::-1]
        val = False
        if ans == temp:
            val = True
        return val

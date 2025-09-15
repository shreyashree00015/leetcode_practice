class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        for i in s:
            if i.isalnum():
                s2+=i.lower()
        
        if (s2[::-1]==s2):
            return True
        else:
            return False
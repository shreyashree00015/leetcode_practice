class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x)):
            if x[i] == x[-1-i]:
                continue
            else:
                return False
        return True
        
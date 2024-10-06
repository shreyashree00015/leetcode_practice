class Solution:
    def isHappy(self, n: int) -> bool:
        a = n
        t = 100
        while (t):
            b = 0
            for i in str(a):
                b += int(i)**2
                
            if b==1:
                return True
            a = b
            t-=1
        return False
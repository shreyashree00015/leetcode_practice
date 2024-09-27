class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        res = num
        while t>0:
            res+=2
            t-=1
        return(res)
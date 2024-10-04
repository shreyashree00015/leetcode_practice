class Solution:
    def finalString(self, s: str) -> str:
        s2 = ''
        for i in s:
            if i!="i":
                s2 += i
            else:
                s2 = s2[::-1]
        return s2
        
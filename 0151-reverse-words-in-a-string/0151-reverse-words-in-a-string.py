class Solution:
    def reverseWords(self, s: str) -> str:
        li1 = s.split()
        s2 = ''
        s2+=li1[-1]
        for i in li1[-2::-1]:
            s2+=" "+i
        return s2
        
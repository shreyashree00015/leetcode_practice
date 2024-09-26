class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        s5 = ''
        for i in l[::-1]:
            s5+=i
            s5+=' '
        return s5.rstrip()
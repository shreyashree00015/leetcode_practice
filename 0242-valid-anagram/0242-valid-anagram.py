class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cn = Counter(s)
        ct = Counter(t)
        if cn == ct:
            return True
        else:
            return False
        